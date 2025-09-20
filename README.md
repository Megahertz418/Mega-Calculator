# 🧮 Mega-Calculator (Tkinter)

A simple GUI-based calculator built with **Python** and **Tkinter**.  
Packaged into a portable executable (`.exe`) using **PyInstaller**, so it runs on Windows without requiring Python or Tkinter installed.

---

## ✨ Features
- Clean and minimal **dark UI**  
- Supports basic operations: `+  -  ×  ÷  .`  
- Clear button (`C`) and backspace (`⌫`)  
- Error handling for invalid expressions  
- Portable **one-file executable** (no installation required)

---

## 📂 Project Structure
```

Mega-Calculator/
│   calculator.py      # main source code
│   README.md
│   LICENSE
│   CREDITS.md
│   .gitignore
│
└── assets/            # icons and resources
Calculator.ico
Calculator.png

````

> ⚠️ The `dist/` folder and `.exe` file are **not included in the repo**.  
> You can always download the ready-to-use executable from the [Releases](#-download).

---

## 🚀 Run Locally (from source)
1. Install Python (3.9+ recommended)
2. Clone this repository:
   ```bash
   git clone https://github.com/YourUser/Mega-Calculator.git
   cd Mega-Calculator
```

3. Run the app:

   ```bash
   python calculator.py
   ```

---

## 💾 Download

The portable Windows executable is available in the **Releases section**:
👉 [Download Mega-Calculator.exe](https://github.com/YourUser/Mega-Calculator/releases)

---

## 🔨 Build Instructions (PyInstaller)

If you want to build your own `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name Mega-Calculator ^
  --icon "assets\Calculator.ico" ^
  --add-data "assets\Calculator.ico;assets" ^
  --add-data "assets\Calculator.png;assets" ^
  calculator.py
```

The executable will be generated inside the `dist/` folder.

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute.