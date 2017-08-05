import os
import sys
import re
import subprocess



def countPages(filename):  
	''' Counts number of pages in PDF '''
	rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)
	data = open(filename,"r", encoding = "ISO-8859-1").read()
	return len(rxcountpages.findall(data))

def to_text(file_loc, page_nums = True, page_count = True):
	if os.path.isabs(file_loc):
		full_file_loc = file_loc
	else:
		cd = os.path.dirname(os.path.realpath(__file__))
		full_file_loc = os.path.join(cd, file_loc)
	text = ''
	actual_count = 0
	if page_nums:
		num = countPages(full_file_loc)
		if num == 0:
			num = 40
		for i in range(num):
			actual = i + 1
			subprocess.call(['pdftotext', full_file_loc, '-f', str(actual), '-l', str(actual)])
			saved_file = full_file_loc.replace('.pdf','.txt')
			file = open(saved_file,'r', encoding = "ISO-8859-1")
			t = file.read()
			if t == '':
				continue
			else:
				actual_count += 1
			text += 'Page {} {}'.format(actual, t)
			file.close()
	os.remove(saved_file)


	if page_count:
		return text, actual_count
	else:
		return text

