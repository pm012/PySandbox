from reports import Report

class CSVAnnualReport(Report):
    def __init__(self):
        super().__init__()
        self.report_type="CSV Annual Report"

   

class CSVMonthReport(Report):
    def __init__(self):
        super().__init__()
        self.report_type="CSV Month Report"