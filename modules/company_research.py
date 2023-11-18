from modules.submodules.finnhub_downloads import * 
from modules.submodules.download_analysis import * 
class CompanyResearch():
    def __init__(self):
        print("[INFO] {:.2f}...initializing company research module".format(
            time.time()-start_time
        ))
        
        self.ticker = None 
        self.start_date = None 
        self.start_date_long = None 
        self.end_date = None 
        
        self.finnhub_downloads = FinnHubDownloads()
        self.download_analysis = DownloadAnalysis()
        
    def run(self):
        print("[INFO] {:.2f}...running company research module".format(
            time.time()-start_time
        ))
        
        self.ticker = "AAPL"
        self.start_date = "2023-01-01"
        self.start_date_long = "2018-01-01"
        self.end_date = "2023-03-31"
        
        self.finnhub_downloads.ticker           = self.ticker 
        self.finnhub_downloads.start_date       = self.start_date 
        self.finnhub_downloads.start_date_long  = self.start_date_long 
        self.finnhub_downloads.end_date         = self.end_date
        
        self.finnhub_downloads.get_company_info()
        
        self.download_analysis.ticker           = self.ticker 
        self.download_analysis.start_date       = self.start_date 
        self.download_analysis.start_date_long  = self.start_date_long
        self.download_analysis.end_date         = self.end_date
        
        self.download_analysis.company_analysis()