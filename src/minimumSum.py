class Solution:
	def minimumSum(self, num: int) -> int:
		#	in ascending order, [0][2] + [1][3] is always the smallest
		new_list = sorted(list(str(num)))
		new1 = int(new_list[0]) * 10 + int(new_list[2])
		new2 = int(new_list[1]) * 10 + int(new_list[3]])
		return new1 + new2
			 	
			 	
			