import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget
from PyQt5.QtCore import QSize

Ui_TeamEditor, QtBaseWindow = uic.loadUiType("team_editor.ui")


class TeamEditor(QMainWindow, Ui_TeamEditor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setMinimumSize(QSize(800, 759))

        self.add_button.clicked.connect(self.add_member)
        self.update_button.clicked.connect(self.update_member)
        self.edit_button.clicked.connect(self.edit_member)
        self.delete_button.clicked.connect(self.delete_member)

    def add_member(self):
        name = self.lineEdit.text()
        email = self.lineEdit_2.text()

        if name.strip() and email.strip():
            member_text = f"{name} - {email}"
            self.league_list_widget.addItem(member_text)

            self.lineEdit.clear()
            self.lineEdit_2.clear()

    def update_member(self):
        pass

    def edit_member(self):
        pass

    def delete_member(self):
        selected_item = self.league_list_widget.currentItem()
        if selected_item is not None:
            self.league_list_widget.takeItem(self.league_list_widget.row(selected_item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TeamEditor()
    window.show()
    sys.exit(app.exec())
