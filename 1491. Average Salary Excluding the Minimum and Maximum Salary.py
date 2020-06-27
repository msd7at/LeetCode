#link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        l=len(salary)
        s=sum(salary)
        su=salary[0]+salary[l-1]
        return ((s-su)/(l-2))
