# evoforge-target

Demo target repository for [EvoForge](https://evoforge-web-230852112787.asia-northeast3.run.app/), a verifiable AI engineering collective.

EvoForge takes a mission written in plain language, has a Builder write the change and a Critic check it, runs the visible tests plus a sealed held-out suite, and opens a pull request here only when every gate passes. Each PR carries an evidence id and an Ed25519-signed proof certificate that anyone can check on the EvoForge verify page.

## The demo mission

`stats.median` has a deliberate bug: for a list of even length it returns the upper middle element instead of the average of the two middle elements. The visible test only covers an odd-length list, so a change that merely passes the visible tests is not enough; the held-out suite decides.

Example mission:

> In stats.py, fix median(xs) so that for an even number of items it returns the average of the two middle items. Keep mean unchanged.

`calc.py` (add, sub, mul) is the history of earlier missions: each of those bugs was fixed by a merged EvoForge PR.

## Checking a PR

1. Open the `Verify:` link in the PR body and confirm the verdict is VERIFIED.
2. Compare the certificate id, public key fingerprint and signature shown there with the ones in the PR body.
3. The `tests` workflow runs `pytest` on every PR independently of EvoForge.

## Running the tests

```
pip install pytest
python -m pytest -v
```
