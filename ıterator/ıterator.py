# -*- coding: utf-8 -*-

sehirler = ["Ankara", "Istanbul", "Izmir"]

iteratorum = iter(sehirler)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print("----------")

for sehir in sehirler:
    print(sehir)
