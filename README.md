# Task Tracker

[![test and linting](https://github.com/leoreinmann/tast-tracker/actions/workflows/ci.yml/badge.svg)](https://github.com/leoreinmann/tast-tracker/actions/workflows/ci.yml)
[![License: MIT](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c34_License-MIT-blue.svg)](/LICENSE)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Contributing](#contributing)
- [License](#license)

Task tracker is a simple CLI tool to add, update, delete, and list tasks.

## Installation

1. Clone the repository:

  ```bash
   git clone git@github.com:leoreinmann/tast-tracker.git
  ```

2. Install dependencies:

  ```bash
   poetry install
   ```

## Usage

To run the project, use the following command:
```bash
todo add "Buy coffee"
```
Below are the different options listed: 

| Option | Argument(s)                          | Explanation                                          |
|--------|--------------------------------------|------------------------------------------------------|
| add    | id: int, description: string         | Add a new task with an ID and description            |
| update | id: int, description: string         | Update an existing task by ID with a new description |
| delete | id: int                              | Delete a task by its ID                              |
| mark   | id: int, choice: (in-progress, done) | Mark a task as in-progress or done                   |
| list   | choice: [done, todo, in-progress]    | Optionally filter tasks based on their status        |

## Data structure

The data is saved in a json file with following structure:
```json
{
  "id_count": 2,
  "tasks": [
    {
      "id": 1,
      "description": "Buy coffee",
      "status": "todo",
      "createdAt": "2024-08 19-14:43",
      "updatedAt": "2024-08 19-14:43"
    }
  ]
}
```


## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.

## License
This project is licensed under the [MIT License](LICENSE).




