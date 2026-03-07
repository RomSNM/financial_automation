from pathlib import Path
import argparse
from src.email_sender import EmailSender

from src.loader import DataLoader
from src.processor import FinancialProcessor
from src.report_generator import ReportGenerator
from src.pdf_generator import PDFReport


def parse_args():
    parser = argparse.ArgumentParser(
        description="Financial Data Automation Tool"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to input CSV or Excel file"
    )

    parser.add_argument(
        "--output",
        default="reports",
        help="Output directory for reports"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    file_path = Path(args.file).resolve()
    output_dir = Path(args.output)

    loader = DataLoader(file_path)
    df = loader.load()

    processor = FinancialProcessor(df)

    report = ReportGenerator(processor, output_dir)
    report.generate_csv_report()
    report.generate_excel_report()

    pdf = PDFReport(processor, output_dir)
    pdf.generate_pdf()

    print("Reports generated successfully!")

        # Send email
    email_sender = EmailSender()

    recipients = [
        "romulo-arj@outlook.com",
        "romulotatico01@gmail.com",
    ]

    excel_file = output_dir / "financial_report.xlsx"

    email_sender.send_email_with_attachment(
        subject="Monthly Financial Report",
        body="Please find attached the financial report.",
        recipients=recipients,
        attachment_path=excel_file,
    )


if __name__ == "__main__":
    main()