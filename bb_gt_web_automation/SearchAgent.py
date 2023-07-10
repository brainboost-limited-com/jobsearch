class SearchAgent:


    def __init__(self) -> None:
        subscription_key = "541eeef47fb64b44bca71d257758ff20"
        endpoint = "https://api.bing.microsoft.com/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        
        
    def search(query):
        params = {"q": "Senior Software Engineer jobs", "mkt": "global"}