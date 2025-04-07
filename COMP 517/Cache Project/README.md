# FIFO Cache Memory Simulation – COMP517 Coursework  
MSc Data Science and Artificial Intelligence  
University of Liverpool

This project simulates a simplified cache memory system using the First-In, First-Out (FIFO) page replacement strategy. It was completed as part of the COMP517 module, which introduces core programming concepts using Python.

## Description

The program replicates how cache memory manages page requests. It processes a list of user-input integers (representing memory pages), tracks hits and misses, and manages the cache list based on FIFO eviction rules when the cache reaches capacity.

### Key Features:
- Interactive batch input system for repeated memory request simulations
- FIFO-based cache eviction when memory exceeds the 8-page limit
- Dynamic tracking of hits and misses
- Full reset of state between request batches

### Example Behavior:
Input requests: 2, 3, 6, 5, 2, 7  
Cache before: []  
Result: hit/miss notifications, updated cache after each request

## Technical Requirements
- Pure Python implementation (no external libraries)
- 8-slot cache capacity
- Clean I/O structure with batch clearing
- Final output displays updated cache content after each batch

## Disclaimer

This project was completed as part of assessed coursework and is shared here for educational and portfolio purposes only.

© 2024 Benjamin Yiu
