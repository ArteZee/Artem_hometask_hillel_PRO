from typing import List


def find_uniq(dataset: List[int]) -> int:
    """
    function get unique number of list
    """
    # create unique number in set
    unique_number = set(dataset)
    # count how many number in massive


    # search repeating number
    for number_element in unique_number:
        # count how many number in massive
        counter_number = 0
        for element in dataset:
            # if nuber in list counter increase 1
            if number_element == element:
                counter_number += 1
        # if counter = 1 - number is  unique
        if counter_number == 1:
            return number_element



def find_uniq_2(dataset: List[int]) -> int:
    """
        function get unique number of list
    """
    # sorted our massive
    sort_num = sorted(dataset)

    # this cycle five unique number
    for i in range(len(sort_num)):
        # if this first numer in massive compare with second
        if i == 0:
            if sort_num[i] != sort_num[i + 1]:
                return sort_num[i]
        #  if it is  last number compare with penultimate number
        elif i == len(sort_num) - 1:
            if sort_num[i] != sort_num[i - 1]:
                return sort_num[i]
        # for other compare with adjacent numbers
        else:
            if sort_num[i] == sort_num[i - 1] or sort_num[i] == sort_num[i + 1]:
                continue
            else:
                return sort_num[i]

if __name__ == "__main__":
    print(find_uniq([54, 90, 52, 10, 62, 54, 90, 52, 10, 62, 42]))
    print(find_uniq_2([1, 2, 3, 2, 1]))






