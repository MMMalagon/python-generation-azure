import pymssql

# Establishing connection
connection = pymssql.connect(server='localhost:1433', user='sa',
                             password='YourStrong@Passw0rd',
                             database='Northwind')

# Establishing cursor
cursor = connection.cursor()

# Returning dicts
cursor = connection.cursor(as_dict = True)  # if False, they're tuples

'''
cursor.execute("SELECT * FROM dbo.Customers")

row = cursor.fetchone()
while row:
    print(f"     ID: {row['CustomerID']}" )
    print(f"Company: {row['CompanyName']}")
    print()
    row = cursor.fetchone()

for row in cursor.fetchall():
    print(f"     ID: {row['CustomerID']}")
    print(f"Company: {row['CompanyName']}")
    print()
'''

'''
# cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
# cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "Spain")
# cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d ORDER BY City", "Spain")
cursor.execute("SELECT CustomerID, CompanyName, City, Country FROM dbo.Customers WHERE Country = %d ORDER BY City", "Spain")

for row in cursor.fetchall():
    print(f"      ID: {row['CustomerID']}")
    print(f" Company: {row['CompanyName']}")
    print(f"Location: {row['City']} ({row['Country']})")
    print()
'''

cursor.execute("SELECT CustomerID, CompanyName, City, Country FROM dbo.Customers ORDER BY Country, City")

for row in cursor.fetchall():
    print(f"      ID: {row['CustomerID']}")
    print(f" Company: {row['CompanyName']}")
    print(f"Location: {row['City']} ({row['Country']})")
    print()

print()

'''
insert_result = cursor.execute("INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactName, City, Country) " +
                               "VALUES ('DEM61', 'Comidas 1 2 3, SL', 'Borja Cabeza', 'Madrid', 'Spain')")

print(insert_result)
'''
# command = "INSERT INTO dbo.Customers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
command = "INSERT INTO dbo.Customers(CustomerID, CompanyName, City, Country) VALUES (%d, %d, %d, %d)"

data = []

data.append(('MMM99', 'Empresa 1 SL', 'Madrid', 'Spain'))
data.append(('MMM89', 'Empresa 2 SL', 'Valencia', 'Spain'))
data.append(('MMM79', 'Empresa 3 SL', 'Málaga', 'Spain'))

cursor.executemany(command, data)

connection.commit()

# connection.rollback()

cursor.execute("SELECT CustomerID, CompanyName, City, Country FROM dbo.Customers WHERE CustomerID LIKE 'MMM%' ORDER BY Country, City")

for row in cursor.fetchall():
    print(f"      ID: {row['CustomerID']}")
    print(f" Company: {row['CompanyName']}")
    print(f"Location: {row['City']} ({row['Country']})")
    print()
