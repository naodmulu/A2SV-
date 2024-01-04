class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        num = skill[0]+skill[-1]
        ans = 0
        for i in range(len(skill)//2):
            if skill[i]+skill[len(skill)-1-i] != num:
                return -1
            ans += skill[i]*skill[len(skill)-1-i]
        return ans
