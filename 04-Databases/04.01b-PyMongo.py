from pymongo import MongoClient
from pprint import pprint

url = "mongodb://localhost:27017/"
usr = "admin"
pwd = "password"

client = MongoClient(host=url, username=usr, password=pwd)
db = client.Northwind
customers = db.Customers

# Insert example with dict (can be multiple with list)
'''
customer_id = input("Insert customer ID: ")

customer = {
    "CustomerID": customer_id,
    "CompanyName": "Uno Comidas SL",
    "ContactName": "Borja Cabeza",
    "ContactTitle": "Propietario",
    "Address": "Calle Gran Vía, 42",
    "City": "Madrid",
    "Country": "Spain",
    "PostalCode": "28044",
    "Region": "Madrid",
    "Phone": "+34912002020",
    "Fax": "+34912002021"
}

transaction_result = customers.insert_one(customer)

print("Result:", transaction_result)
print("ObjectID:", transaction_result.inserted_id)
print("ACK:", transaction_result.acknowledged)
'''

# Regex search
'''
# customers_cursor = customers.find({"CustomerID": "DEMO"})  # if cursor is empty, it raises StopIteration exception, which is wild
# customers_cursor = customers.find({"CustomerID": {"$regex": "DEMO"}})
customers_cursor = customers.find({"CustomerID": {"$regex": "^DEMO"}})

while customers_cursor.alive:
    customer = customers_cursor.next()
    print(f"#{customer['CustomerID']} - {customer['CompanyName']}")
'''


# Example with Customer class and __dict__
'''
class Customer:

    def __init__(self, CustomerID: str, CompanyName: str, ContactName: str,
                 ContactTitle: str, Address: str, City: str, Country: str,
                 PostalCode: str, Region: str, Phone: str, Fax: str) -> None:
        self.CustomerID = CustomerID
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Country = Country
        self.PostalCode = PostalCode
        self.Region = Region
        self.Phone = Phone
        self.Fax = Fax


customer = Customer("DEM10", "Uno Comidas SL", "Borja Cabeza", "Propietario",
                    "Calle Gran Vía, 42", "Madrid", "Spain", "28044", "Madrid",
                    "+34912002020", "+34912002021")

# pprint(customer.__dict__)

transaction_result = customers.insert_one(customer.__dict__)

print("Result:", transaction_result)
print("ObjectID:", transaction_result.inserted_id)
print("ACK:", transaction_result.acknowledged)
'''

query = {"CustomerID": "DEM10"}
customer = customers.find_one(query)
print("BEFORE:")
pprint(customer)

customer_update = {
    "$set": {
        "Address": "Calle Serrano, 81",
        "PostalCode": "28016",
        "Phone": "+34914502525"
    }
}

update_result = customers.update_one(query, customer_update)

print("Matched count:", update_result.matched_count)
print("Modified count:", update_result.modified_count)
print("ACK:", update_result.acknowledged)

customer = customers.find_one(query)
print("AFTER")
pprint(customer)

client.close()
