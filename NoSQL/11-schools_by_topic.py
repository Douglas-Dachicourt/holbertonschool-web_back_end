#!/usr/bin/env python3
"""
    Module that provide a function that returns the list of
    school having a specific topic

"""


def schools_by_topic(mongo_collection, topic):
    """
        function schools_by_topic

        Arguments:
            - mongo_collection: the mongo object to work with
            - topic: the list of languages to search in the
            collection

        Return:
             the list of school having a specific topic

    """
    result = mongo_collection.find({"topics": topic})
    return result
