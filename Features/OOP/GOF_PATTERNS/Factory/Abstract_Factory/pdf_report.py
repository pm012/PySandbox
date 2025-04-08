from reports import Report

class PDFAnnualReport(Report):
    def __init__(self):
        super().__init__()
        self.report_type="PDF Annual Report"

class PDFMonthReport(Report):
    def __init__(self):
        super().__init__()
        self.report_type="PDF Month Report"