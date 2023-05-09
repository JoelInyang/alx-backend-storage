#!/usr/bin/env python3
"""lists all documents present"""

def list_all(mongo_collection):
    """
    empty list if no doc found    """
    return mongo_collection.find()
