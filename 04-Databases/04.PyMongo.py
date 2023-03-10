from pymongo import MongoClient, ASCENDING, DESCENDING
from pprint import pprint
# from time import sleep

url = "mongodb://localhost:27017/"
usr = "admin"
pwd = "password"

def find_orders_by_country(customers_collection, orders_collection, country: str):
    pipeline = [
        {"$match": {"Country": country}},
        {"$lookup": {
            "from": orders_collection.name,
            "localField": "CustomerID",
            "foreignField": "CustomerID",
            "as": "Orders"
        }}
    ]
    return customers_collection.aggregate(pipeline)
    # return list(result)


def main():
    global url, usr, pwd
    
    # client = MongoClient("mongodb://admin:password@localhost:27017/")
    client = MongoClient(host=url, username=usr, password=pwd)

    print(f"Databases in '{client.HOST}:{client.PORT}': {client.list_database_names()}")

    # pprint(client.admin.command("serverStatus"))    
    
    db = client["Northwind"]  # client.Northwind

    print(f"Collections in '{db.name}': {db.list_collection_names()}")

    collection = db['Customers']  # collection.Customers

    print(f"Documents estimated count in '{collection.name}': {collection.estimated_document_count()}")
    print(f"Documents count in '{collection.name}': {collection.count_documents({})}")

    '''
    result = collection.find_one({'Country': 'USA'})
    # print(result)
    pprint(result)

    result = collection.find_one()
    pprint(result)

    result = collection.find_one({'Country': 'Spain'})
    pprint(result)
    '''

    # object_id = '6409a5f35d827a401277d6bc'

    cursor = collection.find({'Country': 'USA'})
    print(f"Pending documents: {cursor.alive}")

    while cursor.alive:
        pprint(cursor.next())
        # document = cursor.next()
        # print(document["CompanyName"], document['City'])
        print()

    # sleep(5)
    print(f"Pending documents: {cursor.alive}")

    cursor = collection.find({'Country': 'USA'})
    cursor_list = list(cursor)  # we do not lose them

    for hint in cursor_list:
        pprint(hint)

    '''
    cursor = collection.find({'Country': 'USA'})
    cursor = collection.find({'Country': 'USA'}).limit(3)
    cursor = collection.find({'Country': 'USA'}).skip(5)

    cursor = collection.find({'Country': 'USA'}).limit(2)
    cursor = collection.find({'Country': 'USA'}).skip(2).limit(2)
    cursor = collection.find({'Country': 'USA'}).skip(4).limit(2)
    cursor = collection.find({'Country': 'USA'}).skip(6).limit(2)

    cursor = collection.find({'Country': 'USA'}).sort("City")
    cursor = collection.find({'Country': 'USA'}).sort("City", ASCENDING)  # 1
    '''
    cursor = collection.find({'Country': 'USA'}).sort("City", DESCENDING)  # -1

    while cursor.alive:
        document = cursor.next()
        print(document["CompanyName"], "-", document['City'])

    '''
    data = collection.find()

    for document in data:
        print(document)
    '''

    """
    ===================================================
    Literal operators list
    ===================================================
    $eq  - equal to
    $lt  - lower than
    $lte - lower than or equal to
    $gt  - greater than
    $gte - greater than or equal to
    $ne  - not equal to
    $in  - in
    $nin - not in
    """

    cursor = collection.find({'Country': 'USA'})
    cursor = collection.find({'Country': {'$eq': 'USA'}})
    cursor = collection.find({'Country': {'$ne': 'USA'}})
    cursor = collection.find({'Country': {'$in': ['USA', 'Mexico']}}).sort([("Country", 1), ("City", 1)])

    while cursor.alive:
        document = cursor.next()
        print(document["CompanyName"], "-", document['Country'], f"({document['City']})")

    cursor = collection.find({'Country': 'USA', 'City': 'San Francisco'})
    cursor = collection.find({"$and": [{"Country": "USA"}, {"City": "San Francisco"}]})
    cursor = collection.find({"$or": [{"Country": "USA"}, {"City": "Berlin"}]})
    cursor = collection.find({"$or": [{"Country": "USA"}, {"Country": "Germany"}]})

    cursor = collection.find({'Country': 'Mexico'})
    collection_while = db.Orders

    while cursor.alive:
        document =  cursor.next()
        cursor_while = collection_while.find({'CustomerID': document['CustomerID']})

        print(f"Orders of {document['CompanyName']}:")
        while cursor_while.alive:
            document_while = cursor_while.next()
            print("*", document_while['OrderID'], "-", document_while['OrderDate'])

    print("###################################################")
    print("###################################################")
    print("###################################################")

    orders_cursor = find_orders_by_country(collection, collection_while, 'Mexico')

    while orders_cursor.alive:
        orders = orders_cursor.next()
        print(f"Orders of {orders['CompanyName']} - Customer {orders['CustomerID']}:")
        for order in orders['Orders']:
            print("*", order['OrderID'], "-", order['OrderDate'])

    '''
    cursor = collection.aggregate([
        {"$match": {"CustomerID": "ANATR"}},
        {"$sort": {"City": 1}},
        {"$lookup": {
            "from": "Orders",
            "localField": "CustomerID",
            "foreignField": "CustomerID",
            "as": "Orders"
        }}
    ])
    '''

    client.close()


if __name__ == "__main__":
    main()
