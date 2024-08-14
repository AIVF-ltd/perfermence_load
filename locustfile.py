from locust import HttpUser, TaskSet, task, between

class PatientAPITasks(TaskSet):
    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjo1LCJ1dWlkIjoiZjQyM2NhY2MtNTE0Ni00YTMyLWE1MGYtMjIyMTkxNDBkZTg2IiwiaWF0IjoxNzIzNjE2NTk1LCJleHAiOjE3MjM2MTY4OTV9.6JLjk0M6hBjgh-GqY0ArjpQR2E5mFWmn0HXTys7M9hQ',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'connection': 'keep-alive',
            'cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjo1LCJ1dWlkIjoiYmY2YjdlMTctZWNiNi00YWUzLTg0MzQtZDMyZGM4MmE5MWU5IiwiaWF0IjoxNzIzNTU1MjEyLCJleHAiOjE3MjM1NTcwMTJ9.6TX0NQgSA9tDoHtwIZxpAl2QZjlo2UpK2-IrOlJFCm4',
        }

    @task
    def get_patients(self):
        url = "/api/v1/ema-server/patients?search=&sort=fertilization_time&sortByActive=false&isMyPatients=false&dir=asc&currentPage=1&itemsPerPage=50&differenceInHours=0&filterByDay=-1"
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
    host = "http://qa4.aivflab.com"
