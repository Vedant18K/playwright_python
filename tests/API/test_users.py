from api.api_client import APIClient

class TestUsers:
    def setup_class(cls):
        cls.api = APIClient()
    
    def test_create_user(self):
        payload={
            "username":"emilys",
            "password":"emilyspass"
        }
        response = self.api.post("/auth/login",payload , auth=False)
        assert response.status == 200
        token = response.json().get("accessToken")
        self.api.save_token(token)
        print("Token Saved Successfully")
    def get_user(self):
        
        user_response = self.api.get("auth/me",auth=True)
        assert user_response.status == 200
        print(user_response.json())