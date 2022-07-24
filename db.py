from pymongo import MongoClient
from werkzeug.security import generate_password_hash

client = MongoClient("mongodb+srv://levent:levent@leventchatapp.ar9zqz4.mongodb.net/?retryWrites=true&w=majority")
chat_db = client.get_database("ChatDB")
user_collection = chat_db.get_collection("users")

def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    user_collection.insert_one({'_id':username, 'email':email, 'password':password_hash})

if __name__ == '__main__':
    save_user('levo', 'levo@levo.com', 'levo')