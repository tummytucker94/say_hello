# 👋 Say Hello Software

A simple Python console application that greets users by name — built to practice the **Software Development Life Cycle (SDLC)** from planning to maintenance.

> Repository: [https://github.com/tummytucker94/say_hello](https://github.com/tummytucker94/say_hello)

---

## 📜 Table of Contents

1. [Project Overview](#project-overview)
2. [Objectives & Scope](#objectives--scope)
3. [System Design](#system-design)
4. [Implementation](#implementation)
5. [Testing](#testing)
6. [Maintenance](#maintenance)
7. [Repository Structure](#repository-structure)
8. [How to Run](#how-to-run)
9. [Contributing](#contributing)
10. [License](#license)

---

## 🧭 Project Overview

**Purpose:**
To gain hands-on experience building software using the **SDLC** process while creating a functional console application.

**Problem Definition:**

> “I want to create a software that greets the user when they enter their name because I want to gain experience creating software using the SDLC process.”

**Goal:**

* Learn to plan, design, code, test, and maintain a Python application end-to-end.

**Objective:**

* Develop a console program that greets the user based on their name input and handles blank or whitespace inputs gracefully.

---

## 🎯 Objectives & Scope

### In Scope

* Accepting user name input
* Printing a personalized greeting
* Handling blank or whitespace-only input

### Out of Scope

* GUI design
* Saving or storing user data
* Complex validation

**Performance Requirement:**

* Must respond in under **1 second**

---

## 🧠 System Design

### Architecture

* **Type:** Single-module, sequential console application
* **Language:** Python 3.x
* **Platform:** macOS / Linux / Windows (any Python-supported environment)

### Execution Flow

1. Start
2. Prompt user for name
3. Read and validate input
4. Display greeting
5. End

### Pseudocode

```text
BEGIN
  DISPLAY "Enter your name: "
  READ user_name
  IF user_name IS empty THEN
      greeting_msg ← "Hello there!"
  ELSE
      greeting_msg ← "Hello " + user_name
  ENDIF
  DISPLAY greeting_msg
END
```

### Data Dictionary

| Name           | Type   | Description                  |
| -------------- | ------ | ---------------------------- |
| `user_name`    | string | Name entered by the user     |
| `greeting_msg` | string | Constructed greeting message |

---

## 🔧 Implementation

### Environment & Dependencies

* **Language:** Python 3.x
* **External Libraries:** None (standard library only)
* **Virtual Environment:** `.venv/` created with

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

### How to Build & Run

```bash
# Clone the repo
git clone https://github.com/tummytucker94/say_hello.git
cd say_hello

# (Optional) Create virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux

# Run the program
python src/main.py
```

### Coding Standards

* PEP 8 style conventions
* Use of f-strings for formatting
* Single-purpose, well-named functions
* Input sanitized with `.strip()` and defaults to “there” if blank

---

## 🤪 Testing

### Strategy

* **Level:** Unit & functional (console I/O)
* **Method:** Manual black-box + automated pytest
* **Framework:** `pytest`, `pytest-cov` (optional)
* **Performance:** Must execute under 1 second

### Test Cases

| ID  | Description    | Input                              | Expected Output                           |
| --- | -------------- | ---------------------------------- | ----------------------------------------- |
| TC1 | Typical name   | Jermaine                           | Hello Jermaine!                           |
| TC2 | Alternate name | Maria                              | Hello Maria!                              |
| TC3 | Blank input    | [Enter]                            | Hello there!                              |
| TC4 | Spaces only    | `" "`                              | Hello there!                              |
| TC5 | Long name      | Supercalifragilisticexpialidocious | Hello Supercalifragilisticexpialidocious! |
| TC6 | Performance    | Any                                | Response < 1 s                            |

### How to Run Tests

```bash
# Install dependencies
pip install pytest pytest-cov

# Run tests
pytest -v

# Optional coverage
pytest --maxfail=1 --disable-warnings -q --cov=src --cov-report=term-missing
```

All tests should **pass** with 100 % success and sub-1 second response time.

---

## 🛠️ Maintenance

### Versioning

Semantic Versioning: **MAJOR.MINOR.PATCH**

```bash
git tag -a v1.0.0 -m "Initial release"
git push --tags
```

### Change Control

1. Update documentation (SRS/SDS) if functionality changes
2. Write or modify tests first (TDD)
3. Implement change → PR → Review → Merge

### KPIs

| Metric                  | Target                        |
| ----------------------- | ----------------------------- |
| Mean Time to Fix (MTTR) | < 1 day                       |
| Test Pass Rate          | 100 %                         |
| Docs Freshness          | Updated within 24 h of change |

---

## 📁 Repository Structure

```
# SAY_HELLO Repository Structure

SAY_HELLO/
├── .pytest_cache/
├── .venv/
├── docs/
│   ├── 1_Planning/
│   │   ├── Project_Overview.md
│   │   ├── SRS.md
│   │   ├── SysRS.md
│   │   └── URS.md
│   ├── 2_Design/
│   │   ├── architecture.md
│   │   └── design_spec.md
│   ├── 3_Implementation/
│   │   └── Implementation.md
│   ├── 4_Testing/
│   │   └── TestPlan.md
│   └── 5_Maintenance/
├── src/
│   ├── functions/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── greetings.py
│   ├── __init__.py
│   ├── main.py
│   └── runtime.log
├── tests/
│   └── test_greetings.py
├── README.md
└── runtime.log

```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push branch (`git push origin feature/new-feature`)
5. Submit a pull request

---

## ⚖️ License

This project is open-sourced under the **MIT License**.
See `LICENSE` for details.

---

**Author:** Jermaine Tucker
**Version:** 1.0.0
**Last Updated:** November 2025


