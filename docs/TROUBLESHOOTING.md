# Troubleshooting

Add new problems and fixes as you find them (in a pull request). Include the **exact error message**.

## Git and GitHub

| Problem | What to try |
|---|---|
| "Permission denied" or "Repository not found" when cloning | You may not have accepted the invitation yet, or you are signed in to a different GitHub account. Check your email and github.com/notifications |
| `git push` rejected | Someone pushed first. Run `git pull`, fix any conflicts, push again. **Never use `--force`** |
| Merge conflict | Open the file, look for `<<<<<<<` and `>>>>>>>`, keep the correct text, delete the markers, save, `git add` the file, `git commit`. If unsure, ask before continuing |
| I committed to `main` by mistake | Do not push. Tell the team. We will fix it together |
| A file I need is not appearing in `git status` | It may be ignored by `.gitignore` (downloaded data, model files, `.env` are ignored on purpose) |

## Calculating a SHA-256 fingerprint with an independent tool

Use these to double-check our Python code. Replace `file.txt` with your file.

| System | Command |
|---|---|
| Linux | `sha256sum file.txt` |
| macOS | `shasum -a 256 file.txt` |
| Windows PowerShell | `Get-FileHash file.txt -Algorithm SHA256` |

All tools must print the same 64 characters for the same file. Letter case may differ; compare ignoring case.

## Python

| Problem | What to try |
|---|---|
| `python` not found | Try `python3`. Record which one works in `docs/ENVIRONMENT.md` |
| PyTorch will not install | Use the install command from the official PyTorch "Get Started" selector for your system (choose CPU). Check your Python version is one PyTorch supports |
| Wrong packages after switching computers | Recreate the virtual environment and reinstall. Record versions in `docs/ENVIRONMENT.md` |

## Node, Hardhat, and the local blockchain

| Problem | What to try |
|---|---|
| Hardhat complains about the Node version | Install a Node.js version supported by the current Hardhat docs. Check with `node --version` |
| Python says it cannot connect to the blockchain | The local node is not running, or the address in `.env` is wrong. Start the node and copy the exact address it prints |
| Contract "not found" at the address | The local chain was restarted, so it forgot the contract. Redeploy and update `CONTRACT_ADDRESS` |
| Transaction rejected | Read the reason. Is it the designated account? Is the run and stage already registered? |

## Fingerprint surprises

| Problem | What to try |
|---|---|
| Same model, different fingerprint after saving again | Expected possibility. A new save can have different bytes. Fingerprint the exact file you will register and never overwrite it |
| Copied file does not match | Make sure you copied the file itself. Do not open and re-save it. Check the copy finished and the sizes are equal |
| Fingerprint differs between computers | Confirm both files have the same size and that neither was opened in a text editor |

## Where to ask

1. Check this page.
2. Open a **Help request** issue.
3. Post in team chat the same day.
