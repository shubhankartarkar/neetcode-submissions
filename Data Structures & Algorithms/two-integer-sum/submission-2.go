func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)

	for idx, num := range nums {

		diff := target - num

		i, exist := seen[diff]

		if exist {
			return []int{i, idx}
		}

		seen[num] = idx
	}
	return nil
}
