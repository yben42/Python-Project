# Voting Rules Implementation – COMP517 Coursework

This project was developed as part of COMP517 (Advanced Algorithm Design) in the MSc Data Science and AI program at the University of Liverpool. It focuses on implementing core voting systems from computational social choice theory using Python and object-oriented programming principles.

## About the Module

COMP517 explores advanced algorithm design, covering topics such as preference aggregation, decision theory, and algorithmic fairness. This assignment specifically required implementing voting rules that determine outcomes based on agents’ ranked preferences.

## Voting Rules Implemented
- **Dictatorship** – Selects the top-ranked alternative of a designated agent.
- **Scoring Rule** – Applies a weighted score vector to preferences and selects the highest scoring candidate.
- **Plurality** – Chooses the candidate with the most first-place rankings.
- **Veto** – Eliminates each agent’s lowest-ranked alternative and scores the rest.
- **Borda Count** – Assigns decreasing scores from top to bottom rank.
- **STV (Single Transferable Vote)** – Eliminates least-favored candidates in rounds until one remains.

Each rule includes tie-breaking logic using a selected agent’s ranking and built-in error handling.

## System Design

The program uses a provided `Preference` object with the following interface:
- `candidates()` – Returns a list of alternatives.
- `voters()` – Returns a list of agent IDs.
- `get_preference(candidate, voter)` – Returns the preference rank (0 = highest) for a candidate from a voter.

The voting functions query this interface and are fully modular, allowing for unit testing and reuse in other models.

## Tools and Skills
- **Language:** Python 3  
- **Skills:** Algorithm design, object-oriented programming, ranking logic, preference modeling, test-driven development

## License and Disclaimer
This project was submitted as assessed coursework and is shared for educational and portfolio use only. Please do not copy, reuse, or submit this code for academic credit elsewhere.

## Attribution
**Module:** COMP517 – Advanced Algorithm Design  
**Program:** MSc Data Science and AI  
**Institution:** University of Liverpool  
**Author:** Benjamin Yiu  
© 2024 Benjamin Yiu

