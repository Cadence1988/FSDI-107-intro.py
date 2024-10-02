import pymongo
import certifi
con_str="mongodb+srv://test:FSDIflask@cluster0.glkph.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_str, tlsCAfile=certifi.where())
db=client.get_database("tacoburger")