# Student Information
* **Name:** Ceren Karademir
* **Student Number:** 2404109062
* **Department:** Management Information Systems
* **Course Name:** MIS203 Basic Programming

---

### AI Tool Usage
* **AI Tool Used:** Gemini
* **Prompt Used:** Write a simple Python program that asks the user for Name, Department, Age, and Career Goal, then prints a short student profile.
* **What did you change?:** I updated the prompt text to English and added formatted print output to match the required example structure.



## Week 02

* **AI Tool Used:** Gemini
* **Prompt Used:** Write a Python program named grade_calculator.py using an infinite while loop that calculates student letter grades and average scores.
* **What did you change?** I adjusted the input prompt messages and score validation logic to strictly match the assignment instructions and formatting requirements.
* **What does break do in your program?** When the user enters the letter 'q', it exits the while loop; this stops data entry and displays the previous statistics on the screen.




* # Lab Quiz 01 - Student Introduction Card

## Testing Summary
- **Test Executed:** I ran the program in the terminal and tested it using my own details (Name, Student ID, Department, GitHub Username, and Programming Goal).
- **Change Made After Testing:** After testing the initial output, I increased the length of the border lines (`=`) from 30 to 40 characters to ensure longer input texts fit nicely without awkward line breaks.
- **Boundary/Error Case (Stretch Task):** I tested a boundary case by providing an empty input for the name field and pressing Enter. The program executed without crashing, but it displayed a blank space next to the `Name:` label.
- **Future Improvement:** In the future, input validation (such as a `while` loop or checking if `.strip()` is empty) can be added to prompt the user again if required fields are left blank.


## Concept Explanations
1. **`input()` function:** Reads user input from the terminal/console as a string and stores it in a variable for later use.
2. **`print()` function:** Outputs formatted text, variables, or `f-strings` to the terminal/console screen for the user to see.
