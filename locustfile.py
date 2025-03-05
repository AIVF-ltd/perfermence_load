import json
import random
from locust import HttpUser, TaskSet, task, between


class PatientAPITasks(TaskSet):
    def on_start(self):
        """Executed when a user starts a test session."""
        self.access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inh2TTRPUzNhalRJNXFteVEtVGQzZCJ9.eyJwYXRpZW50X3VzZXJfcGsiOjYsImlzcyI6Imh0dHBzOi8vZW1hLWRldmVsb3BtZW50LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzBmNjJmM2I5MzhjMDBhMzgyNjYyYTQiLCJhdWQiOlsiaHR0cHM6Ly9saXJhbi10ZXN0ZXIuY29tIiwiaHR0cHM6Ly9lbWEtZGV2ZWxvcG1lbnQuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTc0MTA4NTgxNSwiZXhwIjoxNzQxMTcyMjE1LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwib3JnX2lkIjoib3JnX3hDNHlKYmdoQ1RKSkZIY2YiLCJvcmdfbmFtZSI6ImFpdmYiLCJhenAiOiJ4SEVpb29PWWF4b0RNbjRMRFVHekhQdFBiVldQOTRWcyJ9.gKAmkaUVgoC39bK8zC_Sq5TK7eX7xKbdA1FNPDmFkKgATbfAGQNiwZpIABxClLZ-m-lIj6Iw7D1MmgX7gyUcI33vx3pDcewxU2rna72SrdBYOsg1Ggx79IXJz-N2htX2rptHZTTOb9-eixD9nQk45oEPWJnvILXCLie1_lJoa4aUYavKB174EBwO1pl5bTKmyV5FmpMN12b30FtF9nxn_fPjibPRAsYMNk_2RiM-0DkT_B8WnOLprbCRZhHG7FOaeVfsJO4J2zTXm7gOVU7oIObL1k893EJCSPHXi4ZnTkS50f4eXnPz7Lw4McsdicO1pZAQsq_sZ0b0gJhfMtwWSw"  # Replace with a valid token
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

    @task(1)
    def create_chat(self):
        """Creates a new chat with a random topic."""
        url = "/api/v1/patient/messaging/chats"
        topic_id = random.randint(0, 4)  # Select a random topic

        payload = {
            "tenantId": self.tenant_id,  # Tenant ID is now included
            "topicId": topic_id,
            "initialMessage": {"messageContent": "Hello, this is a test message."}
        }

        response = self.client.post(url, headers=self.headers, json=payload)
        data = self.process_response(response)

        if data and "chatId" in data:
            self.chat_id = data["chatId"]
            print(f"✅ New chat created: chatId={self.chat_id}")

    @task(3)
    def get_chat_messages(self):
        """Fetches messages from an existing chat."""
        if not self.chat_id:
            print("⚠️ Skipping get_chat_messages: No chatId found!")
            return

        url = f"/api/v1/patient/messaging/chats/{self.chat_id}/messages?limit=10&offset=0"
        response = self.client.get(url, headers=self.headers)
        self.process_response(response)

    # @task(3)
    # def send_message(self):
    #     """Sends a message to an existing chat."""
    #     if not self.chat_id:
    #         print("⚠️ Skipping send_message: No chatId found!")
    #         return
    #
    #     url = f"/api/v1/patient/messaging/chats/{self.chat_id}/messages"
    #     payload = {"messageContent": "This is a test message from Locust!"}
    #
    #     response = self.client.post(url, headers=self.headers, json=payload)
    #     self.process_response(response)

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
