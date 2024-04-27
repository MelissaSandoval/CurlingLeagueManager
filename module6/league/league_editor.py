import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, \
    QLineEdit, QWidget
from PyQt5.QtCore import QSize

Ui_LeagueEditor, QtBaseWindow = uic.loadUiType("league_editor.ui")


class LeagueEditor(QMainWindow, Ui_LeagueEditor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setMinimumSize(QSize(896, 691))

        # Connect signals to slots
        self.import_button.clicked.connect(self.import_data)
        self.edit_button.clicked.connect(self.edit_team)
        self.delete_button.clicked.connect(self.delete_team)
        self.add_button.clicked.connect(self.add_team)

    def import_data(self):
        pass

    def edit_team(self):
        pass

    def delete_team(self):
        pass

    def add_team(self):
        team_name = self.lineEdit.text()

        if team_name.strip():
            self.league_list_widget.addItem(team_name)

            self.lineEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LeagueEditor()
    window.show()
    sys.exit(app.exec())
