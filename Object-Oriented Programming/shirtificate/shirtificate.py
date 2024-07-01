from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 45)
        self.cell(0, 70, "CS50 Shirtificate", align="C")

    def text(self, name):
        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", "", 30)
        self.cell(-185, 255, f"{name} took CS50", align="C")

    @classmethod
    def shirt(cls, obj, name):
        obj.add_page(orientation="portrait", format="A4")
        obj.text(name)
        obj.output("shirtificate.pdf")

def main():
    pdf = PDF()
    pdf.shirt(pdf, input("Enter your name: "))

if __name__ =="__main__":
    main()
