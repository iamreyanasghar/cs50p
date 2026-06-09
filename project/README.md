# CLI Task Manager
### Video Demo: [Watch Demo Here](https://www.youtube.com/watch?v=CDgWpPr0jz4)

# Description:

## Overview

CLI Task Manager is a terminal-based task management application built with Python. It allows users to manage their daily to-do list directly from the command line — no GUI, no internet connection, no unnecessary complexity. The project was built as the final submission for CS50's Introduction to Programming with Python by Harvard University.

The application greets the user with a clean, emoji-styled main menu and lets them add, view, and remove tasks through simple numbered options. It is designed to be minimal, readable, and easy to extend.

---

## Features

- **Add Tasks** — Prompts the user for a task name and stores it in memory. Task names are automatically title-cased for consistency.
- **View Tasks** — Displays all current tasks in a neatly formatted table using the `tabulate` library, with index numbers for easy reference.
- **Remove Tasks** — Supports removal by either the task's index number or its exact name, giving the user flexibility.
- **Save & Exit** — Exits the program cleanly with a confirmation message.
- **Input Validation** — Invalid menu choices are caught and handled with a friendly error message, keeping the loop running without crashing.


---

## Project Structure

```
project/
├── main.py            # Entry point, menu loop, input validation
├── operations.py      # Core task logic: add, view, remove
├── test_functions.py  # pytest-based unit tests
└── requirements.txt   # Project dependencies
```

### `main.py`

Contains the main() function which runs an infinite loop displaying the menu. It reads the user's choice, validates it using the valid() helper, and delegates to the appropriate function in operations.py using a match statement. Invalid inputs raise a ValueError which is caught and handled gracefully.

### `operations.py`

Holds the in-memory tasks list and three core functions:

- `add()` — reads a task from the user, title-cases it, appends it to the list, and returns a confirmation string.
- `view()` — returns a plain-text table of all tasks using `tabulate`, or a helpful message if the list is empty.
- `remove()` — accepts either an index or a task name, handles both cases, and returns a meaningful result or error message.

### `test_functions.py`

Contains four pytest unit tests covering the core operations. It uses `unittest.mock.patch` to simulate user input without requiring actual keyboard interaction. A `reset_tasks` fixture ensures each test starts with a clean state by clearing the shared tasks list before and after every test.

---

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python main.py
```

3. Run tests:

```bash
pytest test_functions.py
```

---

## Dependencies

| Package          | Purpose                        |
|------------------|--------------------------------|
| `tabulate`       | Formats task list as a table   |
| `pytest`         | Unit testing framework         |
| `unittest.mock`  | Mocking user input in tests    |

---

> **Note:** Tasks are stored in memory only. All data will be lost once the program is closed, as there is no local storage or file persistence.

## Design Decisions

The tasks list is kept in memory (in `operations.py`) rather than persisted to a file to keep the scope focused on core Python concepts. The separation between `main.py` and `operations.py` keeps the menu logic and business logic decoupled, making the code easier to test and maintain. Using `match` instead of `if/elif` chains in `main.py` improves readability and reflects modern Python (3.10+) style.
