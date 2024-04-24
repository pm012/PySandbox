from docx import Document
from docx2pdf import convert

# Provide the path to your Word document


docx_file = 'pdfconverter/Serhii_Kroshka_PythonDeveloper.docx'

#convert doc to docx
#doc = Document(doc_file)
#doc.save(docx_file)

# Provide the path where you want to save the PDF file
pdf_file = 'pdfconverter/Serhii_Kroshka_PythonDeveloper.pdf'

# Convert the Word document to PDF
convert(docx_file, pdf_file)



