import PyPDF2
import camelot

def extract_text(file_path):
    with open(file_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_metadata(file_path):
    with open(file_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        metadata = pdf.documentInfo
    return dict(metadata)

def extract_tables(file_path):
    tables = camelot.read_pdf(file_path, pages='all', flavor='stream')
    return tables