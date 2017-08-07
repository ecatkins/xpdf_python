xpdf python
===============================

version number: 0.0.3
author: Edward Atkins

Overview
--------

Python wrapper for xpdf

Installation / Usage
--------------------

To install using pip from pypi:

    $ pip install xpdf_python

To install using pip from github:

    $ pip install git+https://github.com:/ecatkins/xpdf_python

Or clone the repo:

    $ git clone https://github.com/ecatkins/xpdf_python.git
    $ python setup.py install


If automatic installation of xpdf fails either:
1. Instructions for your OS found [here](http://www.foolabs.com/xpdf/download.html) OR 
2. The bash scripts found in this repo's install_xpdf subdirectory
    

Operating Systems
------------

macOS, Linux

Example
-------

    from xpdf_python import to_text

    pdf_location = '/path/to/my.pdf'
    text = to_text(pdf_location)

Supported by
------------

<a href = "http://dealstatrei.com"><img src="dealstat-logo.png" width="100"> </a>

   