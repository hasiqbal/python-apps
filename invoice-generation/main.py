import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoice-generation/invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    invoiceNumber = filename.split('-')[0]
    date = filename.split('-')[1]
    
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt= f'Invoice Number:{invoiceNumber}')
    pdf.ln()

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt= f'date:{date}', ln=1)


    pdf.output(f'invoice-generation/invoices{filename}.pdf')
