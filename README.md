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

Run these commands from the repository root:

```bash
python -m unittest testbench.tb_list
python -m unittest testbench.tb_pd
```
