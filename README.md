# 👋 Say Hello Software

A simple Python console application that greets users by name — built to practice the **Software Development Life Cycle (SDLC)** from planning to maintenance.

> Repository: [https://github.com/tummytucker94/say_hello](https://github.com/tummytucker94/say_hello)

---

## 📜 Table of Contents
1. [Project Overview](#project-overview)
2. [Objectives & Scope](#objectives--scope)
3. [System Design](#system-design)
4. [Implementation](#implementation)
5. [Testing](#testing)
6. [Maintenance](#maintenance)
7. [Repository Structure](#repository-structure)
8. [How to Run](#how-to-run)
9. [Contributing](#contributing)
10. [License](#license)

---

## 🧭 Project Overview

**Purpose:**  
To gain hands-on experience building software using the **SDLC** process while creating a functional console application.

**Problem Definition:**  
> “I want to create a software that greets the user when they enter their name because I want to gain experience creating software using the SDLC process.”

**Goal:**  
- Learn to plan, design, code, test, and maintain a Python application end-to-end.

**Objective:**  
- Develop a console program that greets the user based on their name input and handles blank or whitespace inputs gracefully.

---

## 🎯 Objectives & Scope

### In Scope
- Accepting user name input  
- Printing a personalized greeting  
- Handling blank or whitespace-only input  

### Out of Scope
- GUI design  
- Saving or storing user data  
- Complex validation  

**Performance Requirement:**  
- Must respond in under **1 second**

---

## 🧠 System Design

### Architecture
- **Type:** Single-module, sequential console application  
- **Language:** Python 3.x  
- **Platform:** macOS / Linux / Windows (any Python-supported environment)  

### Execution Flow
1. Start  
2. Prompt user for name  
3. Read and validate input  
4. Display greeting  
5. End  

### Pseudocode
```text
BEGIN
  DISPLAY "Enter your name: "
  READ user_name
  IF user_name IS empty THEN
      greeting_msg ← "Hello there!"
  ELSE
      greeting_msg ← "Hello " + user_name
  ENDIF
  DISPLAY greeting_msg
END
