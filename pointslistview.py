from PyQt5.QtWidgets import QListView
from PyQt5.QtGui import QFont


class PointsListView(QListView):

    def __init__(self):
        super(PointsListView, self).__init__()
        # self.setFont(QFont("Consolas"))
        self.setFont(QFont("Courier New"))
