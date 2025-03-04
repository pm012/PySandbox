from af import PDFReport, CSVReport, AbstractReport

def test_report_factory(factory: AbstractReport):
    annual_report = factory.create_annual_report()
    month_report = factory.create_month_report()

    annual_report.print_report()
    month_report.print_report()

if __name__ == "__main__":
   # Test PDF Reports
    print("Testing PDF Reports:")
    pdf_factory = PDFReport()
    test_report_factory(pdf_factory)

    # Test CSV Reports
    print("\nTesting CSV Reports:")
    csv_factory = CSVReport()
    test_report_factory(csv_factory)