import fitz

output = fitz.open()

input_files = ['input_file_name1.pdf', 'input_file_name2.pdf', 'input_file_name3.pdf']

for input_file in input_files:
    input_file = fitz.open(input_file)
    output.insertPDF(input_file)

output.save("output_file_name.pdf")
