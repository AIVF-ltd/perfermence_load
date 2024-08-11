# import json
# from locust import HttpUser, TaskSet, task, between
#
# class APITestTasks(TaskSet):
#     def on_start(self):
#         self.headers = {
#             'Content-Type': 'application/json',
#             'dal-secret-key': 'SPECIAL_NEW_KEY!@#$-$',
#             'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjo2LCJ1dWlkIjoiYTVmZDIwYTAtNzk1Ny00M2VhLTljMjAtZGMwODkwOTg0ZmY3IiwiaWF0IjoxNzIzMDIzMTg3LCJleHAiOjE3MjMwMjM0ODd9.eNojtiLhh4G-c24mgjHjlJ5Aj5fSfCV4G9ToDsczpw4',
#             'accept': 'application/json, text/plain, */*',
#             'accept-encoding': 'gzip, deflate, br, zstd',
#             'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
#             'connection': 'keep-alive',
#             'cookie': '__Host-grv_app_session=71c404da2ef4dd0e4ebf63a3a13c7455c0e8a392c035d3133b6e449fd0036f61; __Host-grv_app_session_subject=f5755d7979d3835adc3928459962e16c1050b37558ac8c12c119095e69c0b3a4; refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjo2LCJ1dWlkIjoiYTZhNjc0YjAtNzE5NS00Y2E1LWFkN2MtMzVjODc2NWE4MWQ4IiwiaWF0IjoxNzIyOTMxNjAzLCJleHAiOjE3MjI5MzM0MDN9.32jJZKKXseP9zKBcceLcalQGKy930x39-XJhdZA5vEY; mp_eb9ace6da1976d69be62f16e645e1efe_mixpanel=%7B%22distinct_id%22%3A%20%22ruslang%2B11222%40aivf.co%22%2C%22%24device_id%22%3A%20%2219122b169ca19d684-0db93314fd0754-18525637-1fa400-19122b169ca19d684%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fema-qa4.aivf-mgt.aivf.co%2F%22%2C%22%24initial_referring_domain%22%3A%20%22ema-qa4.aivf-mgt.aivf.co%22%2C%22%24user_id%22%3A%20%22ruslang%2B11222%40aivf.co%22%2C%22__timers%22%3A%20%7B%22Patient%20Card%20Closed%22%3A%201722931588036%2C%22Page%20Exit%22%3A%201722931590192%7D%7D',
#             'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"macOS"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-origin',
#             'referer': 'https://ema-qa4.aivf-mgt.aivf.co/patients',
#             'if-none-match': 'W/"5878-GSyWOSJFtpveUGyGZNTT4PQSesI"'
#         }
#
#     @task(1)
#     def create_patient(self):
#         payload = json.dumps({
#             "id": "patient_id_123",
#             "name": "John Doe",
#             "birth_date": "1990-01-01T00:00:00Z"
#         })
#         self.client.post("/api/v1/internal/patient", data=payload, headers=self.headers)
#
#     @task(2)
#     def get_patient(self):
#         patient_id = 1
#         self.client.get(f"/api/v1/internal/patient/{patient_id}", headers=self.headers)
#
#     @task(3)
#     def get_patients(self):
#         self.client.get("/patients", headers=self.headers)
#
#     @task(4)
#     def get_internal_treatment(self):
#         treatment_id = 77
#         self.client.get(f"/api/v1/internal/treatment/{treatment_id}", headers=self.headers)
#
#     @task(5)
#     def create_algorithm_result(self):
#         payload = json.dumps({
#             "algorithm_version": "1.0",
#             "frame_number": 10,
#             "result": "positive",
#             "result_json": {},
#             "calculation_time": "2024-01-01T00:00:00Z",
#             "algorithm_pk": 1,
#             "embryo_pk": 1
#         })
#         self.client.post("/api/v1/internal/algorithm-result", data=payload, headers=self.headers)
#
#     @task(6)
#     def get_patients_with_params(self):
#         url = ("/api/v1/internal/patients?search=&sort=fertilization_time&sortByActive=false&"
#                "isMyPatients=false&dir=asc&currentPage=1&itemsPerPage=50&differenceInHours=0&filterByDay=-1")
#         self.client.get(url, headers=self.headers)
#
#     @task(7)
#     def create_embryo_frame(self):
#         payload = json.dumps({
#             "embryo_pk": 0,
#             "frame_number": 0,
#             "frame_time": "2024-08-04T14:11:31.716Z",
#             "is_in_h5": True
#         })
#         self.client.post("/api/v1/internal/embryo-frame", data=payload, headers=self.headers)
#
#     @task(8)
#     def get_ema_server_patients(self):
#         url = ("/api/v1/ema-server/patients?search=&sort=fertilization_time&sortByActive=false&"
#                "isMyPatients=false&dir=asc&currentPage=1&itemsPerPage=50&differenceInHours=0&filterByDay=-1")
#         self.client.get(url, headers=self.headers)
#
#     @task(9)
#     def get_ema_server_patients_active(self):
#         url = ("/api/v1/ema-server/patients?search=&sort=fertilization_time&sortByActive=true&"
#                "isMyPatients=false&dir=asc&currentPage=1&itemsPerPage=50&differenceInHours=0&filterByDay=-1")
#         self.client.get(url, headers=self.headers)
#
#     @task(10)
#     def get_ema_server_patients_with_active_false(self):
#         url = ("/api/v1/ema-server/patients?search=&sort=fertilization_time&sortByActive=false&"
#                "isMyPatients=false&dir=asc&currentPage=1&itemsPerPage=50&differenceInHours=0&filterByDay=-1")
#         self.client.get(url, headers=self.headers)
#
# class WebsiteUser(HttpUser):
#     tasks = [APITestTasks]
#     wait_time = between(1, 5)
#     host = "https://ema-qa4.aivf-mgt.aivf.co"
import json
from locust import HttpUser, TaskSet, task, between

class PatientAPITasks(TaskSet):
    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            'dal-secret-key': 'SPECIAL_NEW_KEY!@#$-$',
            'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjo2LCJ1dWlkIjoiNjBmM2NjMDktNGM4YS00MTk5LTlkYWEtZGU2N2IzZTY3YzY1IiwiaWF0IjoxNzIzMDM0NzgyLCJleHAiOjE3MjMwMzUwODJ9.tynhaGm24Do5H4LlzrFq5F12wacSEUriRwhcYJEHiNM',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'connection': 'keep-alive',
            'cookie': '__Host-grv_app_session=4883f1bf3902b685b1ec2becc684b78f95dbee87f31fcffacdf31beff5a76d65; __Host-grv_app_session_subject=0f0395cc0965d2816e5906cea59920db9c319dba6cd5de4f6769783856ac7fe1; refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjo2LCJ1dWlkIjoiMjdhOWRkNWUtMGM1Ni00YjE4LWE0NDMtODZjNDA0ZTU5M2IzIiwiaWF0IjoxNzIzMDMxNDAyLCJleHAiOjE3MjMwMzMyMDJ9.1CaFSxcx1xKlGs0tiBgtCg5_BrgWUxqT11Q4gmG3mYM; mp_eb9ace6da1976d69be62f16e645e1efe_mixpanel=%7B%22distinct_id%22%3A%20%22ruslang%2B11222%40aivf.co%22%2C%22%24device_id%22%3A%20%221912ca50d934adf-050efedf0e5f5e-18525637-1fa400-1912ca50d934adf%22%2C%22%24user_id%22%3A%20%22ruslang%2B11222%40aivf.co%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__timers%22%3A%20%7B%22Page%20Exit%22%3A%201723030911190%7D%7D',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'if-none-match': 'W/"5878-2Ag8uc3XP3XICDD5QSjqIl7hcu0"'
        }

    @task(1)
    def get_patients_with_sort_by_active_false(self):
        url = ("/api/v1/ema-server/patients?search=&sort=fertilization_time&sortByActive=false&"
               "isMyPatients=false&dir=asc&currentPage=1&itemsPerPage=50&differenceInHours=0&filterByDay=-1")
        response = self.client.get(url, headers=self.headers)
        self.process_response(response)

    @task(2)
    def get_patients_with_sort_by_active_true(self):
        url = ("/api/v1/ema-server/patients?search=&sort=fertilization_time&sortByActive=true&"
               "isMyPatients=false&dir=asc&currentPage=1&itemsPerPage=50&differenceInHours=0&filterByDay=-1")
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
    host = "https://ema-qa4.aivf-mgt.aivf.co"


