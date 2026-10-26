# ism3232-midterm: Seabreeze Inn

- Name: Cameron McGraw
- Version: 1.0
- Date: 10/25/26

## What This Program Does

This program allows for Seabreeze Inn to test its business rules so that anyone is able to read it. This allows for these rules to be tested so you can see the limits of these rules and how they can be changed or made better or if they are running smooth already.

## Business Rules

Rule one is that room cost is nightly rate times nights stayed.
Rule two is a discount given to customers depending on if they stayed less than 4, 4-13, or more than 13 nights.
Rule three states all corporate guests get at least the 6% discount no matter what.
Rule four states that there is 40 dollar cleaning fee if the cost is less than 300.
Rule five states a credit check is needed past 2000.
Rule six gives guests a welcome package if they stay 6 or more nights and spend more than 1000.

## How to Run

python3 and running the tests with pytest -v.

## How to Test

I wrote 26 tests to make sure that everything was correct and as accurate as possible. In test_business_rules you run pytest -v in order to see if the tests pass or not.

## Files in This Repository

ism3232-midterm is the folder which holds all the files.
business_rules.py is where I put all the rules that python must follow when running the pytests.
main.py shows the stays and the people who have stayed at the hotel.
commands.md is answering questions to prove that I built and checked the project throughout the making of it.
README.md is this file where I am also answering questions about this repository so someone else could potentially use it.
requirements.txt holds pytest and ruff  which are needed in running the tests.
.gitignore makes sure git does not go to certain folders and ignores .venv.
tests is where run the tests to see if all the requirements pass and there is nothing wrong with the repository.

## AI Use Statement

I did not use AI in this exam.