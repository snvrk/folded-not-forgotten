# Publishing plan: Folded, Not Forgotten

This is a conceptual paper in the philosophy of physics. The right path is a DOI, then the philosophy-of-science preprint server, then a journal that takes foundational arguments from independent researchers.

| # | Step | Who | Status |
|---|---|---|---|
| 1 | ORCID iD 0009-0000-1948-412X in the paper, `CITATION.cff` and `.zenodo.json` | Done | ✓ |
| 2 | Zenodo DOI from a GitHub release | You (2 clicks), then me | Ready for the release |
| 3 | PhilSci-Archive preprint | You submit | Ready |
| 4 | arXiv `physics.hist-ph` (optional) | You submit | Needs an endorser |
| 5 | Journal: *Foundations of Physics* | You submit; I convert to LaTeX | After the preprint |
| 6 | Essay version for a general audience | Optional | — |

## 2. Zenodo DOI

1. At https://zenodo.org go to **Account → GitHub** and switch on `snvrk/folded-not-forgotten`. Do this first.
2. On GitHub, open **Releases → Draft a new release**, type `v1.0` in the tag box, choose **Create new tag: v1.0 on publish**, target `main`, title it `Folded, Not Forgotten v1.0`, and publish.
3. On the new Zenodo record, set **License** to "Other (Open)" with https://snvrkotics.com/licenses/w2fpl.
4. Send me the DOI. I'll add it to the README, `CITATION.cff` and the paper.

## 3. PhilSci-Archive

The archive for philosophy of science, at https://philsci-archive.pitt.edu. It is free and lightly moderated for relevance, and philosophers of physics follow it.

- **Subjects:** Specific Sciences → Physics → Cosmology; General Issues → Determinism/Indeterminism; Specific Sciences → Physics → Quantum Mechanics.
- **Upload:** `paper/folded-not-forgotten-v1.pdf`. Paste the abstract from `.zenodo.json`, and the keywords: determinism; predictability; free will; cyclic cosmology; black holes; unitarity; information; entropy.

## 4. arXiv (optional)

Use the category `physics.hist-ph` (History and Philosophy of Physics). Don't cross-list to `gr-qc`, whose moderators expect new technical results in gravitation. First-time submitters need an endorsement, so ask an author whose work the paper cites on unitarity or cyclic cosmology. The endorsement email in the Missing Minute repo's `PUBLISHING.md` can be adapted.

## 5. Journal: *Foundations of Physics*

**Why this journal.** *Foundations of Physics* (Springer) publishes conceptual work on determinism, the interpretation of quantum mechanics, and information in physics. It reviews papers on their argument, regardless of the author's affiliation.

**What I'll do first:**
- Convert the paper to LaTeX in Springer's template.
- Tighten Section 4, the cosmology review, which reviewers will consider background.
- Strengthen Theorem 1, the consistency result, which is the paper's original contribution. One option is a short appendix stating it for general quantum channels rather than only unitary maps.

**Backups:**
1. *European Journal for Philosophy of Science*
2. *Studies in History and Philosophy of Science*
3. *Entropy* (MDPI). It is open access but charges a publication fee, so check the current amount before submitting.

Be realistic about the odds. Conceptual papers face high rejection rates in these journals, and the most likely request is to sharpen what is new. The new part here is Theorem 1, together with the "determined but not revealed" account of prediction and choice. Lead with both.

### Cover letter (draft)

> Dear Editor,
>
> Please consider "Folded, Not Forgotten: Seeds, Cycles and the Persistence of Information" for *Foundations of Physics*.
>
> The paper examines a common cluster of claims: that the universe's initial state fixes everything, that knowing it would allow complete prediction, that free will is therefore illusory, and that a cyclic universe preserves every trace of each cycle in the next. It separates determination from prediction, and shows that complete prediction from an exact seed is possible in principle, but that it requires exactness, storage that only a compact seed allows, and a predictor outside what it predicts. Its main result is a consistency theorem. Endless cycles, entropy carried across cycles, and signatures that persist forever are jointly consistent if and only if the dynamics preserve fine-grained information while the entropy that is carried or reset is coarse-grained. That links the persistence question to black-hole unitarity.
>
> A preprint is on PhilSci-Archive ([link]), and code for the illustrative simulations is public (DOI: [Zenodo DOI]). The manuscript is not under consideration elsewhere. An AI writing tool assisted with drafting, as the paper discloses; I am responsible for all content.
>
> Sincerely,
> Caleb Gottfried

## 6. Essay version (optional)

A 2,000–3,000-word essay, "Folded, not forgotten," with the tootsie roll up front and the unitarity result as its payoff. It would suit long-form essay magazines that publish philosophy of science for general readers (pitch them with a one-paragraph summary), or a post on your own site. Publish it after the PhilSci-Archive preprint, so the essay can link to it.

## SSRN

Your first paper, *Ticketstorm as Mass Visual Disruption*, is on SSRN (abstract 5454695), so you already have an author page there. Once the Zenodo DOI exists, post this paper to SSRN too, with the DOI in the abstract page, so it appears alongside your first paper.

## Timeline

| When | What |
|---|---|
| Week 1 | ORCID; Zenodo DOI; PhilSci-Archive upload |
| Week 2–3 | I convert the paper to LaTeX and tighten it; optional arXiv |
| Week 4 | Submit to *Foundations of Physics* |
| Months 2–6 | Peer review |
