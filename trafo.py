'''
todo module docstring
'''

import dill
import numpy as np


class Trafo(object):
    '''
    class that performs the transformation operations
    '''

    def __init__(self, precision=3):
        self.precision = precision
        with open('shift_e2s.pcl', 'rb') as f:
            self.f_e2s = dill.load(f)

        with open('shift_s2e.pcl', 'rb') as f:
            self.f_s2e = dill.load(f)

    def transform_to_etrs(self, easting, northing, elevation=0):
        '''
        todo docstring
        '''
        yx = np.round(self.f_s2e([(easting, northing)])[0], self.precision)
        return yx[0], yx[1], round(elevation, self.precision)

    def transform_to_soldner(self, easting, northing, elevation=0):
        '''
        todo docstring
        '''
        yx = np.round(self.f_e2s([(easting, northing)])[0], self.precision)
        return yx[0], yx[1], round(elevation, self.precision)

    def trasform(self, point, kind):
        if kind.lower() == 's2e':
            x, y, z = self.transform_to_etrs(point.east, point.north, point.elev)
            point.reset_coo(x, y, z, "489")

        elif kind.lower() == 'e2s':
            x, y, z = self.transform_to_soldner(point.east, point.north, point.elev)
            point.reset_coo(x, y, z, "500")
        else:
            raise ValueError("argument 'kind' should be either 's2e' or 'e2s'")
