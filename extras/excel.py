import pandas as pd




path = 'D:/JMM/11 twilio for call/call-recording-log-ACd3b2983fb783e5a8ede5301eb338715a_2022-12-09.csv'

df = pd.read_csv(path)

print(df.info())