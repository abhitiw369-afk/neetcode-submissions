class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
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
        #     for n in freq[i]: #value at frequncy
        #         res.append(n) #add value to the list
        #         if len(res) == k: #checking if list got top k elements
        #             return res

        hmap = {} #empty hash map for storing value : frequency

        farr = [[] for i in range(len(nums)+1)] #for each index in list there is a sub list

        for i in nums:
            hmap[i] = 1 + hmap.get(i,0) #val and there freq in hashmap

        for val, freq in hmap.items(): #.items is used to get key and value pair same time
            farr[freq].append(val) #as we've to store freq at valued index

        #as we've to return in a for of list
        res = []  #empty list

        for i in range(len(farr)-1,0,-1):
            for n in farr[i]:
                res.append(n)
                if len(res)==k:
                    return res








































