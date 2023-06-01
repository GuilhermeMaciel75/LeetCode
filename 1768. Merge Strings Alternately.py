class Solution:
    def reverseVowels(self, s: str) -> str:
        listidx = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for x in range(len(s)):
            if s[x] in vowels:
                listidx.append(x)

        s = list(s)
        
        for _ in range(len(listidx)//2):
            firstChar = listidx.pop(0)
            lastChar = listidx.pop(-1)

            s[firstChar], s[lastChar] = s[lastChar],  s[firstChar]

        return ''.join(s)