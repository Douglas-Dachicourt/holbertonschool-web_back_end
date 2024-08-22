#!/usr/bin/env python3
"""
    Module with a function that changes all topics of a school document
    based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
        function update_topics

        Arguments:
            - mongo_collection: mongo collection to work with
            - name: name (string) will be the school name to update
            - topics: topics (list of strings) will be the list of topics
            approached in the school

    """

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
