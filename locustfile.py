import json
from locust import HttpUser, TaskSet, task, between

class PatientAPITasks(TaskSet):
    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVfd1lzTFFYT1VkaDBKSldWOTZaRiJ9.eyJhaXZmL3JvbGVzIjpbIkxhYiBEaXJlY3RvciJdLCJvcmdhbml6YXRpb24iOnsiZGlzcGxheV9uYW1lIjoiQUlWRiIsImlkIjoib3JnX0VpN2d2ajlnZXY5aUxla28iLCJtZXRhZGF0YSI6eyJiaWxsaW5nX2xhdW5jaF9kYXRlIjoiMjAyMy4xMC4wMSIsInRlbmFudF9pZCI6IjEwMCIsInRpbWV6b25lIjoiQXNpYS9KZXJ1c2FsZW0ifSwibmFtZSI6ImFpdmYtZGV2In0sImlzcyI6Imh0dHBzOi8vYXV0aC5zdGF0aWMuYWl2Zi1kZXYuYXV0b21hdC1pdC5pby8iLCJzdWIiOiJhdXRoMHw2NTlhOWRiNDAxZTNmNmM3NmUyMmI5OTYiLCJhdWQiOlsiYWl2ZiIsImh0dHBzOi8vZGV2LXRpNXZqdnBtMXZkdDg4eWsuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcyMzM1MzIxOCwiZXhwIjoxNzIzNDM5NjE4LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwib3JnX2lkIjoib3JnX0VpN2d2ajlnZXY5aUxla28iLCJvcmdfbmFtZSI6ImFpdmYtZGV2IiwiYXpwIjoiMFJYeU9YUk9NUTc0dWNMQXhsZmtzVjJDWGxvekdROUYiLCJwZXJtaXNzaW9ucyI6WyJ1c2VyczppbnZpdGUiLCJ1c2VyczpyZWFkIiwidXNlcnM6dXBkYXRlIl19.bWLe4LuZOAgH_A62w09ILbzoIfkblzLJBbQHGT1COCEgVHcvmnfLuUSf4skkyQ5lb5eKAerShVqqkmv15y0jS13sM_LC_SnYlS8Azcqp1xaeK5VSTLcrnboy0Hp00Xbu80OtEldyoRN6SCNxLAF5JSHQHZCa9eqUvc-2ML1xpcbFNYUHQLfqL-HwVLZ4TR8d4Vc-73HeAYPCCMvHfED-nSaMHBSYT7ULEQejDZQFswj0WFjdHZwuzBYO6Fiun5bqYbit2my8vgHMGYdy1q3yhDXOTQMuxf5kfMar2oExUJ_-9pAd5ibGlNpSUbShhnGc16g3xkbSyAhippLBLs_xIQ',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'connection': 'keep-alive',
        }

    @task
    def get_patients(self):
        url = "/api/v1/ema-server/patients?page=1&limit=30&order=asc&sort=day&treatment_status=active"
        response = self.client.get(url, headers=self.headers)
        self.process_response(response)

    def process_response(self, response):
        print("Request URL:", response.request.url)
        print("Response Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        try:
            data = response.json()
            print("Response JSON Data:", data)
        except ValueError:
            print("Response Text:", response.text)

class WebsiteUser(HttpUser):
    tasks = [PatientAPITasks]
    wait_time = between(1, 5)
    host = "https://static.aivf-dev.automat-it.io"
