func isAnagram(s string, t string) bool {
	if len([]rune(s)) != len([]rune(t)) {
		return false
	}

	count := make(map[rune]int)

	for _, ch := range s {
		count[ch]++
	}

	for _, ch := range t {
		count[ch]--

		if count[ch] < 0 {
			return false
		}
	}

	return true
}
