# mergepdf
To merge multiple pdf files into one.  
It uses [pymupdf](https://github.com/pymupdf/PyMuPDF) for merging the files.  
It uses [easygui](https://pypi.org/project/easygui/) for selecting files using the system file select box.  

__Install modules using pip__  
`pip install pymupdf`  
`pip install easygui`  

__To use run__  
`python joinpdf_dialogue.py` in command line


Select multiple files using __ctrl__

Also With pymupdf multiple pdf's can be merged simply with this one line command.  
`python -m fitz join -o outputfilename.pdf inputfilename1.pdf inputfilename2.pdf inputfilename3.pdf`  
To join all the pdf's in the folder  
`python -m fitz join -o outputfilename.pdf ./*.pdf`  
`python -m fitz join -o outputfilename.pdf ./somesimilarthing*.pdf`  
