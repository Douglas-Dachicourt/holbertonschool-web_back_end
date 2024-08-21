#!/usr/bin/env python3
"""
    Module with a function that inserts a new document in a collection
    based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
        function insert_school

        Arguments:
            - mongo_collection: mongo collection to work with
            - kwargs: key and values pairs to insert in the document

    """
    insert_doc = mongo_collection.insert_one(kwargs)
    return insert_doc.inserted_id
