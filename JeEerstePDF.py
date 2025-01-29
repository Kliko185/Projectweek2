import os
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
except ModuleNotFoundError:
    import sys
    print("Module 'reportlab' is not installed. Installing now...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

def generate_pdf(filename, title, text):
    os.makedirs("PDF_INVOICE", exist_ok=True)
    filepath = os.path.join("PDF_INVOICE", filename)
    
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 100, title)
    
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 130, text)
    
    c.save()
    print(f"PDF '{filepath}' is gegenereerd.")

# Gebruik het programma
generate_pdf("resultaat.pdf", "Project week2", "Hallo, dit is mijn eerste PDF.")

subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "reportlab"])