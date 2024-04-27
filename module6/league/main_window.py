import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Connect signals to slots
        self.load_button.clicked.connect(self.load_data)
        self.save_button.clicked.connect(self.save_data)
        self.add_button.clicked.connect(self.add_item)
        self.edit_button.clicked.connect(self.edit_item)
        self.delete_button.clicked.connect(self.delete_item)

    def load_data(self):
        pass

    def save_data(self):
        pass

    def add_item(self):
        item_name = self.name_line.text().strip()
        if item_name:
            self.league_list_widget.addItem(item_name)
            self.name_line.clear()

    def edit_item(self):
        pass

    def delete_item(self):
        current_row = self.league_list_widget.currentRow()
        if current_row != -1:
            self.league_list_widget.takeItem(current_row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
