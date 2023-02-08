import json
import inspect
import logging

import pandas
import psycopg2 as psycopg2
import requests
import csv
import datetime as dt
import  random
import glob
import os
import shutil




class BaseClass:


    def req(self,x,y):
        url = x
        resp = requests.get(url=url,timeout=y)
        return resp.status_code

    def card_req(self):
        url = 'http://172.16.129.36:8087/fileUploadService'
        resp = requests.get(url=url)
        return resp.status_code

    def card_gen(self):
        url = 'http://172.16.129.36:8087/cardGenerationService'
        resp = requests.get(url=url)
        return resp.status_code

    def embossa_gen(self):
        url = 'http://172.16.129.36:8087/EmbossingGeneration'
        resp = requests.get(url=url)
        return resp.status_code

    def gen_dt(self):
        t = dt.datetime.now()

        tmp = t.strftime("%m%d%Y_%f ")[0:-3]
        return tmp

    def gen_file_name(self , n):
        tmp= self.gen_dt()
        fn= "CR"+tmp+".csv"
        n=n
        dirmame = os.path.dirname(__file__)
        filename = os.path.join(dirmame, f"fn/{fn}")
        for a in range(n):
            x= random.randint(100000,999999)
            data=[x,"FT GIFT A","Physical Card","","","","","","0","00000222"]


            with open(filename,"a") as f:
                writer=csv.writer(f)
                writer.writerow(data)

        dirmame=os.path.dirname(__file__)
        filename=os.path.join(dirmame,f"fn/{fn}")
        #print(filename)
        return filename

    def cr_file(self):
        dirname = os.path.dirname(__file__)
        #print(dirname.split("/"))
        if dirname.split("/")[0] != dirname:
            t11 = dirname.split("/")[0:3]
            t12 = "/".join(t11) + "/Downloads/*.csv"
        else:
            t11 = dirname.split("\\")[0:3]
            t12 = "/".join(t11) + "/Downloads/*.csv"
        # print(t12)
        list_of_files = glob.glob(t12)
        # list_of_files = glob.glob('/home/sohansagar/Downloads/*.csv')
        latest_file = max(list_of_files, key=os.path.getctime)
        #print(latest_file)
        tmp = latest_file.split("/")[-1]
        x = random.randint(1000, 9999)
        tmp2 = tmp.split(" ")[0].split(".")[0] +"_"+str(x) + ".csv"
        # print(tmp2)
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, f'fn/{tmp2}')
        file = open(latest_file)
        # print(type(file))
        csv_read = csv.reader(file)
        # header=next(csv_read)
        # print(header)
        for i, row in enumerate(csv_read):
            if i == 0:

                with open(filename, "a") as f:
                    writer = csv.writer(f)
                    data = row
                    # print(data,i)
                    writer.writerow(data)
            else:
                with open(filename, "a") as f:
                    writer = csv.writer(f)
                    data = row
                    data.append("Test")
                    data.append(dt.datetime.now().strftime("%d%m%Y"))
                    data.append("AWB000")
                    data.append("Mumbai")
                    writer.writerow(data)



        return filename

    def get_crn(self,bn,db):


        # establishing the connection
        # print(datetime.datetime(y1, m1, d1,hh1,mm1),datetime.datetime(y2, m2, d2,hh2,mm2))
        conn = psycopg2.connect(
            # database="prepaid_gpr_qa_db", user='sandbox_prepaid_qa', password='asdf1234', host='172.16.129.52', port='5444'
            database=db["database"], user=db["user"], password=db["password"], host=db["host"],
            port=db["port"]
        )

        # Setting auto commit false
        conn.autocommit = True

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Retrieving data
        # cursor.execute('''select * from ccu_master."Transaction_Accounting_Card"  where record_date BETWEEN %s AND %s order by insert_date DESC
        # ''',(datetime.datetime(y1, m1, d1,hh1,mm1),datetime.datetime(y2, m2, d2,hh2,mm2)))

        query = '''select card_ref_number , batch_no ,status from card_detail where batch_no ='{bn}'
        '''.format(bn=bn)
        # print(query)
        cursor.execute(query)
        outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)

        with open(f'Utilities/bn/{bn}.csv', 'w') as f:
            cursor.copy_expert(outputquery, f)
        conn.close()
        print("Ok")
        return f'Utilities/bn/{bn}.csv'

    def cr_link(self,x,y,z):
        url=z
        headers = {"ChannelId": "SMB0000001",
                   "tenantId": "tenant1",
                   "OutletId": "00003497",
                   }
        obj={
            "cardRefNumber": f"{x}",
            "firstName": f"{y['firstName']}",
            "middleName": f"{y['middleName']}",
            "lastName": f"{y['lastName']}",
            "mobileNo": f"{y['mobileNo']}",
            "emailId": f"{y['emailId']}",
            "pan": f"{y['pan']}",
            "kycType": f"{y['kycType']}",
            "otpAuthenticated": f"{y['otpAuthenticated']}"
        }
        re = requests.post(url, json=obj,headers=headers)
        tmp=[x,"CARD LINK",re.status_code,re.text]
        with open("temp.csv",'a') as f:
            writer = csv.writer(f)
            writer.writerow(tmp)
        return re.status_code , [re.text,json.dumps(obj, indent=2)]


    def cr_ac(self , x,y,z):
        url = z
        headers = {"ChannelId": "SMB0000001",
                   "tenantId": "tenant1",
                   "OutletId": "00003497",
                   }

        obj = {
        "cardRefNumber": f"{x}",
        "firstName": f"{y['firstName']}",
        "middleName": f"{y['middleName']}",
        "lastName": f"{y['lastName']}",
        "mobileNo": f"{y['mobileNo']}",
        "emailId": f"{y['emailId']}",
        "pan": f"{y['pan']}",
        "kycType": f"{y['kycType']}",
        "otpAuthenticated": f"{y['otpAuthenticated']}",
        "address1": "@##$",
        "address2": "Pune",
        "city": "vetican",
        "dateOfBirth": "01/01/1990",
        "pinCode": "230532"
        }
        re = requests.post(url, json=obj, headers=headers)
        tmp = [x,"CARD ACTIVATE", re.status_code, re.text]
        with open("temp.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow(tmp)
        return re.status_code , [re.text,json.dumps(obj, indent=2)]



    def get_data(self,re):

        df = pandas.read_excel('gpr.xlsx',
                               sheet_name=re)
        df_json = df.to_json()
        df_d = json.loads(df_json)
        data_take = []

        #print(len(df_d))
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
        col_len = 0
        t = 0
        for x, y in df_d.items():
            col_len = len(y)
            b.append(x)

            for m, n in y.items():
                #print(t)
                #print(m, n)
                if t < col_len:
                    c.append(n)
                    t = t + 1
                elif t < col_len * 2:
                    d.append(n)
                    t = t + 1
                elif t < col_len * 3:
                    e.append(n)
                    t = t + 1
                elif t < col_len * 4:
                    f.append(n)
                    t = t + 1
                elif t < col_len * 5:
                    g.append(n)
                    t = t + 1
                elif t < col_len * 6:
                    h.append(n)
                    t = t + 1

        #print(b, c, d, e)

        for n in range(0, col_len):
            a = {}

            a[b[0]] = c[n]
            a[b[1]] = d[n]
            a[b[2]] = e[n]
            a[b[3]] = f[n]
            a[b[4]] = g[n]
            a[b[5]] = h[n]

            data_take.append(a)
        #print(data_take)
        return data_take

    def create_corp(self,x,re,tc):
        df = pandas.read_excel('gpr.xlsx',
                               sheet_name=x)
        df_json = df.to_json()
        df_d = json.loads(df_json)
        data_take = []

        #print(len(df_d))
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
        i = []
        j = []
        k = []
        l = []
        o = []
        col_len = 0
        t = 0
        for x, y in df_d.items():
            col_len = len(y)
            b.append(x)

            for m, n in y.items():
                #print(t)
                #print(m, n)
                if t < col_len:
                    c.append(n)
                    t = t + 1
                elif t < col_len * 2:
                    d.append(n)
                    t = t + 1
                elif t < col_len * 3:
                    e.append(n)
                    t = t + 1
                elif t < col_len * 4:
                    f.append(n)
                    t = t + 1
                elif t < col_len * 5:
                    g.append(n)
                    t = t + 1
                elif t < col_len * 6:
                    h.append(n)
                    t = t + 1
                elif t < col_len * 7:
                    i.append(n)
                    t = t + 1
                elif t < col_len * 8:
                    j.append(n)
                    t = t + 1
                elif t < col_len * 9:
                    k.append(n)
                    t = t + 1
                elif t < col_len * 10:
                    l.append(n)
                    t = t + 1
                elif t < col_len * 11:
                    o.append(n)
                    t = t + 1

        #print(b, c, d, e)
        tmp = self.gen_dt()
        fn = "CR" + tmp + ".csv"

        dirmame = os.path.dirname(__file__)
        filename = os.path.join(dirmame, f"fn/{fn}")

        for n in range(0, col_len):
            a = {}

            a[b[0]] = c[n]
            a[b[1]] = d[n]
            a[b[2]] = e[n]
            a[b[3]] = f[n]
            a[b[4]] = g[n]
            a[b[5]] = h[n]
            a[b[6]] = i[n].split("|")[1]
            a[b[7]] = j[n]
            a[b[8]] = k[n]
            a[b[9]] = l[n]
            a[b[10]] = o[n]
            a[b[10]]=str(a[b[10]])
            while len(a[b[10]])!=8:
                a[b[10]]= "0"+a[b[10]]


            data_take.append(a)
            #print(data_take)

        #print(data_take)
        if tc:
            return data_take[0:re]
        zz=re
        #print(zz)
        for q in range(zz):

            tmp1=data_take[q]
            #print(tmp1)

            tmp2=[]
            for m,n in tmp1.items():
                tmp2.append(n)
            #print(tmp2)
            with open(filename, "a") as f:
                writer = csv.writer(f)
                writer.writerow(tmp2)
        return filename ,data_take[0]

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(f'log/{dt.datetime.now().strftime("%d%m%Y_%H%M%S")}.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def get_data_product(self,re):

        df = pandas.read_excel('product.xlsx',
                               sheet_name=re)
        df_json = df.to_json()
        df_d = json.loads(df_json)
        data_take = []

        #print(len(df_d))
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        col_len = 0
        t = 0
        for x, y in df_d.items():
            col_len = len(y)
            b.append(x)

            for m, n in y.items():
                #print(t)
                #print(m, n)
                if t < col_len:
                    c.append(n)
                    t = t + 1
                elif t < col_len * 2:
                    d.append(n)
                    t = t + 1
                elif t < col_len * 3:
                    e.append(n)
                    t = t + 1
                elif t < col_len * 4:
                    f.append(n)
                    t = t + 1
                elif t < col_len * 5:
                    g.append(n)
                    t = t + 1

        #print(b, c, d, e)

        for n in range(0, col_len):
            a = {}

            a[b[0]] = c[n]
            a[b[1]] = d[n]
            a[b[2]] = e[n]
            a[b[3]] = f[n]
            a[b[4]] = g[n]

            data_take.append(a)
        #print(data_take)
        return data_take

    def product_clean(self,re, times=1):

        df = pandas.read_excel('product.xlsx',
                               sheet_name=re)
        df_json = df.to_json()
        df_d = json.loads(df_json)
        clean=[]
        for i in range(0,times):
            if i == 0:
                d = {}
            for a,b in df_d.items():
                c=a
                if i==0:
                    d[a]=[(df_d[f"{c}"][f"{i}"])]
                else:
                    d[a].append(df_d[f"{c}"][f"{i}"])


                clean.append(a)
        print(d)
        return d

    def get_api(self,re):

        df = pandas.read_excel('gpr.xlsx',
                               sheet_name=re)
        df_json = df.to_json()
        df_d = json.loads(df_json)
        data_take = []

        #print(len(df_d))
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h=[]

        col_len = 0
        t = 0
        for x, y in df_d.items():
            col_len = len(y)
            b.append(x)

            for m, n in y.items():
                #print(t)
                #print(m, n)
                if t < col_len:
                    c.append(n)
                    t = t + 1
                elif t < col_len * 2:
                    d.append(n)
                    t = t + 1
                elif t < col_len * 3:
                    e.append(n)
                    t = t + 1
                elif t < col_len * 4:
                    f.append(n)
                    t = t + 1
                elif t < col_len * 5:
                    g.append(n)
                    t = t + 1
                elif t < col_len * 6:
                    h.append(n)
                    t = t + 1

        #print(b, c, d, e)

        for n in range(0, col_len):
            a = {}

            a[b[0]] = c[n]
            a[b[1]] = d[n]
            a[b[2]] = e[n]
            a[b[3]] = f[n]
            a[b[4]] = g[n]
            a[b[5]] = h[n]

            data_take.append(a)
        print(data_take)
        return data_take

    def data_cleaning(self,re,ex, times=1):

        df = pandas.read_excel(f'{ex}.xlsx',
                               sheet_name=re)
        df_json = df.to_json()
        df_d = json.loads(df_json)
        clean=[]
        for i in range(0,times):
            if i == 0:
                d = {}
            for a,b in df_d.items():
                c=a
                if i==0:
                    d[a]=[(df_d[f"{c}"][f"{i}"])]
                else:
                    d[a].append(df_d[f"{c}"][f"{i}"])


                clean.append(a)
        print(d)
        return d


# a=BaseClass()
# a.get_api("api")
# b=a.product_clean("limitProfile",1)
# if b["ATM cash withdrawal"][0]=='Yes':
#     print('OO')
#     print(b["ATM Total Life Time Amt"][0].split("-")[1])
# a.cr_file()
#a.get_crn('BU3006222320')
# a.gen_file_name(10)
#a.cr_file()
#a.create_corp("FT GIFT A",3)
#a.get_data('user')