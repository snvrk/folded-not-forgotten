"""
"The Tootsie Roll Universe": toy-universe simulations.
  1. A reversible universe: Arnold's cat map on an N x N grid is a bijection, so a
     signature written into the seed is scrambled but never lost, and the exact
     state recurs (Poincare recurrence).
  2. A leaky ("tootsie roll") universe: each cycle keeps each cell with probability p
     and replaces it with fresh material; the recoverable signature is p^n.
  3. The precision horizon: on the continuous torus the cat map doubles errors
     every ~0.72 steps, so a seed known to d digits predicts only ~2.4 d steps.
Seeded; run:  python3 code/toy.py   (writes results/results.json and paper/figures/)
"""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "paper" / "figures"
rng = np.random.default_rng(20261003)
out = {}

# ---------------------------------------------------------------- the signature
N = 101
img = Image.new("L", (N, N), 0)
d = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 40)
except OSError:
    font = ImageFont.load_default()
d.text((N / 2, N / 2 - 2), "US", fill=255, font=font, anchor="mm")
sig = (np.array(img) > 127).astype(float)
out["signature_cells"] = int(sig.sum())

# ---------------------------------------------------------------- 1. reversible universe
y, x = np.indices((N, N))
def cat(a):
    """(x, y) -> (2x + y, x + y) mod N, a bijection of the grid (determinant 1)."""
    b = np.empty_like(a)
    b[(x + y) % N, (2 * x + y) % N] = a[y, x]
    return b

def cat_inv(a):
    b = np.empty_like(a)
    b[y, x] = a[(x + y) % N, (2 * x + y) % N]
    return b

def corr(a, b):
    return float(np.corrcoef(a.ravel(), b.ravel())[0, 1])

state, period = sig.copy(), None
overlap = []
for n in range(1, 2000):
    state = cat(state)
    overlap.append(corr(state, sig))
    if period is None and np.array_equal(state, sig):
        period = n
        break
out["cat_map_N"] = N
out["cat_map_period"] = period
out["overlap_with_signature_by_step"] = overlap

# ---------------------------------------------------------------- 2. leaky universe
# Each cycle: apply the reversible map, then replace each cell with probability 1 - p
# by fresh material (a Bernoulli draw with the signature's own density). The best an
# observer can do is undo the map; the recovered signature correlates p^n with the original.
dens = sig.mean()
leaky = {}
for p in (0.9, 0.5):
    s = sig.copy()
    rec = []
    for n in range(1, period + 1):
        s = cat(s)
        fresh = rng.uniform(size=s.shape) > p
        s[fresh] = (rng.uniform(size=fresh.sum()) < dens).astype(float)
        r = s.copy()
        for _ in range(n):
            r = cat_inv(r)
        rec.append(corr(r, sig))
    leaky[str(p)] = {"recovered_corr": rec, "theory_p_to_n": [p ** n for n in range(1, period + 1)]}
out["leaky"] = leaky

# ---------------------------------------------------------------- 3. precision horizon
lam = float(np.log((3 + np.sqrt(5)) / 2))
horizon = []
for digits in (3, 6, 9, 12, 15):
    eps = 10.0 ** -digits
    a = np.array([0.1234567890123, 0.4321098765432])
    b = a + np.array([eps, 0.0])
    n = 0
    while n < 1000:
        a = np.array([(2 * a[0] + a[1]) % 1.0, (a[0] + a[1]) % 1.0])
        b = np.array([(2 * b[0] + b[1]) % 1.0, (b[0] + b[1]) % 1.0])
        n += 1
        dd = np.abs(a - b)
        dd = np.minimum(dd, 1 - dd)
        if dd.max() > 0.1:
            break
    horizon.append({"seed_digits": digits, "steps_until_forecast_fails": n,
                    "theory_steps": float(np.log(0.1 / eps) / lam)})
out["lyapunov_exponent"] = lam
out["precision_horizon"] = horizon

json.dump(out, open(ROOT / "results" / "results.json", "w"), indent=1)

# ---------------------------------------------------------------- figures
INK, MUTED, GRID, BLUE, ORANGE, AQUA = "#1a1a19", "#5c5b55", "#e4e3dd", "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({"font.family": "Liberation Serif", "font.size": 9, "axes.edgecolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED})

# Figure 1: snapshots
steps = [0, 1, 3, period // 2, period - 1, period]
rows = [("Reversible", None), ("Leaky, p = 0.9", 0.9)]
fig, axes = plt.subplots(2, len(steps), figsize=(6.4, 2.45))
rng2 = np.random.default_rng(7)
for r, (label, p) in enumerate(rows):
    s = sig.copy()
    snaps = {0: s.copy()}
    for n in range(1, period + 1):
        s = cat(s)
        if p is not None:
            fresh = rng2.uniform(size=s.shape) > p
            s[fresh] = (rng2.uniform(size=fresh.sum()) < dens).astype(float)
        if n in steps:
            snaps[n] = s.copy()
    for c, n in enumerate(steps):
        ax = axes[r, c]
        ax.imshow(snaps[n], cmap="Greys", interpolation="nearest", vmin=0, vmax=1)
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color(GRID)
        if r == 0:
            ax.set_title(f"cycle {n}", fontsize=8, color=INK)
        if c == 0:
            ax.set_ylabel(label, fontsize=8, color=INK)
fig.tight_layout(pad=0.4)
fig.savefig(FIG / "fig1-cycles.png", dpi=220)

# Figure 2: how long the signature lasts
fig, ax = plt.subplots(figsize=(5.6, 3.0))
n = np.arange(1, period + 1)
ax.plot(n, np.ones_like(n, dtype=float), color=BLUE, linewidth=1.8, label="Reversible: recoverable signature")
ax.plot(n, overlap, color=BLUE, linewidth=0.7, alpha=0.55, label="Reversible: resemblance before unscrambling")
for p, col, ls in (("0.9", ORANGE, "--"), ("0.5", AQUA, ":")):
    ax.plot(n, leaky[p]["theory_p_to_n"], color=col, linewidth=1.6, linestyle=ls, label=f"Leaky, p = {p}: p$^n$")
    ax.plot(n, leaky[p]["recovered_corr"], linestyle="none", marker="o", markersize=2.2, color=col)
ax.set_xlabel("Cycles, n")
ax.set_ylabel("Signature remaining (correlation)")
ax.set_ylim(-0.1, 1.08)
ax.set_xlim(0, period + 1)
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
ax.grid(True, color=GRID, linewidth=0.6)
ax.legend(frameon=False, fontsize=7.2, loc="center right")
fig.tight_layout()
fig.savefig(FIG / "fig2-persistence.svg")
print(json.dumps({k: v for k, v in out.items() if k not in ("overlap_with_signature_by_step", "leaky")}, indent=1))
