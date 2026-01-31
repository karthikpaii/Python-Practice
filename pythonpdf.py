from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=16)
pdf.cell(0,10,"Welcome BAck To India",ln=True,align="c")
pdf.output("new.pdf")
