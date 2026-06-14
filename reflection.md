# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Failed to give me the correct hints.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The hints were backwards. When I clicked a new game button it did not start a new game. Told me to go lower when I guessed 1, but 1 is the lowest possible number, and the secret number was 95.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 99  | Too high hint | Too low hint | none |
|guess of 50 | Too low | Too high | none |
| clicked new game button | Start new game | Doesn't start new game | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked Copilot to write a test for the check_guess function. It generated a test that included multiple assertions for different inputs. I ran the test using pytest and it passed, which verified that the AI's suggestion was correct.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Pytest was not working for copilot, so it added the system path to the test file. I verified this by running pytest which worked correctly.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
