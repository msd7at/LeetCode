def LTA(m, n, o):
	ar = abs(((m[0]-o[0])*(n[1]-m[1])) - ((m[0] - n[0])*(o[1] - m[1])))
	return 0.5*ar
class Solution:
	def largestTriangleArea(self, points: List[List[int]]) -> float:
		maxarea = 0
		for i in range(len(points)-2):
			for j in range(i+1, len(points)-1):
				for k in range(j+1, len(points)):
					area = LTA(points[i], points[j], points[k])
					if area>maxarea:
						maxarea = area
		return maxarea
