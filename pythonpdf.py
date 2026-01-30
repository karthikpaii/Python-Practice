from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=16)
pdf.cell(0,10,"Hello My Name is Chew CHEw Chew",ln=True,align="c")
pdf.output("Hello.pdf")
