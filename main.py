from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

#PAGE BEGIN
pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There!", align="L",
         ln=1)
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="Hi!", align="L",
         ln=1)
#PAGE END

#Creates output file as PDF
pdf.output("output.pdf")