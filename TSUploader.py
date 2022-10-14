#!/usr/bin/env python3

from pymongo import MongoClient
import dateutil.parser
import csv
import time

header = [ "timestamp", "time_in_milliseconds", "price", "volume"]
csvfile = open('Prices.csv', 'r')
reader = csv.DictReader( csvfile )

client = MongoClient("mongodb+srv://USERNAME:PASSWORD@CLUSTER_URI")
db = client.prices
db.create_collection('ticks', timeseries={ 'timeField': 'timestamp', 'granularity': 'minutes' })

for each in reader:
    row={}
    for field in header:
        if field == "timestamp":
            row[field]=dateutil.parser.parse(each[field])
        elif field == "time_in_milliseconds":
            row[field]=int(each[field])
        else:
            row[field]=float(each[field])
    print (row)
    db.ticks.insert_one(row)
    time.sleep(60)