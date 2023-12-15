import pymongo
from datetime import datetime

#Connection
client = pymongo.MongoClient("xxxx")
db = client["StockExApp"]
collection = db["Accounts"]

collection.create_index("account_id", unique=True)

# Replace this with your Unix timestamp
current_timestamp = datetime.now().timestamp()

# Convert the Unix timestamp to a datetime object
dt_object = datetime.fromtimestamp(current_timestamp)

# Format the datetime object as a string
formatted_time = dt_object.strftime("%d.%m.%Y %H:%M:%S")  # Customize the format as needed

print(formatted_time)

# Create a document (dictionary) to insert
document_to_insert = {
    "account_id" : "xxx",
    "client_id": "xxx",
    "secret_key": "xxx",
    "access_token": "",
    "ts_token_updated":"",
    "ts_account_creation":formatted_time
}

# Insert the document into the collection
result = collection.insert_one(document_to_insert)

# Print the inserted document's ObjectID
print("Inserted document ID:", result.inserted_id)