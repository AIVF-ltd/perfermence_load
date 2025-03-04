import json
from locust import HttpUser, TaskSet, task, between

class PatientAPITasks(TaskSet):
    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            # 'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVfd1lzTFFYT1VkaDBKSldWOTZaRiJ9.eyJhaXZmL3JvbGVzIjpbIkxhYiBEaXJlY3RvciJdLCJmdWxsTmFtZSI6IlJ1c2xhbiBnIiwib3JnYW5pemF0aW9uIjp7ImRpc3BsYXlfbmFtZSI6IkFJVkYiLCJpZCI6Im9yZ19FaTdndmo5Z2V2OWlMZWtvIiwibWV0YWRhdGEiOnsiYmlsbGluZ19sYXVuY2hfZGF0ZSI6IjIwMjMuMTAuMDEiLCJ0ZW5hbnRfaWQiOiIxMDAiLCJ0aW1lem9uZSI6IkFzaWEvSmVydXNhbGVtIn0sIm5hbWUiOiJhaXZmLWRldiJ9LCJpc3MiOiJodHRwczovL2F1dGguc3RhdGljLmFpdmYtZGV2LmF1dG9tYXQtaXQuaW8vIiwic3ViIjoiYXV0aDB8NjU5YTlkYjQwMWUzZjZjNzZlMjJiOTk2IiwiYXVkIjpbImFpdmYiLCJodHRwczovL2Rldi10aTV2anZwbTF2ZHQ4OHlrLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MjY2NTY0MzMsImV4cCI6MTcyNjc0MjgzMywic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsIm9yZ19pZCI6Im9yZ19FaTdndmo5Z2V2OWlMZWtvIiwib3JnX25hbWUiOiJhaXZmLWRldiIsImF6cCI6IjBSWHlPWFJPTVE3NHVjTEF4bGZrc1YyQ1hsb3pHUTlGIiwicGVybWlzc2lvbnMiOlsidXNlcnM6aW52aXRlIiwidXNlcnM6cmVhZCIsInVzZXJzOnVwZGF0ZSJdfQ.fbC2ejtCNi-t9WFeU6wZDCtP9jWzdtFLEgcmhG3KB-AELsTLlSSokmfoTd2u5NpG1L-yVxZkcMyPbWu4xVJFKz1O1l77Aa82lZzj4Vr6oY32Hho8wYOGeaBES5-qPmUAWHlf4IaOcU8NSqnjFFxq5t6tL0Lqp4wzn-gLtu75x87MRhAkEGP3fIRd4a9ftDcvxtUhHuW2PpW3dhT3IRf-YKi1VWInHL7E75nrsIpOOVhpp5JmtEcExI0O-mkwjjt5yCaWB9xPfoX1TokX6i05v_cLxKBvKW4e3yJooGAaKcp3K6sDdS4Tuq0dwNLRui875Fo8BO1K9g6Pjgyx1yroJA',
            # 'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVfd1lzTFFYT1VkaDBKSldWOTZaRiJ9.eyJhaXZmL3JvbGVzIjpbIkxhYiBEaXJlY3RvciJdLCJmdWxsTmFtZSI6IlJ1c2xhbiBnIiwib3JnYW5pemF0aW9uIjp7ImRpc3BsYXlfbmFtZSI6IkFJVkYiLCJpZCI6Im9yZ19FaTdndmo5Z2V2OWlMZWtvIiwibWV0YWRhdGEiOnsiYmlsbGluZ19sYXVuY2hfZGF0ZSI6IjIwMjMuMTAuMDEiLCJ0ZW5hbnRfaWQiOiIxMDAiLCJ0aW1lem9uZSI6IkFzaWEvSmVydXNhbGVtIn0sIm5hbWUiOiJhaXZmLWRldiJ9LCJpc3MiOiJodHRwczovL2F1dGguc3RhdGljLmFpdmYtZGV2LmF1dG9tYXQtaXQuaW8vIiwic3ViIjoiYXV0aDB8NjU5YTlkYjQwMWUzZjZjNzZlMjJiOTk2IiwiYXVkIjpbImFpdmYiLCJodHRwczovL2Rldi10aTV2anZwbTF2ZHQ4OHlrLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MzE4MzQzMjMsImV4cCI6MTczMTkyMDcyMywic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsIm9yZ19pZCI6Im9yZ19FaTdndmo5Z2V2OWlMZWtvIiwib3JnX25hbWUiOiJhaXZmLWRldiIsImF6cCI6IjBSWHlPWFJPTVE3NHVjTEF4bGZrc1YyQ1hsb3pHUTlGIiwicGVybWlzc2lvbnMiOlsidXNlcnM6aW52aXRlIiwidXNlcnM6cmVhZCIsInVzZXJzOnVwZGF0ZSJdfQ.XQd04evCRMyhoM8-KHiDbdOUT9T-IOvlD4XPJuV7TYUo0aHJ7qnSEi7fIbwt06AW1C3IsqYTr_zQH0LfkckuQWs3vm9p2-0uGhjayWurAffScxXYoPt2JT-Igx6lL--=',
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVfd1lzTFFYT1VkaDBKSldWOTZaRiJ9.eyJhaXZmL3JvbGVzIjpbIkxhYiBEaXJlY3RvciJdLCJmdWxsTmFtZSI6IlJ1c2xhbiBnIiwib3JnYW5pemF0aW9uIjp7ImRpc3BsYXlfbmFtZSI6InFhLWNsaW5pYy0xIiwiaWQiOiJvcmdfeWdqcWhxVm9JZFRhd1UySSIsIm1ldGFkYXRhIjp7InRlbmFudF9pZCI6IjIwMCIsInRpbWV6b25lIjoiQXNpYS9KZXJ1c2FsZW0ifSwibmFtZSI6ImFpdmYtcWEtY2xpbmljLTEifSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnN0YXRpYy5haXZmLWRldi5hdXRvbWF0LWl0LmlvLyIsInN1YiI6ImF1dGgwfDY1OWE5ZGI0MDFlM2Y2Yzc2ZTIyYjk5NiIsImF1ZCI6WyJhaXZmIiwiaHR0cHM6Ly9kZXYtdGk1dmp2cG0xdmR0ODh5ay5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzM4NzU2MTgxLCJleHAiOjE3Mzg4NDI1ODEsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJvcmdfaWQiOiJvcmdfeWdqcWhxVm9JZFRhd1UySSIsIm9yZ19uYW1lIjoiYWl2Zi1xYS1jbGluaWMtMSIsImF6cCI6Im5UV1pZbTREbnpONkY0elM0UVM4NlgwaHZYQzJoWWZnIiwicGVybWlzc2lvbnMiOlsidXNlcnM6aW52aXRlIiwidXNlcnM6cmVhZCIsInVzZXJzOnVwZGF0ZSJdfQ.IJ7CWe-PfRRNItXAT3VcyeUFuUbgNPXdPRcY1HtieRAlj6_NZfxUESN_uOLCVQV0_eD-6dkIKuqU8AtM1ivk9DvHs8YxHfD2Iqm4knBhsunOGGmW9ioez7gTTfphu2W-UrKEcoPSyzmM2Bzf47elKLCwwsvcBOZ67Q8R4anMl9jEtFMIIal9xBY8jObhHGTShVRqhmeaQ38iAHfuFh7mRujrUn_5XHN4p_Enu0BGD0i-GhkUE6_wr2mQq4g9YXYt_B1kFtfJnaRLtn2x2el6Pn37LSC42jFxuMQGa9mibnRmIvBpSARn00M0kX4yor0xAVGo22h2V6gSFTM-4895hQ',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'connection': 'keep-alive',
        }

    @task
    def get_patients(self):
        # url = "/api/v1/ema-server/patients?treatment_status=active&page=1&limit=30&sort=day&order=asc"
        url = "/api/v1/ema-server/notifications?type=received"
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
