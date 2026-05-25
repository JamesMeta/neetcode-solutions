class Solution:
    def romanToInt(self, s: str) -> int:

        numeral_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        sum_stack = []
        

        for numeral in s:

            current = numeral_dict[numeral]

            if (len(sum_stack) > 0):
                
                while sum_stack[-1] < current:
                    prev = sum_stack.pop()
                    current -= prev

                    if (len(sum_stack) == 0):
                        break
            
            sum_stack.append(current)

        return sum(sum_stack)



        