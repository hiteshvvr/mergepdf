import fitz as ft
import easygui as eg

output = ft.open()

input_files = eg.fileopenbox(msg="Use Ctrl/cmd to select multiple files", multiple=True)

# # print(str(len(input_files)) + "  files to Merge")
print(f'Merging  ---> {len(input_files)} <---  files')

for an_infile in input_files:
    an_infile = ft.open(an_infile)
    output.insertPDF(an_infile)

output_file_name = eg.filesavebox(msg="Give Output FileName")
output.save(output_file_name)
