import json
import random
from locust import HttpUser, TaskSet, task, between


class PatientAPITasks(TaskSet):
    def on_start(self):
        """Executed when a user starts a test session."""
        self.access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inh2TTRPUzNhalRJNXFteVEtVGQzZCJ9.eyJwYXRpZW50X3VzZXJfcGsiOjQ5NywiaXNzIjoiaHR0cHM6Ly9lbWEtZGV2ZWxvcG1lbnQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY3YmVkOWYwMDIyNTNmYjcxZDQ4NTk5NCIsImF1ZCI6WyJodHRwczovL2xpcmFuLXRlc3Rlci5jb20iLCJodHRwczovL2VtYS1kZXZlbG9wbWVudC5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzQxNTEwODQ2LCJleHAiOjE3NDE1OTcyNDYsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJvcmdfaWQiOiJvcmdfeEM0eUpiZ2hDVEpKRkhjZiIsIm9yZ19uYW1lIjoiYWl2ZiIsImF6cCI6InhIRWlvb09ZYXhvRE1uNExEVUd6SFB0UGJWV1A5NFZzIn0.uT2m1NLILcC66fc2_lGyufge0QhYxETjW6Oe9Mpf64MTE1UjQCffiSccVHcZt89Y1zpZJmfTQcqUvV9R2_eobk3wx4qX-BhzmhEiDQEmw5i5xK5KHGSgl3NLHJ4tLAtZ9QFXyiEVfUiNzdoIBsqZwyJyyLkTkd3O2jkxx4Wy2C_UEwhctB4cTAdZAl509gGRVXvN--lpqhPchksTNHd0sdBXkX76n1SEDSgldpIw7lxe8aR16AQcuWCvkcgiSzZkq3892GrivHjS3dEDPWC8dZB-Y_ATuYtAiFkbQplLbCme65yWuQMPRzco9yDaQVZOP-VPTzwEO8mMWoDyrQHZTA"  # Replace with a valid token
        if not self.access_token:
            raise ValueError("❌ ERROR: ACCESS_TOKEN is not set!")

        self.headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': f'Bearer {self.access_token}',
            'tzOffsetInMinutes': '120',
        }

        self.chat_id = None  # Store chat ID dynamically
        self.tenant_id = "100"  # Replace if necessary

    @task(2)
    def get_chats(self):
        """Fetches the list of patient chats."""
        url = "/api/v1/patient/messaging/chats"
        response = self.client.get(url, headers=self.headers)
        data = self.process_response(response)

        if data and "content" in data and len(data["content"]) > 0:
            self.chat_id = data["content"][0]["chatId"]
            print(f"💬 Using chatId: {self.chat_id}")

    @task(4)
    def get_bfm_cycle(self):
        """Fetches the list of patient chats."""
        url = "/api/v1/LastCycle"
        response = self.client.get(url, headers=self.headers)
        data = self.process_response(response)

    @task(5)
    def get_bfm_profile(self):
        """Fetches the list of patient chats."""
        url = "/api/v1/profile"
        response = self.client.get(url, headers=self.headers)
        data = self.process_response(response)

    # @task(1)
    # def create_chat(self):
    #     """Creates a new chat with a random topic."""
    #     url = "/api/v1/patient/messaging/chats"
    #     topic_id = random.randint(0, 4)  # Select a random topic
    #
    #     payload = {
    #         "tenantId": self.tenant_id,  # Tenant ID is now included
    #         "topicId": topic_id,
    #         "initialMessage": {"messageContent": "Hello, this is a test message."}
    #     }
    #
    #     response = self.client.post(url, headers=self.headers, json=payload)
    #     data = self.process_response(response)
    #
    #     if data and "chatId" in data:
    #         self.chat_id = data["chatId"]
    #         print(f"✅ New chat created: chatId={self.chat_id}")

    @task(3)
    def get_chat_messages(self):
        """Fetches messages from an existing chat."""
        # if not self.chat_id:
        #     print("⚠️ Skipping get_chat_messages: No chatId found!")
        #     return

        #self.chat_id = 36
        url = f"/api/v1/patient/messaging/chats/{self.chat_id}/messages?limit=10&offset=0"
        response = self.client.get(url, headers=self.headers)
        self.process_response(response)

    @task(3)
    def send_message(self):
        """Sends a message to an existing chat."""
        # if not self.chat_id:
        #     print("⚠️ Skipping send_message: No chatId found!")
        #     return

        #self.chat_id = 41
        url = f"/api/v1/patient/messaging/chats/{self.chat_id}/messages"
        payload = {"messageContent": "This is a test message from Locust!"}

        response = self.client.post(url, headers=self.headers, json=payload)
        self.process_response(response)

    def process_response(self, response):
        """Handles API responses and logs output."""
        print(f"🔗 Request URL: {response.request.url}")
        print(f"📡 Status: {response.status_code} | Time: {response.elapsed.total_seconds()} sec")

        if response.status_code == 401:
            print("❌ ERROR: Unauthorized (401). Check your access token!")
            return None
        elif response.status_code == 400:
            print(f"❌ ERROR: Bad Request (400) - {response.text}")
            return None

        try:
            data = response.json()
            print(f"✅ Response JSON: {json.dumps(data, indent=2)}")
            return data
        except ValueError:
            print(f"⚠️ Non-JSON Response: {response.text}")
            return None


class WebsiteUser(HttpUser):
    """Locust user configuration."""
    tasks = [PatientAPITasks]
    wait_time = between(1, 5)
    host = "https://1dc684udt4.execute-api.eu-central-1.amazonaws.com/dev/bfm"
