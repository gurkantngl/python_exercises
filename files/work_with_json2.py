# -*- coding: utf-8 -*-
import json

# with ile açıldığında dosya otomatik kapatılır
with open("users.json") as users:
    data = json.load(users)
    
    for i in range(5):
        print(i+1, ". data:")
        print(data[i]["username"])
        print(data[i]["email"])
        print(data[i]["address"])
        print(data[i]["address"]["street"])
        print(data[i]["address"]["geo"]["lat"])
        print("---------------------\n")