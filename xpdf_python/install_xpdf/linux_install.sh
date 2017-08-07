#!/bin/bash

echo "INSTALLING XPDF"
cd /tmp/
wget ftp://ftp.foolabs.com/pub/xpdf/xpdfbin-linux-3.04.tar.gz
tar -xvzf xpdfbin-linux-3.04.tar.gz
cp xpdfbin-linux-3.04/bin64/* /usr/local/bin
cp xpdfbin-linux-3.04/doc/sample-xpdfrc /usr/local/etc/xpdfrc

