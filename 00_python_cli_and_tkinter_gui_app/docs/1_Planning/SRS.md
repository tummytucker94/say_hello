```markdown
# 📘 Software Requirements Specification (SRS)
## Project: Say Hello Software — Version 1.1.0

This document defines the complete software requirements for the **Say Hello Software**, including:
- The original **v1.0.0 console-only** behavior
- The enhanced **v1.1.0 GUI mode**
- The updated core logic through the `greeting()` function
- The layered architecture introduced in v1.1.0

The SRS preserves past requirements while clearly defining the current software behavior.

---

# 🔄 Version History
| Version | Description |
|---------|-------------|
| **1.1.0** | Added GUI requirements, layered architecture requirements, updated functional & non-functional requirements, aligned to `greeting()`. |
| **1.0.0** | Initial console-only SRS. |

---

# 🆕 SRS Addendum — Version 1.1.0
This is the **active specification** aligned with the current GitHub codebase.

## 1. Introduction
Version 1.1.0 extends the Say Hello Software by introducing:
- A Tkinter GUI
- A layered architecture: `core` + `adapters`
- The shared greeting logic function `greeting()`

The software still preserves full console functionality.

---

## 2. Scope
### **In Scope**
- Console mode input/output
- Tkinter GUI mode input/output
- Greeting generation through shared logic
- Input validation (minimal)

### **Out of Scope**
- Database storage
- Networking
- Multi-language support
- Configuration files
- Advanced name parsing

---

## 3. Definitions & Abbreviations
- **SRS** – Software Requirements Specification
- **URS** – User Requirements Specification
- **SyRS** – System Requirements Specification
- **GUI** – Graphical User Interface
- **Core Logic** – The greeting-generating logic in `greeting()`

---

## 4. Overall Description
The system receives user input (name) via **console** or **GUI**, passes that input to the `greeting()` function, and displays the result.

The system must behave identically across interfaces.

---

## 5. Functional Requirements
### **Console Requirements**
| ID | Requirement |
|----|------------|
| **SRS-F-01** | System shall prompt the user for input via console. |
| **SRS-F-02** | System shall send input to `greeting()` for processing. |
| **SRS-F-03** | System shall print the returned greeting to the console. |

### **GUI Requirements**
| ID | Requirement |
|----|------------|
| **SRS-F-04** | Tkinter GUI window shall display an entry field and Greet button. |
| **SRS-F-05** | Clicking Greet shall send input to `greeting()`. |
| **SRS-F-06** | GUI shall display greeting in a label or popup. |

### **Core Logic Requirements**
| ID | Requirement |
|----|------------|
| **SRS-F-07** | Greeting logic shall be implemented in function `greeting()`. |
| **SRS-F-08** | `greeting()` shall trim whitespace. |
| **SRS-F-09** | If trimmed input is empty, return "Hello there!". |
| **SRS-F-10** | If trimmed input is valid, return message: `Hello <Name>!`. |

---

## 6. Non-Functional Requirements
| ID | Requirement |
|----|------------|
| **SRS-N-01** | Console mode shall respond within 1 second. |
| **SRS-N-02** | GUI mode shall respond within 2 seconds of button click. |
| **SRS-N-03** | Code shall follow PEP8 standards. |
| **SRS-N-04** | Application shall run on Windows, macOS, and Linux. |
| **SRS-N-05** | The architecture shall remain modular and maintainable. |

---

## 7. Constraints & Assumptions
- Python 3.x is required.
- Tkinter must be available for GUI mode.
- User input may contain arbitrary characters.
- No network access is required.

---

## 8. Verification
- Unit tests validate `greeting()` logic.
- Manual tests verify GUI behavior.
- Integration tests verify UI → core → output flow.

---

# 📘 Original SRS — Version 1.0.0 (Preserved)
The original version described a simple console-only greeting application.

## 1. Introduction
The system greets users by name entered via console.

## 2. Scope
Console-only; no GUI.

## 3. Functional Requirements
| ID | Requirement |
|----|------------|
| FR1 | Prompt user for input |
| FR2 | Read and store user input |
| FR3 | Print greeting using input name |

## 4. Non-Functional Requirements
| ID | Requirement |
|----|------------|
| NFR1 | Respond within 1 second |
| NFR2 | Follow Python conventions |

## 5. Constraints
Python terminal required.

---

**End of SRS.md**


