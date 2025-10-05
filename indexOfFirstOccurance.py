class Solution:
    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle
        
    
    def index_checker(self):
        parentString = str(self.haystack)
        childString = str(self.needle)
        
        index = [ parentString.index(childString) if childString in parentString else -1]
        return index[0]
    
        
    
        

solution = Solution("Mufassir", "sir")

print(solution.index_checker())

