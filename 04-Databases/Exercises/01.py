from pymongo import MongoClient
from pprint import pprint
from copy import deepcopy


# Define client connection
url = "mongodb://localhost:27017/"
usr = "admin"
pwd = "password"

client = MongoClient(host=url, username=usr, password=pwd)
db = client.Northwind
products_collection = db.Products


# Count products
# Print count and list
products = list(products_collection.find())

print(f"Total products: {len(products)}")
[print(product.get('ProductID'), '-', product.get('ProductName')) for product in products]
print()


# Filter products with stock = 0 ('UnitsInStock' key) using filter()
products_without_stock = list(filter(lambda product: product['UnitsInStock'] == '0', products))

print('Total products without stock:', len(products_without_stock))
[print(product.get('ProductID'), '-', product.get('ProductName')) for product in products_without_stock]
print()


# Print stock value (multiply units per price: UnitsInStock * UnitPrice)
# Both with FOR loop and with map() sum()
# OPTIONAL: aggregate function with $sum and $multiply operators against mongoDB
# products_with_stock_value_map_sum = list(map(lambda product: product.update({'StockValue': str(float(product['UnitsInStock']) * float(product['UnitPrice']))}), products))

products_with_stock_value_map = list(map(lambda product: {**product, **{'StockValue': float(product['UnitsInStock']) * float(product['UnitPrice'])}}, products))

print(f"Stock value using map() and sum() functions - Total is {sum([product['StockValue'] for product in products_with_stock_value_map]):.2f}:")
[print(product.get('ProductID'), '-', product.get('ProductName'), '-', 'Stock value:', f"{product.get('StockValue'):.2f}") for product in products_with_stock_value_map]
print()


products_with_stock_value_for = deepcopy(products)

total = 0
for product in products_with_stock_value_for:
    product_total = float(product['UnitsInStock']) * float(product['UnitPrice'])
    total += product_total
    product.update({'StockValue': product_total})

print(f"Stock value using for loop - Total is {total:.2f}:")
[print(product.get('ProductID'), '-', product.get('ProductName'), '-', 'Stock value:', f"{product.get('StockValue'):.2f}") for product in products_with_stock_value_for]
print()


products_with_stock_value_aggregate = list(products_collection.aggregate([
    {
        "$addFields": {
            "StockValue": {
                "$multiply": [
                    # { "$convert": { "input": "$UnitsInStock", "to": "double" } },
                    { "$toInt": "$UnitsInStock" },
                    # { "$convert": { "input": "$UnitPrice", "to": "double" } }
                    { "$toDouble": "$UnitPrice" },
                ]
            }
        }
    },{
        "$group": {
            "_id": None,
            "TotalStockValue": {"$sum": "$StockValue"},
            "products": {"$push": "$$ROOT"}
        }
    }
]))[0]

# pprint(products_with_stock_value_aggregate)
print(f"Stock value using aggregate function - Total is {products_with_stock_value_aggregate['TotalStockValue']}:")
[print(product.get('ProductID'), '-', product.get('ProductName'), '-', 'Stock value:', product.get('StockValue')) for product in products_with_stock_value_aggregate['products']]
print()


# Given an OrderID, list associated data (like ShipName, ShipAddress, ShipCity,
# ShipCountry, OrderDate, ShippedDate). Also list order details (Product,
# Quantity, Price, Total price, Total order).

orders_collection = db.Orders
order_details_collection = db.Order_Details
order_id = input("Insert an OrderID: ")

'''
pipeline = [
    {
        "$match": {
            "OrderID": order_id
        }
    },{
        "$lookup": {
            "from": order_details_collection.name,
            "localField": "OrderID",
            "foreignField": "OrderID",
            "as": "Details"
        }
    }
]

order_and_its_details = orders_collection.aggregate(pipeline)

for order in order_and_its_details:
    total = 0
    print(f"Order #{order['OrderID']} - {order['ShipName']}, {order['ShipAddress']}, {order['ShipCity']}, {order['ShipCountry']}, {order['OrderDate']}, {order['ShippedDate']}")
    for detail in order['Details']:
        total_product_detail = float(detail['UnitPrice']) * float(detail['Quantity'])
        total += total_product_detail
        print(f" * Product #{detail['ProductID']} - {detail['UnitPrice']} x {detail['Quantity']} = {total_product_detail:.2f}")
    print(f"Total amount: {total}")
'''

pipeline = [
    {
        "$match": {
            "OrderID": order_id
        }
    },
    {
        '$lookup': {
            'from': order_details_collection.name,
            'localField': 'OrderID',
            'foreignField': 'OrderID',
            'as': 'order_details'
        }
    },
    {
        '$unwind': '$order_details'
    },
    {
        '$lookup': {
            'from': 'Products',
            'localField': 'order_details.ProductID',
            'foreignField': 'ProductID',
            'as': 'product_details'
        }
    },
    {
        '$unwind': '$product_details'
    },
    {
        '$addFields': {
            "order_details.ProductInfo": "$product_details",
            'order_details.TotalProductPrice': {
                '$multiply': [
                    { "$toDouble": "$order_details.UnitPrice" },
                    { "$toInt": "$order_details.Quantity" }
                ]
            }
        }
    },
    {
        '$group': {
            '_id': '$OrderID',
            'TotalOrderPrice': { '$sum': '$TotalProductPrice' },
            # Include all fields from Orders collection
            'Orders': { '$first': '$$ROOT' },
            # Include all fields from Order_Details collection
            'Order_Details': { '$push': '$order_details' }
        }
    },
    { 
        "$replaceRoot": {
            "newRoot": {
                "$mergeObjects": [
                    "$Orders",
                    { "TotalOrderPrice": "$TotalOrderPrice" },
                    { "Order_Details": "$Order_Details" }
                ]
            }
        }
    },
    { 
        # Exclude order_details field from final result
        # This happens on unwind, and I don't know why...
        # Like, yeah, I know what unwind does in a basic manner,
        # but in this case neither StackOverflow nor MongoDB
        # documentation are giving me enough information.
        "$project": {
            "order_details": 0,
            "product_details": 0
        }
    }
]

order_and_its_details = orders_collection.aggregate(pipeline)

# pprint(list(order_and_its_details))

for order in order_and_its_details:
    print(f"Order #{order['OrderID']} (Total: {order['TotalOrderPrice']:.2f})- {order['ShipName']}, {order['ShipAddress']}, {order['ShipCity']}, {order['ShipCountry']}, {order['OrderDate']}, {order['ShippedDate']}")
    for order_detail in order['Order_Details']:
        print(f" * Product #{order_detail['ProductID']} ({order_detail['ProductInfo']['ProductName']}): {order_detail['UnitPrice']} x {order_detail['Quantity']} = {order_detail['TotalProductPrice']:.2f}")

# print(f"{product:<30} {text:<10}")

client.close()
