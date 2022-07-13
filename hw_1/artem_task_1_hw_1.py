from typing import Any, Dict, List


def filter_by_first_met_value(dataset: List[Dict[str, Any]], keys: List[str]):
    """Filter dataset by first met value in keys"""

    # list of values of key in keys
    list_values: list = []
    # list of dicts with unique values
    result: list = []
    # this list help us to delete duplicate values
    used_values: list = []

    for element in dataset:
        # append all values of keys
        list_values.append([value for key, value in element.items() if key in keys])
        for i in list_values:
            # check our unique values in dataset dicts
            # and append in "used_values" - values that we add that add dict in  result
            if any(x in i for x in element.values()) and i not in used_values:
                result.append(element)
                used_values.append(i)

    return result


print(filter_by_first_met_value([
    {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
    {"name": "Serhii", "company": "Hillel", "job": "Python Trainer"},
    {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
    {"name": "Vlad", "company": "A-Level", "job": "Python Trainer"},
    {"name": "Serhii", "company": "A-Level", "job": "Python Trainer"},
], ["name", "job"]))
