from variables.variables import * 

class FinnHubDownloads():
    def __init__(self):
        print("[INFO] {:.2f}...initializing finnhub downloads".format(
            time.time()-start_time
        ))
        
        self.ticker = None 
        self.start_date = None 
        self.start_date_long = None 
        self.end_date = None 
        
        self.finnhub_client = finnhub.Client(api_key=PrivateData.finnhub_api_key)
        
    def _company_news(self):
        print("[INFO] {:.2f}...getting company news for {} from {} to {}".format(
            time.time()-start_time, self.ticker, self.start_date, self.end_date
        ))
        
        #UPTO 1 YEAR OF HISTORY FREE
        #datetime - UNIX timestamp
        news = self.finnhub_client.company_news(
            symbol=self.ticker,
            _from=self.start_date,
            to=self.end_date
        )
        
        json.dump(
            news,
            open("./downloads/finnhub/news {} - {} - {}.json".format(
                self.ticker, self.start_date, self.end_date
            ), "w")
        )
        
    def _company_peers(self):
        print("[INFO] {:.2f}...getting company peers for {}".format(
            time.time()-start_time, self.ticker
        ))
        
        peers = self.finnhub_client.company_peers(self.ticker)
        
        json.dump(
            peers,
            open("./downloads/finnhub/peers {}.json".format(self.ticker), "w")
        )
        
    def _insider_sentiments(self):
        print("[INFO] {:.2f}...getting insider sentiments {}: {} - {}".format(
            time.time()-start_time, self.ticker, self.start_date_long, self.end_date
        ))
        
        #MSPR RANGES FROM -100 (MOST NEGATIVE) TO +100 (MOST POSITIVE)
        #CAN SIGNAL PRICE CHANGES IN THE COMING 30-90 DAYS
        #MSPR IS MONTHLY SHARE PURCHASE RATIO - https://medium.com/@stock-api/finnhub-insiders-sentiment-analysis-cc43f9f64b3a
        
        insider_sentiment = self.finnhub_client.stock_insider_sentiment(
            self.ticker, self.start_date_long, self.end_date
        )
        
        json.dump(
            insider_sentiment,
            open("./downloads/finnhub/insider sentiment {} - {} - {}.json".format(
                self.ticker, self.start_date_long, self.end_date
            ), "w")
        )
        
    def _recommendation_trends(self):
        print("[INFO] {:.2f}...getting recommendation trends {}".format(
            time.time()-start_time, self.ticker
        ))
        
        #GETS LATEST TRENDS
        #ANALYSIS WOULD ENTAIL A NET RECOMMENDATION RATIO (DOUBLE WEIGHT TO STRONG)
        
        rec_trends = self.finnhub_client.recommendation_trends(self.ticker)
        
        json.dump(
            rec_trends,
            open("./downloads/finnhub/recommendation trends {}.json".format(self.ticker), "w")
        )
        
    def _earnings_surprises(self):
        print("[INFO] {:.2f}...getting earnings surprises for {}".format(
            time.time()-start_time, self.ticker
        ))
        
        #QUARTERLY GOING BACK TO 2000
        #FREE TIER ONLY GOES BACK 4 QUARTERS
        earnings_surp = self.finnhub_client.company_earnings(self.ticker)
        
        json.dump(
            earnings_surp,
            open("./downloads/finnhub/earnings surprises {}.json".format(self.ticker), "w")
        )
        
    def get_company_info(self):
        self._company_news()
        self._company_peers()
        self._insider_sentiments()
        self._recommendation_trends()
        self._earnings_surprises()
        