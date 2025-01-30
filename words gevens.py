import os
import subprocess
import sys

# Installeer reportlab indien niet aanwezig
subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

def generate_invoice_template(filename):
    os.makedirs("PDF_INVOICE", exist_ok=True)
    filepath = os.path.join("PDF_INVOICE", filename)
    
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4
    
    # Bedrijfsgegevens
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, "Sourdough Delights B.V.")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, "Bakkerstraat 12, 1012 AB Amsterdam")
    c.drawString(50, height - 85, "KVK: 98765432 | BTW: NL123456789B01")
    c.drawString(50, height - 100, "IBAN: NL12BANK0123456789")
    
    # Factuurkop
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 140, "Factuur")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 160, "Factuurnummer: 2024001")
    c.drawString(50, height - 175, "Factuurdatum: 30-01-2025")
    c.drawString(50, height - 190, "Vervaldatum: 13-02-2025")
    
    # Klantinformatie
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 220, "Factuur aan:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 235, "Klantnaam: Jan Jansen")
    c.drawString(50, height - 250, "Adres: Kerkstraat 5, 1234 AB Utrecht")
    
    # Tabel voor factuurregels (met voorbeelddata)
    data = [["Omschrijving", "Aantal", "Prijs per stuk", "Totaal"],
            ["Zuurdesembrood", "2", "€3.50", "€7.00"],
            ["Croissant", "4", "€1.20", "€4.80"],
            ["Baguette", "1", "€2.50", "€2.50"],
            ["Totaal", "", "", "€14.30"]]
    
    table = Table(data, colWidths=[220, 70, 90, 90])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    table.wrapOn(c, width, height)
    table.drawOn(c, 50, height - 350)
    
    # Totaal sectie (met bedragen)
    c.drawString(300, height - 450, "Subtotaal: €13.15")
    c.drawString(300, height - 465, "BTW (9%): €1.15")
    c.drawString(300, height - 480, "Totaal: €14.30")
    
    c.save()
    print(f"Factuur '{filepath}' is gegenereerd.")

# Genereer een factuur met gegevens
generate_invoice_template("factuur.pdf")

# Verwijder reportlab na uitvoering
subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "reportlab"])
