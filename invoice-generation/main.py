import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoice-generation/invoices/*.xlsx')

# to read file paths
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

   # table column names
    columns = list(df.columns)
    columns = [item.replace('_', ' ').title() for item in columns]
    pdf.set_font(family='Times', size=10, style= 'B')
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=35, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    
   # table rows     
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10, style= 'B')
        pdf.cell(w=30, h=8, txt= f'{row["product_id"]}', border=1),
        pdf.cell(w=70, h=8, txt= f'{row["product_name"]}', border=1)
        pdf.cell(w=35, h=8, txt= f'{row["amount_purchased"]}', border=1)
        pdf.cell(w=30, h=8, txt= f'{row["price_per_unit"]}', border=1)
        pdf.cell(w=30, h=8, txt= f'{row["total_price"]}', border=1, ln=1)
       
total_sum = df['total_price'].sum()       
pdf.set_font(family='Times', size=10, style= 'B')
pdf.cell(w=30, h=8, txt= '', border=1),
pdf.cell(w=70, h=8, txt= '', border=1)
pdf.cell(w=35, h=8, txt= '', border=1)
pdf.cell(w=30, h=8, txt= '', border=1)
pdf.cell(w=30, h=8, txt= str(total_sum), border=1, ln=1)


pdf.set_font(family='Times', size=10, style= 'B')
pdf.cell(w=30, h=8, txt=f'the the total price is {total_sum}', ln=1)

pdf.output(f'invoice-generation/invoices{filename}.pdf')

