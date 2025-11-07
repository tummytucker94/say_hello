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
say_hello/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   └── functions/
│       └── greetings.py
├── tests/
│   └── test_greetings.py
└── docs/
    └── (all SDLC documentation)
```

---

## 7. Commit Log (Example)
| Commit | Date | Summary |
|---------|------|----------|
| a1b2c3d | 2025-10-31 | Initial project skeleton: src/tests/docs |
| d4e5f6g | 2025-10-31 | Implement `say_hello()` with blank input handling |
| h7i8j9k | 2025-11-01 | Add tests and README run instructions |
