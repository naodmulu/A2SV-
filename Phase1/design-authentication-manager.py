class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.timeSlot = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.timeSlot[tokenId] = currentTime + self.timeToLive
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.timeSlot:
            if self.timeSlot[tokenId] > currentTime:
                self.timeSlot[tokenId] = currentTime + self.timeToLive
            
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for key,value in self.timeSlot.items():
            if value > currentTime:
                count += 1
        
        return count

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)