import os
import sys

if os.path.isfile('/usr/local/bin/pdftotext'):
	print("Detected successful installation of xpdf!")
else:
	sys.exit("Did not detect correctly installed xpdf. Please follow install instructions at: https://github.com/ecatkins/xpdf_python.")