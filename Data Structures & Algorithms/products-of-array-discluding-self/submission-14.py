# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]

        #     res[i] = prod
        # return res


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         res = [1]*len(nums)
#         pre = 1
#         for i in range(len(nums)) :
#             res[i] = pre
#             pre *= nums[i]

#         post = 1
#         for i in range(len(nums)-1,-1,-1) :
#             res[i] *= post
#             post *= nums[i]

#         return res



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]*len(nums)

        pre=1
        for i in range(len(nums)):
                res[i]=pre
                pre*=nums[i]

        post=1
        for i in range(len(nums)-1,-1,-1):
                res[i]*=post
                post*=nums[i]

        return res

        
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        #L2R traversal
        pre=1
        for i in range(len(nums)):
                res[i]=pre
                pre*=nums[i]
        #R2L traversal
        post=1
        for i in range(len(nums)-1,-1,-1): #excluding 0th idx
                res[i]*=post
                post*=nums[i]
        return res        


















