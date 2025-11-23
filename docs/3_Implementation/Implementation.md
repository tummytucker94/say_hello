# Implementation Phase — "Say Hello Software"

## 1. Overview
The implementation phase transforms the approved design into working software.

- **Language/Runtime:** Python 3.x  
- **Entry Point:** `src/main.py`  
- **Primary Function:** `say_hello()` — reads input, formats greeting, prints output  
- **Source Control:** Git (main branch)

---

## 2. Environment & Dependencies
- **OS:** macOS (Apple Silicon M2)  
- **Python Version:** 3.x (document exact version)  
- **External Libraries:** None (standard library only)  
- **Virtual Environment:** `.venv/` created via:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

---

## 3. Build & Run Instructions
```bash
# create & activate virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux

# run the program
python src/main.py
```

---

## 4. Coding Standards & Conventions
- Follow **PEP 8** style guidelines  
- Use **f-strings** for string formatting  
- Functions are small, single-purpose, and clearly named  
- Handle whitespace with `.strip()`; default to `"there"` if input is empty  

---

## 5. Implementation Traceability
| Functional Req | Implementation Element |
|----------------|------------------------|
| FR1 – Prompt for input | `input()` call |
| FR2 – Read and store name | `user_name` variable |
| FR3 – Format and display greeting | `greeting_msg → print()` |

---

## 6. Repository Structure
```
SAY_HELLO/
├── docs/
│   ├── 1_Planning/
│   │   ├── Project_Overview.md
│   │   ├── URS.md
│   │   ├── SRS.md
│   │   ├── SysRS.md
│   ├── 2_Design/
│   │   ├── architecture.md
│   │   └── design_spec.md
│   ├── 3_Implementation/
│   │   └── Implementation.md
│   ├── 4_Testing/
│   │   └── TestPlan.md
│   └── 5_Maintenance/
│       ├── Maintenance.md
│       └── CHANGELOG.md
│
├── src/
│   ├── adapters/tkinter/gui_main.py
│   ├── core/functions/greetings.py
│   ├── __init__.py
│   ├── main.py
│   └── runtime.log
│
├── tests/
│   ├── test_greetings.py
│   └── test_gui_tkinter.py
│
└── README.md


```

---

## 7. Commit Log
| Commit | Date | Summary |
|---------|------|----------|

- **25e7c8d** — (2025-11-23) updated SysRS.md, SRS.md, and URS.md
- **fe8f38b** — (2025-11-17) all tests passed CLI and GUI
- **c7ceaba** — (2025-11-17) correcting test setup
- **b3ddf41** — (2025-11-17) added 6 test cases for tkinter GUI
- **6506ee2** — (2025-11-13) corrected the test code
- **2182d0a** — (2025-11-13) created GUI for say hello app using tkinter
- **448d730** — (2025-11-13) organized folders into core/adapters + test program
- **685ea5e** — (2025-11-10) updated README.md
- **d9fec83** — (2025-11-10) added Changelog.md
- **cf5050c** — (2025-11-10) Update README.md
- **e19b0fb** — (2025-11-09) Update README.md
- **164c3b5** — (2025-11-09) updated repo structure in Implementation.md
- **a28babe** — (2025-11-09) updated commit log in Implementation.md
- **d9ca471** — (2025-11-09) changed variable name in main.py
- **064e022** — (2025-11-08) Update README.md
- **7f9a65d** — (2025-11-08) Update README.md
- **48ca36f** — (2025-11-07) added TC2 alternate name
- **544d4e7** — (2025-11-07) add performance test for TC6
- **cfdfb54** — (2025-11-07) removed semicolon in greetings.py
- **e23a873** — (2025-11-07) added __init__.py to support pytest
- **8eb2a2e** — (2025-11-07) added implementation/testing/maintenance docs
- **f5f463f** — (2025-11-07) isolated execution time measurement
- **ffa12a4** — (2025-11-07) changed code format
- **329cb41** — (2025-11-07) changed variable name in greetings.py
- **4d3d89e** — (2025-11-07) corrected code to fit specs
- **a20735c** — (2025-11-07) reformatted code, added logs/time measure
- **2c110d0** — (2025-11-06) added logger + execution time
- **03ecace** — (2025-11-06) Initial commit
