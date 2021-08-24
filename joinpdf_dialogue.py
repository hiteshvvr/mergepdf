import fitz as ft
import easygui as eg

output = ft.open()

listofinputfiles = eg.fileopenbox(msg="Use Ctrl/cmd to select multiple files", multiple=True)

print(str(len(listofinputfiles)) + "  files to Merge")

for afile in listofinputfiles:
    tfile = ft.open(afile)
    output.insertPDF(tfile)

outputfilename = eg.filesavebox(msg="Give Output FileName")
output.save(outputfilename)
