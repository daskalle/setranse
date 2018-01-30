"""
todo Docstring
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout,
                             QPushButton)
from PyQt5.QtGui import QIcon
from pointsetmodel import PointsetModel
from pointslistview import PointsListView
from cooreader import CooReader


class MyWindow(QWidget):
    """
    todo docstring
    """

    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(27, 49, 900, 600)
        self.setWindowIcon(QIcon("test_run_48.png"))
        self.setWindowTitle("S-E-Transe")

        self.pmodel = PointsetModel()
        reader = CooReader()
        self.pmodel.load_points(reader.readdata("./example_data/17-005-lp-kv.bav"))

        self.table = PointsListView()
        self.table.setModel(self.pmodel)
        self.initui()

        self.show()

    def initui(self):
        """sets up the gui elements and the interaction logic
        """
        main_layout = QHBoxLayout()

        but_layout = QVBoxLayout()
        but_layout.addStretch(1)
        but1 = QPushButton("Load")
        but2 = QPushButton("Save")
        but3 = QPushButton("Exit")
        but_layout.addWidget(but1)
        but_layout.addWidget(but2)
        but_layout.addWidget(but3)

        main_layout.addLayout(but_layout)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

        but3.clicked.connect(self.close)

if __name__ == '__main__':
    application = QApplication(sys.argv)
    wind = MyWindow()

    sys.exit(application.exec_())
