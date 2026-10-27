# 2026PDDS-Python-Assessment
This repository is created to evaluate the Python coding capability of students in the Programming for Data-Driven Systems Course at National Tsing Hua University.

# Note for Students

Please **fork** this repository to your own GitHub account by clicking the **Fork** button at the top-right of this page on GitHub. Then clone your forked repository to your local machine:

```bash
git clone https://github.com/<your-username>/2026PDDS-Python-Assessment.git
```

> **Note:** `git fork` is not a valid Git command — forking is done through the GitHub web interface. After forking, use `git clone` to download your copy locally.

And after that enjoy your Python practice.

# Student Instructions

## Setup

Open a terminal in the repository root and install the required library:

```bash
python -m pip install -r requirements.txt
```

## Submit Your Solutions

Complete the Python list question in `python_list_src` and the pandas question in
`pandas_src`. You may rename the starter files, but each folder must contain
exactly one Python submission file. Do not add extra `.py` files to either folder.

Keep the required variable names from the questions because the testbenches use
them to check your results.

### Submission Process

1. After completing your solutions, stage and commit your changes:

   ```bash
   git add python_list_src/ pandas_src/
   git commit -m "Submit Python assessment solutions"
   ```

2. Push your changes to your forked repository:

   ```bash
   git push origin main
   ```

3. Submit the **URL of your forked repository** (e.g., `https://github.com/<your-username>/2026PDDS-Python-Assessment`) via the course submission system (eeClasss) before the deadline.

**Submission Deadline: 2026/11/27**

> **Privacy Notice:** Forks of a public repository are also public on GitHub. Do **not** include any personal information beyond your student ID in your code. If you have concerns about privacy, please contact the TA to arrange an alternative submission method.

## Run the Testbenches

The testbenches are automated testing suites provided to help you verify your solutions locally as you work. Each test case corresponds directly to a section in the exercises, allowing you to check whether your variables, data structures, and outputs meet the assignment requirements before submitting.

- **PASS**: The variable exists and its value matches the expected output.
- **FAIL**: The variable value or structure does not match the expected output. Read the failure trace in your terminal to see what differed.
- **Still None**: The variable placeholder (`None`) has not been replaced with your solution yet.

Run these commands from the repository root:

```bash
# Recommended: Run directly to see formatted section-by-section PASS / FAIL results
python testbench/tb_list.py
python testbench/tb_pd.py

# Alternatively, run via Python's unittest module
python -m unittest -v testbench.tb_list
python -m unittest -v testbench.tb_pd
```

## Grading Scheme & Rubric

The assessment is graded out of **100 points** (50 points for Python List + 50 points for Pandas):

| Part | Section | Target Variable | Points |
| :--- | :--- | :--- | :--- |
| **Part 1: Python List** | Section 1: List Joining | `user_orders` | 12.5 pts |
| | Section 2: List Grouping | `grouped` | 12.5 pts |
| | Section 3: List Sorting | `sorted_grouped` | 12.5 pts |
| | Section 4: List Indexing | `highest_total_price_user` | 12.5 pts |
| **Part 2: Pandas** | Section 1: DataFrame Creation | `users_df`, `orders_df` | 12.5 pts |
| | Section 2: DataFrame Merging | `merged_df` | 12.5 pts |
| | Section 3: DataFrame Grouping & Sorting | `grouped_sorted_df` | 12.5 pts |
| | Section 4: DataFrame Indexing | `highest_total_price_user` | 12.5 pts |
| **Total** | | | **100 pts** |

### Grading Policy: Output vs. Required Methods

Grading evaluates **both** output correctness and adherence to the required programming methods:

1. **Automated Verification (Testbench):** The testbench automatically checks that your code runs without unhandled exceptions and produces variables with the required names, types, and values.
2. **Method Adherence (TA Code Review):** Each section specifies target methods or functions that must be practiced (for example, using the `sorted()` function in Section 3 of the List exercise, and using `pd.merge()`, `groupby()`, `agg()`, and DataFrame indexing in the Pandas exercise).
   - TAs will inspect your code during manual review.
   - **Hardcoding values** (e.g., pasting the expected result dictionary/DataFrame directly) or **bypassing the required functions** will result in point deductions for that section, even if the testbench passes.

