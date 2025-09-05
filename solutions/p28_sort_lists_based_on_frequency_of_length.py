# Sort a list of lists based their length frequency
# Lists with rare lengths are placed first, other with more frequent length come later

from collections import Counter

def sort_by_frequency_of_length_v1[T](lst: list[list[T]]) -> list[list[T]]:
    length_counts = Counter((len(sub_lst) for sub_lst in lst))
    return sorted(lst, key=lambda sub_lst: length_counts[len(sub_lst)])