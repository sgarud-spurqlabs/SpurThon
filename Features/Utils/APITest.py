from  Features.Utils.APIUtility import APIUtility

obj=APIUtility()

print(obj.CheckkProjectNameExist("Test103"))
print(obj.GetProjectIDbyName("Test103"))
print(obj.GetOfficeMasterProjectIDbyName("Test101"))
print("deleted =",obj.DeleteProject("13705"))
print("deleted=",obj.PermenentdeleteProject("13705"))
