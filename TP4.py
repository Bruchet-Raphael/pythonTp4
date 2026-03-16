import pandas as pd
import random as rd

def Zpredict(x):
    w = rd.randint(-10,10)
    b = w*x
    Z = w*x + b
    if(Z >= 0):
        return 1
    else:
        return 0

data = pd.read_csv("donnevrai.csv")
#data["danger"] = data["danger"].map({0: "safe", 1: "danger"})

X = data["vitesse"].tolist()
Y = data["danger"].tolist()

for i in range(100):
    print("Vitesse :", X[i],":",Y[i])

print(X[:5], Y[:5])

for x in X:
    print(f"x = {x},prédiction = {Zpredict(x)}")

for x,y in zip(X,Y):
    laPreY = Zpredict(x)
    erreur = y - laPreY
    if(erreur < 0):
        erreur = 1
    print(f"x = {x},y = {y},Y_pred = {laPreY}, Erreur = {erreur}")