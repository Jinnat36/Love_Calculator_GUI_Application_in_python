# Love_Calculator_GUI_Application_in_python
# Love Calculator GUI Application

## Description
This is a simple Love Calculator GUI application built using Python's `tkinter` module. The application takes two names as input and calculates a random "love percentage" between them.

## Features
- Graphical User Interface (GUI) created using `tkinter`
- Randomly generates a love percentage between 0% to 99%
- User-friendly and easy to use

## Prerequisites
- Python 3.x
- `tkinter` module (usually comes pre-installed with Python)

## How to Run the Application
1. Ensure you have Python installed on your system.
2. Save the provided code in a Python file, e.g., `love_calculator.py`.
3. Run the Python file using the command:
   ```
   python love_calculator.py
   ```
4. The Love Calculator GUI window will open.

## Code Explanation
- **Importing Modules**:
  ```python
  from tkinter import *
  import random
  ```

- **Creating Main Window**:
  ```python
  root = Tk()
  root.geometry('300x200')
  root.title("Love Calculator GUI application in Python")
  ```

- **Setting Fonts**:
  ```python
  f = ("Comic Sans MS", 10, "bold")
  font_for_names = ("Times", 10, "bold")
  ```

- **Defining the Love Calculator Function**:
  ```python
  def love_calculator():
      st = '0123456789'
      d = 2
      temp = "".join(random.sample(st, d))
      result_label.config(text=temp + "%")
  ```

- **Creating GUI Elements**:
  - **Heading**:
    ```python
    heading = Label(root, text="\U0001F970 LOVE CALCULATOR \U0001F970", fg='red', font=f)
    heading.pack()
    ```
  - **Your Name**:
    ```python
    f_name = Label(root, text="YOUR NAME :", font=font_for_names)
    f_name.pack()
    name1 = Entry(root)
    name1.pack()
    ```
  - **Partner's Name**:
    ```python
    l_name = Label(root, text="PARTNER'S NAME :", font=font_for_names)
    l_name.pack()
    name2 = Entry(root)
    name2.pack()
    ```
  - **Calculate Button**:
    ```python
    b = Button(root, text="Calculate Love %", command=love_calculator, background="red")
    b.pack(pady=10)
    ```
  - **Result Label**:
    ```python
    result_label = Label(root, text="")
    result_label.pack()
    ```

- **Running the Application**:
  ```python
  root.mainloop()
  ```

## Usage
1. Enter your name in the "YOUR NAME" field.
2. Enter your partner's name in the "PARTNER'S NAME" field.
3. Click on the "Calculate Love %" button.
4. The result will be displayed below the button.

## License
This project is licensed under the MIT License.

## Author
[Jinnat Ara Khatun]

Output :--
![Screenshot 2024-07-05 131638](https://github.com/Jinnat36/Love_Calculator_GUI_Application_in_python/assets/157870456/05845102-f017-42f3-9f03-d9f829307be5)![Screenshot 2024-07-05 131748](https://github.com/Jinnat36/Love_Calculator_GUI_Application_in_python/assets/157870456/e9479e51-1818-448f-9cdb-cc455d898847)

