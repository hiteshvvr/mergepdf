import fitz

output = fitz.open()

listofinputfiles = ['file1.pdf', 'file2.pdf', 'file3.pdf']

for afile in listofinputfiles:
    tfile = fitz.open(afile)
    output.insertPDF(tfile)

output.save("outputfile.pdf")
