# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative guess | "Generate pytest cases that cover negative numeric guesses, decimal string guesses, and extremely large numeric guesses for the number guessing game." | `test_negative_guess_is_too_low()` | Yes | Ensures guesses below the valid range still compare correctly and do not crash the game logic. |
| Decimal input | "Generate pytest cases that cover negative numeric guesses, decimal string guesses, and extremely large numeric guesses for the number guessing game." | `test_decimal_guess_parses_to_int()` | Yes | Verifies decimal input is parsed to an integer and does not reject valid numeric guesses. |
| Extremely large value | "Generate pytest cases that cover negative numeric guesses, decimal string guesses, and extremely large numeric guesses for the number guessing game." | `test_extremely_large_guess_is_too_high()` | Yes | Ensures very large guesses still compare correctly and return a graceful hint. |

**Prompt used:**

```
Generate pytest cases that cover negative numeric guesses, decimal string guesses, and extremely large numeric guesses for the number guessing game.
```

**Why these edge cases were chosen:**
- Negative numbers test values outside the expected positive range.
- Decimal strings test the input parser's ability to normalize floats.
- Extremely large values test that comparisons still work without overflow or unexpected behavior.

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
