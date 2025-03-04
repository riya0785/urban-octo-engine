# Random Text Generator

This repository contains a Python script that generates a random six-letter string.

## Features
- Generates random six-letter text
- Uses Python's `random` module
- Includes a test suite using `pytest`

## Installation
Clone the repository and install dependencies:

git clone https://github.com/your-username/random-text-generator.git
cd random-text-generator
pip install -r requirements.txt


## After fixing the Bugs 

# Overview
This Python script generates a random string of letters (both uppercase and lowercase) with a customizable length. By default, it generates a 6-character string.

# Features
* Generates random text using uppercase and lowercase English letters.
* Default length is 6 characters, but you can specify any positive integer length.
* Includes input validation to ensure the length is a positive integer.
* Uses Python's built-in random and string libraries.
  
# Bug Fixes
1. Input Validation Fix
   
Bug: The original code lacked validation for the length parameter.


Fix: Added a check to ensure length is a positive integer.



2. Missing Import Fix
   
Bug: The original code did not include import string, which caused string.ascii_letters to fail.


Fix: Added:import string to the import section 


**********************Go through Bugfix(Randomtextgeneration.py) ****************
