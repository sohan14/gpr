import hashlib
import hmac
from Utilities.BaseClass import BaseClass
import base64
import requests
import json


class CallBack(BaseClass):
    def cb(self):
        xdata = self.data_cleaning('cb','callback',2)
        # print(xdata)
        key = xdata['Key'][0].encode('ASCII')


        # print(key,type(key))
        for n in range(0, int(xdata['times'][0])):
            # print(n)
            message = ""

            for a,b in xdata.items():

                if a not in ("Key", "ChannelId" ,"OutletId" ,"TenantId", "url", "times"):
                    if xdata[a][n]==None:
                        xdata[a][n] ="NA"


                    message=message + str(xdata[a][n])


            print(message)
            message=message.encode('ASCII')
            signature = hmac.new(
                key,
                message,
                hashlib.sha512
            ).digest()
            signature=base64.b64encode(signature)
            signature=signature.decode()
            print(signature)
            while len(str(xdata['OutletId'][n]))!=8:
                xdata['OutletId'][n]= "0"+str(xdata['OutletId'][n])

            url = xdata["url"][n]
            headers = {"ChannelId": f"{xdata['ChannelId'][n]}",
                       "tenantId": f"{xdata['TenantId'][n]}",
                       "OutletId": f"{xdata['OutletId'][n]}",
                       }

            obj = {
                "channelid": f"{xdata['channelid'][n]}",
                "appid": f"{xdata['appid'][n]}",
                "partnerid": f"{xdata['partnerid'][n]}",
                "token": f"{xdata['token'][n]}",
                "signcs": f"{signature}",
                "cardRefNo": f"{xdata['cardRefNo'][n]}",
                "useruniqid": f"{xdata['useruniqid'][n]}",
                "reqby": f"{xdata['reqby'][n]}",
                "reqbytype": f"{xdata['reqbytype'][n]}",
                "kycStatus": f"{xdata['kycstatus'][n]}",
                "verifyontype": f"{xdata['verifyontype'][n]}",
                "verifyon": f"{xdata['verifyon'][n]}",
                "custname": f"{xdata['custname'][n]}",
                "response": f"{xdata['response'][n]}"
            }
            print(obj)

            re = requests.post(url, json=obj, headers=headers)
            tmp = ["Response code", re.status_code, re.text]
            print(tmp)



c=CallBack()
c.cb()

