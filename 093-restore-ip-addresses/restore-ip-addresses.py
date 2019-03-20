# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# Example:
#
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
#
#


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def dfs(s, groups, path):
            if groups == 4:
                if not s:
                    ans.append(path[:-1])
            else:
                for i in range(1,4):
                    if i <= len(s):
                        if i == 1:
                            dfs(s[i:], groups + 1, path + s[:i] + '.')
                        elif i == 2 and s[0] != '0':
                            dfs(s[i:], groups + 1, path + s[:i] + '.')
                        elif i == 3 and s[0] != '0' and int(s[:i]) < 256:
                            dfs(s[i:], groups + 1, path + s[:i] + '.')
        ans = []
        dfs(s, 0, '')
        return ans
            
