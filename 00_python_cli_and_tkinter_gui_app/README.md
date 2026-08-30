# 👋 Say Hello Software — Version 1.1.0

A Python application that greets users by name through both **Console** **and** **GUI (Tkinter)** interfaces — built as a full **Software Development Life Cycle (SDLC)** project with complete documentation, testing, architecture, and design specifications.

> **Repository:** https://github.com/tummytucker94/say_hello  

---

# 📜 Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Objectives & Scope](#objectives--scope)  
4. [System Architecture](#system-architecture)  
5. [Implementation](#implementation)  
6. [Testing](#testing)  
7. [Documentation](#documentation)  
8. [Repository Structure](#repository-structure)  
9. [How to Run](#how-to-run)  
10. [Version History](#version-history)  
11. [Contributing](#contributing)  
12. [License](#license)  

---

# 🧭 Project Overview

**Purpose:**  
To gain hands-on SDLC experience by building a real, multi-interface application with full documentation and testing.

**Summary:**  
Say Hello Software started as a console-only greeting program (v1.0.0).  
In **v1.1.0**, the project expanded with:

- A **Tkinter GUI**
- A **layered architecture** (core + adapters)
- Modular design for testability and scalability
- Updated documentation (URS, SRS, SysRS, SDS, Architecture, Testing)

---

# ✨ Features

### **Console Mode**
- Prompts user for their name
- Outputs a greeting in the terminal

### **GUI Mode (Tkinter)**
- Text entry field  
- “Greet” button  
- Greeting output label  
- Persistent window  
- Fast response time (<2 seconds)
- 

### **Shared Core Logic**
Both UIs use:

```python
greeting(name)
````

Located in:

```
src/core/functions/greetings.py
```

---

# 🎯 Objectives & Scope

### **In Scope**

* Console input/output
* GUI input/output
* Shared greeting logic
* Handling blank / whitespace names
* Cross-platform Python support

### **Out of Scope**

* Persistent storage
* Networking
* Multi-language support

### **Performance**

* Console response < **1 second**
* GUI response < **2 seconds**

---

# 🧠 System Architecture

### **Layered Architecture**

```
+-----------------------------+
|     Application Layer       |
|-----------------------------|
| Console: main.py            |
| GUI: gui_main.py            |
+-----------------------------+
             ↓
+-----------------------------+
|        Core Logic           |
|-----------------------------|
| greeting()                  |
| in greetings.py             |
+-----------------------------+
```

### Components

* **Console Adapter:** `src/main.py`
* **GUI Adapter:** `src/adapters/tkinter/gui_main.py`
* **Core Logic:** `src/core/functions/greetings.py`

---

# 🔧 Implementation

### Environment & Dependencies

* **Python:** 3.x
* **Libraries:** Tkinter (built-in), Standard Library
* **Optional:** `pytest`, `pytest-cov`

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
```

---

### Run Console Version

```bash
python src/main.py
```

### Run GUI Version

```bash
python src/adapters/tkinter/gui_main.py
```

---

# 🧪 Testing

### **Testing Levels**

* Unit tests (core logic)
* Integration tests (console + GUI)
* Functional tests
* Performance testing

### **Run Tests**

```bash
pip install -r requirements.txt
pytest -v
```

### Optional Coverage

```bash
pytest --cov=src --cov-report=term-missing
```

---

# 📄 Documentation

All SDLC documentation is stored in:

```
docs/
```

### Included Documents

| Document              | Description                          |
| --------------------- | ------------------------------------ |
| **URS.md**            | User Requirements Specification      |
| **SRS.md**            | Software Requirements Specification  |
| **SysRS.md**          | System Requirements Specification    |
| **architecture.md**   | High-level system architecture       |
| **design_spec.md**    | Detailed SDS / internal design       |
| **Testing_Phase.md**  | Testing strategy, cases, and results |
| **Implementation.md** | Implementation log + commit record   |

---

# 📁 Repository Structure

```
say_hello/
├── docs/
│   ├──1_Planning/
│   │   ├── URS.md
│   │   ├── SRS.md
│   │   ├── SysRS.md
│   ├──2_Design/
│   │   ├── architecture.md
│   │   ├── design_spec.md
│   ├──3_Implementation/
│   │   └── Implementation.md
│   ├──4_Testing/
│   │   └── Testing_Phase.md
│   └──5_Maintenance/
│       └── CHANGELOG.md
│
├── src/
│   ├── core/
│   │   └── functions/
│   │       └── greetings.py
│   ├── adapters/
│   │   └── tkinter/
│   │       └── gui_main.py
│   └── main.py
│
├── tests/
│   ├── test_greetings.py
│   └── test_gui_tkinter.py
│
└── README.md
```

---

# 🕒 Version History

## **v1.1.0 — Current Version**

✔ Added Tkinter GUI
✔ Added layered architecture
✔ Updated URS, SRS, SysRS, SDS, Architecture, Testing docs
✔ Added GUI test cases
✔ Updated repository structure
✔ Improved modular design
✔ Updated README.md

## **v1.0.0 — Initial Version**

✔ Console-only application
✔ Basic greeting logic
✔ Initial documentation set
✔ Basic unit tests

---

# 🤝 Contributing

1. Fork the repository
2. Create a feature branch:

   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit:

   ```bash
   git commit -m "Description of change"
   ```
4. Push:

   ```bash
   git push origin feature/new-feature
   ```
5. Open a Pull Request

---

# ⚖ License

This project is licensed under the **MIT License**.
See the `LICENSE` file for details.

---

# 👤 Author

**Jermaine Tucker**
Version **1.1.0**
Last Updated **2025**

```# 📚 Combined Documentation — Say Hello Software (v1.1.0)

This document compiles all major Markdown files into a **single unified specification**:

- URS.md
- SRS.md
- SysRS.md
- Architecture.md
- Design_Spec.md (SDS)
- Testing_Phase.md

---

# 🧩 User Requirements Specification (URS)

## Version 1.1.0 — Current Requirements

### URS-10 — GUI Window Interaction
User shall be able to open a graphical window.

### URS-11 — GUI Input Field
System shall provide a text entry field.

### URS-12 — Greet Button
System shall provide a button that triggers greeting.

### URS-13 — GUI Greeting Display
Greeting shown via label/popup.

### URS-14 — Shared Logic
Console + GUI must use `greeting()`.

### URS-15 — Performance
GUI must respond within 2 seconds.

### URS-16 — Multiple Attempts
User can generate multiple greetings.

### URS-17 — Blank Input Handling
Blank input → "Hello there!".

### URS-18 — Accessibility & Usability
Readable text, clickable buttons.

### URS-19 — Window Persistence
GUI window stays open until closed.

### URS-20 — Console/GUI Parity
Both UIs must behave identically.

---

## URS v1.0.0 — Historical
Console-only requirements preserved.

---

# 📘 Software Requirements Specification (SRS)

## Version 1.1.0 — Current Requirements

### Console Functional Requirements
- SRS-F-01 console prompt
- SRS-F-02 send input to `greeting()`
- SRS-F-03 display output

### GUI Functional Requirements
- SRS-F-04 GUI window with entry + button
- SRS-F-05 button sends input to `greeting()`
- SRS-F-06 display greeting

### Core Logic Requirements
- SRS-F-07 logic in `greeting()`
- SRS-F-08 trim whitespace
- SRS-F-09 blank → "Hello there!"
- SRS-F-10 name → "Hello <Name>!"

### Non‑Functional Requirements
- SRS-N-01 console <1s
- SRS-N-02 GUI <2s
- SRS-N-03 PEP8
- SRS-N-04 cross-platform
- SRS-N-05 modular architecture

---

## SRS v1.0.0 — Historical
Console‑only behavior.

---

# 🖥 System Requirements Specification (SysRS)

## Version 1.1.0 — Current Requirements

### SysRS-01 — System Interfaces
Console + GUI interfaces.

### SysRS-02 — Unified Core Logic Access
All UIs call `greeting()`.

### SysRS-03 — Input Acquisition
Console input + Tkinter Entry.

### SysRS-04 — Greeting Generation
Whitespace trimming, default message, valid name output.

### SysRS-05 — Output Display
Console print + GUI label/popup.

### SysRS-06 — Multi-Attempt Support
Multiple greetings in one session.

### SysRS-07 — System Performance
Console <1s, GUI <2s.

### SysRS-08 — Validation and Stability
No crashes from blank input.

### SysRS-09 — Environment Compatibility
Runs on Windows/macOS/Linux.

### SysRS-10 — Architectural Constraints
Layered architecture: core + adapters.

---

## SysRS v1.0.0 — Historical
Console-only, no GUI elements.

---

# 🧱 Architecture Specification

## 1. Purpose
Describes the high-level architecture of Say Hello Software v1.1.0.

## 2. Architecture Goals
- Separation of concerns
- Reusability
- Testability
- Extensibility
- Simplicity

## 3. Layered Architecture
```

+---------------------------+

| Application / Adapters        |
| ----------------------------- |
| Console (main.py)             |
| GUI (gui_main.py)             |
| +---------------------------+ |

```
        ↓
```

+---------------------------+

| Core Logic                    |
| ----------------------------- |
| greeting() in greetings.py    |
| +---------------------------+ |

```

## 4. Components
### Console Adapter
Handles input/output via terminal.

### GUI Adapter
Tkinter window, entry, button, label.

### Core Logic
Implements `greeting(name)`.

---

# 🛠 Software Design Specification (SDS)

## Version 1.1.0 — Current Design

### 1. Purpose
Defines detailed internal design.

### 2. Design Inputs
- URS v1.1.0
- SysRS v1.1.0
- SRS v1.1.0

### 3. Modules
- `main.py` — console adapter
- `gui_main.py` — GUI adapter
- `greeting()` — core logic

### 4. Data Design
| Variable | Type | Purpose |
|---------|------|----------|
| name | str | raw user input |
| greeting_msg | str | final greeting |

### 5. Interfaces
- Console I/O
- Tkinter widgets
- Shared core logic

### 6. Algorithms
- Trim input
- Select default or personalized output

### 7. Error Handling
- Blank input safe
- GUI safe updates

### 8. Testability
- Core logic unit-tested
- Console/GUI integration tests

---

# 🧪 Testing Phase

## 1. Objective
Test console + GUI behavior using unit, integration, and functional tests.

## 2. Strategy
- Pytest for automation
- Manual GUI testing

## 3. Test Cases
Core, console, and GUI test tables included.

## 4. Results
All tests passed.

## 5. Acceptance Criteria
- Correct greetings
- Performance thresholds
- No crashes

---

```

