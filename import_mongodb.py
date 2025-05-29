import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

# Load the .env file
load_dotenv()

# Access the MongoDB password from the environment variable
mongodb_uri = os.getenv('MONGODB_URI')

# Load the CSV file into a DataFrame
df = pd.read_csv('data/Battery_RUL.csv')

# Convert the DataFrame to a list of dictionaries
data_dict = df.to_dict(orient='records')

# Create a MongoDB client
client = MongoClient(f'{mongodb_uri}')

# Specify the database and collection
db = client['battery_experiments']
collection = db['battery_rul']

# Insert the data into MongoDB
collection.insert_many(data_dict)

# Confirm insertion
print("Data inserted successfully")