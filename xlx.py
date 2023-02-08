import pandas
import json



df = pandas.read_csv('/home/sohansagar/PycharmProjects/GPR /resultsfiles.csv')
df_json = df.to_json()
df_d = json.loads(df_json)
data_take = []
print(df_d)

print(len(df_d))
b = []
c = []
d= []
col_len = 0
t = 0
for x, y in df_d.items():
    col_len = len(y)
    b.append(x)

    for m, n in y.items():
        print(t)
        print(m, n)
        if t < col_len:
            c.append(n)
            t = t + 1
        # elif t < col_len * 2:
        #     d.append(n)
        #     t = t + 1
        # elif t < col_len * 3:
        #     e.append(n)
        #     t = t + 1
        # elif t < col_len * 4:
        #     f.append(n)
        #     t = t + 1

print(b, c, d)

for n in range(0, col_len):
    a = {}
    #a["Qty"] = "1"
    a[b[0]] = c[n]
    #a[b[1]] = d[n]
    # a[b[2]] = e[n]
    # a[b[3]]=f[n]


    #a["Amt"] = ""
    data_take.append(a)

print(data_take)
print(type(data_take))
for a in data_take:
    print(a['card_ref_number'])
