import pandas as pd


df = pd.read_csv("C:\\Users\\Abhinay\\Desktop\\sample.csv")

keys=['Typical Price','Positive Money Flow','Negative Money Flow','Positive Money Flow Sum','Negative Money Flow Sum','Money Flow Index']

TP=[]
PMF=[]
NMF=[]

for ind,row in df.iterrows():
    val = (row['High']+row['Low']+row['Close'])/3
    TP.append(val)
    if ind ==0:
        PMF.append(None)
        NMF.append(None)
    else:
        if TP[ind] > TP[ind-1]:
            PMF.append(row['Volume'] * val)
            NMF.append(None)
        elif TP[ind] < TP[ind-1]:
            NMF.append(row['Volume'] * val)
            PMF.append(None)

#print TP
#print PMF
#print NMF

df['Typical Price'] = TP
df['Positive Money Flow'] = PMF
df['Negative Money Flow'] = NMF
n = 10
PMFS=[]
tmp = df['Positive Money Flow'].fillna(0)
for i in range(0,len(tmp)):
    if i-n >= 0:
        PMFS.append(sum(tmp[(i+1-n):i+1]))
    else:
        PMFS.append(None)
df['Positive Money Flow Sum']=PMFS

NMFS=[]
tmp = df['Negative Money Flow'].fillna(0)
for i in range(0,len(tmp)):
    if i-n >= 0:
        NMFS.append(sum(tmp[(i+1-n):i+1]))
    else:
        NMFS.append(None)
df['Negative Money Flow Sum']=NMFS

ps=df['Positive Money Flow Sum']
ns=df['Negative Money Flow Sum']
MRI=[]
for i in range(0,len(df)):
    mr = ps[i]/ns[i]
    MRI.append((mr/(1+mr))*100)




