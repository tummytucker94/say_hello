```markdown
# 🧩 Software Design Specification (SDS)
## Say Hello Software — Version 1.1.0

This SDS describes the **updated design** for the Say Hello Software after the introduction of:
- A **layered architecture** (core + adapters)
- A **Tkinter GUI interface**
- Shared logic through the `greeting()` function

The original v1.0.0 SDS is preserved below for historical continuity and SDLC traceability.

---

# 📘 1. Purpose
The purpose of this SDS is to describe how the software is designed internally, how modules interact, and how the design satisfies the SRS, SysRS, and URS for **version 1.1.0**.

Version 1.1.0 expands the system from a console-only application to a **dual-interface design** (Console + GUI), supported by a reusable and isolated core logic module.

---

# 📘 2. Design Inputs
This design is informed by the following requirements documents:
- **URS v1.1.0** – User expectations for both GUI and console behavior
- **SysRS v1.1.0** – System-level interface behavior and architecture
- **SRS v1.1.0** – Detailed functional, non-functional, and core logic requirements

Historical references:
- URS v1.0.0
- SysRS v1.0.0
- SRS v1.0.0

---

# 📘 3. Architectural Overview
Version 1.1.0 adopts a **layered architecture**:

## 3.1 Architecture Style
- **Layered / Modular Architecture**
- **Adapters → Core Logic → Output** pipeline
- UI layers do not contain business logic

## 3.2 Components

### **Application / Adapter Layer**
- `src/main.py` → Console interface
- `src/adapters/tkinter/gui_main.py` → GUI interface (Tkinter)

### **Core Logic Layer**
- `src/core/functions/greetings.py` → Contains `greeting(name)`

## 3.3 Execution Flow Diagrams

### **Console Flow**
```

User → main.py → greeting() → output to console

```

### **GUI Flow**
```

User → gui_main.py → greeting() → output to label/popup

```

---

# 📘 4. Data Design

| Variable        | Layer                | Type   | Description                               |
|----------------|----------------------|--------|-------------------------------------------|
| `name_input`    | UI (Console/GUI)     | string | Raw user input                             |
| `trimmed_name`  | Core Logic           | string | User input after `.strip()`                |
| `greeting_msg`  | Core Logic → UI      | string | Output greeting string                     |

### Data Rules
- Input is always passed as **raw text**
- All processing happens in core logic
- Output is a **pure string** returned to the adapter layer

---

# 📘 5. Interface Design

## 5.1 Console Interface (`main.py`)
- Prompt: `Enter your name:`
- Reads name using `input()`
- Passes string to `greeting(name)`
- Prints returned message

## 5.2 GUI Interface (`gui_main.py`)
### Components
- Tkinter Window
- Label: title
- Entry widget: user name input
- Button: **Greet**
- Output Label or popup

### Behaviors
- User types name → clicks button
- Adapter retrieves text from entry
- Passes text to `greeting(name)`
- Updates output label or popup with returned message

---

# 📘 6. Processing Design

## 6.1 Core Logic (`greeting(name)`) — Actual Code Behavior
```

def greeting(name: str) -> str:
name_clean = name.strip()
if not name_clean:
return "Hello there!"
return f"Hello {name_clean}!"

```

## 6.2 Console Processing (main.py)
1. Display prompt
2. Read user input
3. Send input to `greeting()`
4. Print result

## 6.3 GUI Processing (gui_main.py)
1. Display window
2. Read entry widget text
3. Send input to `greeting()`
4. Display result in label

---

# 📘 7. Error & Edge Case Handling

### Shared Handling (Core Logic)
- Blank input → `"Hello there!"`
- Whitespace-only → Trim → treated as blank
- Very long names → Accepted as-is

### Console-Specific
- KeyboardInterrupt → outside scope
- Empty input → handled by core

### GUI-Specific
- Empty entry → handled by core
- GUI remains stable for multiple requests

---

# 📘 8. Design for Testability

## 8.1 Unit Test Targets
- `greeting()` — Core function

## 8.2 Integration Test Targets
- Console → main.py → greeting()
- GUI → gui_main.py → greeting()

## 8.3 Example Test Mapping
| Requirement | Component | Test |
|------------|-----------|-------|
| SRS-F-07   | greeting() | test_greetings.py |
| SRS-F-04   | GUI Input  | test_gui_tkinter.py |
| URS-20     | Logic Parity | Both test files |

---

# 📘 9. Traceability (v1.1.0)
| Requirement | Design Element |
|-------------|-----------------|
| URS-14      | Shared greeting() logic |
| SRS-F-04-06 | GUI design in adapter layer |
| SysRS-01    | Both interface types implemented |
| SysRS-07    | Simple, fast processing |

---

# 📘 10. Test Hooks
- Console input/output can be wrapped with mocks
- GUI buttons and text fields can be tested using Tkinter test utilities
- Core logic fully deterministic → ideal for unit tests

---

# 🏛 Historical SDS — Version 1.0.0 (Preserved)

## 1. Purpose
Describes the design of the “Say Hello” console application that fulfills the SRS requirements.

## 2. Design Inputs
- URS v1.0
- SyRS v1.0
- SRS v1.0

## 3. Architecture
- **Architecture Style:** Single-module, sequential console application in Python 3.x
- **Execution Flow:**
  1. Start
  2. Prompt for name
  3. Build greeting string
  4. Print greeting
  5. End

## 4. Data Design
| Variable | Type   | Source | Used by | Description |
|----------|--------|--------|---------|-------------|
| `user_name`    | string | User input | Greeting builder | Name entered by user |
| `greeting_msg` | string | Constructed from `user_name` | Output | Final message shown to user |

## 5. Interface Design
**Input**
- Prompt: `Enter your name:`
- Device: Keyboard
- Validation: If blank or spaces → `Hello there!`

**Output**
- Format: `Hello <name>`
- Example:
  - Input: `Jermaine`
  - Output: `Hello Jermaine`

## 6. Processing Design (Pseudocode)
1. Start
2. Prompt for name
3. Set greeting to "Hello " + name
4. Print greeting
5. Stop

## 7. Error & Edge Case Handling
- Blank input → `Hello there!`
- Spaces-only → Trim → treat as blank
- Long input → Accepted as-is

## 8. Design for Testability
| Req ID | Design Element | Test Case |
|--------|----------------|------------|
| FR1 | Input prompt | "Enter your name:" appears |
| FR2 | Read/store name | Input accepted |
| FR3 | Output greeting | Correct greeting shown |
| NFR1 | Performance | < 1 second response time |

## 9. Traceability
| Functional Req | Design Component  |
|----------------|-------------------|
| FR1 | Input prompt |
| FR2 | Data storage |
| FR3 | Output generation |
| NFR1 | Sequential design |

## 10. Test Hooks
- Manual tests: normal, blank, spaces-only, unusual names

---
**End of design_spec.md**
```
