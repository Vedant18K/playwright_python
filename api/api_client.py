import os
import json
from playwright.sync_api import sync_playwright
from utils.env import Env

class APIClient:
    def __init__(self):
        self.base_url = Env.API_BASE_URL
        print("Base URL Loaded:", self.base_url)
        self.token = self.get_token()
        
        self.playwright = sync_playwright().start()
        
        
        self.context = self.playwright.request.new_context(
            base_url=self.base_url,
            extra_http_headers={
                "Content-type":"application/json"
            }
        )
        
    def get_token(self):
        token_path = os.path.join("storage","auth.json")
        
        if os.path.exists(token_path):
            with open(token_path,"r") as f:
                data = json.load(f)
                return data.get("access_token")
            
        return None
    
    def save_token(self,token):
        os.makedirs("storage",exist_ok=True)
        
        with open("storage/auth.json","w") as f:
            json.dump({"access_token":token},f)
            
        self.token = token
        
    def _auth_header(self):
        if not self.token:
            raise Exception("Token is not available. Please login first.")
        return {"Authorization": f"Bearer {self.token}"}
    
    def get(self,endpoint,auth=True,params=None):
        headers = self._auth_header() if auth else{}
        return self.context.get(endpoint,headers=headers,params=params)
    
    def post(self,endpoint, payload=None , auth=True,):
        headers = self._auth_header() if auth else{}
        return self.context.post(endpoint,data=payload ,headers=headers)
    
    def put(self,endpoint, payload=None , auth=True,):
        headers = self._auth_header() if auth else{}
        return self.context.put(endpoint,data=payload ,headers=headers)
    
    def delete(self,endpoint,  auth=True):
        headers = self._auth_header() if auth else{}
        return self.context.delete(endpoint,headers=headers)
    
    def close(self):
        self.context.dispose()
        self.playwright.stop()