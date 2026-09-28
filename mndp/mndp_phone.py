# A class is a blueprint (the "cookie cutter"). LeetCode requires this wrapper.
class Solution:
    def maxDepth (self, s: str) -> int:
        depth = best = 0
        
        for ch in s:
            if ch == "(":
                depth += 1
                best = max(best, depth)
            elif ch == ")":
                depth -= 1
        return best 
                
# True only when this file is run directly (python3 mndp_phone.py).
# On `import mndp_phone` it is False, so these checks stay quiet.
if __name__ == "__main__":
    # assert = "this better be true, or crash loudly".
    assert Solution().maxDepth("(1+(2*3)+((8)/4))+1") == 3  # example 1
    assert Solution().maxDepth("(1)+((2))+(((3)))") == 3  # example 2
    assert Solution().maxDepth("()(())((()()))") == 3  # example 3
    assert Solution().maxDepth("1+(2*3)/(2-1)") == 1  # never nested
    assert Solution().maxDepth("1") == 0  # no parens at all
    print("ok")
