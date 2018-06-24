from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

# print convert('https://arxiv.org/pdf/1801.00054.pdf')

import urllib

url = 'https://arxiv.org/pdf/1801.00054.pdf'
webFile = urllib.urlopen(url)
pdfFile = open(url.split('/')[-1], 'w')
pdfFile.write(webFile.read())
webFile.close()
pdfFile.close()

# base = os.path.splitext(pdfFile)[0]
# os.rename(pdfFile, "test.pdf")

print convert(pdfFile.name)
