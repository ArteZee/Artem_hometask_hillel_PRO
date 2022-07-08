from typing import Any, Dict, List


def filter_by_first_met_value(dataset: List[Dict[str, Any]], keys: List[str]):
    """Filter dataset by first met value in keys"""
    # set in list values of keys user
    user_values_of_key: list = []
    # list of dicts with unique values
    result: list = []
    for user_key in keys:
        for i in range(len(dataset)):
            # check value of user key in dateset and if we don`t have in result this dict - add to result
            # And add in users_value_of_key to compare with all values
            if dataset[i].get(user_key) in list(dataset[i].values()) \
                    and dataset[i].get(user_key) not in user_values_of_key:
                # add unique values
                user_values_of_key.extend(list(dataset[i].values()))
                # add unique dict
                result.append(dataset[i])
                return result


print(filter_by_first_met_value([
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
], ["foo", "bar"]))
