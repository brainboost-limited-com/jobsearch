from bb_gt_web_automation.SearchAgent import SearchAgent


class BingSearch(SearchAgent):
    
    
    def __init__(self) -> None:
        super().__init__()
        subscription_key = "541eeef47fb64b44bca71d257758ff20"
        endpoint = "https://api.bing.microsoft.com/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        
        
    def search(self,query):
        params = {"q": "Senior Software Engineer jobs", "mkt": "global"}