import sys
import string
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QCheckBox,
    QMessageBox, QVBoxLayout, QStackedLayout, QScrollArea
)
from PyQt6.QtGui import QIcon, QPixmap, QFont


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setWindowIcon(QIcon("cadeado.png"))
        self.setGeometry(150, 150, 500, 500)
        self.setFixedSize(500, 500)

        self.password_list = []

        self.stack = QStackedLayout()
        self.setLayout(self.stack)

        self.main_screen = QWidget(self)
        self.password_screen = QWidget(self)

        self.setup_main_screen()
        self.setup_password_screen()

        self.stack.addWidget(self.main_screen)
        self.stack.addWidget(self.password_screen)

        self.stack.setCurrentWidget(self.main_screen)
        self.show()

    def setup_main_screen(self):
        self.main_screen.setStyleSheet("background: white;")
        background = QLabel(self.main_screen)
        background.setPixmap(QPixmap("cadeado.png").scaled(580, 550))

        self.add_label("Password Generator", 70, 50, 30, self.main_screen)

        self.add_label("Number of Characters", 175, 160, 10, self.main_screen)
        self.input_chars = self.add_line_edit("N° of characters", 175, 190, self.main_screen)

        self.add_label("Number of Generated Passwords", 175, 240, 10, self.main_screen)
        self.input_passwords = self.add_line_edit("N° of Passwords", 175, 260, self.main_screen)

        self.checkbox_special = QCheckBox("Use Special Characters", self.main_screen)
        self.checkbox_special.setStyleSheet("background: transparent;")
        self.checkbox_special.move(175, 310)

        self.add_button("Generate Passwords", 180, 350, self.handle_generation, self.main_screen)
        self.add_button("About", 370, 440, self.show_about, self.main_screen, (250, 250, 250), 80)

    def setup_password_screen(self):
        layout = QVBoxLayout(self.password_screen)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.password_container = QWidget()
        self.password_layout = QVBoxLayout(self.password_container)

        scroll_area.setWidget(self.password_container)

        layout.addWidget(scroll_area)

        btn_back = QPushButton("Return")
        btn_back.clicked.connect(lambda: self.stack.setCurrentWidget(self.main_screen))
        layout.addWidget(btn_back)

        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.exit_app)
        layout.addWidget(btn_exit)

    def add_label(self, text, x, y, font_size, parent):
        label = QLabel(text, parent)
        label.setFont(QFont("Arial", font_size))
        label.setStyleSheet("background: transparent;")
        label.move(x, y)

    def add_line_edit(self, placeholder, x, y, parent):
        box = QLineEdit(parent)
        box.setPlaceholderText(placeholder)
        box.setStyleSheet("""
            border: 4px solid black;
            border-radius: 10px;
            padding: 0 6px;
            background: white;
            min-width: 8em;
        """)
        box.move(x, y)
        return box

    def add_button(self, text, x, y, callback, parent, bg_color=(150, 150, 150), width=140):
        btn = QPushButton(text, parent)
        btn.move(x, y)
        btn.clicked.connect(callback)
        btn.setStyleSheet(f"""
            background-color: rgb({bg_color[0]}, {bg_color[1]}, {bg_color[2]});
            border-style: inset;
            border-width: 4px;
            border-radius: 10px;
            border-color: black;
            min-width: 5em;
            padding: 6px;
        """)
        return btn

    def handle_generation(self):
        try:
            num_chars = int(self.input_chars.text())
            num_passwords = int(self.input_passwords.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Insert only integer numbers.")
            return

        confirm = QMessageBox.question(
            self, "Confirmation", f"N° de characters: {num_chars}\nN° de Passwords: {num_passwords}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
        )

        if confirm == QMessageBox.StandardButton.Yes:
            self.generate_passwords(num_chars, num_passwords, self.checkbox_special.isChecked())
            self.display_passwords()
            self.stack.setCurrentWidget(self.password_screen)

    def generate_passwords(self, length, count, use_special):
        values =  ''.join(str(i) for i in range(1, 10))
        base = string.ascii_letters + values
        symbols = string.punctuation #'@#$%&*?/\\'
        characters = base + symbols if use_special else base
        self.password_list = [''.join(random.sample(characters, length)) for _ in range(count)]

        filename = 'PASSWORDS-GENERATED.txt' if use_special else 'GENERATED_PASSWORDS.txt'
        with open(filename, 'w') as f:
            for i, pwd in enumerate(self.password_list):
                f.write(f'Password {i}: {pwd}\n')
                f.write('*********************\n')

    def display_passwords(self):
        # Limpa senhas anteriores
        for i in reversed(range(self.password_layout.count())):
            widget = self.password_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for i, pwd in enumerate(self.password_list):
            label = QLabel(f"Password {i + 1}:")
            field = QLineEdit()
            field.setText(pwd)
            field.setReadOnly(True)
            field.setStyleSheet("""
                border: 2px solid gray;
                border-radius: 10px;
                padding: 0 6px;
                background: rgb(200,200,200);
                min-width: 8em;
            """)
            self.password_layout.addWidget(label)
            self.password_layout.addWidget(field)

    def show_about(self):
        QMessageBox.information(self, "Solutions C.A", "Powered By: Barbosa, R.D.\nAll Rights Reserved.")

    def exit_app(self):
        QMessageBox.information(
            self, "Solutions C.A",
            "A file called 'GENERATED_PASSWORDS.txt' with the generated passwords was save on directory where the main code is located."
        )
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    sys.exit(app.exec())
