import pymongo
import json

client = pymongo.MongoClient('mongodb://cit498:cit498cube@docdb-2020-04-14-19-15-16.cluster-c7jggitb6poy.us-east-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client.moveLog_db
col = db.movelog
with open('1588563158658.json') as f:
    file_data = json.load(f)
col.insert_one(file_data)
f.close()
client.close()

