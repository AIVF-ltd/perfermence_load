import json
from locust import HttpUser, TaskSet, task, between

class PatientAPITasks(TaskSet):
    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            # 'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVfd1lzTFFYT1VkaDBKSldWOTZaRiJ9.eyJhaXZmL3JvbGVzIjpbIkxhYiBEaXJlY3RvciJdLCJvcmdhbml6YXRpb24iOnsiZGlzcGxheV9uYW1lIjoicWEtY2xpbmljLTEiLCJpZCI6Im9yZ195Z2pxaHFWb0lkVGF3VTJJIiwibWV0YWRhdGEiOnsibWZhX3R5cGUiOiJtZmEiLCJ0ZW5hbnRfaWQiOiIyMDAifSwibmFtZSI6ImFpdmYtcWEtY2xpbmljLTEifSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnN0YXRpYy5haXZmLWRldi5hdXRvbWF0LWl0LmlvLyIsInN1YiI6ImF1dGgwfDY1OWE5ZGI0MDFlM2Y2Yzc2ZTIyYjk5NiIsImF1ZCI6WyJhaXZmIiwiaHR0cHM6Ly9kZXYtdGk1dmp2cG0xdmR0ODh5ay5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzIzMzYxNTk0LCJleHAiOjE3MjM0NDc5OTQsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJvcmdfaWQiOiJvcmdfeWdqcWhxVm9JZFRhd1UySSIsIm9yZ19uYW1lIjoiYWl2Zi1xYS1jbGluaWMtMSIsImF6cCI6Im5UV1pZbTREbnpONkY0elM0UVM4NlgwaHZYQzJoWWZnIiwicGVybWlzc2lvbnMiOlsidXNlcnM6aW52aXRlIiwidXNlcnM6cmVhZCIsInVzZXJzOnVwZGF0ZSJdfQ.WvSsxeJi6YNlQV0traRHYkKvqFcHwOa-cnAhCrQuh2VisqWIe0JAdlUs-Mn2DZuVPe5lQ3lpCanhKuH7pqtAye3_B2kNrkl9jb6Whz-qvB6u3tJc86fm-Yh9yS-qPsW1t42TGWzFM47Qf_H-cOr1P50Ke-lOyE2u9S3sxq8FoIaWWzhjA87dLs3TZNlnEHrmSKRMuEd9YZrl43YmK7nV1Xo9PP-e7fGBwGTfCTQqxXox9pbbHlkX0LK7NXL9jOc2-cTGov9XTM47JZOgZGhN4m2ei5G6FgGorVjmcYdW0380lgZTZIkMN-as_HoMR5SvT1W58CD6TMwBuo4sMwW7kQ',
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVfd1lzTFFYT1VkaDBKSldWOTZaRiJ9.eyJhaXZmL3JvbGVzIjpbIkxhYiBEaXJlY3RvciJdLCJvcmdhbml6YXRpb24iOnsiZGlzcGxheV9uYW1lIjoicWEtY2xpbmljLTEiLCJpZCI6Im9yZ195Z2pxaHFWb0lkVGF3VTJJIiwibWV0YWRhdGEiOnsibWZhX3R5cGUiOiJtZmEiLCJ0ZW5hbnRfaWQiOiIyMDAifSwibmFtZSI6ImFpdmYtcWEtY2xpbmljLTEifSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnN0YXRpYy5haXZmLWRldi5hdXRvbWF0LWl0LmlvLyIsInN1YiI6ImF1dGgwfDY1OWE5ZGI0MDFlM2Y2Yzc2ZTIyYjk5NiIsImF1ZCI6WyJhaXZmIiwiaHR0cHM6Ly9kZXYtdGk1dmp2cG0xdmR0ODh5ay5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzIzMzYxNTk0LCJleHAiOjE3MjM0NDc5OTQsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJvcmdfaWQiOiJvcmdfeWdqcWhxVm9JZFRhd1UySSIsIm9yZ19uYW1lIjoiYWl2Zi1xYS1jbGluaWMtMSIsImF6cCI6Im5UV1pZbTREbnpONkY0elM0UVM4NlgwaHZYQzJoWWZnIiwicGVybWlzc2lvbnMiOlsidXNlcnM6aW52aXRlIiwidXNlcnM6cmVhZCIsInVzZXJzOnVwZGF0ZSJdfQ.WvSsxeJi6YNlQV0traRHYkKvqFcHwOa-cnAhCrQuh2VisqWIe0JAdlUs-Mn2DZuVPe5lQ3lpCanhKuH7pqtAye3_B2kNrkl9jb6Whz-qvB6u3tJc86fm-Yh9yS-qPsW1t42TGWzFM47Qf_H-cOr1P50Ke-lOyE2u9S3sxq8FoIaWWzhjA87dLs3TZNlnEHrmSKRMuEd9YZrl43YmK7nV1Xo9PP-e7fGBwGTfCTQqxXox9pbbHlkX0LK7NXL9jOc2-cTGov9XTM47JZOgZGhN4m2ei5G6FgGorVjmcYdW0380lgZTZIkMN-as_HoMR5SvT1W58CD6TMwBuo4sMwW7kQ',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'connection': 'keep-alive',
            'cookie': '_legacy_auth0.nTWZYm4DnzN6F4zS4QS86X0hvXC2hYfg.is.authenticated=true; auth0.nTWZYm4DnzN6F4zS4QS86X0hvXC2hYfg.is.authenticated=true',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

    @task(1)
    def get_patients(self):
        url = "/api/v1/ema-server/patients?page=1&limit=30&order=desc&sort=day&treatment_status=active"
        # url = "/api/v1/ema-server/patients?page=1&limit=30&order=desc&sort=day"
        response = self.client.get(url, headers=self.headers)
        self.process_response(response)

    def process_response(self, response):
        print("Request URL:", response.request.url)
        print("Request Headers:", response.request.headers)
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
    host = "https://static.aivf-qa.aivflab.com"
