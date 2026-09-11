class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        res = 2
        l, r = 0, 1
        freq = {fruits[l]: 1, fruits[r]: 1}
        c = 1 if fruits[l] == fruits[r] else 2
        while r < len(fruits) - 1:
            print(l, r)
            nf = fruits[r + 1]
            if nf in freq and freq[nf] > 0:
                freq[nf] += 1
                res = max(res, r - l + 1)
                r += 1
                continue
            if c == 1:
                freq[nf] = freq.get(nf, 0) + 1
                res = max(res, r - l + 1)
                r += 1
                c = 2
                continue
            of = fruits[r]
            tmp = r
            while fruits[tmp] == of:
                tmp -= 1
            freq.pop(fruits[tmp])
            freq[nf] = 1
            l = tmp + 1
            r += 1
        return res + 1

            
            

