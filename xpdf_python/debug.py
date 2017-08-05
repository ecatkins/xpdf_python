from wrapper import *

if __name__ == '__main__':
	if len(sys.argv) > 1:
		pdf_loc = sys.argv[1]
	else:
		pdf_loc = '/path/to/pdf'
	test = to_text(pdf_loc)
	print(test)