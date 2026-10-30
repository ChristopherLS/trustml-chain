# How We Work on GitHub

## Words you need (one sentence each)

- **Repository (repo):** the project folder, with its full history, stored on GitHub.
- **Branch:** your own copy of the project timeline where you can make changes without disturbing the main version.
- **Commit:** a saved snapshot of your changes with a short message.
- **Push:** sending your commits from your computer up to GitHub.
- **Pull request (PR):** a request on GitHub asking teammates to review your branch before it joins the main version.
- **Merge:** combining the reviewed changes from your branch into the main version.

## The ten steps

1. **Pick an assigned task** from your file in `team/` or from a GitHub issue.
2. **Create a branch** named `yourname/topic`.
3. **Make changes.**
4. **Run the relevant checks** (see below).
5. **Commit and push.**
6. **Open a pull request** on GitHub.
7. **Attach evidence** (logs, file paths, screenshots) using the PR template.
8. **Request review** from the reviewer named in your task.
9. **Merge after review.** The reviewer approves; then the author clicks merge. Nothing merges automatically.
10. **Close the task:** check the box in your `team/` file (in the same or a follow-up PR) and close the issue.

## Branch names

| Person | Example branch |
|---|---|
| Shabach | `shabach/integration` |
| Kaleb | `kaleb/blockchain` |
| Remington | `remington/model` |
| Chris | `chris/documentation` |

For different pieces of work, add a short topic: `kaleb/contract-tests`, `remington/data-split`.

## Commands that work right now

First time only (you must have been invited to the private repository and be signed in to GitHub):

```bash
git clone https://github.com/ChristopherLS/trustml-chain.git
cd trustml-chain
```

Starting a task:

```bash
git switch main
git pull
git switch -c kaleb/blockchain      # use your own branch name
```

Saving and sharing your work:

```bash
git status                          # see what changed
git add path/to/the/file.md         # add specific files (avoid "git add ." until you know what it will include)
git commit -m "Add Hardhat version to ENVIRONMENT.md"
git push -u origin kaleb/blockchain # first push of a new branch
git push                            # later pushes of the same branch
```

Then open the repository on GitHub and click the "Compare & pull request" button.

Catching up with teammates' merged work:

```bash
git switch main
git pull
git switch kaleb/blockchain
git merge main                      # if Git reports a conflict, see docs/TROUBLESHOOTING.md and ask for help
```

## Commands that only work after the team builds the files

These do **not** work today because the files do not exist yet. Each owner will replace the placeholder with the real command in their folder's README once it works.

| Purpose | Example (placeholder, not yet real) | Owner |
|---|---|---|
| Prepare data | `python ml/<script>.py` | Remington |
| Train model | `python ml/<script>.py` | Remington |
| Run contract tests | `npx hardhat test` (inside `blockchain/`, after Hardhat is set up) | Kaleb |
| Verify a file | `python integration/<script>.py <file> <run> <stage>` | Shabach |

## Rules

- **Never** `git push --force`. **Never** overwrite a teammate's work.
- **Never** commit directly to `main` after Boss 1. Use a branch and a PR.
- **Never** merge your own PR before the named reviewer has approved it.
- **Never** commit `.env`, private keys, downloaded datasets, or large model files (they are in `.gitignore`).
- Small commits with clear messages beat one giant commit.
- If you are unsure whether something is safe to commit, ask first.

## Protecting `main`

GitHub's free plan may not let private repositories enforce review rules. If that is the case here, "review before merge" is a team promise. Everyone keeps it.

## Future automated checks (plan only, not built)

No GitHub Actions are set up because the code they would test does not exist yet. After the code exists, we may add: Python tests on pull requests, Hardhat contract tests, a check that no `.env` is committed. Whoever builds the tests proposes the workflow in a PR.
