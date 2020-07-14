import os
from locust import HttpUser, task, between, TaskSet, tag
#from app.config import env
#from app.config.constants import EnvKey

#APIM test token
APIM_TEST_TOKEN = "8b0c1f73-0f38-4edf-a848-c7bc222a44d2"

X_APIM_SESSION_TOKEN = "b58005ee-00eb-43e8-9f58-55b7a978979a"

OCP_APIM_SUBSCRIPTION_KEY = "65fab861-baad-11ea-ae24-6d12723d9004"


def auth_header():
    return {"ocp-apim-session-token": APIM_TEST_TOKEN}

def auth_header_2():
    return {"x-apim-session-token": X_APIM_SESSION_TOKEN}

def auth_header_3():
    return {"ocp-apim-subscription-key":  OCP_APIM_SUBSCRIPTION_KEY}

class WebsiteUser(HttpUser):
    wait_time = between(1,2)
    
    @tag('tag1')
    @task(1)
    def readmission0(self):
        r=self.client.request(method="GET", url='//api/default_period?hospital=JBN', headers=auth_header())
        assert r.status_code == 200

    @tag('tag1')
    @task(1)
    def readmission1(self):
        r=self.client.request(method="GET", url='/api/hospital_readmission_rate?hospital=JBN&frequency=Monthly&unplanned=true&govdata=true&fromDate=2018-11-01&toDate=2019-10-31', headers=auth_header())
        assert r.status_code == 200

    @tag('tag1')
    @task(1)
    def readmission2(self):
        r=self.client.request(method="GET", url='/api/hospital_percent_readmit_diagnosis?hospital=JBN&frequency=Monthly&unplanned=true&fromDate=2018-11-01&toDate=2019-10-31', headers=auth_header())
        assert r.status_code == 200

    @tag('tag1')
    @task(1) 
    def readmission3(self):
        r=self.client.request(method="GET", url='/api/percent_sections?hospital=JBN&frequency=Monthly&unplanned=true&fromDate=2018-11-01&toDate=2019-10-31', headers=auth_header())
        assert r.status_code == 200

    @tag('tag2')
    @task(1)
    def readmission8(self):
        r=self.client.request(method="GET", url='https://aics-medical-bi-stage.azurewebsites.net/api/v1/dashboard/pbi', headers=auth_header_2(), name="https://aics-medical-bi-stage.azurewebsites.net/api/v1/dashboard/pbi")
        assert r.status_code == 200

    @tag('tag2')
    @task(1)
    def readmission9(self):
        r=self.client.request(method="GET", url='https://aics-medical-bi-stage.azurewebsites.net/api/v1/dashboard/pbi/e7a4e83c-a8be-44e8-991e-66b910186759', headers=auth_header_2(), name="https://aics-medical-bi-stage.azurewebsites.net/api/v1/dashboard/pbi/e7a4e83c-a8be-44e8-991e-66b910186759")
        assert r.status_code == 200
    

    @tag('tag3')
    @task(1)
    def SequentialTest(self):

        # verify/face/add
        image_path = os.path.join("", "1.jpg")
        files = {
            'imageDatas' : open(image_path, "rb")
        }
        data = {
            'dbName' : "azure_stage",
            'enableQualityFilter' : True
        }
        r = self.client.post(url='https://fr-jbo-stage.southeastasia.cloudapp.azure.com/verify/face/add', \
        headers={'ocp-apim-subscription-key': '65fab861-baad-11ea-ae24-6d12723d9004'}, \
        files=files,
        data=data
        )
        
        content = r.json()
        imageId = content['success'][0]['imageId']

        # verify/face/gets
        GET_URL = 'https://fr-jbo-stage.southeastasia.cloudapp.azure.com/verify/face/gets?imageId=' + imageId
        r = self.client.request(method="GET", url=GET_URL, headers={"ocp-apim-subscription-key": "65fab861-baad-11ea-ae24-6d12723d9004", "accept":"application/json"} , name="verify/face/gets")
        
        # verify/face/deletes
        DELETE_URL = 'https://fr-jbo-stage.southeastasia.cloudapp.azure.com/verify/face/deletes?dbName=azuer_stage&imageId=' + imageId
        r = self.client.request(method="DELETE", url=DELETE_URL, headers={"ocp-apim-subscription-key": "65fab861-baad-11ea-ae24-6d12723d9004", "accept":"application/json"}, name="verify/face/deletes")
        
        # verify/face/match

        image_path = os.path.join("", "1.jpg")
        image_file = {
            'imageDatas' : open(image_path, "rb")
        }

        params = {
            'dbName' : "azure_stage",
        }

        r = self.client.post(url='https://fr-jbo-stage.southeastasia.cloudapp.azure.com/verify/face/match', \
        headers={'ocp-apim-subscription-key': '65fab861-baad-11ea-ae24-6d12723d9004'}, \
        files=image_file,
        data=params
        )


    @tag('tag4')
    @task(1)
    def readmission10(self):
        r=self.client.request(method="GET", url="https://fr-jbo-stage.southeastasia.cloudapp.azure.com/hello", headers=auth_header_3(), name="hello")
        assert r.status_code == 200  
    @tag('tag4')
    @task(1)
    def readmission11(self):
        r=self.client.request(method="GET", url="https://fr-jbo-stage.southeastasia.cloudapp.azure.com/verify/target/gets", headers=auth_header_3(), name="verify/target/gets")
        assert r.status_code == 200
        
    @tag('tag4')
    @task(1)
    def readmission12(self):
        r=self.client.request(method="GET", url="https://fr-jbo-stage.southeastasia.cloudapp.azure.com/verify/target/query?dbName=azure_stage", headers=auth_header_3(), name=" verify/target/query")
        assert r.status_code == 200  
