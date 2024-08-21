#!/usr/bin/env python3
"""
    Module that provide a Python function that lists all documents in
    a collection:
"""


def list_all(mongo_collection):
    """
        function list_all

        Argument:
            - mongo_collection: the pymongo collection object

        Return:
            - the documents found in the collection if collection
            is not empty else an empty list
    """
    doc_list = mongo_collection.find()
    if doc_list is None:
        return []
    else:
        return doc_list
