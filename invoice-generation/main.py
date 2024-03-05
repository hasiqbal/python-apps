import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoice-generation/invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.set_font(family='Times', size=16, style='B')
    pdf.add_page()
    filename = Path(filepath).stem
    invoiceNumber = filename.split('-')[0]
    pdf.cell(w=50, h=8, txt=f'Invoice Number:{invoiceNumber}')
    pdf.output(f'invoice-generation/invoices{filename}.pdf')
