# Project Explained in Plain English

## The one-sentence version

We save an AI model file, record its fingerprint somewhere hard to quietly change, and later check whether a file we are handed still matches that record.

## The two halves

```
HALF 1: BASKETBALL MODEL (Remington)          HALF 2: SECURITY SYSTEM (Kaleb + Shabach)

games spreadsheet                              saved model file (stage 1, 2, 3)
      |                                                |
      v                                                v
 split: 80% train / 20% test                  fingerprint (SHA-256)
      |                                                |
      v                                                v
 train in 3 stages                            register on practice blockchain
      |                                          (run + stage + fingerprint + accuracy)
      v                                                |
 save 3 model files + measure accuracy  ---->  later: check a file -> MATCH / CHANGED / NO RECORD
```

### Half 1: what the basketball program does

1. Reads a spreadsheet of **completed** basketball games.
2. Learns patterns connecting game statistics (shooting percentage, rebounds, assists for both teams) with whether the home team won.
3. Classifies **separate completed games** that were not used for training.
4. Saves **three model versions** during continued training.
5. Records each version's measured accuracy.

This is **completed-game classification**. It is **not** forecasting future games, because the statistics are only known after a game is over.

### Half 2: what the security system does

1. Calculates a **SHA-256 fingerprint** of each saved model file.
2. Registers the fingerprint, training run, stage, and reported accuracy on a **local practice blockchain**.
3. **Retrieves** the registered record when checking a file.
4. **Compares** the supplied file's fingerprint with the official fingerprint.
5. Displays **MATCH**, **CHANGED**, or **NO RECORD**.

An exact copy should MATCH. A deliberately altered copy should be flagged **CHANGED**.

## Vocabulary

| Term | Plain meaning | In our project |
|---|---|---|
| **Dataset** | The examples the program studies | A spreadsheet of past NBA games (`games.csv`) |
| **Training** | Software adjusts the model using examples and the correct answers | The model sees training games and whether the home team won |
| **Test set** | Examples held back and never used for training | The 20% of games used to measure accuracy |
| **Model** | The learned pattern-matcher | A very small PyTorch model |
| **Model file / checkpoint** | A file holding the model's saved learned settings | One file per stage (three total) |
| **Stage** | One round of continued training | Stage 1, 2, 3 |
| **Accuracy** | Share of basketball guesses that were right | Measured on the test set. Measures basketball guesses only |
| **Baseline** | A simple guess to compare against | For example, "always predict the more common outcome in the training data" |
| **Fingerprint (hash)** | A value calculated from a file's exact contents; change one byte and it changes | SHA-256, shown as 64 characters of 0-9 and a-f |
| **Blockchain** | A shared record book that is very hard to quietly rewrite | We run a private practice one on our own computers |
| **Smart contract** | A small program that lives on the blockchain and enforces rules | Our registry: who may add records and what a record holds |
| **Blockchain record** | The official reference used for comparison | Run + stage + fingerprint + accuracy + who submitted it |
| **Registration** | Writing a record to the blockchain | Done once per run and stage |
| **Verification** | Checking whether a file matches its registered record | Produces MATCH, CHANGED, or NO RECORD |
| **Gas** | A unit measuring how much computing a blockchain action uses | We report **gas units** only, never dollar costs |
| **Hardhat** | A toolkit for building and testing smart contracts locally | Starts our practice blockchain and runs contract tests |
| **Web3.py** | A Python library that talks to a blockchain | Lets Python register and look up records |
| **PyTorch** | A Python library for building and training models | Our one machine learning library |

## What a MATCH proves, and what it does not

**A MATCH proves:** the file you checked has the same fingerprint as the file that was registered.

**A MATCH does not prove:**
- the AI is accurate,
- the AI is fair,
- the AI can explain its decisions,
- the data the AI learned from was trustworthy,
- the person who registered it told the truth about its accuracy.

## Common misunderstandings

1. **"Changing the dataset changes the model file."** No. A saved model file is just a file. Changing the dataset later does not touch it. Only retraining and saving a new file makes a new model file.
2. **"The fingerprint measures accuracy."** No. Accuracy measures basketball guesses. The fingerprint only identifies exact file contents.
3. **"Re-saving the same model gives the same file."** Not guaranteed. A new save can produce different bytes. Always fingerprint the exact file you plan to register, and never overwrite a registered file.
4. **"The blockchain stores the model."** No. It stores a small record: the fingerprint and a few facts. The model file stays outside it.
5. **"Our practice blockchain is as strong as a real one."** No. It runs on one computer, so it demonstrates the idea. The paper must say this plainly.
6. **"High accuracy means a good forecasting model."** No. The inputs (rebounds, shooting percentage) are measured **during** the game. We are classifying finished games.

## A safety rule about damaged files

Deliberately modified copies are only **hashed** (their bytes are read). They are **never loaded** as models. Loading untrusted model files can run harmful code.

## Where to go next

[START_HERE.md](../START_HERE.md) -> your file in [team/](../team/) -> [BUILD_ORDER.md](BUILD_ORDER.md)
