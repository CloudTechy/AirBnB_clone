
---

# AirBnB Clone Project

## Description
Welcome to the AirBnB clone project! This project aims to create a simplified version of the popular AirBnB platform. The first step involves building a command-line interpreter (CLI) to manage AirBnB objects such as users, states, cities, and places. This CLI serves as the foundation for the subsequent development of the full web application.

## Command Interpreter
The command interpreter allows users to interact with AirBnB objects through a command-line interface. Users can create, retrieve, update, and delete objects, as well as display information about objects.

### How to Start
To start the command interpreter, follow these steps:
1. Clone this repository to your local machine:
   ```
     git clone https://github.com/your-username/airbnb-clone.git
   ```
 2. Navigate to the project directory:
   ```
     cd airbnb-clone
   ```
 3. Run the command interpreter:
   ```
     python console.py
   ```

### How to Use
Once the command interpreter is running, you can use the following commands:
   - `create <class_name>`: Create a new instance of the specified class.
   - `show <class_name> <id>`: Show details of a specific instance.
   - `update <class_name> <id> <attribute_name> "<new_value>"`: Update an attribute of a specific instance.
   - `destroy <class_name> <id>`: Delete a specific instance.
   - `all <class_name>`: Show all instances of a specified class.
   - `quit`: Exit the command interpreter.

### Examples
Here are some examples of how to use the command interpreter:

  1. Creating a new User:
    ```
     (hbnb) create User
    ```

  2. Showing details of a State with ID `1234-5678`:
    ```
      (hbnb) show State 1234-5678
    ```

  3. Updating the name of a City with ID `9876-5432`:
    ```
	(hbnb) update City 9876-5432 name "New City Name"
    ```

  4. Deleting a Place with ID `1111-2222`:
    ```
    (hbnb) destroy Place 1111-2222
    ```

  5. Showing all instances of the User class:
    ```
    (hbnb) all User
   ```

   ---
