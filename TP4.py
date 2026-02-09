import pandas as pd
import random as rd

data = pd.read_csv("donnevrai.csv")
data["danger"] = data["danger"].map({0: "safe", 1: "danger"})

w = rd.randint(-10,10)
b = rd.randint(-10,10)

X = data["vitesse"].tolist()
Y = data["danger"].tolist()

for i in range(100):
    print("Vitesse :", X[i],":",Y[i])

print(w,b)