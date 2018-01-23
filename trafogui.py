"""
todo Docstring
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from pointsetmodel import PointsetModel
from pointslistview import PointsListView
from cooreader import CooReader

class MyWindow(QMainWindow):
    """
    todo docstring
    """

    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(27, 49, 800, 600)
        self.setWindowIcon(QIcon("test_run_48.png"))
        self.setWindowTitle("Transe")

        self.pmodel = PointsetModel()
        reader = CooReader()
        self.pmodel.load_points(reader.readdata("./example_data/17-005-lp-kv.bav"))

        self.table = PointsListView()
        self.table.setModel(self.pmodel)
        self.setCentralWidget(self.table)

        self.show()


application = QApplication(sys.argv)
wind = MyWindow()

sys.exit(application.exec_())
