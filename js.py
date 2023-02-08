import requests
# import datetime as dt
# url = 'http://172.16.129.36:8087/fileUploadService'
#
#
#
# resp = requests.get(url=url)
# print(resp.status_code)
# print(type((resp.status_code)))
# t = dt.datetime.now()
# tmp= t.strftime("%m%d%y_%f ")[0:-3]
#
# print(tmp)
#
# import glob
# import os
# import csv
#
# list_of_files = glob.glob('/home/sohansagar/Downloads/*.csv')
# latest_file = max(list_of_files, key=os.path.getctime)
# print(latest_file)
# tmp=latest_file.split("/")[-1]
# tmp2 = tmp.split(" ")[0] + ".csv"
# #print(tmp2)
# file=open(latest_file)
# #print(type(file))
# csv_read=csv.reader(file)
# # header=next(csv_read)
# # print(header)
# for i,row in enumerate(csv_read):
#     if i==0:
#
#         with open(tmp2,"a") as f:
#             writer = csv.writer(f)
#             data=row
#             #print(data,i)
#             writer.writerow(data)
#     else:
#         with open(tmp2, "a") as f:
#             writer = csv.writer(f)
#             data=row
#             data.append("Test")
#             data.append("24062022")
#             data.append("AWB000")
#             data.append("Mumbai")
#             writer.writerow(data)
#

# url="https://cloud-spring-qa-eastus2-card-management-service.azuremicroservices.io/card/link"
# headers={"ChannelId":"SMB0000001",
#           "tenantId":"tenant1",
#           "OutletId":"00003497",
#           }
#
# obj={
#     "cardRefNumber": "AWD000000076",
#     "firstName": "ss",
#     "middleName": "ss",
#     "lastName": "ss",
#     "mobileNo": "8668258966",
#     "emailId": "sohan.sagar@paycraftsol.com",
#     "pan": "",
#     "kycType": "MIN",
#     "otpAuthenticated": "Y"
# }
# x = requests.post(url,json= obj, headers=headers)
# print(x.status_code)
# print(x.text)


a=[1,2,4,5,5,6,6]
b=[1,2,4,5,5,6,6]
c=[(a,b)]

for m in range(len(a)):

    print(a[m],b[m])


