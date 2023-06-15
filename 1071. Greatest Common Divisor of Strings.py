class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        word = ""
        lastWord = ""
        size1 = len(str1)
        size2 = len(str2)

        for i in range(len(min(str1, str2))):
            if str1[i] != str2[i]:
                break

            word += str1[i]
            
            it = i + 1
            
            if size1 % it == 0 and size2 % it ==0:
                if (size1 // it) * word == str1 and (size2 // it) * word == str2:
                    lastWord = word
        return lastWord