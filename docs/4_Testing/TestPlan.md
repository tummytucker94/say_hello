# Testing Phase — "Say Hello Software"

## 1. Objective
Verify that the implementation satisfies the SRS and SDS requirements.

---

## 2. Test Strategy
- **Level:** Unit and functional (console I/O)
- **Method:** Manual black-box + automated pytest
- **Scope:** Input prompt, name handling, default greeting, response time

---

## 3. Test Environment
- **Platform:** macOS M2  
- **Language:** Python 3.x  
- **Tools:** `pytest`, `pytest-cov` (optional)

---

## 4. Test Cases

| ID | Description | Input | Expected Output |
______________________________________________
| TC1 | Typical name | Jermaine | Hello Jermaine! |
| TC2 | Alternate name | Maria | Hello Maria! |
| TC3 | Blank input | [Enter] | Hello there! |
| TC4 | Spaces only | " " | Hello there! |
| TC5 | Long name | Supercalifragilisticexpialidocious | Hello Supercalifragilisticexpialidocious! |
| TC6 | Performance | Any | Response time under 1s |

---

## 5. Automated Test Command
```bash
pip install -r requirements.txt
pytest -q
# optional coverage
pytest --maxfail=1 --disable-warnings -q --cov=src --cov-report=term-missing
```

---

## 6. Test Results Summary

| ID | Pass/Fail | Notes |
|----|------------|-------|
| TC1 | ✅ | Works as expected |
| TC2 | ✅ | Works as expected |
| TC3 | ✅ | Handles blank input |
| TC4 | ✅ | Handles whitespace input |
| TC5 | ✅ | Handles long names |
| TC6 | ✅ | Executes under 1 second |

---

## 7. Defect Tracking Example
| Defect ID | Description | Severity | Status | Resolution |
|------------|-------------|-----------|----------|-------------|
| DF-001 | Output missing exclamation mark | Minor | Closed | Added `!` in format |

---

## 8. Acceptance Criteria
- All functional tests (TC1–TC5) pass  
- Response time ≤ 1s (TC6)  
- No unhandled exceptions or crashes
