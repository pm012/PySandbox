from abc import ABC, abstractmethod
from pdf_report import PDFAnnualReport, PDFMonthReport
from csv_report import CSVAnnualReport, CSVMonthReport

class AbstractReport (ABC):
    @abstractmethod
    def create_month_report(self):
        pass

    @abstractmethod
    def create_annual_report(self):
        pass


class PDFReport(AbstractReport):
    def create_annual_report(self):
        return PDFAnnualReport()
    
    def create_month_report(self):
        return PDFMonthReport()
    

class CSVReport(AbstractReport):
    def create_annual_report(self):
        return CSVAnnualReport()
    
    def create_month_report(self):
        return CSVMonthReport()