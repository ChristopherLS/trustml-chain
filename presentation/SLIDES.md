# TrustML-Chain: Final Class Presentation

CS 400 / Computer Science Seminar II, Grambling State University, Fall 2026.

Live deck (Google Slides): https://docs.google.com/presentation/d/12BmQhDlLuAlPtgjIAs_yRfXNadviqbQAk4zByrYrPUc/edit

This file is a text copy of the deck (slide text and speaker notes) kept in the repository. The Google Slides deck is the source of truth. For a PowerPoint copy, use File > Download > Microsoft PowerPoint in Google Slides.
## Slide 1

**On the slide**

- CS 400  /  Computer Science Seminar II
- TrustML-Chain Presentation
- Christopher Stills, Kaleb Strong, Remington Detiege, Shabach Amuwah
- Grambling State University
- Final Class Presentation |  Fall 2026

**Speaker notes**

```text
PRESENTER: Christopher Stills (Chris)

WHAT TO SAY (just talk like this, don't read it word for word):

"Hey everybody. Quick question. If I hand you a file called homework.docx, how do you know it's the same one you turned in last week, and not one somebody secretly changed? You don't. The name tells you nothing. Anybody can change what's inside a file and keep the same name.

That's the problem we worked on. Our project is called TrustML-Chain. 'ML' stands for machine learning, which is just a computer program that studies a pile of old examples so it can make guesses on new ones. We saved one of those programs as a file, and we built a way to check that the file you get later is the exact same one we saved at the start.

Who did what: Remington built the guessing program. Kaleb built the record-keeping part. Shabach is writing our final paper. And I set up our GitHub, which is the shared folder online where all our work lives, plus the plans and documents, and I hooked the pieces together and tested them."

WORDS THAT SOUND SCARY:
- Machine learning model = a program that learned from past examples (ours learned from old basketball games).
- GitHub = a shared online folder where the whole team keeps its work.

IF SOMEONE ASKS "WHY BASKETBALL?": Because everybody knows the stats, we already know who won each game, and training the program gave us real files to check.

Then hand off: "Shabach is going to explain how the check works."
```

## Slide 2

**On the slide**

- TRUSTML-CHAIN  |  PROJECT OVERVIEW
- How we check a saved model
- Project overview
- 01  SAVE
- 02  REGISTER
- 03  COMPARE
- Save a version of the trained model. / This gives us a file to verify.
- Calculate a digital fingerprint from the file contents. / Keep that fingerprint in the registry.
- Calculate a new fingerprint before use. / Compare it with the saved reference.
- Next: Kaleb shows where the fingerprint and the model file are stored.

**Speaker notes**

```text
PRESENTER: Shabach Amuwah

WHAT TO SAY (just talk like this, don't read it word for word):

"So how do we actually check a file? Three steps. Save it, register it, compare it.

Step 1, SAVE. We train the program, then save it as a file. Now we have something to check.

Step 2, REGISTER. We make a 'fingerprint' of that file. A fingerprint here is a short code a math formula makes from everything inside the file. Think of it like a receipt for the file's contents. Same contents, same code, every time. We store that code in a registry, which is basically a record book.

Step 3, COMPARE. Later, when somebody hands us a file, we make a fresh fingerprint from it and compare it to the one in the record book. Same code means same file. Different code means something changed.

The key thing: the file's name doesn't matter at all. We only care about what's inside. Kaleb will show you where that record book lives."

WORDS THAT SOUND SCARY:
- Fingerprint (the technical name is a 'hash') = a short code made from a file's contents. Change even one tiny thing in the file and the code comes out totally different.
- Registry = the record book where we keep the original fingerprints.

IF SOMEONE ASKS "SO IS THE FILE LOCKED?": No. The fingerprint doesn't lock or hide anything. It only lets us tell if the file got changed.
```

## Slide 3

**On the slide**

- TRUSTML-CHAIN   /   SYSTEM DESIGN
- Where the file and fingerprint live
- The registry keeps the reference. The model file stays in ordinary storage.
- 01  SAVE THE FILE
- 02  REGISTER THE HASH
- 03  CHECK BEFORE USE
- The training team saves a model checkpoint.
- Python calculates a SHA-256 fingerprint and records it on the local blockchain.
- Python hashes the file again and compares it with the saved reference.
- A trusted registration is the starting point for later checks.

**Speaker notes**

```text
PRESENTER: Kaleb Strong
The actual model file stays in ordinary storage. The local blockchain stores the reference fingerprint so we can look it up later. Our Python tool uses SHA-256 to calculate the fingerprint from the file’s bytes. We chose it because the same contents give the same result, and it’s designed to make finding a different file with the same fingerprint extremely difficult. The reference only helps if we registered the right file to begin with. Next I'll show what one record holds, how registration works, and a quick test of the registry.
```

## Slide 4

**On the slide**

- TRUSTML-CHAIN   /   REGISTRY RECORD
- One record per run and stage
- Each training run gets one on-chain record for every stage (1–3).
- IDENTITY
- Run ID + stage (1–3)
- INTEGRITY
- 32-byte SHA-256 model fingerprint
- TRAINING RESULT
- Reported accuracy in basis points
- AUDIT TRAIL
- Registration timestamp + submitting account
- Model files stay off-chain. Sample: 6523 basis points = 65.23%.

**Speaker notes**

```text
PRESENTER: Kaleb Strong
WHAT TO SAY (just talk like this, don't read it word for word):
"So what does the record book actually keep? One record for each training run and each stage, stages one through three. Each record has four parts.
Identity: the run ID plus the stage number, so we know exactly which save point this is.
Integrity: the fingerprint of the model file. It's made with SHA-256 and it's 32 bytes long.
Training result: the accuracy that the training run reported. We store it in basis points, which is just hundredths of a percent. So 6523 means 65.23 percent. We use a whole number because smart contracts don't do decimals.
Audit trail: when the record was registered and which account submitted it.
One more thing: the model file itself never goes on the chain. Only the fingerprint and these few facts do. The sample number at the bottom, 65.23 percent, is just example data I used for testing."
WORDS THAT SOUND SCARY:
- Basis points = hundredths of a percent. 100 basis points is 1 percent.
- Smart contract = the program on the blockchain that holds the record book and enforces its rules.
- Off-chain = stored somewhere ordinary, not on the blockchain. Our model files live off-chain.
IF SOMEONE ASKS "IS 65.23% THE MODEL'S ACCURACY?": No. That's a sample number for the test. Remington's real reported accuracy is on the evaluation slide: 83.11 percent at epoch ten, on 5,926 games the model hadn't seen.
Then hand off: "Next, how a record actually gets registered."
```

## Slide 5

**On the slide**

- TRUSTML-CHAIN   /   REGISTRATION FLOW
- How a record gets registered
- Three steps, all enforced by the smart contract.
- 1
- Registrar sends run ID, stage, fingerprint and accuracy.
- 2
- Contract checks the sender, inputs and duplicate records.
- 3
- Contract stores the record with no update or delete function.
- Verification: compare the file hash with the registered fingerprint.
- The contract trusts the registrar’s submitted hash and accuracy.

**Speaker notes**

```text
PRESENTER: Kaleb Strong
WHAT TO SAY (just talk like this, don't read it word for word):
"Registering a record takes three steps.
Step 1: the registrar sends in the run ID, the stage, the fingerprint, and the accuracy. The registrar is the one approved account that's allowed to add records.
Step 2: the contract checks three things. Is the sender really the registrar? Are the inputs valid? And is there already a record for this run and stage?
Step 3: if everything checks out, the contract stores the record. And here's the important part: the contract has no update function and no delete function. Once a record is in, nobody can quietly change it.
Later, to verify a file, you take its fingerprint and compare it to the registered one.
Here's the honest catch, and it's on the slide: the contract trusts what the registrar submits. It never opens the model file. If the registrar sends in the wrong fingerprint or the wrong accuracy, the contract stores exactly that."
WORDS THAT SOUND SCARY:
- Registrar = the one approved account allowed to submit records.
- Duplicate record = trying to register the same run and stage a second time. The contract refuses.
- No update or delete = records can only be added, never edited or removed.
IF SOMEONE ASKS "CAN THE CONTRACT TELL IF THE ACCURACY IS REAL?": No. It only stores what it's given. That's why you have to register the right file and the right numbers first.
Then hand off: "I tested all of this on a practice chain. Here's what happened."
```

## Slide 6

**On the slide**

- TRUSTML-CHAIN   /   SAMPLE DATA  ·  LOCAL HARDHAT CHAIN 31337
- Smoke test on a local chain
- Sample data only. This test does not verify Rem’s model.
- Register + readback
- exists: true
- Sample accuracyBps
- 6523 (65.23%)
- Missing record
- exists: false
- Wrong account
- refused: NotRegistrar
- Overwrite
- refused: AlreadyRegistered
- DEPLOYED CONTRACT
- 0x5FbDB2315678afecb367f032d93F642f64180aa3
- Original record unchanged. Smoke test passed.

**Speaker notes**

```text
PRESENTER: Kaleb Strong
WHAT TO SAY (just talk like this, don't read it word for word):
"This is a quick smoke test I ran on a local practice blockchain. It's called Hardhat, it runs on our own computer, and it uses chain number 31337. Everything here is sample data.
Five checks. One: I registered a record and read it back, and it came back as existing. Two: the accuracy came back as 6523 basis points, which is 65.23 percent, exactly what I put in. Three: I asked for a record that was never registered, and it correctly said it doesn't exist. Four: I tried to register from the wrong account, and the contract refused with an error called NotRegistrar. Five: I tried to register the same record again, and it refused with AlreadyRegistered.
After all of that, the original record was unchanged. Smoke test passed. The address at the bottom is where the contract was deployed on the practice chain."
WORDS THAT SOUND SCARY:
- Smoke test = a quick check that the basics work before you test anything bigger.
- Hardhat = a tool that runs a practice blockchain on your own computer. 31337 is its default chain number.
- Refused / NotRegistrar / AlreadyRegistered = the contract rejecting a request and telling us why.
- Basis points = hundredths of a percent (6523 = 65.23%).
IMPORTANT: This is sample data and a terminal output I shared with the team. It does NOT verify Remington's model, and 65.23 percent is a test number, not the model's accuracy.
IF SOMEONE ASKS "HOW IS THIS DIFFERENT FROM CHRIS'S TESTS?": Mine checks the record book's rules: who is allowed to write, and that records can't be overwritten. Chris's tests check whether a model file matches its registered fingerprint.
Then hand off: "Rem, show us where that model file came from."
```

## Slide 7

**On the slide**

- TRUSTML-CHAIN  |  BASKETBALL MACHINE-LEARNING COMPONENT
- My Role: Building the Basketball Win Predictor
- CBS 410 Applied Cryptography / TrustML-Chain
- MY RESPONSIBILITY
- MY DELIVERABLE
- WHAT I WILL SHOW
- Data: prepare NBA game records for learning. / Model: train and save PyTorch checkpoints.
- Predictor: a runnable script that accepts six game statistics. / Output: home/away win probabilities and a predicted winner.
- Process: source, troubleshooting, and model versions. / Evidence: one real terminal prediction and its limits.
- Focus: explain the work clearly without presenting one prediction as proof of model accuracy.

**Speaker notes**

```text
PRESENTER: Remington DeTiege

I built the basketball model we needed for the demonstration. Basketball gives us familiar statistics and known outcomes, so we can see whether the model classifies the game correctly. It also gives the verification team real saved model files to check. I’ll show you the data, how the model works, and what the results mean.
```

## Slide 8

**On the slide**

- TRUSTML-CHAIN  |  BASKETBALL ML COMPONENT
- 02/05
- 1. Data source and preparation
- The model learns from historical NBA game statistics—not live play-by-play.
- SOURCE & REPOSITORY
- WHAT THE MODEL USES
- Dataset: NBA Games dataset on Hugging Face / Dataset page: huggingface.co/datasets/davdsdfd/nba-games / Attribution: dataset record associated with Nathan Lauga / Project: github.com/ChristopherLS/trustml-chain / ML files: ml/prepare_data.py • ml/train_model.py • ml/predict.py / Training input: data/train.csv (the project training CSV path)
- Home team: FG_PCT_home, REB_home, AST_home / Away team: FG_PCT_away, REB_away, AST_away / Preparation: clean/format records and create numeric features for training / Learning task: classify whether the home or away team wins / Important: the interactive predictor asks for completed-game statistics

**Speaker notes**

```text
PRESENTER: Remington DeTiege

We used historical NBA games. The six inputs are shooting percentage, rebounds, and assists for each team. The result we’re trying to classify is whether the home or away team won. These are statistics from completed games. We’re grading how the model classifies those games, not claiming it can forecast a winner before tipoff.
CAUTION: Don't say the data provenance is fully verified. The exact training CSV and its row-level match to the saved checkpoints should be confirmed from the training manifest and report first.
```

## Slide 9

**On the slide**

- TRUSTML-CHAIN  |  BASKETBALL ML COMPONENT
- 03/05
- 2. My responsibilities, trials and troubleshooting
- The development work involved more than training a model: the pipeline had to run reliably.
- MY RESPONSIBILITIES
- ISSUES WE WORKED THROUGH
- WHAT IMPROVED
- Prepare the basketball data for the ML pipeline. / Run training and save model checkpoints. / Build/test the command-line prediction script. / Check that the correct checkpoint is loaded. / Package evidence for the team’s presentation and handoff.
- Environment: PowerShell/virtual-environment activation and running commands from the project folder. / Script cleanup: an earlier predictor file contained duplicated Epoch 1 and Epoch 10 sections, which could trigger two runs. / Input discipline: the script expects six numeric statistics in the correct order. / Evaluation: a successful prediction is not the same as a held-out accuracy test.
- Used the project virtual environment. / Checked repository status and model files. / Confirmed checkpoints existed for Epoch 1, 5 and 10. / Ran the interactive predictor successfully using Epoch 10. / Kept the result separate from claims about general accuracy.
- Evidence shown in the terminal log: branch rem/ml-training; checkpoints basketball_epoch_1.pt, basketball_epoch_5.pt, basketball_epoch_10.pt.

**Speaker notes**

```text
PRESENTER: Remington DeTiege

Getting the code to train was only part of the work. I also had to make sure the prediction script loaded the intended saved file and accepted the stats in the correct order. One epoch is one pass through the training data. A checkpoint is a saved copy of the model after a pass. We recorded results at passes one, five, and ten. The verification team has now tested all three checkpoints, epochs one, five, and ten, on the local chain. Don’t confuse a saved model or a prediction run with an on-chain check.
```

## Slide 10

**On the slide**

- TRUSTML-CHAIN  |  BASKETBALL ML COMPONENT
- 04/05
- 3. Final working version: how the predictor works
- A compact PyTorch feed-forward network turns six features into a win probability.
- MODEL FLOW
- SIMPLIFIED CORE INFERENCE LOGIC
- Input (6 values): three completed-game statistics for each team. / Network: Linear(6 → 16) → ReLU → Linear(16 → 1). / Normalization: use the mean and standard deviation saved with the checkpoint. / Probability: apply sigmoid to the model score. / Decision: compare home and away probabilities; report the higher one.
- This is the core model/inference pattern for explaining the working predictor; the full ml/predict.py also loads the selected checkpoint and collects inputs.

**Speaker notes**

```text
PRESENTER: Remington DeTiege

The six stats go into a small PyTorch model. We put the inputs on comparable scales using the values saved with the checkpoint. The model turns those inputs into a score, converts it into a probability, and picks the side with the higher value. If asked about the code, point to the 6-to-16-to-1 network and the final sigmoid. The audience only needs to follow input, score, and decision.
```

## Slide 11

**On the slide**

- TRUSTML-CHAIN  |  BASKETBALL ML COMPONENT
- 05/05
- 4. Live run, interpretation and next steps
- The latest PowerShell run successfully loaded the Epoch 10 checkpoint and returned a prediction.
- ACTUAL OUTPUT FROM THE PROVIDED RUN
- WHAT THIS RESULT MEANS
- Model checkpoint: Epoch 10 /   / FG_PCT_home: 0.400 / REB_home:    45 / AST_home:    25 / FG_PCT_away: 0.450 / REB_away:    42 / AST_away:    22 /   / Home win probability: 33.67% / Away win probability: 66.33% /   / PREDICTION: AWAY TEAM WINS
- For these six inputs, Epoch 10 assigned the away team a higher predicted probability. / It demonstrates that the saved model loads and the prediction pipeline runs end-to-end.
- WHAT IT DOES NOT PROVE / NEXT STEPS
- Not accuracy: one interactive example is not a held-out test. / Not verified here: This terminal output does not measure accuracy. See the next slide for held-out test results. / Next: Compare the reported results for Epochs 1, 5 and 10 on the next slide.
- Closing line: “My contribution was turning historical basketball data into a runnable prediction component, then identifying what still needs formal evaluation.”

**Speaker notes**

```text
PRESENTER: Remington DeTiege

In this example, the saved epoch-ten model loaded and gave the away team 66.33% for the six stats entered. That number describes this one example. It’s not how often the model was right. On the next slide, we’ll use the reported held-out results to show how accuracy was measured.
```

## Slide 12

**On the slide**

- TRUSTML-CHAIN   /   MODEL EVALUATION
- How accurately did the model classify games?
- Reported accuracy on 5,926 held-out games. These are completed-game stats.
- Simple baseline
- 55.69%
- Epoch 1
- 77.24%
- Epoch 5
- 83.04%
- Epoch 10
- 83.11%
- Source: training_report.json  /  View the reported results

**Speaker notes**

```text
PRESENTER: Remington DeTiege

The report measures how often the model classified the winner correctly over 5,926 games held back from training. The simple baseline was 55.69%. Epoch one reached 77.24%, epoch five reached 83.04%, and epoch ten reached 83.11%. Most of the gain came by epoch five. These results describe completed-game classification. Chris will show the separate test for whether a saved file changed.
```

## Slide 13

**On the slide**

- TRUSTML-CHAIN   /   LIVE DEMO & RESULTS
- Same name. Different contents.
- The same four tests, run on all three basketball checkpoints (epochs 1, 5 and 10).
- TEST CASE
- OBSERVED
- Original model file
- MATCH
- Identical copy with a new name
- MATCH
- Edited copy with the original name
- CHANGED
- Unregistered run ID
- NO RECORD
- 12 of 12 checks passed. Registry readback matched at all three stages.

**Speaker notes**

```text
PRESENTER: Christopher Stills (Chris)

THIS IS MY PART. HERE'S WHAT I DID, IN ORDER:

"Remember the two files from the start, same name, maybe different insides? Here's what I did to test that.

I took all three saved copies of Remington's basketball program: epoch one, epoch five, and epoch ten. Those are the save points after the program went through its practice games one time, five times, and ten times. For each one I made its fingerprint and put it in Kaleb's record book. Then I asked the record book to give each one back, and every one matched what I put in. So the record book works.

Then, for each of the three saved copies, I ran the same four tests:
1. The original file. Result: MATCH. Good, it recognizes the real one.
2. An identical copy with a different name. Result: MATCH. So renaming doesn't fool it, and it doesn't wrongly flag it either.
3. A copy I edited, keeping the ORIGINAL name. I added a few extra bytes to a copy. Result: CHANGED. This is the whole point. Same name, different insides, and it caught it. (I made the edit on a temporary copy, so the real files stayed untouched.)
4. A made-up ID that was never registered. Result: NO RECORD. It can't compare to something that was never saved.

Four tests on each of three saved copies is twelve checks, and all twelve did what they should."

HOW I RAN IT: I used GitHub Codespaces, which is basically a computer in the cloud. I started a practice blockchain on it (a blockchain is a shared record book where entries can't be quietly erased or rewritten; ours is a practice one that only runs on our own setup, not the real internet). Then I ran one script that does all twelve checks and saves a log and a spreadsheet of the results.

THE CATCH (say this, it's honest): The check only proves the file matches what we saved. If we saved the wrong file at the start, it would happily confirm the wrong file. So you have to register the right one first.

IF THIS SLIDE IS A BACKUP: If the live demo works, show the real output instead. The saved log is at results/raw/all-epochs-verification.txt, and the spreadsheet version is all-epochs-verification.csv. To replay it, run present_verification.py from the blockchain folder in the repo. Add --live to run all twelve checks fresh.

Then hand off: "Here are the full results, including cost and timing."
```

## Slide 14

**On the slide**

- TRUSTML-CHAIN   /   VERIFICATION RESULTS
- All three checkpoints verified
- Model accuracy and blockchain file verification are separate tests.
- EPOCH 1
- EPOCH 5
- EPOCH 10
- 4 of 4 checks passed
- 4 of 4 checks passed
- 4 of 4 checks passed
- Stage 1 / 94,609 gas to register / 13.8 ms median check
- Stage 2 / 77,509 gas to register / 11.3 ms median check
- Stage 3 / 77,509 gas to register / 15.7 ms median check
- 12 of 12 checks passed. Gas is in local-chain units, not dollars. Check times are medians of 10 runs.

**Speaker notes**

```text
PRESENTER: Christopher Stills (Chris)

WHAT TO SAY (just talk like this, don't read it word for word):

"Here's the full scoreboard. All three saved copies, epoch one, epoch five, and epoch ten, passed all four checks. That's twelve out of twelve, and every one did what we expected.

We also measured two more things for each copy.

First, gas. Gas is the fee a blockchain charges to store something. On our practice chain, registering epoch one cost 94,609 gas, and epoch five and epoch ten each cost 77,509. The first one costs more because it was the very first record the contract ever stored.

Second, timing: how long one check takes. That means reading the file, making its fingerprint, looking up the record, and comparing. The typical time, which is the median, was about 14 milliseconds for epoch one, 11 for epoch five, and 16 for epoch ten. That's a tiny fraction of a second.

And remember: none of this says anything about how good the model is. Accuracy was a separate test."

WORDS THAT SOUND SCARY:
- Epoch = one full lap through the practice data. Epoch 1, 5, and 10 are saves after lap 1, lap 5, lap 10.
- Median = the middle number when you line the results up. We timed 10 checks per saved copy after one warm-up run.
- Gas = the fee a blockchain charges to store something. Ours is counted in gas units on a practice chain, so no real money is involved.
- Millisecond = one thousandth of a second.

IMPORTANT: "Twelve out of twelve" is about file integrity only. Gas is units, not dollars. The times come from one computer (our Codespace) and will vary on another.

IF SOMEONE ASKS WHERE THESE NUMBERS COME FROM: Our GitHub, in results/raw/all-epochs-verification.txt and the matching .csv. Every number on this slide is in that file.

IF SOMEONE ASKS WHY KALEB'S GAS NUMBERS ARE A LITTLE DIFFERENT: His separate gas report used a different run ID, and his report notes that longer run IDs cost a little more because the text is stored in the transaction. Ours was longer.

IF SOMEONE ASKS "SO IS EPOCH 10 THE BEST MODEL?": That's an accuracy question, a different test. See the accuracy slide: 83.11 percent at epoch ten versus 83.04 at epoch five.
```

## Slide 15

**On the slide**

- TRUSTML-CHAIN  |  RESULTS & LIMITATIONS
- What a match actually tells us
- Takeaway and questions
- FILE INTEGRITY
- MODEL QUALITY
- CAMPUS USE
- The file matches the registered fingerprint. / A mismatch flags a difference.
- Accuracy needs its own test on unseen games. / A match does not establish accuracy or safety.
- Research teams could verify model versions before reuse. / Start with a trusted reference.
- RESPONSIBLE USE   Public NBA game statistics, no claims beyond the evidence, practice chain only.
- Same name or different name, the check depends on the contents.

**Speaker notes**

```text
PRESENTER: Shabach Amuwah

WHAT TO SAY (just talk like this, don't read it word for word):

"So what did we actually prove? Three things, and one thing we did NOT prove.

One, FILE INTEGRITY. If a file matches its saved fingerprint, it's the same file we registered. If it doesn't match, something changed. Doesn't matter what it's named.

Two, this does NOT tell you the program is any good. A match says 'same file', not 'smart file'. How accurate the basketball program is was a totally separate test, and it got about 83 percent right on games it hadn't seen. Different question, different test. A match also doesn't say the model is fair or safe.

Three, where this could be used. A research team could check a model before reusing it, so they know they got the real one.

One more catch: the check only works if the right file was registered first. And the fingerprint doesn't hide the file or prove who made it. It only shows if it changed.

Same name or different name, what matters is what's inside. Thanks everybody, we'll take questions."

IF SOMEONE ASKS "SO IS THE MODEL ACCURATE?": That's a different test. On 5,926 games the program hadn't seen, it got 83.11 percent right at epoch ten. Guessing the home team every time would get 55.69 percent. That's the comparison.

NOTE: This is also the conclusion of the paper, so use the paper's wording if someone asks follow-ups.

ON RESPONSIBLE USE (the line at the bottom of the slide):
"One more thing about using this responsibly. Our data is public NBA game statistics, so we aren't handling anybody's private information. We only claim what we actually tested. And everything ran on a practice blockchain on our own computers, not on a real network. This is a demonstration of the idea, not a finished security product."
IF SOMEONE ASKS "IS THE DATA PRIVATE OR LICENSED?": It's a public dataset of game statistics, and Remington's data slide credits the source. Don't state license terms unless Remington has confirmed them.
IF SOMEONE ASKS ABOUT THE FULL TEST: All three saved copies passed all four checks, twelve out of twelve. Typical check times were 11 to 16 milliseconds, and registering a record cost about 77,500 to 94,600 gas on our practice chain. Those are file-integrity numbers only, and gas is units, not dollars.
```
