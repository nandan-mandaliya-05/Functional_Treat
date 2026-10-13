# Functional_Treat

<div align="center">

# 📊 Data Analyzer and Transformer Program

### A Python-Based Data Analysis and Transformation System

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=26&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=850&lines=Data+Analyzer+and+Transformer;Analyze+and+Transform+Data+Easily;Filter+%7C+Sort+%7C+Calculate+Statistics;Python+%7C+Functions+%7C+Recursion;Console-Based+Data+Analysis+System" alt="Animated Typing Header"/>

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Data%20Analyzer-00C2FF?style=for-the-badge)
![Application](https://img.shields.io/badge/Application-Console-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)

<br>

</div>

---

# 🌟 About The Project

**Data Analyzer and Transformer** is a Python-based console application designed to accept, analyze, filter, sort, and calculate statistics from numerical datasets.

The program supports both **1D lists and 2D matrices** and provides a menu-driven interface for performing different data-processing operations.

The application demonstrates practical usage of Python **Lists, Nested Lists, Global Variables, User-Defined Functions, Recursion, Lambda Functions, `filter()`, `sorted()`, `*args`, `**kwargs`, and Multiple Return Values**.

It is a learning project designed to build a strong foundation in Python programming and prepare for further studies in Data Science and AI/ML.

> **"Analyze data. Transform information. Build practical Python projects."**

---

# 🎯 Project Objectives

The main objectives of this project are:

- 📥 Accept numerical data in 1D and 2D formats.
- 📊 Calculate basic dataset summaries.
- 🧮 Calculate factorials using recursion.
- 🔍 Filter data using a user-defined threshold.
- ↕️ Sort numerical values in ascending or descending order.
- 📈 Calculate minimum, maximum, sum, and average.
- 🔄 Return multiple values from a function.
- 🌍 Understand the use of global variables.
- 🧠 Practise `*args` and `**kwargs`.
- 🏗️ Combine Python fundamentals into a practical application.

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### 📥 Input Data

Enter numerical values manually as a 1D list or a 2D matrix.

</td>
<td width="50%">

### 📊 Data Summary

Display the total number of values, minimum, maximum, sum, and mean.

</td>
</tr>
<tr>
<td width="50%">

### 🧮 Factorial Calculator

Calculate the factorial of a non-negative integer using recursion.

</td>
<td width="50%">

### 🔍 Threshold Filtering

Filter and display values greater than or equal to a specified threshold.

</td>
</tr>
<tr>
<td width="50%">

### ↕️ Data Sorting

Sort 1D data in ascending or descending order and sort each row of a 2D matrix.

</td>
<td width="50%">

### 📈 Dataset Statistics

Calculate and display minimum, maximum, total, and average using a function that returns multiple values.

</td>
</tr>
<tr>
<td width="50%">

### 📦 `*args` Demonstration

Pass multiple positional arguments to a function and display them individually.

</td>
<td width="50%">

### 🗝️ `**kwargs` Demonstration

Pass named arguments containing dataset information and display their keys and values.

</td>
</tr>
</table>

---

# 🧰 Technology Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,vscode,git,github" alt="Python, VS Code, Git and GitHub"/>

</div>

### Core Technologies

| Technology | Purpose |
|---|---|
| 🐍 Python | Application development |
| 📋 Lists | Store 1D numerical datasets |
| 🧮 Nested Lists | Represent 2D matrices |
| 🌍 Global Variables | Maintain shared dataset state |
| 🔧 User-Defined Functions | Organize operations into reusable functions |
| 🔁 Loops | Process input values and matrix rows |
| 🔀 Conditional Statements | Handle menu choices and decisions |
| 🧮 Built-in Functions | Use `sum()`, `min()`, `max()`, and `len()` |
| 🧠 Recursion | Calculate factorials |
| 🔍 Lambda Functions | Define a compact filtering condition |
| 🧰 `filter()` | Select values that meet a threshold |
| ↕️ `sorted()` | Sort numerical data |
| 📦 `*args` | Accept multiple positional arguments |
| 🗝️ `**kwargs` | Accept multiple keyword arguments |
| 📤 Multiple Return Values | Return statistics from a function |
| 📖 Docstrings | Describe the purpose of functions |

---

# 🏗️ Data Structures

The program uses two main lists to store numerical data.

### 1. One-Dimensional List

```python
data_1d = []
```

Example:

```python
data_1d = [10, 25, 30, 45, 50]
```

A 1D list stores numerical values in a single sequence.

### 2. Two-Dimensional List

```python
data_2d = []
```

Example:

```python
data_2d = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

A 2D list stores values in rows and columns, making it useful for representing matrix-like data.

### 3. Dataset Summary Dictionary

The program initializes a dictionary to maintain summary information.

```python
data_summary = {
    "total_values": 0,
    "min_value": None,
    "max_value": None,
    "sum_of_values": 0,
    "mean_value": 0.0
}
```

Each key represents a particular dataset statistic.

### Data Structure Overview

```text
Data Analyzer and Transformer
            |
      +-----+-----+
      |           |
    1D List    2D Matrix
      |           |
      +-----+-----+
            |
     Data Processing
            |
     +------+------+------+
     |      |      |      |
    Sum    Min    Max   Average
```

---

# 🔄 Application Workflow

```text
              +----------------------+
              |        START         |
              +----------+-----------+
                         |
              +----------v-----------+
              |     Display Menu     |
              +----------+-----------+
                         |
              +----------v-----------+
              |    Enter Choice      |
              +----------+-----------+
                         |
        +----------------+----------------+
        |                |                |
   Input Data       Analyze Data      Transform Data
        |                |                |
   +----+----+      +----+----+      +----+----+
   |         |      |         |      |         |
  1D        2D   Summary   Statistics Filter   Sort
   |         |      |         |      |         |
   +---------+------+---------+------+---------+
                         |
              +----------v-----------+
              |    Continue Menu?    |
              +----------+-----------+
                         |
                Exit when selected
                         |
              +----------v-----------+
              |         END          |
              +----------------------+
```

---

# 📋 Menu Options

When the program starts, it displays the following menu:

```text
==================== Welcome to the Data Analyzer and Transformer Program ====================

Main Menu:
1. Input Data (1D or 2D)
2. Display Data Summary (Built-in functions)
3. Calculate Factorial (Recursion)
4. Filter data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. *args Demo
8. **kwargs Demo
9. Exit Program

Enter your choice:
```

The program uses a `while` loop to continue displaying the menu until the user selects option 9.

---

# 📥 1. Input Data (1D or 2D)

The `input_data()` function allows the user to select the type of dataset to enter.

### Option 1: Enter 1D Data

Example input:

```text
Please enter your choice (1-2): 1
Enter a data for 1D array (separated by spaces): 10 20 30 40 50
1D array stored succesfully.
```

The program converts the space-separated input into integers.

```python
user_data = input("Enter a data for 1D array (separated by spaces): ")

data_1d = []

for x in user_data.split():
    data_1d.append(int(x))
```

The `split()` method separates the input into individual values, and `int()` converts each value into an integer.

### Option 2: Enter 2D Data

Example input:

```text
Please enter your choice (1-2): 2
Enter number of rows: 2
Enter row 1 values (separated by spaces): 10 20 30
Enter row 2 values (separated by spaces): 40 50 60

2D array stored successfully.
```

The resulting matrix is:

```python
data_2d = [
    [10, 20, 30],
    [40, 50, 60]
]
```

The program can also flatten the matrix into a single list when performing calculations:

```python
matrix = []

for row in data_2d:
    for item in row:
        matrix.append(item)
```

This allows the same statistical operations to work with values from either data structure.

---

# 📊 2. Display Data Summary

The `display_data_summary()` function displays a summary of the selected dataset.

The summary includes:

- Total number of values
- Minimum value
- Maximum value
- Sum of all values
- Average value

### Built-in Functions Used

```python
len(data)
min(data)
max(data)
sum(data)
```

### Example

For the input:

```python
data_1d = [10, 20, 30, 40, 50]
```

The output is:

```text
Data Summary:
~ Total values: 5
~ Minimum values: 10
~ Maximum values: 50
~ Sum of all values: 150
~ Average values: 30.00
```

The average is calculated by dividing the sum by the number of values.

```python
average = sum(data) / len(data)
```

The program formats the average to two decimal places using `:.2f`.

---

# 🧮 3. Calculate Factorial (Recursion)

The `factorial()` function calculates the factorial of a non-negative integer using recursion.

A factorial is the product of all positive integers up to a given number.

For example:

\[
5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
\]

The factorial of zero is defined as:

\[
0! = 1
\]

### Implementation

```python
def factorial(num):
    """Finds the factorial of a number using recursion."""

    if num < 0:
        return "Invalid number"

    if num == 1 or num == 0:
        return 1

    return num * factorial(num - 1)
```

### How Recursion Works

For `factorial(5)`, the function calls itself with progressively smaller numbers until it reaches the base case.

```text
factorial(5)
    |
5 * factorial(4)
    |
5 * 4 * factorial(3)
    |
5 * 4 * 3 * factorial(2)
    |
5 * 4 * 3 * 2 * factorial(1)
    |
120
```

### Example Output

```text
Enter a number: 5
Factorial 5 is 120
```

This feature demonstrates recursive function calls and base cases.

---

# 🔍 4. Filter Data by Threshold

The `filter_data_by_threshold()` function selects values greater than or equal to a user-defined threshold.

It supports both 1D and 2D datasets.

### Implementation

```python
threshold = int(input("Enter a threshold value: "))

filter_data = list(
    filter(lambda x: x >= threshold, data)
)
```

### Concepts Used

- `lambda` creates a small anonymous function.
- `filter()` selects values for which the function returns `True`.
- `list()` converts the filter result into a list.

### Example

Input:

```python
data_1d = [10, 25, 30, 45, 50]
threshold = 30
```

Output:

```text
Filtered Data (values >= 30):
30, 45, 50
```

The filtering condition is:

```python
lambda x: x >= threshold
```

Only values greater than or equal to the specified threshold are included.

---

# ↕️ 5. Sort Data

The `sort_data()` function supports sorting 1D data in ascending or descending order.

For 2D data, it sorts each row independently in ascending order.

### Ascending Order

```python
sorted_list = sorted(data_1d)
```

Example:

```python
data_1d = [40, 10, 50, 20, 30]

sorted_list = sorted(data_1d)

print(sorted_list)
```

Output:

```text
[10, 20, 30, 40, 50]
```

### Descending Order

```python
sorted_list = sorted(data_1d, reverse=True)
```

Output:

```text
[50, 40, 30, 20, 10]
```

### Sorting a 2D Matrix

```python
sorted_2d = []

for row in data_2d:
    sorted_2d.append(sorted(row))
```

Input:

```python
data_2d = [
    [30, 10, 20],
    [60, 40, 50]
]
```

Output:

```text
[10, 20, 30]
[40, 50, 60]
```

The original list is not modified by `sorted()`; the function returns a new sorted list.

---

# 📈 6. Display Dataset Statistics

The `display_dataset_statistics()` function calculates four statistics for the selected dataset:

- Minimum value
- Maximum value
- Total sum
- Average value

The program uses a nested function named `get_statistics()`.

### Implementation

```python
def get_statistics(nums):
    minimum = min(nums)
    maximum = max(nums)
    total = sum(nums)
    avg = total / len(nums)

    return minimum, maximum, total, avg
```

The function returns multiple values, which are unpacked into separate variables.

```python
min_value, max_value, total_value, average_value = get_statistics(data)
```

### Example

Input:

```python
data = [15, 25, 35, 45, 55]
```

Output:

```text
Dataset Statistics:
~ Minimum value: 15
~ Maximum value: 55
~ total value: 175
~ Average value: 35.00
```

This feature demonstrates nested functions, built-in functions, and multiple return values.

---

# 📦 7. `*args` Demonstration

The `demo_args()` function demonstrates how a function can accept a variable number of positional arguments.

### Implementation

```python
def demo_args(*args):
    """Shows how to pass multiple values using *args."""

    print(demo_args.__doc__)

    for arg in args:
        print(f"~ {arg}")
```

### Function Call

```python
demo_args(20, 50, 30, 16, 79)
```

### Example Output

```text
Shows how to pass multiple values using *args.
~ 20
~ 50
~ 30
~ 16
~ 79
```

The `*args` parameter collects the positional arguments into a tuple.

This feature demonstrates flexible function arguments and iteration.

---

# 🗝️ 8. `**kwargs` Demonstration

The `demo_kwargs()` function demonstrates how to pass a variable number of keyword arguments.

### Implementation

```python
def demo_kwargs(**kwargs):
    """Shows how to pass named values using **kwargs."""

    print(demo_kwargs.__doc__)

    for key, value in kwargs.items():
        print(f"~ {key}: {value}")
```

### Function Call

```python
demo_kwargs(
    Dataset_Type="1D List",
    Element_Count=5
)
```

### Example Output

```text
Shows how to pass named values using **kwargs.
~ Dataset_Type: 1D List
~ Element_Count: 5
```

The `**kwargs` parameter collects named arguments into a dictionary.

In the main program, the dataset type and element count are determined from the currently stored data before being passed to this function.

This feature demonstrates keyword arguments, dictionaries, and the `.items()` method.

---

# 🌍 Global Variables and Data Summary

The program defines shared variables outside its functions:

```python
data_1d = []
data_2d = []
```

It also maintains a global summary dictionary:

```python
data_summary = {
    "total_values": 0,
    "min_value": None,
    "max_value": None,
    "sum_of_values": 0,
    "mean_value": 0.0
}
```

The `update_data_summary()` function uses the `global` keyword to reassign the summary dictionary when the supplied data is empty.

```python
def update_data_summary(summary):
    """Updates the summary with the latest data values."""

    global data_summary

    if not summary:
        data_summary = {
            "total_values": 0,
            "min_value": None,
            "max_value": None,
            "sum_of_values": 0,
            "mean_value": 0.0
        }
        return

    data_summary["total_values"] = len(summary)
    data_summary["min_value"] = min(summary)
    data_summary["max_value"] = max(summary)
    data_summary["sum_of_values"] = sum(summary)
    data_summary["mean_value"] = sum(summary) / len(summary)
```

This function demonstrates how to calculate and store summary information in a shared dictionary.

**Implementation note:** The current summary display function calculates statistics directly from the selected data instead of displaying the stored `data_summary` dictionary.

---

# 🧠 Python Concepts Practised

### 🐍 Variables and Data Types

```python
threshold = 30
average = 25.50
data_1d = [10, 20, 30]
```

Practised integers, floating-point values, strings, lists, and dictionaries.

### 📋 Lists and Nested Lists

```python
data_1d = [10, 20, 30]
data_2d = [[10, 20], [30, 40]]
```

Used lists to store and manipulate numerical data.

### 🌍 Global Variables

```python
global data_summary
```

Practised accessing and reassigning a global variable inside a function.

### 🔧 User-Defined Functions

```python
def input_data():
    ...
```

Organized application functionality into separate reusable functions.

### 📖 Docstrings

```python
def sort_data():
    """Sorts the data in ascending or descending order."""
```

Practised documenting functions and accessing their documentation using `__doc__`.

### 🔁 Loops

```python
for row in data_2d:
    for item in row:
        ...
```

Used nested loops to process matrix values.

### 🔀 Conditional Statements

```python
if choice == "1":
    ...
elif choice == "2":
    ...
else:
    ...
```

Handled menu selections and input decisions.

### 🧮 Built-in Functions

```python
len(data)
min(data)
max(data)
sum(data)
sorted(data)
```

Used built-in functions for data processing and analysis.

### 🧠 Recursion

```python
return num * factorial(num - 1)
```

Practised a function calling itself.

### 🔍 Lambda and Filter

```python
filter(lambda x: x >= threshold, data)
```

Practised filtering numerical data using a condition.

### 📤 Multiple Return Values

```python
return minimum, maximum, total, avg
```

Returned multiple results from a function and unpacked them.

### 📦 Variable-Length Arguments

```python
def demo_args(*args):
    ...
```

```python
def demo_kwargs(**kwargs):
    ...
```

Practised accepting flexible positional and keyword arguments.

---

# 📁 Project Structure

```text
PR-4 - Functional Treat/
│
└── Data_analyzer_and_transformer.py

README.md
```

**Note:** This project uses Python's built-in functions and requires no external libraries.

---

# 🚀 How to Run the Project

### 1. Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd "PR-4 - Functional Treat"
```

### 3. Run the Python Program

```bash
python Data_analyzer_and_transformer.py
```

If Python is installed and configured correctly, the main menu will appear in the terminal.

**Requirements:**

- Python 3.x
- A terminal or command prompt
- A code editor such as Visual Studio Code (optional)

---

# 🖥️ Example Application

```text
==================== Welcome to the Data Analyzer and Transformer Program ====================

Main Menu:
1. Input Data (1D or 2D)
2. Display Data Summary (Built-in functions)
3. Calculate Factorial (Recursion)
4. Filter data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. *args Demo
8. **kwargs Demo
9. Exit Program

Enter your choice: 1

==================== Input data ====================
1. Enter 1D array manually (space-separated integers)
2. Enter 2D array (nested list) manually

Please enter your choice (1-2): 1
Enter a data for 1D array (separated by spaces): 10 20 30 40 50

1D array stored succesfully.
```

---

# 📈 Project Learning Outcomes

Through this project, I practised:

- 🐍 Python fundamentals
- 📋 One-dimensional lists and nested lists
- 🌍 Global variables and shared state
- 🔧 User-defined functions
- 📖 Docstrings
- 🔁 For loops and while loops
- 🔀 Conditional statements
- 🧮 Built-in mathematical and data-processing functions
- 🧠 Recursive function calls
- 🔍 Lambda functions and filtering
- ↕️ Sorting numerical datasets
- 📤 Returning multiple values
- 📦 `*args` and `**kwargs`
- 🗂️ Processing structured numerical data
- 🏗️ Building a menu-driven console application

---

# 🔮 Future Enhancements

The project can be extended with the following features:

- 🔎 Search for specific values in a dataset.
- 📊 Calculate the median and mode.
- 📈 Calculate variance and standard deviation.
- 📉 Display data using charts and graphs.
- 📂 Import datasets from CSV files.
- 💾 Save and load datasets using JSON.
- 📋 Export filtered and sorted data to CSV.
- 🧹 Handle invalid input and empty datasets more robustly.
- 🧮 Support floating-point numbers.
- ↕️ Add descending sorting for 2D rows.
- 🔢 Sort an entire matrix rather than only individual rows.
- 🗄️ Integrate NumPy and Pandas for larger datasets.
- 🖥️ Build a graphical user interface.
- 🌐 Convert the application into a web-based data analysis tool.

---

# 🗺️ Project Roadmap

```text
[████████████████████] 100% 1D Data Input

[████████████████████] 100% 2D Data Input

[████████████████████] 100% Data Summary

[████████████████████] 100% Recursive Factorial

[████████████████████] 100% Threshold Filtering

[████████████████████] 100% Data Sorting

[████████████████████] 100% Dataset Statistics

[████████████████████] 100% *args and **kwargs Demo

[░░░░░░░░░░░░░░░░░░░░]   0% CSV Import and Export

[░░░░░░░░░░░░░░░░░░░░]   0% Data Visualization

[░░░░░░░░░░░░░░░░░░░░]   0% NumPy and Pandas Integration
```

*Roadmap percentages describe the planned project stages and can be updated as new features are implemented.*

---

# 🧩 Future Data Science Integration

This project provides a starting point for understanding how numerical data can be processed before applying more advanced data analysis techniques.

The current program uses Python lists and built-in functions. In the future, NumPy and Pandas could provide more advanced data-processing capabilities.

```text
Python Fundamentals
        |
        v
Lists and Nested Lists
        |
        v
Data Processing
        |
        v
Statistical Analysis
        |
        v
NumPy and Pandas
        |
        v
Data Visualization
        |
        v
Data Science and Machine Learning
```

---

# ⭐ Why I Built This Project

I created this project to strengthen my understanding of Python functions, collections, recursion, and data-processing techniques.

Rather than practising each concept separately, I combined multiple Python fundamentals into one interactive application.

The project helped me practise how to:

- Accept and organize numerical input.
- Process 1D and 2D datasets.
- Calculate useful statistics.
- Filter and sort data.
- Apply recursion to mathematical problems.
- Use flexible function arguments.
- Structure a program using reusable functions and a menu-driven interface.

This project is part of my journey toward learning **Python, Data Science, and AI/ML**.

---

# 👨‍💻 About the Developer

<div align="center">

## Python Developer | Data Science and AI/ML Learner

Currently learning and building projects using:

```text
Python
  ↓
Data Structures
  ↓
Functions and Problem Solving
  ↓
Data Analysis
  ↓
Data Science
  ↓
AI / ML
```

</div>

---

# 🌐 Connect With Me

<div align="center">

### GitHub

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nandan-mandaliya-05/)

</div>

---

# ⭐ Support the Project

If you find this project useful or interesting:

- ⭐ **Star** the repository.
- 🍴 **Fork** the repository.
- 💬 **Share** your feedback.
- 🤝 **Connect** with me on GitHub.

Your feedback and suggestions can help improve future versions of this project.

---

<div align="center">

# 🚀 Keep Learning. Keep Building. Keep Growing.

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=750&lines=Python+%7C+Data+Analysis+%7C+Problem+Solving;Build+Projects+%7C+Learn+Concepts+%7C+Grow+Skills;Keep+Learning+%7C+Keep+Building" alt="Animated Footer"/>

<br><br>

**Made with ❤️ and Python by Nandan Mandaliya**

</div>
