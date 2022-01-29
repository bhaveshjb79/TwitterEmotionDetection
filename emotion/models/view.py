import pandas as pd 
import numpy as np
import pickle
obj=[]
file1=open("vectorizer","rb")
while True:
    try:
        obj.append(pickle.load(file1))
    except EOFError:
        break

file1.close()

print(obj)