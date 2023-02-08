import pandas
import json
df = pandas.read_excel('gpr.xlsx',
                               sheet_name="db")
df_json = df.to_json()
df_d = json.loads(df_json)
data_take = []

print(len(df_d))
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
    print(col_len)
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
print(data_take)
