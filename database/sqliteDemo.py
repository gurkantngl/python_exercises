#  -*- coding: utf-8 -*-
import sqlite3

def selectOperations():
    # if the file does not exist it creates a new file
    connection = sqlite3.connect("chinook.db")

    #cursor = connection.execute("""select FirstName,LastName 
    #                           from customers 
    #                            where city='Prague' or city = 'Berlin' 
    #                            order by FirstName""")

    #for row in cursor:
    #    print("First Name: ", row[0])
    #    print("Last Name: ", row[1])
    #    print("**********")
    
    #cursor = connection.execute("""select city, count(*) from Customers 
    #                            group by city having count(*)>1
    #                            order by count(*)""")
    
    #for row in cursor:
    #    print("City: ", row[0])
    #    print("Count: ", row[1])
    #    print("***********")
    
    
    cursor = connection.execute("""select FirstName,LastName
                                from customers
                                where FirstName like '%a%' """)
    
    for row in cursor:
        print("City: ", row[0])
        print("Count: ", row[1])
        print("***********")
        
        
    connection.close()
    
    
selectOperations()

def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""
                       insert into customers 
                       (firstName,lastName,city,email)
                       values ('Gürkan','Töngel','Sakarya','gurkantngl@gmail.com')
                       """)
    connection.commit()
    connection.close()
    
#insertCustomer()


def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""
                       update customers set city = 'Ankara' 
                       where city = 'Sakarya'""")
    connection.commit()
    connection.close()
    
#updateCustomer()


def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" delete from customers
                            where customerid=60 """)
    connection.commit()
    connection.close()

#deleteCustomer()

def joinOperations():
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute(""" select albums.Title,
                                artist.Name from artists
                                inner join albums
                                on artists.ArtistId = albums.ArtistId """)
    
    for row in cursor:
        print("Title: ", row[0])
        print("Name: ", row[1])
        print("************")