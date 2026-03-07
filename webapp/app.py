from flask import Flask, render_template, request, redirect, flash
from pathlib import Path
import os
import uuid

from src.loader import DataLoader
from src.processor import FinancialProcessor
from src.report_generator import ReportGenerator
from src.pdf_generator import PDFReport
from src.email_sender import EmailSender

app = Flask(__name__)
app.secret_key = "supersecretkey"  # pode melhorar depois

UPLOAD_FOLDER = Path("webapp/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        emails = request.form.get("emails")

        if not file or not emails:
            flash("File and emails are required.")
            return redirect("/")

        # salvar arquivo com nome único
        filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = UPLOAD_FOLDER / filename
        file.save(file_path)

        try:
            loader = DataLoader(file_path)
            df = loader.load()

            processor = FinancialProcessor(df)

            output_dir = Path("webapp/reports")
            report = ReportGenerator(processor, output_dir)
            report.generate_excel_report()

            pdf = PDFReport(processor, output_dir)
            pdf.generate_pdf()

            email_sender = EmailSender()
            recipients = [e.strip() for e in emails.split(",")]

            excel_file = output_dir / "financial_report.xlsx"

            email_sender.send_email_with_attachment(
                subject="Financial Report",
                body="Your financial report is attached.",
                recipients=recipients,
                attachment_path=excel_file,
            )

            flash("Report generated and sent successfully!", "success")

        except Exception as e:
            flash(f"Error: {str(e)}", "error")

        return redirect("/")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)