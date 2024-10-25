package test

import "core:fmt"
print :: fmt.println

main :: proc() {

	my_list := [dynamic][dynamic]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	my_list2 := [dynamic][dynamic]int {
		{5, 1, 9, 11},
		{2, 4, 8, 10},
		{13, 3, 6, 7},
		{15, 14, 12, 16},
	}

	defer {
		for val in my_list {
			defer delete(val)
		}

		delete(my_list)

		for val in my_list2 {
			defer delete(val)
		}

		delete(my_list2)
	}

	rotate(my_list)
	rotate(my_list2)

	print(my_list) // [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
	print(my_list2) // [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

}

rotate :: proc(mat: [dynamic][dynamic]int) {
	local_array: [dynamic]int
	defer delete(local_array)

	for i in 0 ..< len(mat) {
		for val in mat[i] {
			append(&local_array, val)
		}
	}

	idx := 0
	for i := len(mat) - 1; i > -1; i -= 1 {
		for j in 0 ..< len(mat) {
			mat[j][i] = local_array[idx]
			idx += 1
		}
	}
}
