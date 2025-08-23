# 39. Combination Sum - Dynamic Programming Approach return all unique combinations of candidates that sum to target
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # sorting helps keep combinations in non-decreasing order
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  # one way to make 0: the empty list

        for c in candidates:
            for t in range(c, target + 1):
                for comb in dp[t - c]:
                    # ensure non-decreasing order to avoid duplicates
                    if not comb or c >= comb[-1]:
                        dp[t].append(comb + [c])

        return dp[target]
