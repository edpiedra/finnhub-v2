from utilities.fingpt import * 

class FinnHubAnalysis():
    def __init__(self):
        print("[INFO] {:.2f}...initializing finhub analysis module".format(
            time.time()-start_time
        ))
        
        self.ticker = None 
        self.start_date = None 
        self.start_date_long = None 
        self.end_date = None 
        
        self.fingpt = FinGPT()
        
    def _load_downloads(self):
        print("[INFO] {:.2f}...loading downloads".format(
            time.time()-start_time
        ))
        
        filename = "news {} - {} - {}.json".format(
            self.ticker, self.start_date, self.end_date
        )
        
        print("[INFO] {:.2f}...loading {}".format(
            time.time()-start_time, filename
        ))
        
        self.news = json.load(open("./downloads/finnhub/" + filename, "r"))
        
        filename = "insider sentiment {} - {} - {}.json".format(
            self.ticker, self.start_date_long, self.end_date
        )
        
        print("[INFO] {:.2f}...loading {}".format(
            time.time()-start_time, filename
        ))
        
        self.insider_sentiment = json.load(open("./downloads/finnhub/" + filename, "r"))
        
        filename = "recommendation trends {}.json".format(self.ticker)
        
        print("[INFO] {:.2f}...loading {}".format(
            time.time()-start_time, self.ticker
        ))
        
        self.recommendation_trends = json.load(open("./downloads/finnhub/" + filename, "r"))
        
        filename = "earnings surprises {}.json".format(self.ticker)
        
        print("[INFO] {:.2f}...loading {}".format(
            time.time()-start_time, self.ticker
        ))
        
        self.earnings_surprises = json.load(open("./downloads/finnhub/" + filename, "r"))
        
    def _news_analysis(self):
        print("[INFO] {:.2f}...analyzing finnhub news for {} from {} to {}".format(
            time.time()-start_time, self.ticker, self.start_date,
            self.end_date
        ))
        
        self.fingpt.reponse_tag = "Answer: "
        
        data = {
            "datetime"  : [],
            "summary"   : [],
            "result"   : [],
        }
        
        for article in self.news:
            data["datetime"].append(article["datetime"])
            summary = article["summary"]
            data["summary"].append(summary)
            
            self.fingpt.prompt = """
            Instruction: What is the sentiment of this news? Please choose an answer from negative/neutral/positive.
            Input: {}
            Answer: 
            """.format(summary)
            
            self.fingpt.generate_prompt_result()
            data["result"].append(self.fingpt.promt_result)
            
        df = pd.DataFrame(
            data=data
        )
        
        df.to_csv(
            "./results/news {} - {} - {}.csv".format(self.ticker, self.start_date, self.end_date)
        )
    
    def _insider_sentiment_analysis(self):
        print("[INFO] {:.2f} analyzing recent insider sentiment for {} from {} to {}".format(
            time.time()-start_time, self.ticker, self.start_date_long, self.end_date
        ))
        
        sentiments = self.insider_sentiment["data"]  
        
        data = {
            "year"  : [],
            "month" : [],
            "mspr"  : [],
        }
        
        for period in sentiments:
            data["year"].append(period["year"])
            data["month"].append(period["month"])
            data["mspr"].append(period["mspr"])
            
        df = pd.DataFrame(
            data=data
        )      
        
        df.to_csv("./results/insider sentiments {} - {} - {}.csv".format(
            self.ticker, self.start_date_long, self.end_date
        ))
    
    def _recommendation_trend_analysis(self):
        print("[INFO] {:.2f}...analyzing recommendation trends for {}".format(
            time.time()-start_time, self.ticker
        ))    
        
        data = {
            "period"    : [],
            "buy"       : [],
            "hold"      : [],
            "sell"      : [],
            "strongBuy" : [],
            "strongSell"    : [],
        }
        
        for trend in self.recommendation_trends:
            data["period"].append(trend["period"])
            data["buy"].append(trend["buy"])
            data["hold"].append(trend["hold"])
            data["sell"].append(trend["sell"])
            data["strongBuy"].append(trend["strongBuy"])
            data["strongSell"].append(trend["strongSell"])
            
        df = pd.DataFrame(
            data=data
        )
        
        df["result"] = df["buy"] - df["sell"] + (2*df["strongBuy"]) - (2*df["strongSell"])
        df["result"] = df["result"] / (df["buy"] + df["hold"] + df["sell"] + df["strongBuy"] + df["strongSell"])
        
        df.to_csv("./results/recommendation trends {}.csv".format(self.ticker))
        
    def _earnings_surprises_analysis(self):
        print("[INFO] {:.2f}...analyzing earnings surprises for {}".format(
            time.time()-start_time, self.ticker
        ))
        
        data = {
            "period"    : [],
            "surprisePercent"   : [],
        }
        
        for surprise in self.earnings_surprises:
            data["period"].append(surprise["period"])
            data["surprisePercent"].append(surprise["surprisePercent"])
            
        df = pd.DataFrame(
            data=data
        )
        
        df.to_csv("./results/earnings surprises {}.csv".format(self.ticker))
        
    def run(self):
        print("[INFO] {:.2f}...running finnhub analysis module for {}".format(
            time.time()-start_time, self.ticker
        ))
            
        self._load_downloads()
        self._news_analysis()  
        self._insider_sentiment_analysis()
        self._recommendation_trend_analysis()
        self._earnings_surprises_analysis() 