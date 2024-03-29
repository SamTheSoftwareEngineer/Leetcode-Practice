def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    1. Find the midpoint of the list and divide into sublists
    2. Recursively sort the sublist created in previous  step
    3. Merge the sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)