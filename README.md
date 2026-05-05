# 🎲 Lucky Dice — Hack The Box Challenge Writeup

---

# 📌 Overview

**Lucky Dice** initially looks like a basic counting game:

Several players roll dice, their totals are shown, and your task is to identify the winner.

Sounds easy — until the challenge introduces its real obstacle:

## ⏱ You only have 0.3 seconds per round... for 100 rounds.

That changes everything.

This is not a manual challenge.
It is a speed, parsing, and automation challenge disguised as a simple game.

---

---

# 🎯 Challenge Objective

To win, you must successfully complete:

## ✅ 100 consecutive rounds

For every round:

* Multiple players roll dice
* Each player’s dice values are added together
* The highest total wins
* You must answer before timeout
* One wrong answer = immediate failure

---

# ⚠️ The Real Difficulty

The issue is not math.

The issue is:

## 🔥 Speed + Accuracy + Correct Tiebreak Logic

Even if you calculate correctly, a delay beyond 0.3 seconds ends the game.

This immediately signals that:

# 🤖 Automation is mandatory

---

# 🧠 Source Code Analysis

Reading the challenge script reveals the full game logic.

---

## 🎲 Player Count

The number of players is randomized at startup:

### Between:

**8 → 13 players**

---

## 🎲 Dice Growth Per Round

The number of dice increases every round.

### Example progression:

* Round 1 → Few dice
* Mid-game → Much larger totals
* Round 100 → Massive dice lists

### Result:

Manual calculation becomes impossible.

---

# 🏆 How Winning Actually Works

At a glance:

## Highest total score wins

Simple enough...

---

# ⚠️ Critical Hidden Rule: Ties

This is where many solvers fail.

If two or more players have the same highest score:

# ❗ The LAST player in roll order wins

Not the first.
Not random.
Not highest final die.

## The LAST matching player.

---

# 🚨 Common Mistake

Many initial solutions fail because they assume:

## “First player with highest score wins”

This works most rounds... until a tie appears.

Then:

## ❌ Wrong answer

## ❌ Challenge failed

## ❌ Start over

---

# 🔍 Key Insight

The challenge internally preserves player order.

That means tie resolution depends on:

## Position in output order

### Practical meaning:

When scanning players:

* Keep checking all players
* If another player has the same max score later, overwrite previous winner

---

# 🧩 Core Exploitation Logic

## Correct strategy:

### 1.

Read all player lines

### 2.

Calculate each total

### 3.

Find highest score

### 4.

If tied:

## Choose the LAST matching player

---

# ⚡ Why This Matters

A solver can be:

## Fast

…but still fail.

Because:

# Logic > Speed

This challenge punishes incorrect assumptions more than slow arithmetic.

---

# 🚀 Automation Strategy

Because the server provides all visible information, the solution is straightforward:

## Build a bot that:

### ✔ Connects to the server

### ✔ Starts the game automatically

### ✔ Parses each round instantly

### ✔ Calculates totals

### ✔ Applies correct tiebreak logic

### ✔ Responds in milliseconds

---


# 📉 Performance Considerations

Even a correct bot can fail if poorly optimized.

## Major slowdown sources:

* Excessive console printing
* Inefficient parsing
* Buffer delays
* Wrong prompt detection

---

# 🛠 Best Practice

Minimal output.
Fast parsing.
Immediate response.

---


# 🏁 Endgame

After surviving all 100 rounds:

## 🎉 Reward:

The server reveals the flag.

---

# 🧠 Lessons Learned

---

## 📖 1. Read the source carefully

The challenge openly reveals:

* Timeout
* Dice growth
* Winner logic
* Tiebreak rules

---

## ⚖️ 2. Edge cases matter

Most failures come from ties, not normal rounds.

---

## 🤖 3. Automation beats manual effort

This challenge is designed for scripting.

---

## 🔬 4. Logic precision matters more than assumptions

A nearly correct solution is still failure.

---


# 🎯 Final Takeaway

**Lucky Dice** is not about luck.

It is about:

# 🧠 Code Review

# ⚡ Automation

# 🎯 Precision

A simple-looking dice game becomes a parsing and logic challenge where understanding one hidden rule makes the difference between total failure and full completion.

---

# 🏆 Final Difficulty Summary

| Factor         | Difficulty |
| -------------- | ---------- |
| Math           | Easy       |
| Manual Play    | Impossible |
| Automation     | Required   |
| Tiebreak Logic | Critical   |
| Speed          | Essential  |

---


# 🎲 Final Verdict

## “Easy challenge... if your logic is perfect.”

---

# 🚩 Flag Format

```txt
HTB{r0LL1ng-1n-t43_D33P-***_***-********}
```
