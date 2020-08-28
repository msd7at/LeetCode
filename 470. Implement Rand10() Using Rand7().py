class Solution:
    def rand10(self):

        while True:

            random_num = ( rand7() - 1 ) * 7 + rand7()     
            if random_num <= 40:

                return random_num % 10 + 1
