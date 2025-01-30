# Python-mysql-Student-Management-System
# Student Management System using MySQL Connector

## Project Overview
This is a simple student management application that uses Python and MySQL for basic database operations such as creating tables, adding, viewing, updating, and deleting student records.

## Features
- Connects to a local MySQL database.
- Creates a `STUDENTS1` table if it doesn't already exist.
- Supports operations such as:
  - Viewing all student records.
  - Adding a new student.
  - Removing a student.
  - Updating student information (name or roll number).

## Prerequisites
To run this project, you need to have the following installed on your system:
- Python 3.x
- MySQL Server
- MySQL Connector for Python (`mysql-connector-python`)

## Installation
### Step 1: Install MySQL Connector
```bash
pip install mysql-connector-python 

```

### Step 2: Setup MySQL Database
1. Open MySQL Workbench or your preferred MySQL client.
2. Create a database using the following SQL query:
   ```sql
   CREATE DATABASE your_database(here DB_4_1);
   ```
3. Grant necessary privileges to your MySQL user (`root` in this example).

## Configuration
Modify the database connection details in the code according to your setup:
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    auth_plugin="mysql_native_password",
    database="your_database(here DB_4_1)"
)
```

## Usage
1. Clone or download this repository.
2. Run the Python file using:
   ```bash
   python <filename>.py
   ```
3. Interact with the menu to perform operations.

### Menu Options
- **1. View all students:** Displays all student records.
- **2. Add new student:** Prompts for name and roll number to insert a new student record.
- **3. Remove student:** Deletes a student by name.
- **4. Update information:** Allows updating the name or roll number of a student.
- **5. Exit:** Exits the program.

## Code Breakdown
### Connecting to the Database
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anu@14aug",
    auth_plugin="mysql_native_password",
    database="DB_4_1"
)
```
This code establishes the connection to the MySQL database.

### Table Creation
```python
mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENTS1(NAME VARCHAR(20), ROLL_NO INT)")
```
Ensures that the `STUDENTS1` table exists before any operations.

### CRUD Functions
- `show()`: Fetches and displays all student records.
- `add()`: Inserts a new student into the table.
- `remove()`: Deletes a student by name.
- `update()`: Updates either the name or roll number of a student.

## Example Usage
```
**----Welcome to Classroom----**
Enter the choice: 
1. View all students
2. Add new student
3. Remove student
4. Update information of student
5. Exit
```

## Security Note
- Ensure the password is stored securely in production environments by using environment variables or configuration files.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Contact
For any inquiries or issues, please contact me on linkedIn

