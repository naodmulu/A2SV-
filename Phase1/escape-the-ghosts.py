class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
    
        pacman_dis = abs(target[0]) + abs(target[1]) 

        for g in ghosts:
            ghost_dis = abs(target[0] - g[0]) + abs(target[1] - g[1]) 
            
            if ghost_dis <= pacman_dis:
                return False

        return True
