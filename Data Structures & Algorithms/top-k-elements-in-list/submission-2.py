class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [set() for i in range(len(nums))]
        num_freq = {}
        for n in nums:
            if n in num_freq:
                curr_freq = num_freq[n]
                freq[curr_freq].remove(n)
                freq[curr_freq + 1].add(n)
                num_freq[n] += 1
            else:
                freq[0].add(n)
                num_freq[n] = 0
        res = [0] * k 
        k -= 1
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                if k < 0:
                    return res
                res[k] = n
                k -= 1
        return res
