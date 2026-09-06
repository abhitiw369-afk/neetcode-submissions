# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()

        # for n in nums:
        #     if n in seen:
        #         return True
        #     seen.add(n)
        # return False

        # seen = set()
        # for r in nums :
        #     if r in seen:
        #         return True
        #     seen.add(r)
        # return False


        # seen = set()
        # for r in range(len(nums)) :
        #     if nums[r] in seen :
        #         return True
        #     seen.add(nums[r])
        # return False


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return True
        return False
        























