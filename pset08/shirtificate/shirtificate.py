from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()

# add header text
pdf.set_font("helvetica", "B", 40)
pdf.cell(150, 10, text="CS50 Shirtificate")
pdf.ln(20)

# add image
pdf.image("shirtificate.png",x=10, y=50, w=190)

# add text on image
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(255, 255, 255)
pdf.cell(190, 200, text=f"{name} took CS50.", align="C")


# save pdf
pdf.output("shirtificate.pdf")
