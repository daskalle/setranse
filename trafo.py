'''
todo module docstring
'''

import dill
import numpy as np


class Trafo(object):
    '''
    docstring goes here
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


t = Trafo(4)

s0 = (30000, 30000, 50)
e0 = (33396901.855, 5828517.635, 50)

e1 = t.transform_to_etr(*s0)
s1 = t.transform_to_oldner(*e0)

print(np.array(s0) - np.array(s1))
print(np.array(e0) - np.array(e1))
