# Software Design Specification (SDS) — Say Hello Software

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
| Variable | Type | Source | Used by | Description |
|-----------|------|---------|----------|-------------|
| `user_name` | string | User input | Greeting builder | Name entered by user |
| `greeting_msg` | string | Constructed from `user_name` | Output | Final message shown to user |

## 5. Interface Design
- **Input**
  - Prompt: `Enter your name:`
  - Device: Keyboard
  - Validation: If blank or spaces, output defaults to `Hello there!`
- **Output**
  - Format: `Hello <name>`
  - Example:  
    - Input: `Jermaine`  
    - Output: `Hello Jermaine`

## 6. Processing Design (Pseudocode)

1. Start
2. Prompt for name with “Enter your name”
3. Set greeting to “ Hello “ + name
4. Print greeting
5. Stop 

## 7. Error and Edge-Case Handling
- Blank input → print `Hello there!`
- Spaces-only input → trim and treat as blank
- Long input → accept as-is
- Exceptions like `KeyboardInterrupt` are out of scope.

## 8. Design for Testability
| Req ID | Design Element | Test Case |
|--------|----------------|------------|
| FR1 | Input prompt | Run program → “Enter your name:” appears |
| FR2 | Read/store name | Input accepted without error |
| FR3 | Output greeting | Output matches “Hello [Name]” |
| NFR1 | Sequential design | Response under 1 second |

## 9. Traceability
| Functional Requirement | Design Component |
|------------------------|------------------|
| FR1 | Input prompt |
| FR2 | Data storage |
| FR3 | Output generation |
| NFR1 | Performance < 1 second |

## 10. Test Hooks
Manual test cases include:
- Normal name input
- Blank input
- Spaces-only input
- Unusual names or symbols
