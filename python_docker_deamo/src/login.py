from locust import HttpLocust, TaskSet, task
import urllib

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        headers = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        paramMap = {
            'paramMap.uname': '15361858980',
            'paramMap.pwd': 'ZWL119998',
            'paramMap.pageId': 'login',
            'paramMap.stat': '1',
            'paramMap.isCode': 'none',
            'paramMap.RandCode': ''
        }
        response = self.client.post(
            "/RZTPC/wecLogin.do",
            data = urllib.urlencode(paramMap),
            headers = headers,
            catch_response = True
        )

    @task(2)
    def index(self):
        response = self.client.get("/RZTPC/index.do")

        print("index: ", response.status_code)
        # print("index: ", response.content)

    @task(2)
    def investlist(self):
        response = self.client.get("/RZTPC/investlist.do")

        print("investlist: ", response.status_code)
        # print("investlist: ", response.content)

    @task(2)
    def userInfo(self):
        response = self.client.get("/RZTPC/userInfo.do")

        print("userInfo: ", response.status_code)
        # print("userInfo: ", response.content)

    @task(2)
    def buyRecord(self):
        response = self.client.get("/RZTPC/buyRecord.do")

        print("buyRecord: ", response.status_code)
        # print("buyRecord: ", response.content)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000
