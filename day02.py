# Code for the 2018 AoC, day 1
# https://adventofcode.com/2018/day/1
# Michael Bell
# 12/1/2018


def has_n_of_any_char(box_id, n=2):
    unique_chars = set(box_id)

    for uc in unique_chars:
        if box_id.count(uc) == n:
            return True
    return False


def checksum(box_ids):

    ids_w_n = lambda x: sum(
        1 if has_n_of_any_char(box_id, n=x) else 0 for box_id in box_ids
    )

    n_w_2 = ids_w_n(2)
    n_w_3 = ids_w_n(3)

    return n_w_2 * n_w_3


if __name__ == '__main__':

    test_ids = [
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabcdd',
        'abcdee',
        'ababab'  
    ]

    assert checksum(test_ids) == 12

    with open('./data/day02_input.txt', 'r') as f:
        input1 = f.readlines()
    
    print(f"Solution 1: {checksum(input1)}")