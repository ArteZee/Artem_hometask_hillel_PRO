from typing import Any, Dict, List


def filter_by_first_met_value(dataset: List[Dict[str, Any]], keys: List[str]):
    """Filter dataset by first met value in keys"""


    # list of dicts with unique values
    result: list = []
    # add dict to result if dict have key in keys
    for element in dataset:
        result = [element for key, value in element.items() if key in keys]
    return result

print(filter_by_first_met_value([
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
], ["foobar"]))
