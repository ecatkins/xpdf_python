import os

x = "cd /tmp/ && wget ftp://ftp.foolabs.com/pub/xpdf/xpdfbin-mac-3.04.tar.gz && tar -xvzf xpdfbin-mac-3.04.tar.gz && cp xpdfbin-mac-3.04/bin64/* /usr/local/bin && cp xpdfbin-mac-3.04/doc/sample-xpdfrc /usr/local/etc/xpdfrc"
# x = "cd /tmp/"
os.system(x)