class Solution:
    def romanToInt(self, s: str) -> int:
        
        roum_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        total = 0
        previous_val = 0

        dumt = []

        

        for char in reversed(s):
            current_value = roum_map[char]

            if current_value < previous_val:
                total -= current_value
            else:
                total += current_value
                
            previous_val = current_value


        return total
                # break
        # return sum
        # print(previous_val)
        # print(total)
