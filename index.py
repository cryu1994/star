def count_star(arr):
    print arr
    for int_count in arr:
       print "*" * int_count
#count_star([4, 6, 1, 3, 5, 7, 25])        

def countstar (arr):
    for int_count in arr:
        if isinstance(int_count, int):
            print "*" * int_count
        elif isinstance(int_count, str):
            char = len(int_count)
            letter = int_count[0].lower()
            print letter * char
countstar( [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])