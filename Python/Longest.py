def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=j=0
        hs=set()
        for j in range(len(s)):
            while s[j] in hs:
                hs.remove(s[i])
                i+=1
            hs.add(s[j])
            maxLen=max(maxLen, len(hs))
        return maxLen