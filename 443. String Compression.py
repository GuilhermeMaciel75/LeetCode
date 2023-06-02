class Solution:
    def compress(self, chars: List[str]) -> int:
        char = ''
        count = 1

        if len(chars) == 1:
            return 1

        else:
            for c in range(len(chars) -1):
                if chars[c+1] == chars[c]: #Se o próximo for igual ao atual
                    count += 1
                else:
                    if count == 1:
                        char += chars[c]

                    else:
                        char += chars[c] + str(count)
                        count = 1

        if count == 1:
            char += chars[c+1]

        else:
            char += chars[c] + str(count)

        chars.clear()
        for c in char:
            chars.append(c)

        return len(char)