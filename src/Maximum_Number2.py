class Solution:
	def mostWordsFound(self, sentences: List[str]) -> int:
		crr = 0
		max =0
		for sentence in sentences:
			crr = sentence.count(' ') + 1
			if max < crr:
				max = crr
		return max