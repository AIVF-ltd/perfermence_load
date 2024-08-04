import json
from locust import HttpUser, TaskSet, task, between


class APITestTasks(TaskSet):
    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            'dal-secret-key': 'SPECIAL_NEW_KEY!@#$-$',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjo2LCJ1dWlkIjoiOGE5NjRkMGUtY2Q0Ni00MTUzLWE2NDctOWE4MjJmMWMzZDNlIiwiaWF0IjoxNzIyNzc4NDA1LCJleHAiOjE3MjI3Nzg3MDV9.efT8PslG3u2hIPBolLT1OayhsX-hlSpR9XIBIeDJIEk',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'intercom-device-id-yjkgtowf=dec9a556-8db8-470c-a9b2-8e0e8c5fd861; intercom-id-yjkgtowf=9b1aa03a-2a8d-456d-ba1b-c0865ed30215; mp_8e71136e828f915aad0af566dc31eb92_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A190350666d8dcac6-07969d6d800066-1c525637-1fa400-190350666d8dcac6%22%2C%22%24device_id%22%3A%20%22190350666d8dcac6-07969d6d800066-1c525637-1fa400-190350666d8dcac6%22%7D; __Host-grv_app_session=682352c37f61fc57f93b536d9ff55b1a27454f6f62331d338d24a1f157381ca2; __Host-grv_app_session_subject=59edd17b82f62aa52667cbffe27a06e2ebacdacfc7084e4e54644c3b4e4ec562; refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjo2LCJ1dWlkIjoiYzUyZmVmMjctZWU1Zi00OGNiLWIzNTktMWVjZGM1N2FkMWIzIiwiaWF0IjoxNzIyNzc4NDA1LCJleHAiOjE3MjI3ODAyMDV9.jaKLnjVRwEwInj_XkQwAGoQeQ8iDwh6TIp4UEPWg40E; mp_eb9ace6da1976d69be62f16e645e1efe_mixpanel=%7B%22distinct_id%22%3A%20%22ruslang%2B11222%40aivf.co%22%2C%22%24device_id%22%3A%20%221911d5a71f616eb66-00049ed4fe2238-1c525637-1fa400-1911d5a71f616eb66%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%22ruslang%2B11222%40aivf.co%22%2C%22__timers%22%3A%20%7B%22Page%20Exit%22%3A%201722778405313%7D%7D',
            'Host': 'ema-qa4.aivf-mgt.aivf.co',
            'Referer': 'https://ema-qa4.aivf-mgt.aivf.co/patients',
            'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }


    @task(1)
    def create_patient(self):
        payload = json.dumps({
            "id": "patient_id_123",
            "name": "John Doe",
            "birth_date": "1990-01-01T00:00:00Z"
        })
        self.client.post("/api/v1/internal/patient", data=payload, headers=self.headers)

    @task(2)
    def get_patient(self):
        patient_id = 1
        self.client.get(f"/api/v1/internal/patient/{patient_id}", headers=self.headers)

    @task(3)
    def get_patients(self):
        self.client.get("/patients", headers=self.headers)

    # @task(4)
    # def get_treatment(self):
    #     treatment_id = 77
    #     self.client.get(f"/api/v1/ema-server/treatments/{treatment_id}", headers=self.headers)

    @task(5)
    def get_internal_treatment(self):
        treatment_id = 77
        self.client.get(f"/api/v1/internal/treatment/{treatment_id}", headers=self.headers)

    @task(6)
    def create_algorithm_result(self):
        payload = json.dumps({
            "algorithm_version": "1.0",
            "frame_number": 10,
            "result": "positive",
            "result_json": {},
            "calculation_time": "2024-01-01T00:00:00Z",
            "algorithm_pk": 1,
            "embryo_pk": 1
        })
        self.client.post("/api/v1/internal/algorithm-result", data=payload, headers=self.headers)

    @task(7)
    def get_patients_with_params(self):
        url = ("/api/v1/internal/patients?search=&sort=fertilization_time&sortByActive=false&"
               "isMyPatients=false&dir=asc&currentPage=1&itemsPerPage=50&differenceInHours=0&filterByDay=-1")
        self.client.get(url, headers=self.headers)

    @task(8)
    def create_embryo_frame(self):
        payload = json.dumps({
            "embryo_pk": 0,
            "frame_number": 0,
            "frame_time": "2024-08-04T14:11:31.716Z",
            "is_in_h5": True
        })
        self.client.post("/api/v1/internal/embryo-frame", data=payload, headers=self.headers)


class WebsiteUser(HttpUser):
    tasks = [APITestTasks]
    wait_time = between(1, 5)
    host = "https://ema-qa4.aivf-mgt.aivf.co"
