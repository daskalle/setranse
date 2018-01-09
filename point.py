"""
todo module docstring
"""


class GeoPoint(object):
    '''
    allgemeine Klasse für Vermessungspunkte
    '''

    def __init__(self, pnr, east, north, elev=0, csys=None):
        self.pnr = pnr
        self.east = east
        self.north = north
        self.elev = elev
        self.code = '---'
        self.xcode = '5000'
        self.numbez = '00000000'
        self.desc = '------ ------'
        self.csys = csys if csys else self.infer_csys()

    def infer_csys(self):
        """
        todo docstring
        """
        if (self.east >= 33369300) and (self.east <= 33417000):
            if (self.north >= 5799000) and (self.north <= 5837500):
                return "489"
        elif (self.east >= 3000) and (self.east <= 49800):
            if (self.north >= 800) and (self.north <= 39200):
                return "500"
        else:
            return "000"

    def set_coosys(self, csys="000"):
        """
        todo docstring
        """
        self.csys = str(csys).ljust(3)[:3]

    def set_code(self, code):
        """
        todo docstring
        """
        self.code = str(code).ljust(3)[:3]
        self.xcode = '5' + self.code

    def set_desc(self, desc):
        """
        todo docstring
        """
        self.desc = str(desc).ljust(13)[:13]

    def set_numbez(self, numbez=None):
        """
        todo docstring
        """
        if numbez:
            self.numbez = str(numbez).rjust(8, '0')[:8]
        else:
            if self.csys == "489":
                self.numbez = str(self.east)[1:5] + str(self.north)[:4]
            else:
                self.numbez = '00000000'

    def to_bav(self):
        retval = ("{}      {} {} {:^10}   Y {:>12.3f} "
                  "X {:>13.3f} Z {:>9.3f} C {} {:<13}")

        return retval.format(self.csys, self.xcode, self.numbez, self.pnr,
                             self.east, self.north, self.elev, self.code, self.desc)

    def __repr__(self):
        retval = ("GeoPoint('{}', {}, {}, {}")
        return retval.format(self.pnr, self.east, self.north, self.elev)

    def __str__(self):
        retval = ('GeoPoint: N="{}" R={:.3f} H={:.3f} Z={:.3f}')
        return retval.format(self.pnr, self.east, self.north, self.elev)
