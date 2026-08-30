# User Requirements Specification (URS)
## Project: “Say Hello Software”

### 1. Purpose
The user wants a simple software program that greets them personally when they enter their name.

### 2. User Story
As a user, I want to enter my name and receive a friendly message that says “Hello [Name]” so I can confirm the program recognizes my input.

### 3. Functional Needs
- Must accept text input (name)
- Must display a greeting message with the name included

### 4. Non-Functional Needs
- The program should respond instantly
- Must be easy to use and understand

### 5. Acceptance Criteria
- When a user types “Jermaine,” the system should display “Hello Jermaine.”
- The system should not crash on blank input.


# 📘 User Requirements Specification (URS)
## Project: Say Hello Software — Version 1.1.0

This document defines the **user-level requirements** for the Say Hello Software, covering both:
- The original **v1.0.0 console-only** version
- The enhanced **v1.1.0 GUI + layered architecture** version

It clearly separates historical requirements (v1.0.0) from upgraded requirements (v1.1.0) to preserve SDLC evolution.

---

# 🔄 Version History
| Version | Description |
|---------|-------------|
| **1.1.0** | Added GUI requirements, performance updates, parity expectations, and layered architecture considerations. |
| **1.0.0** | Original console-only user requirements. |

---

# 🆕 URS Addendum — Version 1.1.0 (Current Requirements)
These requirements reflect the **latest version** of the Say Hello Software and align with the actual codebase.

## 1. Purpose
Users need a simple software application that greets them by name. Version 1.1.0 expands this capability by providing a **graphical interface**, while preserving the original console experience.

---

## 2. User Requirements (v1.1.0)
### 🎨 **URS-10 — GUI Window Interaction**
The user shall be able to open a graphical window to interact with the system.

### 🧩 **URS-11 — GUI Name Input Field**
The system shall provide a text entry field that allows users to type their name.

### 🖱 **URS-12 — Greet Button**
The GUI shall provide a **Greet** button that the user can click to generate a greeting.

### 🪟 **URS-13 — GUI Greeting Display**
The system shall display the greeting message within the GUI using a label or popup.

### ⚙️ **URS-14 — Shared Greeting Logic**
Both the console interface and GUI interface shall use the **same function**, `greeting()`, to generate greeting text.

### 🎯 **URS-15 — GUI Performance Requirement**
The GUI shall display the greeting within **2 seconds** after the Greet button is clicked.

### 🔁 **URS-16 — Multiple Greeting Attempts**
The user shall be able to enter multiple names and produce multiple greetings without restarting the application.

### 🌈 **URS-17 — Handling Blank Input (GUI)**
If the user clicks Greet with a blank or whitespace-only name, the system shall display:
```

Hello there!

```

### 🧭 **URS-18 — Accessibility & Usability**
The GUI shall:
- Have clearly visible text and buttons
- Provide readable output
- Maintain consistent layout across operating systems

### 🪟 **URS-19 — Window Persistence**
The GUI window shall remain open until the user closes it manually.

### 🧩 **URS-20 — Console & GUI Parity**
The console and GUI shall behave identically regarding:
- Handling blank input
- Processing names
- Output formatting via `greeting()`

---

# 📎 Acceptance Criteria (v1.1.0)
| Requirement ID | Acceptance Criteria |
|----------------|--------------------|
| URS-10 | GUI launches successfully on Windows, macOS, and Linux. |
| URS-11 | User can type into the GUI entry field. |
| URS-12 | Clicking the Greet button calls `greeting()`. |
| URS-13 | A greeting is visibly displayed in the GUI. |
| URS-14 | Console and GUI use the same logic. |
| URS-15 | Greet button results appear within 2 seconds. |
| URS-16 | Multiple greetings can be generated in one session. |
| URS-17 | Blank input produces "Hello there!" consistently. |
| URS-18 | Visual elements are readable and accessible. |
| URS-19 | GUI window stays open until closed manually. |
| URS-20 | Behavior parity between console and GUI confirmed. |

---

# 📘 Original URS — Version 1.0.0 (Historical)
*Preserved for documentation evolution and SDLC traceability.*

### **URS-01 — Console Interaction**
The user shall be able to interact with the system through a console prompt.

### **URS-02 — Name Input**
The user shall be able to enter their name in response to a console prompt.

### **URS-03 — Greeting Output**
The system shall display a greeting using the name the user provided.

### **URS-04 — Blank Input Behavior**
If the user enters no name, the system shall greet them with a generic message.

### **URS-05 — Fast Response**
The system shall respond within 1 second.

### **URS-06 — No Installation Complexity**
The user shall only need Python installed to run the program.

### **URS-07 — No Advanced Features**
The system shall not require or support GUIs, networking, or persistent data.

### **URS-08 — Basic Error Handling**
The system shall handle unexpected input gracefully.

### **URS-09 — Single-Purpose Design**
The system shall serve one purpose: greeting the user by name.

---

**End of URS.md**
