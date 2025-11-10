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
├── .pytest_cache/
├── .venv/
├── docs/
│   ├── 1_Planning/
│   ├── 2_Design/
│   ├── 3_Implementation/
│   ├── 4_Testing/
│   └── 5_Maintenance/
├── src/
│   ├── functions/
│   │   └── __init__.py
│   ├── main.py
│   └── runtime.log
├── tests/
├── README.md
└── runtime.log

```

---

## 7. Commit Log
| Commit | Date | Summary |
|---------|------|----------|
| [03ecace251b7cae86fc6aad30da8505dc71335e1](https://github.com/tummytucker94/say_hello/commit/03ecace251b7cae86fc6aad30da8505dc71335e1) | 11/06/2025 | Initial commit: add hello program |
| [2c110d011cb22e23752a35e2071812fbe0e7295a](https://github.com/tummytucker94/say_hello/commit/2c110d011cb22e23752a35e2071812fbe0e7295a) | 11/06/2025 | add logger and execution time |
| [a20735c33b4dd6ab6e0e38c91fa632c1aeb78fe5](https://github.com/tummytucker94/say_hello/commit/a20735c33b4dd6ab6e0e38c91fa632c1aeb78fe5) | 11/07/2025 | reformatted code, added logs and time measure |
| [4d3d89e7b52ff615685d1076e55a385ad94ecc02](https://github.com/tummytucker94/say_hello/commit/4d3d89e7b52ff615685d1076e55a385ad94ecc02) | 11/07/2025 | corrected code to fit specs |
| [329cb413d9dd37bcbc2755ec8df0020ae4f73e24](https://github.com/tummytucker94/say_hello/commit/329cb413d9dd37bcbc2755ec8df0020ae4f73e24) | 11/07/2025 | changed variable name from greeting to greeting_ms |
| [ffa12a46751e8d8e8faad1e8521386650c0f9fc0](https://github.com/tummytucker94/say_hello/commit/ffa12a46751e8d8e8faad1e8521386650c0f9fc0) | 11/07/2025 | changed code format |
| [f5f463f4b95a048bec1b35784c238e40d20d7875](https://github.com/tummytucker94/say_hello/commit/f5f463f4b95a048bec1b35784c238e40d20d7875) | 11/07/2025 | reformatted code to isolate and measure code execution time |
| [8eb2a2e78b8db2f49394996dc3809837924cc742](https://github.com/tummytucker94/say_hello/commit/8eb2a2e78b8db2f49394996dc3809837924cc742) | 11/07/2025 | added 3_Implementation, 4_Testing, and 5_Maintenance to the project |
| [e23a8731a8bc7e29da9a6419d06336f8c74e769e](https://github.com/tummytucker94/say_hello/commit/e23a8731a8bc7e29da9a6419d06336f8c74e769e) | 11/07/2025 | added __init__.py files to help pytest to execute |
| [cfdfb54475f48eab4b80ea10795f3556cfabfe5c](https://github.com/tummytucker94/say_hello/commit/cfdfb54475f48eab4b80ea10795f3556cfabfe5c) | 11/07/2025 | removed semicolon to correct function in greetings.py for tests to pass |
| [544d4e7aea0b362adf876f4f613259832d8fe638](https://github.com/tummytucker94/say_hello/commit/544d4e7aea0b362adf876f4f613259832d8fe638) | 11/07/2025 | add performance test for TC6 |
| [48ca36f38062753da36a7cdc70715d94f6afb6cc](https://github.com/tummytucker94/say_hello/commit/48ca36f38062753da36a7cdc70715d94f6afb6cc) | 11/07/2025 | added TC2 alternate name |
| [7f9a65d5ff4544b6e6989feb86532f283248c50f](https://github.com/tummytucker94/say_hello/commit/7f9a65d5ff4544b6e6989feb86532f283248c50f) | 11/08/2025 | Update README.md |
| [064e022864e58f3611c3cf3415060875a4ec9460](https://github.com/tummytucker94/say_hello/commit/064e022864e58f3611c3cf3415060875a4ec9460) | 11/08/2025 | Update README.md |
| [d9ca471c542381e2fe886c7edc8fa0c4c3cf3ba4](https://github.com/tummytucker94/say_hello/commit/d9ca471c542381e2fe886c7edc8fa0c4c3cf3ba4) | 11/09/2025 | changed variable name from greeting to greeting_msg in main.py |
