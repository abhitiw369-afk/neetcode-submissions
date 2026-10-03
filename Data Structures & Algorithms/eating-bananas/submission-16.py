# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         l, r = 1, max(piles)
#         res = float('inf')

#         while l <= r :
#             k = (l+r)//2
#             hrs = 0

#             for p in piles :
#                 hrs += math.ceil(p/k)

#             if hrs <= h :
#                 res = min(res,k)
#                 r = k - 1
#             else :
#                 l = k + 1
#         return res
            


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=max(piles)
        while l<=r:
            k=(l+r)//2
            
            hr=0

            for p in piles:
                hr+=math.ceil(p/k)

            if hr <= h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res










class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK=float("INF")
        l,r=1,max(piles)
        while l<=r:
            k=(l+r)//2
            hrs=0
            for i in range(len(piles)):
                hrs+=math.ceil(piles[i]/k)

            if hrs<=h: 
                minK=min(minK,k)
                r=k-1
            else: #hrs>h, increment rate(k)
                l=k+1
        return minK























