import pandas as pd
import seaborn as sns
import unicodedata
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

df = pd.read_csv('players.csv')

print(df.head)

#--1--
print("************* 1 *************")
print(df.head(1))
print(df.tail(1))

#--2--
print("************* 2 *************")
print("number of all missing datas:", df.isna().sum().sum())
temp = df.isna().sum()/(len(df))*100
print("Column with lowest amount of missings contains {} % missings.".format(temp.min()))
print("Column with highest amount of missings contains {} % missings.".format(temp.max()))
print("columns contain missing values:", df.loc[:, df.isnull().any()].columns)
print("missing value checking:")
print(df.isnull())
print("rows contain missing values:")
print(df[df.isnull().any(axis=1)])

#--3--
print("************* 3 *************")
print("Average Weights: ",df["Weight"].mean())
print("max Weight: ",df["Weight"].max())
print("min Weight: ",df["Weight"].min())

#--4--
print("************* 4 *************")
df = df.dropna(subset=['Nationality'])
maxNumber = df['Nationality'].value_counts().head(1)
minNumber = df['Nationality'].value_counts().tail(1)

print("max: ", maxNumber)
print("min: ", minNumber)

#--5--
print("************* 5 *************")
dataFrame = df[df.Potential > 84]
FuturePlayers = dataFrame[dataFrame.Growth>4]
print(FuturePlayers)

#--6--
print("************* 6 *************")
df = df.dropna(subset=['BestPosition'])
df = df.dropna(subset=['Potential'])

sns.set_theme()
style.use('bmh')
sns.boxplot(x="BestPosition", y= "Potential", data=FuturePlayers)
# plt.show()

#--7--
print("************* 7 *************")
maxNumber = FuturePlayers['Club'].value_counts().head(1)
print("max: ", maxNumber)

#--8--
print("************* 8 *************")
print("total value of players: ", FuturePlayers[FuturePlayers.Club == "Chelsea"].ValueEUR.sum())

#--9--
print("************* 9 *************")
df = df.dropna(subset=['ContractUntil'])
ContractUntil2021 = df[(df['ContractUntil'] == 2021)]
res = ContractUntil2021[ContractUntil2021.NationalTeam == "Not in team"]
print("count: ", res[res.columns[0]].count())

#--10--
print("************* 10 *************")
dataFrame = df[df.FullName == "Mehdi Taremi"]
print(dataFrame[["FullName","Positions", "ValueEUR", "Club"]])