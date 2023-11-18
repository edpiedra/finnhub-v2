from modules.submodules.download_analysis_modules.finnhub import * 

class DownloadAnalysis():
    def __init__(self):
        print("[INFO] {:.2f}...initializing download analysis module".format(
            time.time()-start_time
        ))
        
        self.finnhub = FinnHubAnalysis()
        
        self.ticker = None 
        self.start_date = None 
        self.start_date_long = None 
        self.end_date = None 
        
    def _run_finnhub_analysis(self):
        self.finnhub.ticker = self.ticker 
        self.finnhub.start_date = self.start_date 
        self.finnhub.start_date_long = self.start_date_long 
        self.finnhub.end_date = self.end_date 
        
        self.finnhub.run()
        
    def company_analysis(self):
        print("[INFO] {:.2f}...generating company analysis for {}".format(
            time.time()-start_time, self.ticker
        ))
        
        self._run_finnhub_analysis()