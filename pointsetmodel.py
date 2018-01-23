"""
todo docstring
"""

from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt, QVariant
from point import GeoPoint


class PointsetModel(QAbstractListModel):
    def __init__(self, parent=None, **kwargs):
        super(PointsetModel, self).__init__(parent)
        self._data = []

    def rowCount(self, parent=QModelIndex()):
        """
        overidden method to communicate the number of items to the connected view
        """
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        """
        overidden method to communicate the represenation of a listitem
        """
        if (not index.isValid()) or (index.row() not in range(0, len(self._data))):
            return QVariant()

        row = index.row()

        if role == Qt.DisplayRole:
            return str(row).rjust(5) + " | " + self._data[row].to_bav()

        return QVariant()

    def load_points(self, pointdata):
        self._data = pointdata
