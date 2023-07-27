# -*- coding: utf-8 -*-

import os

#w(write) --> dosya varsa da yeniden oluşturur
#f = open("musteriler.txt","w")

#r(read) --> dosya okuma yapar
#f = open("musteriler.txt","r")

#a(append) --> var olan dosyaya ekleme yapar
#f = open("musteriler.txt","a")

#x(create) --> dosya yoksa oluşturur, varsa hata verir
#f = open("musteriler.txt","x")

# default --> read
f = open("file.txt")
#print(f.read()) --> bütün dosyayı okur
#print(f.readline()) # tek bir satır okur

for l in f:
    l = l.strip("\n")
    print(l)


f.close()

fileToAppend = open("ogrenciler.txt", "a")
fileToAppend.write("Gürkan")
fileToAppend.write("\n")

if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt") #--> dosyayı siler
else:
    print("Dosya yok")