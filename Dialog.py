import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout
from ReadMetaData import ReadMeatData
from PutExif2Pic import PutExif2Pic
class FileSelectionWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.file_path = None
        self.init_ui()
    def init_ui(self):
        # 创建选择文件按钮
        self.open_file_button = QPushButton('选择文件', self)
        self.open_file_button.clicked.connect(self.open_file_dialog)

        # 显示选择的文件路径的标签
        self.selected_file_label = QLabel(self)

        # 创建确定、取消按钮
        self.confirm_button = QPushButton('确定', self)
        self.confirm_button.clicked.connect(self.confirm_action)

        self.cancel_button = QPushButton('取消', self)
        self.cancel_button.clicked.connect(self.cancel_action)

        # 创建结果显示标签
        self.result_label = QLabel(self)

        # 创建关闭窗口按钮
        self.close_button = QPushButton('关闭', self)
        self.close_button.clicked.connect(self.close)

        # 设置布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.open_file_button)
        layout.addWidget(self.selected_file_label)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.close_button)

        self.setWindowTitle('文件选择窗口')
        self.show()

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        self.file_path, _ = file_dialog.getOpenFileName(self, '选择文件', '', 'All files (*)')
        if self.file_path:
            self.selected_file_label.setText(f'选择的文件：{self.file_path}')

    def confirm_action(self):
        # self.file_path = '/Users/mindray_mis/PycharmProjects/main/res/20230611_495.jpg'
        if self.file_path:
            pic_exif_list = ReadMeatData().read_exif_data(self.file_path)
            PutExif2Pic().PutExif2Pic(pic_exif_list, self.file_path)

    def cancel_action(self):
        self.result_label.setText('点击了取消按钮')

    def get_file_path(self):
        return self.file_path

