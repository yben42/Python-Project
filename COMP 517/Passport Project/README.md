# Digital Passport System – COMP517 Coursework  
MSc Data Science and Artificial Intelligence  
University of Liverpool

This project implements a digital passport system in Python, developed as part of the COMP517 module. The task was to design a `Passport` class based on a formal specification simulating how passports might be digitized for future global standards.

## Features

The `Passport` class provides:

- Object-oriented structure with class and instance variables
- Human-readable summaries and data validation
- Travel stamping, visit tracking, and destination scoring
- Unique passport numbers using a class-level counter
- Compliance with ISO date formats and PEP-8 standards

## Functionality

Each passport object includes personal information and expiry validation. Key methods allow:

- Checking passport validity (`is_valid`)
- Verifying identity data (`check_data`)
- Generating summaries (`summary`)
- Tracking entry stamps to countries (`stamp`, `countries_visited`, `times_visited`)
- Scoring travel history using sum of squares (`sum_square_visits`)
- Generating a unique passport number (`passport_number`)

Test cases were written under the `if __name__ == "__main__"` block to ensure modularity and testability when imported.

## Disclaimer

This project was completed for academic assessment and is shared for educational and portfolio purposes only.

© 2024 Benjamin Yiu
