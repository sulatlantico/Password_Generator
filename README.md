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

[//]: # (# 🚧 To-Do / Planned Updates)

[//]: # (## Here are some improvements planned for future versions:)

[//]: # (# ---)

## 📦 Requirements

- Python 3.10 or newer
- PyQt6

---

## ⚙️ Setup Instructions

### 🟡 Using `source` (recommended for lightweight setups)
If you want to install the latest version of Password Generator from github, 
you can simply do the following:
```bash
$ https://github.com/sulatlantico/Password_Generator.git
$ cd mayavi
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
### 🟡 Using `venv` (recommended for lightweight setups)

```bash
# 1. Create a virtual environment (requires Python 3.10+)
python3.10 -m venv pass_gen

# 2. Activate the environment
# On Windows:
pass_gen\Scripts\activate

# On Linux/macOS:
source pass_gen/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 🟡 Using `conda` (not sure if works 100%)
```bash

# 1. Create a conda environment (requires Python 3.10+)
conda env create -f conda_environment.yml

# 2. Activate the conda env
conda activate pass_gen
