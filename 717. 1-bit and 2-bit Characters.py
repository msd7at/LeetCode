class Solution(object):
	def isOneBitCharacter(self, bits):
		i=0
		n=len(bits)
		while(i<n):
			if(bits[i]==1):
				i+=2
			else:
				if(i==n-1):
					return True
				i+=1
		return False
