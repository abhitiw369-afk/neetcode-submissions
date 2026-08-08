# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count = {} #hash map for storing number with thier frequencies, in dict format

        # freq = [[] for i in range(len(nums)+1)]   
        # #here: [[],[],[],[],[],[],[]]
        #     #    0   1  2  3  4  5  6
        
        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
            
        #     """count = {    1:3,
        #                     2:2,
        #                     3:1}"""


        # for n , c in count.items():
        #     freq[c].append(n)
        # #here: [[],[3],[2],[1],[],[],[]]
        #     #    0   1  2  3  4  5  6
        # res = []

        # for i in range(len(freq)-1,0,-1): #from largest index/frequency to smallest
        #     for n in freq[i]: #values at frequncy, as there can be many values at same freq
        #         res.append(n) #add value to the list
        #         if len(res) == k: #checking if list got top k elements
        #             return res

        # hmap = {}
        # farr = [[] for i in range(len(nums)+1)]

        # for n in nums:
        #     hmap[n] = 1 + hmap.get(n,0)

        # for val,freq in hmap.items():
        #     farr[freq].append(val)

        # res = []

        # for i in range(len(farr)-1,0,-1):
        #     for n in farr[i]:
        #         res.append(n)
        #         if len(res)==k:
        #             return res


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         seen = {}
#         freqq = [[] for i in range(len(nums)+1)]
#         res = []
#         for r in nums :
#             seen[r] = 1 + seen.get(r, 0)

#         for val, freq in seen.items() :
#             freqq[freq].append(val)

#         for i in range(len(freqq)-1,0,-1) :
#             for n in freqq[i] :
#                 res.append(n)
#                 if len(res) == k :
#                     return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = [[] for i in range(len(nums)+1)]
        op = []
        seen = {}
        for i in nums :
            seen[i] = 1 + seen.get(i, 0)

        for val, freq in seen.items() :
            res[freq].append(val)
        
        for i in range(len(res)-1,0,-1) :
            for j in res[i] :
                op.append(j)
                if len(op) == k :
                    return op




































