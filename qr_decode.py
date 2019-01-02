#!/usr/bin/env python
import sys
import qrtools
myimg = sys.argv[1]
qr = qrtools.QR()
qr.decode(myimg)
print qr.data
