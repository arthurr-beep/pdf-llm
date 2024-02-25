from fastapi import FastAPI, File
from fastapi.responses import JSONResponse
import uvicorn
from pdf_service.parser import extract_metadata, extract_tables, extract_text
app = FastAPI()

@app.post("/parse-pdf/")
async def parse_pdf():
    path = './pdf_service/files/2022-alphabet-annual-report.pdf'
    
    text = extract_text(path)  
    tables = extract_tables(path)  
    metadata = extract_metadata(path)  

    
    response = {
        "text": text,
        "tables": tables,  
        "metadata": metadata,
    }

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8009)
