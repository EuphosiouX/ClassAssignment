# Define a class named "Author"
class Author:
    # Assign "Author" object using def__init__ function
    def __init__(self, name, email, gender):
        self.__name = str(name)
        self.__email = str(email)
        self.__gender = str(gender)

        # To check if the gender valid or not
        if (gender not in ("m","f")):
            raise ValueError

    # Fetch the author name
    def getName(self):
        return self.__name

    # Fetch the author email
    def getEmail(self):
        return self.__email

    # Change the email
    def setEmail(self, email):
        self.__email = str(email)

    # Fetch the author gender
    def getGender(self):
        return self.__gender

    # Print "Author[Name=?,Email=?,,Gender=]"
    def __str__(self):
        return ("Author[Name={},Email={},Gender={}]".format(self.__name,self.__email,self.__gender))

# class Book:
#     def __init__(self, name, author, price, qty=0):
#         self.__name = str(name)
#         self.__author = author
#         self.__price = float(price)
#         self.__qty = int(qty)

#     def getName(self):
#         return self.__name

#     def getAuthor(self):
#         return self.__author
    
#     def getAuthorName(self):
#         return self.__author.getName()

#     def getAuthorEmail(self):
#         return self.__author.getEmail()
    
#     def getAuthorGender(self):
#         return self.__author.getGender()

#     def getPrice(self):
#         return self.__price

#     def setPrice(self, price):
#         self.__price = str(price)
    
#     def getQty(self):
#         return self.__qty
    
#     def setQty(self, qty):
#         self.__qty = int(qty)

#     def __str__(self):
#         return ("Book[Name={},{},Price={},qty={}]".format(self.__name,self.__author,self.__price,self.__qty))

# Define a class named "Book"
class Book:
    # Assign "Book" object using def__init__ function which also have some object from "Author" class
    def __init__(self, name, author, price, qty=0):
        self.__name = str(name)
        self.__authors = list(author)
        self.__price = float(price)
        self.__qty = int(qty)

    # Fetch the book name
    def getName(self):
        return self.__name

    # Fetch the author object
    def getAuthors(self):
        return self.__authors
    
    # Fetch the book price
    def getPrice(self):
        return self.__price

    # Change the price 
    def setPrice(self, price):
        self.__price = str(price)
    
    # Fetch the quantity
    def getQty(self):
        return self.__qty
    
    # Change the quantity
    def setQty(self, qty):
        self.__qty = int(qty)

    # Print "Book[Name=?,authors=[Author[Name=?,Email=?,Gender=?,......],Price=?,Qty=?]"
    def __str__(self):
        authors = []
        for author in self.__authors:
            authors.append(author.__str__())
        return ("Book[Name={},Authors={},Price={},Qty={}]".format(self.__name,", ".join(authors),self.__price,self.__qty))

    def getAuthorName(self):
        get_names = []
        for author in self.__authors:
            get_names.append(author.getName())
        return ", ".join(get_names)

    def getAuthorEmail(self):
        get_emails = []
        for author in self.__authors:
            get_emails.append(author.getEmail())
        return ", ".join(get_emails)

    def getAuthorGender(self):
        get_genders = []
        for author in self.__authors:
            get_genders.append(author.getGender())
        return ", ".join(get_genders)

# Variables needed

author1 = Author("J.K Rowling", "rowling@yahoo.com", "f")
author2 = Author("Stephen King", "stephenkng@gmail.com", "m")
testbook = Book("Harry Potter n The Goblet of Fire", [author1, author2], 18000, 1)

print(testbook.getAuthorName())
print(testbook.getAuthorEmail())
print(testbook.getAuthorGender())
print(testbook)
