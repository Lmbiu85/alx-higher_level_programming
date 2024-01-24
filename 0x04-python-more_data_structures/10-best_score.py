#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        best_score = max(a_dictionary.values())
        best_key = None
        for key, value in a_dictionary.items():
            if value == best_score:
                best_key = key
        return best_key
