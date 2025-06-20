from fpdf import FPDF
import sys

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.set_font("Helvetica", size=14)

    pdf.add_page(format = "A4")
    pdf.image('shirtificate.png', w=178, h=178.3)

    pdf.cell(180, -350, txt="CS50 Shirtcificate", ln=True, align='C')

    pdf.ln(80)

    pdf.set_y(pdf.get_y() + 150)

    pdf.set_font("Helvetica", size=20)

    pdf.set_text_color(255, 255, 255)

    pdf.cell(180, 10, txt=f"{name} took CS50", ln=True, align='C')

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
