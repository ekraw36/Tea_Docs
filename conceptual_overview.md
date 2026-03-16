# Conceptual Overview
---
## Audience and Purpose

This overview is written for two groups of users who approach Tea from different backgrounds. Python‑literate users are comfortable writing code and working with data structures but may not know much about statistics. They want Tea to help them run analyses without choosing tests themselves. Statistically‑literate users understand hypotheses, variables, and assumptions but may not be confident writing code. They want Tea to check assumptions, select tests, and explain results clearly.

Both groups need a shared understanding of what Tea is, how it works, and how its main parts fit together before they begin installing it or running tasks. This document provides that foundation.

---
## What Tea Is

Tea is a small programming tool that automates statistical analysis. Instead of requiring users to pick a test, Tea lets them describe their data and what they want to compare. Based on that description, Tea chooses an appropriate statistical test, checks whether the test’s requirements are met, runs the analysis using predefined functions, and explains the results in plain language. It works inside of coding environments and is used as a tool when programming. There is no graphical interface as all interaction happens through Python.

---
## What Tea Can and Cannot Do

Tea can automate many parts of statistical analysis. It selects tests based on variable types and hypotheses, checks assumptions such as normality or independence, runs tests using already-coded programs that perform math functions, and produces readable explanations of both the reasoning and the results. It also can work with a variety of inputs and data types such as pandas DataFrames - where data is contained in rows and columns. 

There are limits to what Tea can currently do. It does not perform prediction or machine learning, and it cannot handle unstructured data such as text or images. It supports a growing but limited set of statistical tests, and it cannot always infer variable types automatically. Tea also does not replace contextual knowledge; users still need to understand their research questions and the context of their data.

---
## How Tea Works

Tea’s workflow can be understood as a sequence of connected steps. Users begin by writing a Tea specification that tells Tea your dataset, variables, and hypotheses or relationships that you want to test. This specification is written in Python or Tea’s Domain Specific Language (DSL) and acts as a structured description of the analysis.

Tea then interprets the specification using its reasoning engine. This engine applies a set of statistical rules to determine which tests are valid, which assumptions matter, and whether the data meets those assumptions. Once a test is selected, Tea runs it using existing Python statistical libraries rather than implementing the tests itself.

After the test is complete, Tea produces a clear explanation of what it did. This includes the chosen test, the reasoning behind the choice, the results of assumption checks, the statistical output, and a plain‑language interpretation. This final explanation is especially helpful for users who want transparency or who are still learning statistical concepts.

---
## Accepted Data Types

Tea works with structured data, usually stored in a pandas DataFrame. Each row represents an observation, and each column represents a variable. Tea supports categorical data (nominal and ordinal), continuous data (interval and ratio), binary variables, and grouped or experimental data. It does not support unstructured text, images, audio, complex time‑series models, or nested data structures. Users are responsible for loading and cleaning their data in Python before writing a Tea specification. 

---
## Tools and Environment Required

To use Tea, users need a Python environment with Python 3.x and a package manager such as pip. Many users also work in Jupyter Notebook for interactive analysis. Tea relies on pandas for data handling and on SciPy and StatsModels for statistical tests. All interaction with Tea happens through Python code or Tea DSL files, and results appear in the console or notebook output.

