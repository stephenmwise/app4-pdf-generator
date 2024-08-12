from fpdf import FPDF
import pandas as pd

# Page layout
pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Section Page begin
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for y in range(24, 290, 10):
        pdf.line(10, y, 200, y)

    # Adds footer
    pdf.ln(265)

    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Adds additional pages to each section
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)
        # Adds footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    # Added pages end

# Creates output file as PDF
pdf.output("output.pdf")
