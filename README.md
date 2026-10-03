# Folded, Not Forgotten

**Seeds, Cycles and the Persistence of Information**
Caleb Gottfried · Version 1.0 · October 2026

📄 [Paper (PDF)](paper/folded-not-forgotten-v1.pdf) · [HTML](paper/folded-not-forgotten.html)

The paper tests a four-part thesis, the **Fold Hypothesis**:
- the universe began from a **seed** that fixes everything;
- whoever knew the seed could **predict** everything;
- **free will** is therefore an illusion;
- the universe **cycles** as black holes become white holes, and every signature is folded into the next seed, so it **lasts for the entire time of the universe**.

## Verdict

| Claim | Status |
|---|---|
| A seed fixes everything | Open. Holds under Everett, Bohmian or superdeterministic quantum mechanics; fails under the standard reading. |
| Knowing the seed predicts everything | **True in principle; out of reach in practice.** Given the exact seed and the exact laws, the future is a computation, like a backtest run forward. Chaos punishes any rounding (each extra digit buys about 2.4 steps in the toy model), storing the universe takes more than the universe unless the seed is simple, and a predictor inside the universe cannot include itself. |
| Free will is an illusion | True for libertarian free will, given the first claim. Compatibilist free will survives: *the choice is determined, and you are the computation that determines it.* |
| Black-hole/white-hole cycles of ~110 billion years | Speculative. The cycle length has no derivation yet; measurements of dark energy could fix it or rule out global cycles. |
| **Signatures last the entire time** | **Consistent if and only if the dynamics are unitary** (Theorem 1). This is also what most physicists now expect of black holes. |

If any fraction of each seed is replaced, a signature fades as pⁿ. Only lossless (unitary) dynamics keep it forever: scrambled beyond recognition, but fully recoverable.

## Reproduce

```sh
python3 -m pip install -r requirements.txt
python3 code/toy.py     # writes results/results.json and paper/figures/
```

## License

[![W2FPL](https://snvrkotics.com/brand/licenses/w2fpl/w2fpl-88x31.png)](https://snvrkotics.com/licenses/w2fpl)

[W2FPL, Version 1](LICENSE). See https://snvrkotics.com/w2fpl.
