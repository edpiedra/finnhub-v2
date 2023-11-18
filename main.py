
if __name__=="__main__":
    print("[INFO] starting program")
    
    from modules.company_research import * 
    
    company_research = CompanyResearch()
    company_research.run()
    
    print("[INFO] {:.2f}...finished program".format(
        time.time()-start_time
    ))