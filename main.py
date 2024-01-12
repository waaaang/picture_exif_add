import Dialog
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout
import ReadMetaData

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Dialog.FileSelectionWindow()
    sys.exit(app.exec())
