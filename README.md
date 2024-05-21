# My First AirBnB Clone Project Version 1

![AirBnB Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240519%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240519T230839Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=abbaba37aebc1f1af202aefbf5acf32d7f9d085cec77429478224680c519a8d8)

## Project Overview

This project is part of the ALX Software Engineering program. It involves creating a simple version of the Airbnb website using a command-line interface (CLI). The CLI allows users to manage and manipulate objects such as users, places, and amenities.

## Command Interpreter Details

The CLI is a tool that lets users interact with the program. It acts as the frontend for the web application and uses Python OOP programming for the backend. The CLI can handle various commands to manage the application's data.

## Example Commands

Here are some example commands the CLI can handle:

- `create <ClassName>`: Creates a new instance of ClassName and saves it.
- `show <ClassName> <id>`: Shows the details of an instance based on ClassName and id.
- `destroy <ClassName> <id>`: Deletes an instance based on ClassName and id.
- `all <ClassName>`: Shows all instances of ClassName. If no class is specified, it shows all instances of all classes.
- `update <ClassName> <id> <attribute name> "<attribute value>"`: Updates an instance based on ClassName and id with a new attribute value.

## How to Get Started

To get started, simply run the project on your local machine.

## Installation

Clone the repository from GitHub using the below command

```sh
git clone https://github.com/Amaka007/AirBnB_clone.git
```

After cloning the `AirBnB_clone` project, you should have access to the following modules in the package:

- `/console.py`: The main executable of the project, the command interpreter.
- `models/engine/file_storage.py`: Class that serializes instances to a JSON file and deserializes JSON file to instances.
- `models/__init__.py`: A unique `FileStorage` instance for the application.
- `models/base_model.py`: BaseModel defines all common attributes and methods for other classes such as User, Place, State, Amenity, etc. Define public instance attributes: id, created_at, and updated_at.
  Implement the **str** method to provide a custom string representation of the instance.
  Implement the save method to update the updated_at timestamp.
  Implement the to_dict method to return a dictionary representation of the instance.

- `models/user.py`: User class inherits from BaseModel.
- `models/state.py`: State class inherits from BaseModel.
- `models/city.py`: City class inherits from BaseModel.
- `models/amenity.py`: Amenity class inherits from BaseModel.
- `models/place.py`: Place class inherits from BaseModel.
- `models/review.py`: Review class inherits from BaseModel.

## How to Use It

You can use this program in **Interactive** and **Non-interactive** modes

### Interactive Mode

Interactive mode allows continuous interaction until you exit the program.

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) quit
$
```

### Non-Interactive Mode

Non-interactive mode allows you to piped into the shell for execution without showing a prompt.

```sh
$ echo "help" | ./console.py

Documented commands (type help <topic>):
========================================
EOF  help  quit

$
$ cat test_help
help
$
$ cat test_help | ./console.py

Documented commands (type help <topic>):
========================================
EOF  help  quit

$
```

## Command Input Format

Use `echo` to pipe commands using the non-interactive mode.

In Interactive mode, you simply type commands at the prompt and press Enter to execute the command or show an error message if it fails. You can exit the console using either `CTRL + D`, `CTRL + C`, `quit`, or `EOF`.

## Arguments

Most commands accept arguments separated by spaces.

Example:

```sh
user@ubuntu:~/AirBnB_clone$ ./console.py
(hbnb) create BaseModel
389ft56a-64j3-0s9r-2243-853hfd56jds3
user@ubuntu:~/AirBnB_clone$ ./console.py
```

or

```sh
user@ubuntu:~/AirBnB_clone$ echo "create BaseModel" | ./console.py
(hbnb)
j4563dd5-64j3-0s9r-2243-853hfd56jds3
(hbnb)
user@ubuntu:~/AirBnB_clone$ ./console.py
```

## Available Commands and What They Do

| Command         | Description                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| **quit or EOF** | Exits the program                                                                                             |
| **Usage**       | No additional parameter. Use it by itself                                                                     |
| **help**        | Provides a text describing how to use a command.                                                              |
|                 |
| **Usage**       | No additional parameter. Use it by itself or **help <command>**                                               |
|                 |
| **destroy**     | Deletes an instance using the class name and `id` and dumps the change into a JSON file.                      |
|                 |
| **Usage**       | **destroy <class name> <id>** --or-- **<class name>.destroy(<id>)**                                           |
|                 |
| **all**         | Return all string representation of all instances based or not on the class name.                             |
|                 |
| **Usage**       | No additional parameter. Use it by itself or **all <class name>** --or-- **<class name>.all()**               |
|                 |
| **update**      | Updates an instance using the class name and `id` by adding or updating attributes into a JSON file then save |
|                 |
| **Usage**       | **update <class name> <id> <attribute name> "<attribute value>"** --or-- **<class name>.update(...)**         |

                        |

| **create** | Creates a new instance of a valid `Class`, saves it to the JSON file, and prints the `id`.  
 |
| **Usage** | **create <class name>** |
| **show** | Returns the string representation of an instance using the class name and `id`.  
 |
| **Usage** | **show <class name> <id>** --or-- **<class name>.show(<id>)**  
 |
| **count** | Loads the number of class instance  
 |
| **Usage** | **<class name>.count()** |

## Authors

- **Eze Harrison** | [Harystyleseze](mailto:harystyleseze@gmail.com)
- **Martina Okeke** | [Amaka007](mailto:real4amy@gmail.com)

