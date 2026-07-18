class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} #hash map for storing number with thier frequencies, in dict format

        freq = [[] for i in range(len(nums)+1)]  
        #here: [[],[],[],[],[],[],[]]
            #    0   1  2  3  4  5  6
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
            
            """count = {    1:3,
                            2:2,
                            3:1}"""


        for n , c in count.items():
            freq[c].append(n)
        #here: [[],[3],[2],[1],[],[],[]]
            #    0   1  2  3  4  5  6
        res = []

        for i in range(len(freq)-1,0,-1): #from largest index/frequency to smallest
            for n in freq[i]: #value at frequncy
                res.append(n) #add value to the list
                if len(res) == k: #checking if list got top k elements
                    return res

