class TimeMap:

    def __init__(self):
        self.keyMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyMap.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyMap:
            return ""
        arr = self.keyMap[key]
        res = ""
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res 
        
