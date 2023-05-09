#!/usr/bin/env python3
""" return students sorted by average score present"""

def top_students(mongo_collection):
    """
    The top must be ordered accordingly
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
