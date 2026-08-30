# Software Requirements Specification (SRS): Say Hello (v1.0.0)

## 1. Introduction
This document defines the technical software requirements for Version 1.0.0 of the "Say Hello" static web application. It specifies data models, DOM IDs, validation logic, sanitization rules, and state management mechanics.

## 2. Interface & DOM Component Mapping

| Component Description | HTML Tag / Type | DOM ID Attribute | CSS / Accessibility Attributes |
| :--- | :--- | :--- | :--- |
| **Main Form Container** | `<form>` | `#greeting-form` | `novalidate` (prevents default browser tooltips) |
| **First Name Input** | `<input type="text">` | `#first-name` | `autocomplete="given-name"`, `required` |
| **Last Name Input** | `<input type="text">` | `#last-name` | `autocomplete="family-name"`, `required` |
| **First Name Error Banner** | `<span>` | `#first-name-error` | `.error-message`, `.hidden`, `role="alert"` |
| **Last Name Error Banner** | `<span>` | `#last-name-error` | `.error-message`, `.hidden`, `role="alert"` |
| **Submit Button** | `<button type="submit">`| `#submit-btn` | `.btn-primary` |
| **Reset Button** | `<button type="reset">` | `#reset-btn` | `.btn-secondary` |
| **Output Greeting Box** | `<div>` | `#greeting-output` | `.output-card`, `.hidden`, `aria-live="polite"` |

## 3. Input Sanitization & String Processing Rules
- **TR-01 (Whitespace Trimming):** Both input values must be sanitized upon retrieval using JavaScript `String.prototype.trim()` to strip leading and trailing whitespace.
- **TR-02 (Capitalization Handling):** Formatted text output shall apply `text-transform: capitalize` via CSS to format names cleanly while preserving native user entry.

## 4. Business Logic & Validation Flow

```text
[ Submit Triggered ]
         │
         ▼
[ Trim Input Values ]
         │
         ├─── (First Name OR Last Name is Empty) ───► [ Show Inline Error Elements ]
         │                                            [ Add .hidden to Output Box ]
         │
         └─── (Both Inputs Valid) ──────────────────► [ Hide Inline Error Elements ]
                                                      [ Format Output String ]
                                                      [ Remove .hidden from Output Box ]
