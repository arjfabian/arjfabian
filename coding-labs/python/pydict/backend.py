import json
from difflib import get_close_matches


SOURCE_DICT='data.json'
CLOSE_MATCHES_MAX_ENTRIES = 5
CLOSE_MATCHES_CUTOFF_SCORE = 0.6

def search_in_dictionary(query):
    data = json.load(open(SOURCE_DICT))
    query = query.lower()
    if query in data:
        return ["d"] + data[query]
    else:
        query = query.upper()
        if query in data:
            return ["d"] + data[query]
        else:
            possible = get_close_matches(query, data.keys(), n=CLOSE_MATCHES_MAX_ENTRIES, cutoff=CLOSE_MATCHES_CUTOFF_SCORE)
    return ["p"] + possible
