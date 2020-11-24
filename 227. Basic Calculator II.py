class Solution:
	def calculate(self, s: str) -> int:
		stack=[]        
		tem=0
		sign='+'
		for i in range(len(s)):
			if s[i].isdigit():
				tem=tem*10+int(s[i])
			if s[i] in '+-*/' or i==len(s)-1:
				if sign=='+':
					stack.append(tem)
				if sign=='-':
					stack.append(-tem)
				if sign=='*':
					tem2=stack.pop()*tem
					stack.append(tem2)
				if sign=='/':
					a=stack.pop()
					if a>=0:
						tem2=a//tem
					else:
						tem2=-((-a)//tem)
					stack.append(tem2)
				tem=0
				sign=s[i]
		return sum(stack)
