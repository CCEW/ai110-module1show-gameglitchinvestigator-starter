# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User inputs a number
2. System checks if the number is correct
3. System provides feedback (higher/lower)
4. User continues guessing based on feedback
5. User eventually guesses the correct number and wins the game or clicks "New Game" to try again.

**Screenshot** *(optional)*: 
![alt text](image.png)

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/                                              
================================================================= test session starts =================================================================
platform win32 -- Python 3.11.5, pytest-9.1.0, pluggy-1.6.0
rootdir: C:\Users\CAMILA\vscodeProjects\codepath\wk1\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 4 items                                                                                                                                      

tests\test_game_logic.py ....                                                                                                                    [100%]

================================================================== 4 passed in 0.03s ================================================================== 
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
