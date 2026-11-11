# Scholarship Eligibility Checker

A lightweight Python command-line application that evaluates student scholarship eligibility based on Grade Point Average (GPA) and disciplinary history.

## Features

* **Automated Evaluation:** Categorizes applicants into *Full Scholarship*, *Partial Scholarship*, *Not Qualified*, or *Ineligible* based on set academic and conduct criteria.
* **Clean Formatting:** Automatically formats user names and rounds GPA outputs to two decimal places.
* **Input Validation:** Safely handles invalid numeric inputs (such as negative values, GPAs above 4.0, or non-numeric characters) without crashing.

## Eligibility Criteria

| Category | GPA Requirement | Disciplinary Cases | Status Message |
| :--- | :--- | :--- | :--- |
| **Full Scholarship** | 3.70 – 4.00 | 0 | *Fully funded!* |
| **Partial Scholarship** | 3.00 – 3.69 | 0 | *Half funded.* |
| **Not Qualified** | 0.00 – 2.99 | 0 | *Keep working hard.* |
| **Ineligible** | Any valid GPA | 1 or more | *Disciplinary record disqualifies you.* |

## Prerequisites

* **Python 3.10 or higher** (required for structural pattern matching using `match`/`case`).

## Usage

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com
   cd scholarship-eligibility-checker
   ```

2. Run the script from your terminal (replace `scholarship.py` with your actual filename):
   ```bash
   python scholarship.py
   ```

### Example Output

```text
What is your name: jane doe
What is your GPA: 3.85
How many disciplinary cases do you have: 0
Jane Doe has a GPA of 3.85 with 0 disciplinary case(s) — Full Scholarship. Fully funded!
```

## Code Structure

* `main()`: Prompts the user for their name, GPA, and disciplinary cases, then coordinates validation and output formatting.
* `get_eligibility(gpa, cases)`: Evaluates the numeric inputs against the scholarship rules and returns the eligibility status (or `None` if inputs are out of bounds).
* `get_message(eligibility)`: Uses Python's `match` statement to return a custom feedback message corresponding to the applicant's status.
