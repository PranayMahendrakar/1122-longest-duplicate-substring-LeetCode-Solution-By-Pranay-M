class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        MOD = 2**63 - 1
        base = 31
        
        def check(length):
            if length == 0:
                return -1
            
            h = 0
            for i in range(length):
                h = (h * base + ord(s[i])) % MOD
            
            seen = {h: 0}
            base_pow = pow(base, length, MOD)
            
            for i in range(1, n - length + 1):
                h = (h * base - ord(s[i-1]) * base_pow + ord(s[i+length-1])) % MOD
                
                if h in seen:
                    return i
                seen[h] = i
            
            return -1
        
        left, right = 1, n - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            idx = check(mid)
            if idx != -1:
                result = s[idx:idx+mid]
                left = mid + 1
            else:
                right = mid - 1
        
        return result