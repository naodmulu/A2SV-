class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total = 0
        prefix = [0]
        for customer in customers:
            if customer == "Y":
                total += 1
            prefix.append(total)
        penalty = total
        time = 0
        occur = 0
        for i in range(len(customers)):
            if customers[i] == "N":
                occur += 1
            if total-prefix[i+1]+occur < penalty:
                time = i+1
                penalty = total-prefix[i+1]+occur

        return time
            
