# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        # hset = set(nums)
        # longest = 0
        # for n in hset:

        #     if (n-1) not in hset:
        #         length = 0
        #         while (n+length) in hset:
        #             length +=1
        #         longest = max(longest,length)
        # return longest




# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

        # longest = 0
        
        # seen = set(nums)
        # for i in seen :
        #     if (i-1) not in seen :
        #         length =0
        #         while (i+length) in seen :
        #             length += 1
        #         longest= max(longest, length)

        # return longest 





# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

#         longest = 0
#         seen = set(nums)

#         for n in seen :

#             if (n-1) not in seen :
#                 length = 0
#                 while (n+length) in seen :
#                     length += 1
#                 longest = max(longest,length)
#         return longest



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        maxL=0
        for n in seen:
            if (n-1) not in seen:
                length = 0
                while (n+length) in seen:
                    length += 1
                maxL=max(maxL,length)
        return maxL










































