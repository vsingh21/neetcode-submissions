class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = defaultdict(int)
        for c in s:
            freqs[c] += 1
        max_odd = 0
        min_even = len(s)
        for c, f in freqs.items():
            if f % 2 == 0 and f < min_even:
                min_even = f
            if f % 2 == 1 and f > max_odd:
                max_odd = f
        return max_odd - min_even
        
