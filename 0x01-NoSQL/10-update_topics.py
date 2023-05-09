#!/usr/bin/env python3
"""changes all topic document based on the name"""

def update_topics(mongo_collection, name, topics):
    """
    name (string) will be the  to update
    topics (list of strings) will be the school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
