from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit= "mm",format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

dataFrame = pd.read_csv("topics.csv")

for index, row in dataFrame.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
   

    for y in range (20,298,10):
        pdf.line(10, y, 200, y)


    for i in range(row["Pages"] - 1):
        pdf.add_page()
        
        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)
        

        for y in range (20,298,10):
            pdf.line(10, y, 200, y)


pdf.output("output.pdf")

   