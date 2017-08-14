# Sample Test passing with nose and pytest

import xpdf_python

def test_pass():
        assert True, "dummy sample test"

def test_basic():
	result = xpdf_python.to_text('xpdf_python/example_pdf.pdf',page_nums = True)
	assert(result[0][:12] == '***Page 1***')
	assert(result[0][13:].startswith('This is a test PDF document.'))
	assert(result[1] == 1)

