import pandas as pd

df = pd.read_csv("data.csv")
print(df.head() , "io" in df[["hi"]].values)
price = (10,20,30)
food_l = {"apple","banana","coconut"}

def key_pair_merge(Key_L,Val_T):
    KpV ={}
    i = 0
    for key in Key_L:
       KpV[key] = Val_T[i]
       i = i + 1
    return KpV
        
print(key_pair_merge(food_l,price))      
# hi.      