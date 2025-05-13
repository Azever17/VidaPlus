# app/utils/report_generator.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_report(content: str):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 750, content)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
