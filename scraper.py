import requests
from config import userAgent

class Scraper:

    def __init__(self, url):
        try: 
            self.headers = {'user-agent': userAgent}
            self.req = requests.get(url, headers=self.headers, timeout=2)
            self.text = self.req.text 
        except requests.exceptions.Timeout as e: 
            print(e)
            self.text = '' 
        except requests.exceptions.SSLError as e: 
            print(e)
            self.text = '' 

    def resultado(self):
        return self.text
 