from typing import Dict
import requests

class HttpRequester:
    def __init__(self) -> None:
        self.url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
    
    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.url)

        #print(response)
        #print(response.status_code)
        #print(response.text)
        return {
            "status_code": response.status_code,
            "html": response.text
        }