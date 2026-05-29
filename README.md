# Poker Decision Assistant (Monte Carlo + Pot Odds)

An ongoing Python project that provides real-time poker decision support using Monte Carlo simulation and pot odds calculations.

The tool is designed for live poker scenarios where the user manually inputs the current game state (hand, board, pot size), and the program estimates optimal decisions such as call or fold based on probability and expected value reasoning.

---

## What It Does

- Simulates unknown opponent hands using Monte Carlo methods
- Estimates hand equity (win probability + tie adjustment)
- Computes pot odds / required equity for calling decisions
- Recommends actions (call or fold) based on mathematical comparison
- Tracks basic poker phases (preflop, flop, turn, river)

---

## Core Idea

The system is based on two fundamental concepts:

- **Equity**
  - Estimated probability of winning a hand through simulation

- **Pot Odds**
  - Minimum equity required to justify a call

Decision rule:

If equity > required equity → CALL  
Else → FOLD

---

## Implementation Overview

- `GAME` class handles game flow, state tracking, and player actions  
- `monte_carlo()` estimates win/tie/loss probabilities via repeated simulation  
- `pot_odds_decision()` compares equity vs required equity and outputs a recommendation  
- `simulate()` generates full board outcomes against random opponent hands using `phevaluator`

---

## Status

This is an **ongoing experimental project** focused on:
- Improving simulation accuracy
- Refining decision-making logic
- Expanding opponent modeling beyond random hands

Planned improvements include:
- Range-based opponent modeling
- Betting / bluffing behavior for simulation realism
- Improved decision engine beyond basic pot odds
- Optional UI for real-time gameplay assistance

---

## Requirements

```bash
pip install phevaluator
