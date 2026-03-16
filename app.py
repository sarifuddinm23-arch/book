import os
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv

# .env ফাইল থেকে কানেকশন স্ট্রিং লোড করা
load_dotenv()

app = Flask(__name__)

# MongoDB কানেক্ট করা
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

# ডাটাবেস এবং কালেকশন (টেবিল) তৈরি
db = client['IndaneManagerDB'] # আপনার ডাটাবেসের নাম
collection = db['invoices']     # আপনার ইনভয়েস বা বিলের টেবিল

@app.route('/')
def index():
    try:
        # একটি ডামি ডাটা ইনসার্ট করে চেক করা
        test_data = {"item": "Cylinder", "quantity": 1, "price": 1100}
        collection.insert_one(test_data)
        return "MongoDB Connected and Data Saved Successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
