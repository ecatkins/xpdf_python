import os
import sys
import re
import subprocess



def countPages(filename):  
	''' Counts number of pages in PDF '''

	# NOTE: Currently does not work 100% of the time
	rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)
	data = open(filename,"r", encoding = "ISO-8859-1").read()
	return len(rxcountpages.findall(data))

def to_text(file_loc, page_nums = True):
	''' Converts PDF to text

	Args
	- - - - - - -
		file_loc: path to pdf document, string
		page_nums: whether to insert page numbers into document, boolean
	
	Returns
	- - - - - - -
		text: extracted text from pdf document, string
		actual_count: estimated number of pages for pdf document, integer
	
	'''

	# Determines location of file
	if os.path.isabs(file_loc):
		full_file_loc = file_loc
	else:
		cd = os.path.dirname(os.path.realpath(__file__))
		full_file_loc = os.path.join(cd, file_loc)

	text = ''
	actual_count = 0

	# If page numbers are to be inserted
	if page_nums:
		# Count number of pages
		num = countPages(full_file_loc)
		# Accounts for errors occuring in countPages function
		if num == 0:
			num = 100
		for i in range(num):
			actual = i + 1
			# Calls xpdf 
			subprocess.call(['pdftotext', full_file_loc, '-f', str(actual), '-l', str(actual)])
			# Opens file saved to disk 
			saved_file = full_file_loc.replace('.pdf','.txt')
			file = open(saved_file,'r', encoding = "ISO-8859-1")
			t = file.read()
			# If the page is blank, it is not a real page
			if t == '':
				continue
			else:
				actual_count += 1
			# Add text and page count to existing string
			text += '***Page {}*** {}'.format(actual, t)
			file.close()
	else:
		# TO BE IMPLEMENTED
		pass

	# Remove file saved to disk
	os.remove(saved_file)

	return text, actual_count
	

