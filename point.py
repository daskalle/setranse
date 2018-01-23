"""
todo module docstring
"""


class GeoPoint(object):
    '''
    general class for geodetic coordinates
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
        tries to infer the code of the coordinate system from coordinate values
        """
        if (self.east >= 33369300) and (self.east <= 33417000):
            if (self.north >= 5799000) and (self.north <= 5837500):
                return "489"
        elif (self.east >= 3000) and (self.east <= 49800):
            if (self.north >= 800) and (self.north <= 39200):
                return "500"

        return "000"

    def reset_coo(self, east, north, elev=None, csys=None, infercs=False):
        """resets coordinate values and optionally code of the coordinate system inplace

        Parameters:
        ----------
        east, north : float
            the point's 2D coordinate values
        elev : float, optional
            elevation or height of point (the default is None, which mean point is 2D)
        csys : 3-digit-string, optional
            code for the points reference system 'Lagestatus'
            (the default is None, which means reference system is not known)
        infercs : bool, optional
            states whether `csys` shall be inferred from coordinate values
            (the default is False, which implies no inference)
        """

        self.east = east
        self.north = north
        if elev:
            self.elev = elev
        if csys:
            self.set_coosys(csys)
        elif infercs:
            self.set_coosys(self.infer_csys())

    def set_coosys(self, csys="000"):
        """sets the code of the coordinate system and updates automatically
        the code of the numbering area

        Parameters:
        ----------
        csys : 3-digit-string, optional
            code for the points reference system 'Lagestatus'
            (the default is "000", which stands for a local reference system)

        """

        self.csys = str(csys).ljust(3)[:3]
        self.set_numbez()

    def set_code(self, code):
        """sets pointcode and extended pointcode (used in BAVs)

        Parameters:
        ----------
        code : 3 digit int >= 100
            point code that describes the point type
        """

        self.code = str(code).ljust(3)[:3]
        self.xcode = '5' + self.code

    def set_desc(self, desc):
        """sets description string for point

        Parameters:
        ----------
        desc : string
            short description text with not more than 13 letters
        """


        self.desc = str(desc).ljust(13)[:13]

    def set_numbez(self, numbez=None):
        """sets code of numbering area

        numbez : unsigned int, optional
            numbering area code
            (the default is None, for code inference or setting of a default value)

        """

        if numbez:
            self.numbez = str(numbez).rjust(8, '0')[:8]
        else:
            if self.csys == "489":
                self.numbez = str(self.east)[1:5] + str(self.north)[:4]
            else:
                self.numbez = '00000000'

    def to_bav(self):
        """generates point representation used in BAV coordinate files

        Returns
        -------
        string
            point data in 1 line string
        """

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
