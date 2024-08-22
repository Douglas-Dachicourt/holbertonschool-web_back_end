#!/usr/bin/env python3
"""
    This module gives a script that provides some stats about Nginx logs
    stored in MongoDB

"""
from pymongo import MongoClient
"""
    import pymongo

"""

if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client["logs"]
    collection = db["nginx"]

    num_logs = collection.count_documents({})
    print("{} {}".format(num_logs, "logs"))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count_methods = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count_methods}")

    status_check_count = collection.count_documents({"method":
                                                     "GET", "path":
                                                     "/status"})
    print(f"{status_check_count} status check")
