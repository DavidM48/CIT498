import pymongo
import json

client = pymongo.MongoClient('')
db = client.moveLog_db
col = db.movelog
with open('1588563158658.json') as f:
    file_data = json.load(f)
col.insert_one(file_data)
f.close()
client.close()

