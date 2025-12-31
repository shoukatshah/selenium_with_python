import requests
import logging

class SauceDemoAPI:
    BASE_URL = "https://api-lap.webook.rocks/api/v2"
    
    def __init__(self):
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
    
    def login(self,email,password,captcha,signature,lang="en",app_source="rs",login_with="email"):
            payload = {"app_source": app_source,"captcha": captcha,"email": email,"lang": lang,"login_with": login_with,"password": password,"signature": signature}
            self.logger.info(f"Sending login request for user: {email}")
            response = self.session.post(
            f"{self.BASE_URL}/login",
            json=payload
        )

            return response
