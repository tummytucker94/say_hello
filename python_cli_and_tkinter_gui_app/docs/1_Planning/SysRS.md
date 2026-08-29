```markdown

# 🏛️ System Requirements Specification (SysRS)
## Project: Say Hello Software — Version 1.1.0

This document defines the **system-level requirements** for the Say Hello Software. It bridges the high‑level user requirements (**URS**) and the detailed software requirements (**SRS**), ensuring full alignment across all SDLC documentation.

It includes structured references to both:
- **URS.md** (User Requirements Specification)
- **SRS.md** (Software Requirements Specification)

---

# 🔗 Document Mapping Overview
The Say Hello Software documentation stack is organized as follows:


URS.md  →  SysRS.md  →  SRS.md  →  SDS.md  →  Codebase


- **URS.md** defines what the *user* needs.
- **SysRS.md** defines what the *system* must do to satisfy the URS.
- **SRS.md** defines the detailed software behavior.
- **SDS.md** defines code-level architecture and design.
- The **codebase** implements everything.

This SysRS sits in the middle and converts all URS requirements into system‑level behaviors.

---

# 🔄 Version History
| Version | Description |
|---------|-------------|
| **1.1.0** | Added GUI system requirements, layered architecture behavior, and mapping to updated URS/SRS. |
| **1.0.0** | Initial console-only requirements. |

---

# 📘 Reference Documents
This SysRS relies on and aligns with:

## **1. URS.md (User Requirements Specification)**
A complete list of user-facing requirements for both v1.0.0 and v1.1.0.

## **2. SRS.md (Software Requirements Specification)**
Detailed functional and non-functional requirements, including GUI and core logic.

---

# 🧱 System Requirements — Version 1.1.0
These requirements define how the *system* must behave to fulfill all URS entries.

## **SysRS‑01 — System Interfaces**
The system shall expose two user interfaces:
- A console interface
- A Tkinter-based graphical interface

**Maps to:** URS‑01, URS‑10

---

## **SysRS‑02 — Unified Core Logic Access**
All interfaces (console and GUI) shall invoke a shared function named `greeting()` for greeting generation.

**Maps to:** URS‑14, SRS‑F‑07

---

## **SysRS‑03 — Input Acquisition**
The system must be capable of accepting text input from:
- Console input buffer
- Tkinter Entry widget

**Maps to:** URS‑11, URS‑02

---

## **SysRS‑04 — Greeting Generation**
The system must process user input through the core logic module, ensuring that:
- Whitespace is trimmed
- Empty input returns: "Hello there!"
- Valid input returns: "Hello <Name>!"

**Maps to:** URS‑17, SRS‑F‑08, SRS‑F‑09, SRS‑F‑10

---

## **SysRS‑05 — Output Display**
The system must display greetings as follows:
- Console: print to standard output
- GUI: display via label or popup

**Maps to:** URS‑13, URS‑03

---

## **SysRS‑06 — Multi‑Attempt Support**
The system must allow users to attempt multiple greeting generations in a single session.

**Maps to:** URS‑16

---

## **SysRS‑07 — Performance Requirements**
- Console output must appear within **1 second**.
- GUI output must appear within **2 seconds** after pressing Greet.

**Maps to:** URS‑05, URS‑15

---

## **SysRS‑08 — System Validation Behavior**
The system shall not crash due to:
- Empty input
- Whitespace input
- String inputs of unusual length

**Maps to:** URS‑04, URS‑08

---

## **SysRS‑09 — Environment Compatibility**
The system must operate correctly on:
- Windows
- macOS
- Linux

**Maps to:** SRS‑N‑04

---

## **SysRS‑10 — Architectural Constraints**
The system shall follow a modular architecture where:
- Core greeting logic exists independently of UI code
- GUI and console operate via adapter layers

**Maps to:** SRS‑N‑05

---

# 🧪 Verification Criteria
To confirm SysRS compliance, the system must pass:
- Unit tests on the `greeting()` function
- Integration tests for console + GUI interfaces
- Manual GUI interaction tests
- Timing benchmarks for performance confirmation

---

# 📘 Historical SysRS — Version 1.0.0
*(Preserved for completeness)*

The original SysRS supported only:
- Console input
- Console output
- Basic greeting generation
- No GUI elements

---

**End of SysRS.md**