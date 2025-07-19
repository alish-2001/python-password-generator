# PyPassGen 🛡️🔑

A cross‑platform desktop application built with Python and PyQt5 that helps you generate secure, truly random passwords in just a few clicks.

---

## 📥 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Screenshots](#screenshots)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Launching the App](#launching-the-app)  
5. [Usage](#usage)  
6. [Configuration & Customization](#configuration--customization)  
7. [Project Structure](#project-structure)  
8. [Development Workflow](#development-workflow)  
9. [Packaging & Distribution](#packaging--distribution)  
10. [Roadmap](#roadmap)  
11. [Contributing](#contributing)  
12. [License](#license)  
13. [Acknowledgements](#acknowledgements)  

---

## 🧐 Overview

Strong, unpredictable passwords are the first line of defense against unauthorized access. **PyPassGen** provides:

- A **clean**, **intuitive** GUI  
- Fine‑grained control over character sets  
- One‑click clipboard copy  
- Lightweight footprint

Ideal for developers, system administrators, and everyday users who need solid password hygiene without fuss.

---

## ✨ Features

- **Adjustable Length**: Generate anywhere from 8 to 64 characters (default: 12).  
- **Character Sets**  
  - Uppercase (A–Z)  
  - Lowercase (a–z)  
  - Digits (0–9)  
  - Symbols (!@#$…)
- **Clipboard Integration**: Instantly copy your new password.  
- **Entropy Meter**: Visual gauge estimating password strength.  

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+**  
- **pip** (usually bundled with Python)  
- Development libraries for PyQt5 (if your system requires them)

### Installation

```bash
# 1. Clone repositor
# 2. Create & activate virtual environment
python3 -m venv .venv
# 3. Install dependencies
pip install -r requirements.txt
