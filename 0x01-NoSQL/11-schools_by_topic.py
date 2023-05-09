#!/usr/bin/env python3
"""it returns the list of schools having a specific topic:"""

def schools_by_topic(mongo_collection, topic):
    """
    topic (string) will be topic se
    """
    return mongo_collection.find({"topics": topic})
