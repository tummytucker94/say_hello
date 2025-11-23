````markdown
# 🧱 Architecture Specification
## Say Hello Software — Version 1.1.0

## 1. Purpose
This document describes the **high-level architecture** of the Say Hello Software for version **1.1.0**. It explains how the system is structured into layers and modules, how data flows between them, and how the architecture satisfies the requirements in **URS.md**, **SysRS.md**, and **SRS.md**.

The current architecture extends the original v1.0.0 console-only design with:
- A **layered structure** (core + adapters)
- A **Tkinter GUI interface** alongside the console interface
- A shared core function `greeting()` used by both interfaces

---

## 2. Architectural Goals
- **Separation of Concerns**: Keep UI logic separate from core business logic.
- **Reusability**: Allow multiple interfaces (console, GUI, future web/API) to reuse the same greeting logic.
- **Testability**: Make core logic easy to unit test in isolation.
- **Extensibility**: Enable future additions (e.g., new UIs) with minimal changes.
- **Simplicity**: Maintain a clear, understandable structure suitable for learning SDLC.

---

## 3. Layered Architecture Overview

At a high level, the system is organized into **two main layers**:

1. **Application / Adapter Layer**  
   Responsible for interacting with users and adapting inputs/outputs to the core logic.

2. **Core Logic Layer**  
   Contains the reusable greeting logic independent of any UI technology.

```text
+---------------------------+
|   Application / Adapters  |
|---------------------------|
|  Console (main.py)        |
|  GUI (gui_main.py)        |
+---------------------------+
            ↓
+---------------------------+
|       Core Logic          |
|---------------------------|
| greeting() in             |
| core/functions/greetings  |
+---------------------------+
````

---

## 4. Components and Responsibilities

### 4.1 Application / Adapter Layer

**4.1.1 Console Interface (`src/main.py`)**

* Starts the application in console mode.
* Prompts the user to enter their name.
* Reads input from standard input.
* Calls `greeting(name)` from the core layer.
* Prints the returned message to standard output.

**4.1.2 GUI Interface (`src/adapters/tkinter/gui_main.py`)**

* Starts the Tkinter window.
* Renders:

  * A label/title
  * A text entry field for the name
  * A **Greet** button
  * A label or popup to display the greeting
* On button click:

  * Reads the text from the entry widget
  * Calls `greeting(name)` from the core layer
  * Updates the greeting label or popup

The adapter layer **does not** implement any greeting logic; it simply formats inputs/outputs and delegates to the core.

---

### 4.2 Core Logic Layer

**4.2.1 Greeting Logic (`src/core/functions/greetings.py`)**

* Defines the function `greeting(name: str) -> str`.
* Responsibilities:

  * Trim whitespace from the input string.
  * If the result is empty → return `"Hello there!"`.
  * Otherwise → return `"Hello <Name>!"`.
* Contains no UI-specific code.
* Acts as the **single source of truth** for greeting behavior.

---

## 5. Data Flow

### 5.1 Console Flow

1. User runs `python src/main.py`.
2. Console prompts **"Enter your name:"**.
3. User types a name (or leaves blank) and hits Enter.
4. `main.py` passes the raw input to `greeting()`.
5. `greeting()` returns a formatted greeting string.
6. `main.py` prints the greeting to the console.

### 5.2 GUI Flow

1. User runs `python src/adapters/tkinter/gui_main.py`.
2. Tkinter window opens with text field + **Greet** button.
3. User types a name and clicks **Greet**.
4. `gui_main.py` reads the text from the entry widget.
5. `gui_main.py` passes the string to `greeting()`.
6. `greeting()` returns a formatted greeting string.
7. `gui_main.py` updates the greeting label or popup with the result.

---

## 6. Deployment View

The application is a **single-node**, local Python program. There is no client–server split and no external services.

* Runs as a local process on the user’s machine.
* Requires only Python 3.x and Tkinter.
* No database, no network dependencies.

```text
+---------------------------+
|   User Machine            |
|---------------------------|
| Python 3.x                |
| Say Hello Software        |
| - Console app             |
| - Tkinter GUI             |
+---------------------------+
```

---

## 7. Architectural Compliance with Requirements

* **URS-10 – URS-13 (GUI)**: Implemented via `gui_main.py` in the adapter layer.
* **URS-14 / SysRS-02 / SRS-F-07**: Shared `greeting()` function in core layer.
* **URS-15 / SysRS-07 / SRS-N-01/02**: Performance guided by simple, synchronous logic.
* **URS-20 (Parity)**: Both adapters call the same core function.
* **SysRS-10 / SRS-N-05**: Layered, modular architecture.

---

## 8. Future Extensions

The current architecture supports several easy extensions:

* Add a **web interface** (e.g., Flask) as another adapter that calls `greeting()`.
* Add localization support by layering a formatting component around `greeting()`.
* Add logging decorators around core functions without changing UI code.

---

**End of architecture.md**