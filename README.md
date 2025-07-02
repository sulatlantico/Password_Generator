# 🔐 Password Generator

![Password Generator Banner](https://img.shields.io/badge/PyQt6-Password%20App-green?style=flat-square&logo=python&logoColor=white)

A modern and intuitive graphical password generator developed with **PyQt6**. Generates secure and random passwords with or without special characters, and can save the results in `.txt` files.

---

[//]: # (## 🖼️ Interface)

[//]: # ()
[//]: # (<img src="cadeado.png" width="200"/>)

[//]: # ()
[//]: # (> Imagem de fundo personalizável com ícone de cadeado. Interface fixa, amigável e responsiva.)

[//]: # ()
[//]: # (---)

# ✨ Features

- 🔢 Set the **number of characters** per password.
- 🔁 Choose how many **passwords to generate** at once.
- 🔣 Enable or disable the use of **special characters**.
- 💾 **Automatically save** the results to a `.txt` file on the same directory.
- 🔍 Clear view of generated passwords.
- 🔄 Back to home screen button.
- ❌ Exit button with save prompt.
- ℹ️ "About" window with credits.

--- 

# 🚧 To-Do / Planned Updates

## Here are some improvements planned for future versions:

### ❌ Reject non-integer input
- Prevent the user from entering anything other than whole numbers in the input fields.

### ⚠️ Custom warning screen
- Display a warning popup whenever invalid characters or input formats are detected.

### 📏 Unlimited password length
- Allow passwords of any length by removing the current restriction imposed by random.sample().

### 📏 Conda Environment and yml
- Generate yml file with all libraries necessary to run the code.

### 📏 EXE file
- Generate a exe file.
---

## 📦 Requirements

- Python 3.10 or newer
- PyQt6

Instale as dependências com:

```bash
pip install PyQt6


