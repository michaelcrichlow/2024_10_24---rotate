def rotate(matrix: list[list[int]]) -> None:
    local_array = []
    for i in range(len(matrix)):
        for val in matrix[i]:
            local_array.append(val)

    idx = 0
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(0, len(matrix)):
            matrix[j][i] = local_array[idx]
            idx += 1


def main() -> None:
    my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(my_list)
    assert (my_list == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    my_list2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(my_list2)
    assert (my_list2 == [[15, 13, 2, 5], [14, 3, 4, 1],
            [12, 6, 8, 9], [16, 7, 10, 11]])

    print("all tests passed!")


if __name__ == '__main__':
    main()

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
