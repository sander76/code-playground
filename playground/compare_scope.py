a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def find_dups_scoped(my_list: list[int]):
    matches = []
    for i_left in range(len(my_list)):
        left = my_list[i_left]
        for i_right in range(i_left):
            right = my_list[i_right]
            print(f"comparing {left} with {right}")


find_dups_scoped(a)
