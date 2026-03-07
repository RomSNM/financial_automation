from flask import Flask, request, jsonify
import os

from src.loader import DataLoader
from src.processor import FinancialProcessor
from src.report_generator import ReportGenerator
from src.email_sender import EmailSender

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Financial Report API is running"
    }

@app.route("/generate-report", methods=["POST"])
def generate_report():

    try:

        if "file" not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files["file"]
        emails = request.form.get("emails")

        if not emails:
            return jsonify({"error": "No emails provided"}), 400

        email_list = [e.strip() for e in emails.split(",")]

        upload_path = "temp_transactions.csv"
        file.save(upload_path)

        loader = DataLoader(upload_path)
        df = loader.load()

        analyzer = FinancialProcessor(df)
        summary = analyzer.generate_summary()

        report = ReportGenerator(df, summary)
        pdf_path, excel_path, csv_path = report.generate_reports()

        sender = EmailSender()
        sender.send_email(email_list, pdf_path)

        os.remove(upload_path)

        return jsonify({
            "message": "Report generated and sent successfully"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)