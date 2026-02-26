class Solution(object):
    def addBinary(self, a, b):
        max_length = max(len(a),len(b))
        sum = []
        carry = 0
        for i in range(max_length-1, -1 ,-1):
            if ((int(a[i])==1) and (int(b[i])==1)):
                if carry:
                    sum[-1] = 1
                    carry = 1
                else:
                    sum[-1] = 0
                    carry = 1                
            elif ((int(a[i])==1) and (int(b[i])==0)) or ((int(a[i])==0) and (int(b[i])==1)):
                if carry:
                    sum[-1] = 0
                    carry = 1
                else:
                    sum[-1] = 1
                    carry = 0
            elif (int(a[i])==0) and (int(b[i])==0):
                if carry:
                    sum[-1] =  1
                    carry = 0
                else:     
                    sum[-1] = 0
                    carry = 0  
                    
        return sum
        
solution = Solution()
print(solution.addBinary(bin(55)[2:],bin(5)[2:]))


