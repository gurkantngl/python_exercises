# -*- coding: utf-8 -*-
import json

data = '{"firstName":"Gürkan","lastName":"Töngel"}'

y = json.loads(data)

print(type(data))
print(type(y))


customer = {
    "firstName":"gürkan",
    "email":"gurkantngl@gmail.com"
}

customerJson = json.dumps(customer)
print("---------------")
print(type(customer))
print(customer)
print(type(customerJson))
print(customerJson)