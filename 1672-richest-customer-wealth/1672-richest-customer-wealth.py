class Solution(object):
    def maximumWealth(self, accounts):
        maxi=0
        for account in accounts:
            suma=sum(account)
            maxi=max(suma,maxi)
        return maxi


        