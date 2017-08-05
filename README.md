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


If automatic installation of xpdf fails either:
1. Instructions for your OS found [here](http://www.foolabs.com/xpdf/download.html) OR 
2. The bash scripts found in this repo's install_xpdf subdirectory
    
Supported by
------------

<img src="dealstat-logo.png" width="100">
[Dealstat REI](http://dealstatrei.com/)

OS
------------

macOS, Linux

Example
-------

    from xpdf_python import to_text

    pdf_location = '/path/to/my.pdf'
    text = to_text(pdf_location)


   