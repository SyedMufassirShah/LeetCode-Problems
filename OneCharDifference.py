class Solution: 
    def bestMatch(self, arr, word):
        matchedWords = {
            "matchedArr" : [],
        }
        # print(arr, word)
        for i in range(len(arr)):
            counter = 0
            if len(word) == len(arr[i]):
                for j in range(len(word)):
                    if word[j] != arr[i][j]:
                        counter+= 1
                        if counter <= 1:
                            # print(f"{word} = {arr[i]}")
                            matchedWords["matchedArr"].append({"word" : arr[i], "wordLength" : len(arr[i])})
        
        return matchedWords
            



solution = Solution()
myArr = ["abple", 'nana', 'nano', 'bapana', 'banapa', 'panaba']
myWord = "banana"
obj = solution.bestMatch(myArr, myWord)    
for i in obj["matchedArr"]:
    print(f"Word: {i['word']}")
    
