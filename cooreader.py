'''
todo module docstring
'''

import re
import point


class CooReader:
    """Reads Coordinates from BAV and TXT files"""

    def __init__(self, kind='bav'):
        super(CooReader, self).__init__()
        self.kind = kind
        bavstring = r"^(?P<sys>\d{1,3}) +(?P<xcode>\d.{3}) +(?P<nb>\d+) +"
        bavstring += r"(?P<name>[\w\.]+) +y +(?P<ost>\d+\.\d+) +x +"
        bavstring += r"(?P<nord>\d+\.\d+) +z +(?P<z>\d+\.\d+)? +c +"
        bavstring += r"(?P<pktcode>.{3}) *(?P<beschr>[\w\.-]* *[\w\.-]*){0,1}"

        self.rex_bav = re.compile(bavstring, re.IGNORECASE)

    def readdata(self, filename):
        '''
        todo docstring
        '''
        try:
            with open(filename, 'r') as f:
                rawdata = f.readlines()
                rawdata = [line.rstrip('\r\n') for line in rawdata]

        except OSError as exc:
            print("Datei {} kann nicht gelesen werden\n{}".format(filename, exc))
            rawdata = []

        coodata = [self._topoint(line) for line in rawdata]

        return coodata

    def _topoint(self, line):
        '''
        todo docstring
        '''
        match = self.rex_bav.match(line)

        ptnr = match.group('name')
        east = float(match.group('ost'))
        north = float(match.group('nord'))
        try:
            elev = float(match.group('z'))
        except TypeError:
            elev = 0.0

        pnt = point.GeoPoint(ptnr, east, north, elev)

        if match.group('sys') and len(match.group('sys')) == 3:
            pnt.set_coosys(match.group('sys'))

        if match.group('nb'):
            pnt.set_numbez(match.group('nb'))

        if (match.group('pktcode')) and (len(match.group('pktcode')) == 3):
            pnt.set_code(match.group('pktcode'))

        pnt.set_desc(match.group('beschr'))

        return pnt


cr = CooReader()

cr.readdata('17-005-lp-kv.bav')
# print(cr.readdata('17-005-lp-kv.bav'))
