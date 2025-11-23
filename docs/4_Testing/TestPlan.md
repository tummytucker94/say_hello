```markdown
# 🧪 Testing Phase — *Say Hello Software (v1.1.0)*

## 1. Objective
Verify that both the **Console** and **GUI (Tkinter)** implementations satisfy the functional and non-functional requirements defined in:

- **URS v1.1.0**
- **SysRS v1.1.0**
- **SRS v1.1.0**
- **SDS v1.1.0**

Testing confirms:

- Behavior is identical between Console & GUI  
- `greeting()` produces correct output  
- Performance requirements are met  
- UI responds without crashes  
- All edge cases are handled  

---

## 2. Test Strategy

### **Test Levels**
- **Unit Testing**
  - Core function `greeting()`  
  - Pure logic, deterministic

- **Integration Testing**
  - Console → greeting()  
  - GUI → greeting()

- **Functional Testing**
  - Input handling  
  - Blank input behavior  
  - GUI interaction behavior  

### **Test Methods**
- **Automated**: `pytest`, `pytest-cov`
- **Manual**: GUI button click flow

### **Test Scope**
- Greeting correctness  
- Whitespace trimming  
- GUI input/display  
- Console prompt behavior  
- Cross-interface parity  
- Performance timing  

---

## 3. Test Environment

| Component | Specification |
|----------|---------------|
| **OS** | macOS (M2), Windows 10+, Linux |
| **Python** | Python 3.x |
| **GUI Toolkit** | Tkinter (standard library) |
| **Tools** | `pytest`, `pytest-cov`, Tkinter testing utilities |
| **Execution Modes** | Console mode & GUI mode |

---

## 4. Test Cases

### ✔ **Core Logic Test Cases (Unit Tests)**

| ID | Description | Input | Expected Output |
|----|-------------|--------|----------------|
| TC1 | Typical name | `"Jermaine"` | `Hello Jermaine!` |
| TC2 | Alternate name | `"Maria"` | `Hello Maria!` |
| TC3 | Blank input | `""` | `Hello there!` |
| TC4 | Spaces only | `"   "` | `Hello there!` |
| TC5 | Long name | `Supercalifragilisticexpialidocious` | `Hello Supercalifragilisticexpialidocious!` |
| TC6 | Performance | Any input | Response < 1s |

---

### ✔ **Console Integration Test Cases**

| ID | Description | Expected Behavior |
|----|-------------|------------------|
| C1 | Console prompt displays | Shows: `Enter your name:` |
| C2 | Console reads input | Accepts keyboard input |
| C3 | Console outputs greeting | Prints result from `greeting()` |
| C4 | Handles blank input | Prints `Hello there!` |

---

### ✔ **GUI Functional Test Cases**

| ID | Description | Expected Behavior |
|----|-------------|------------------|
| GUI1 | Window loads | Application window appears |
| GUI2 | Entry field accepts input | User can type name |
| GUI3 | Greet button works | Clicking button calls `greeting()` |
| GUI4 | Output displays in label | Label updates with greeting |
| GUI5 | Blank input behavior | Displays `Hello there!` |
| GUI6 | Multiple greetings | GUI updates correctly on repeated clicks |
| GUI7 | GUI performance | Response < 2 sec |

---

## 5. Automated Test Commands
```

pip install -r requirements.txt

# Run all unit + integration tests

pytest -v

# Run coverage

pytest --maxfail=1 --disable-warnings -q --cov=src --cov-report=term-missing

```

---

## 6. Test Results Summary

| ID | Pass/Fail | Notes |
|----|-----------|-------|
| TC1 | ✅ | Expected output returned |
| TC2 | ✅ | Expected output returned |
| TC3 | ✅ | Blank input handled correctly |
| TC4 | ✅ | Whitespace trimmed properly |
| TC5 | ✅ | Handles very long strings |
| TC6 | ✅ | Console response < 1 sec |
| C1–C4 | ✅ | Console integration successful |
| GUI1–GUI7 | ✅ | GUI responsive + correct |

All tests passed for both interfaces.

---

## 7. Defect Tracking Example

| Defect ID | Description | Severity | Status | Resolution |
|-----------|-------------|----------|--------|-------------|
| DF-001 | GUI label not updating | Medium | Closed | Fixed widget `.config(text=...)` call |
| DF-002 | Missing exclamation mark in greeting | Minor | Closed | Updated string format |
| DF-003 | Console did not trim whitespace | Major | Closed | Added `.strip()` in `greeting()` |

---

## 8. Acceptance Criteria

### ✔ Functional Acceptance
- All greetings follow the required format  
- Console and GUI behave identically (URS-20)  
- Blank/whitespace input handled consistently  

### ✔ Performance Acceptance
- Console response < 1 second  
- GUI response < 2 seconds  

### ✔ Stability Acceptance
- No crashes or freezes in either mode  
- GUI supports repeated interaction indefinitely  

### ✔ Documentation Alignment
- SDS, SRS, SysRS fully satisfied  
- Tests trace cleanly to requirements  

---

**End of Testing Phase Document**

```
