import json
from locust import HttpUser, TaskSet, task, between

class PatientAPITasks(TaskSet):
    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVfd1lzTFFYT1VkaDBKSldWOTZaRiJ9.eyJhaXZmL3JvbGVzIjpbIkxhYiBEaXJlY3RvciJdLCJvcmdhbml6YXRpb24iOnsiZGlzcGxheV9uYW1lIjoiQUlWRiIsImlkIjoib3JnX0VpN2d2ajlnZXY5aUxla28iLCJtZXRhZGF0YSI6eyJiaWxsaW5nX2xhdW5jaF9kYXRlIjoiMjAyMy4xMC4wMSIsInRlbmFudF9pZCI6IjEwMCIsInRpbWV6b25lIjoiQXNpYS9KZXJ1c2FsZW0ifSwibmFtZSI6ImFpdmYtZGV2In0sImlzcyI6Imh0dHBzOi8vYXV0aC5zdGF0aWMuYWl2Zi1kZXYuYXV0b21hdC1pdC5pby8iLCJzdWIiOiJhdXRoMHw2NTlhOWRiNDAxZTNmNmM3NmUyMmI5OTYiLCJhdWQiOlsiYWl2ZiIsImh0dHBzOi8vZGV2LXRpNXZqdnBtMXZkdDg4eWsuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcyMzQ1OTMyMCwiZXhwIjoxNzIzNTQ1NzIwLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwib3JnX2lkIjoib3JnX0VpN2d2ajlnZXY5aUxla28iLCJvcmdfbmFtZSI6ImFpdmYtZGV2IiwiYXpwIjoiMFJYeU9YUk9NUTc0dWNMQXhsZmtzVjJDWGxvekdROUYiLCJwZXJtaXNzaW9ucyI6WyJ1c2VyczppbnZpdGUiLCJ1c2VyczpyZWFkIiwidXNlcnM6dXBkYXRlIl19.Ct9adAp-3X8a18zLb6KyRaRGqdSSL_EnvkFd-8Oecf66-JwD63HeefM-dh2ePMVS4PaCo3sD5TYllsBv0jNqE_dvvjdHBYYLCpHDF0D5B-WPE-QHyQbaiEkdblqNHsVNUj09Jhzx7oUGouPQuNIiPEI0DRBigwKN-AykOo1W5gU5svN2x55ShDH4te8hZU9n1RevH-LQuSFQ50-714h_A7xf2dB7Z3znjXJgySMPRaUtatJgOQt95mWA9rvAQ1iawl41asng-xslxJWGmF69ynoS6acSziZxdrw6LWb0pu3SaeE1MG6qU314MxUmDKp7jthuHiGEYWGwSRQR4L8wBQ',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'connection': 'keep-alive',
        }

    @task
    def get_patients(self):
        url = "/api/v1/ema-server/patients?treatment_status=active&page=1&limit=30&sort=day&order=asc"
        #/api/v1/ema-server/patients?treatment_status=active&page=1&limit=30&sort=day&order=asc

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
