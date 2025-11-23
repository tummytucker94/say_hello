# Changelog

## [1.0.0] - 2025-11-09
- Initial public release of Say Hello.
- Implemented SDLC documentation (Planning, Design, Implementation, Testing, Maintenance).
- Added automated tests and logging of execution time.

# 📑 Changelog
All notable changes to the **Say Hello Software** project will be documented in this file.

The format follows **Semantic Versioning**:  
`MAJOR.MINOR.PATCH`

---

## [v1.1.0] - 2025-11-17
### 🎉 Added
- Introduced new **Tkinter GUI mode** (`src/gui_main.py`)
- Added GUI-based greeting with `Greet` button and name input field
- New test file for GUI functionality: `tests/test_gui_main.py`
- Updated README.md to reflect GUI capability and multi-mode (console + GUI) usage
- Expanded system documentation to include GUI architecture and flow

### 🛠 Changed
- Improved input handling: whitespace and blank values now default to `"there"` in both console and GUI modes
- Refactored greeting logic for reuse across console and GUI
- Updated repository structure to include GUI module

### 📚 Documentation
- Added SDLC-aligned explanation of v1.1.0 changes
- Updated Testing and How to Run sections
- Version table added to README.md

---

## [v1.0.0] - 2025-11-01
### 🚀 Initial Release
- Console-only greeting application
- Input sanitization using `.strip()`
- Manual and automated tests (`pytest`) for core greeting behavior
- Complete SDLC documentation including planning, design, testing, and maintenance structure
- Initial repository structure with docs, src, tests, and runtime log
---

### 🧑‍💻 Contributors
- Jermaine Tucker (@tummytucker94)

---

### 📝 Changelog Guidelines
When contributing new changes, please update this file following the style below:

## [v1.1.0] - 2025-11-17

### Added
- New Tkinter GUI mode (`src/gui_main.py`)
- Input field and "Greet" button added for interactive name entry
- New GUI test file: `tests/test_gui_main.py`
- Multi-mode (console + GUI) capability documented in README
- System design updated to include GUI execution flow

### Changed
- Input handling improved so blank/whitespace defaults to `"there"` in both console & GUI
- Greeting logic refactored for reuse across console and GUI modules
- Repository structure updated to include GUI components

### Fixed
- Improved user input validation to prevent empty string errors
- Ensured consistent greeting punctuation and formatting

### Removed
- None (no features removed in this version)
---

### ⚖ License
This project is licensed under the **MIT License**.


