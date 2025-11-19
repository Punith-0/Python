# 🔍 Regex Matcher – Semi Automated Pattern Matching Tool

A Python-based interactive regex matcher that allows users to test **custom** or **default** regular expressions against input text.  
It supports the three most common regex operations: **Match**, **Search**, and **Findall**, with styled console output using ANSI escape sequences.

---

## ✨ Features
- **Custom Pattern Input**: Enter your own regex pattern (auto-compiled, no need for `r""` raw string).
- **Default Pattern**: Predefined regex `^[Aa].*[Zz]$` (matches strings starting with `A/a` and ending with `Z/z`).
- **Regex Operations**:
  - `match()` → Checks if the entire string matches the pattern.
  - `search()` → Finds the first occurrence of the pattern in the text.
  - `findall()` → Finds all occurrences of the pattern in the text.
- **Interactive Flow**: After each operation, you can choose to continue or exit.
- **ANSI Styling**: Color-coded and highlighted output for better readability.

---
