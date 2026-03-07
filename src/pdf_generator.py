from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.lib.units import inch
from pathlib import Path


class PDFReport:
    def __init__(self, processor, output_dir="reports"):
        self.processor = processor
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def generate_pdf(self):
        file_path = self.output_dir / "financial_report.pdf"
        doc = SimpleDocTemplate(str(file_path))
        elements = []
        styles = getSampleStyleSheet()

        summary = self.processor.summary()

        elements.append(Paragraph("Financial Summary Report", styles["Title"]))
        elements.append(Spacer(1, 0.3 * inch))

        data = [["Metric", "Value"]]
        for key, value in summary.items():
            data.append([key, f"${value:,.2f}"])

        table = Table(data)
        elements.append(table)

        doc.build(elements)
        return file_path