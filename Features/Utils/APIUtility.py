import requests
import json
import urllib.parse


class APIUtility:
    data = json.load(open("config.json"))
    Api_URL = data['ApiURL']
    Auth_URL = data['AuthURL']
    User = data['user1']
    Password = data['password1']

    # authanticate & get access token
    def Authenticate(self):
        response = requests.get(self.Auth_URL + "/v1/account/validate/" + self.User + "/" + self.Password)
        if response.ok:
            result = response.json()
        else:
            result = "Authentication Failed"
        return result

    # Check project name exists or not

    def CheckkProjectNameExist(self, ProjectName):
        result = self.Authenticate()
        access_token = result['accessToken']
        # print(access_token)

        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token,
            "Param": "Slc02"
        }
        url = "https://stage-slc-api.bsdspeclink.com/api/projects/CheckProjectNameExist"

        payload = {
            "name": ProjectName,
            "customerId": result['customerId']
        }

        response = requests.post(url, json=payload, headers=header)
        return bool(response.text)

    # GetProjectIDbyName(string projectName)

    def GetProjectIDbyName(self, ProjectName):
        result = self.Authenticate()
        access_token = result['accessToken']

        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token,
            "Param": "Slc02"
        }

        searchdata = {
            "colName": "CreateDate",
            "isDesc": True,
            "participantEmailID": "ALL",
            "customerId": result['customerId'],
            "searchField": ProjectName,
            "userID": result['userId'],
            "page": 1,
            "pageSize": 1000,
            "disciplineId": "",
            "catalogueType": ""
        }
        url = self.Api_URL + "/projects/GetSearchedProjects?PageSize=1000&page=1&IsOfficeMasterTab=false"
        response = requests.post(url, headers=header, json=searchdata)
        print(response.status_code)
        response_data = response.json()
        if (response_data['projectsDtoList']) == []:
            return "Project " + ProjectName + " does not exists"
        else:
            return (response_data['projectsDtoList'][0])['id']

    # GetOfficeMasterProjectIDbyName(string projectName)

    def GetOfficeMasterProjectIDbyName(self, ProjectName):
        result = self.Authenticate()
        access_token = result['accessToken']

        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token,
            "Param": "Slc02"
        }
        searchdata = {
            "colName": "CreateDate",
            "isDesc": True,
            "participantEmailID": "ALL",
            "customerId": result['customerId'],
            "searchField": ProjectName,
            "userID": result['userId'],
            "page": 1,
            "pageSize": 1000,
            "disciplineId": "",
            "catalogueType": ""
        }

        url = self.Api_URL + "/projects/GetSearchedProjects?PageSize=1000&page=1&IsOfficeMasterTab=true"

        response = requests.post(url, headers=header, json=searchdata)
        response_data = response.json()
        if (response_data['projectsDtoList']) == []:
            return "Project " + ProjectName + " does not exists"
        else:
            return (response_data['projectsDtoList'][0])['id']

    # DeleteProject(int ProjectID)

    def DeleteProject(self, ProjectID):
        result = self.Authenticate()
        access_token = result['accessToken']
        customerId = str(result['customerId'])
        userID = str(result['userId'])
        userName = (result['name'])
        userName1 = urllib.parse.quote(userName)

        url = self.Api_URL + "/projects/DeleteProject/" + ProjectID + "/" + customerId + "/" + userID + "/" + userName1

        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token,
            "Param": "Slc02"
        }

        response = requests.get(url, headers=header)
        print("content of 1 =", response.content)
        return not response.json()

    # PermenentdeleteProject(int ProjectID)
    def PermenentdeleteProject(self, ProjectID):
        result = self.Authenticate()
        access_token = result['accessToken']

        url = self.Api_URL + "/projects/deletedprojectpermanent"

        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token,
            "Param": "Slc02"
        }

        payload = {
            "projectID": ProjectID,
            "customerId": result['customerId'],
            "deletedBy": result['userId']
        }
        response = requests.post(url, json=payload, headers=header)
        print(response.status_code)
        return response.json()







