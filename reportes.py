import json
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


with open('prestamos.json', 'r', encoding= "utf-8") as f:
    data = json.load(f)
def generar_reporte():
     for prestamo in prestamos:
          c
     

def generar_pdf(self):
        pdf_file = "reporte.pdf"
        c = canvas.Canvas(pdf_file, pagesize=A4)
        width, height = A4

        c.drawString(100, height - 40, "Reporte de Búsqueda de Libros")

        y_position = height - 80
        for libro in self.resultados:
            c.drawString(100, y_position, f"Título: {libro['titulo']}")
            c.drawString(100, y_position - 20, f"Autor: {libro['autor']}")
            c.drawString(100, y_position - 40, f"Género: {libro['genero']}")
            c.drawString(100, y_position - 60, f"Editorial: {libro['editorial']}")
            y_position -= 100

            if y_position < 100:
                c.showPage()
                y_position = height - 40

        c.save()
        print(f"Reporte generado: {pdf_file}")