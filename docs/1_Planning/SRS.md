# Software Requirements Specification (SRS)
## Project: “Say Hello Software”

### 1. Introduction
This document defines the requirements for a Python-based Hello Program that greets users by name.

### 2. Scope
The program’s scope is limited to command-line interaction.  
It will not include graphical user interfaces, multiple languages, or stored data.

### 3. Definitions and Abbreviations
- **URS** – User Requirements Specification  
- **SyRS** – System Requirements Specification  
- **SRS** – Software Requirements Specification

### 4. Overall Description
The system will prompt the user to enter their name, store the name in memory, and print a greeting.

### 5. Functional Requirements
| ID | Requirement |
|----|--------------|
| FR1 | The system prompts for input from the user |
| FR2 | The system reads input and stores it |
| FR3 | The system prints a message with the input name |

### 6. Non-Functional Requirements
| ID | Requirement |
|----|--------------|
| NFR1 | The system responds within 1 second |
| NFR2 | Code shall be readable and follow Python conventions (PEP8) |

### 7. Assumptions and Constraints
- The user will run the program in a Python-supported terminal.  
- No network connection is required.

### 8. Verification Criteria
Each functional requirement can be tested by running the program and verifying that the output matches expected results.
