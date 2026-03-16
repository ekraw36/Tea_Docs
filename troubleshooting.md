# Troubleshooting & FAQs
This document contains common issues pertaining to installing and running Tea and includes a variety of solutions to each. Additionally, this document answers some common questions about the scope and proper usage of Tea. 

## Installation and Environment Issues
 > Tea won’t install with pip
* Ensure you are using Python 3.8+. Older versions of Python may fail during dependency resolution. 
* Run 'python -m pip install - -upgrade pip' to avoid outdated resolver errors. 
* If you see permission errors, try 'pip install - -user tea-lang' or use a virtual environment.
  
> ModuleNotFoundError: No module named ‘tea’
* Your environment likely differs from the one where you installed Tea. Run 'pip show tea-lang' to confirm installation location.  
* Activate the correct environment using “source venv/bin/activate” or “.\venv\Scripts\activate”

## Data loading and Formatting Issues
> Tea says my data is ‘not recognized’ or ‘invalid format.’
* Tea accepts Pandas DataFrames, CSV files, and Python dictionaries.
* Ensure column names contain no spaces or special characters.
* Confirm that categorical variables are encoded as strings, not integers.
  
> Tea cannot find the data set I referenced”
* Check your working directory with 'os.getcwd()'
* Use absolute paths if running from an IDE
  
## Analysis and Runtime Errors
> Tea reports ‘incomplete specification’
* Every analysis requires: Defined variables, a relationship, and a hypothesis. Missing any of these will cause Tea to stop the analysis.
  
> Tea runs but produces no results.
* This usually means that your specification is valid but incomplete. Double check that all elements of your spec are declared properly. 
* Check that you called 'tea.run()' at the end of your program.
  
# Frequently Asked Questions (FAQs)
> What is Tea actually doing?
Tea reads your specification, infers variable types (if needed), checks assumptions (if needed), and selects a statistically valid test. It then runs that test using established statistical libraries and returns the results of the test.

> Do I need to know statistics to use Tea?
Tea requires a very basic understanding of statistical analysis. Tea handles test selection and assumptions, but you should understand what variables represent, the research question you’re asking, and whether your data meets basic assumptions.
 
> Can Tea run multiple analyses at once?
Yes. You can define multiple relationships and Tea will evaluate each in sequence. 

> Can I override Tea’s choice of statistical test?
Not directly, but you can influence Tea’s choice by changing variable types, adjusting assumptions, and specifying a more precise relationship between variables. 




