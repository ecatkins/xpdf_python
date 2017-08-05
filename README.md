xpdf python
===============================

version number: 0.0.1
author: Edward Atkins

Overview
--------

Python wrapper for xpdf

Installation / Usage
--------------------

To install use pip:

    $ pip install xpdf_python


Or clone the repo:

    $ git clone https://github.com/ecatkins/xpdf_python.git
    $ python setup.py install


Must first use install xpdf using 1) instructions for your OS found (here) [http://www.foolabs.com/xpdf/download.html] OR 2) the bash scripts found in the install_xpdf subdirectory
    
Supported by
------------

(Dealstat REI) [http://dealstatrei.com/] ![Dealstat Logo](dealstat-logo.png)

OS
------------

macOS, Linux

Example
-------

    from xpdf_python.pdf import to_text

    pdf_location = '/path/to/my.pdf'
    text = to_text(pdf_location)


   