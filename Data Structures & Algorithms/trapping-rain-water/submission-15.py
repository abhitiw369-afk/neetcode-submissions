# class Solution:
#     def trap(self, height: List[int]) -> int:
        # area = 0
        # l, r =0, len(height)-1
        # leftMax = height[l]
        # rightMax = height[r]

        # while l < r:
        #     if leftMax < rightMax:
        #         l += 1
        #         leftMax = max(leftMax, height[l])
        #         area += leftMax - height[l]
        #     else:
        #         r -= 1
        #         rightMax = max(rightMax, height[r])
        #         area += rightMax - height[r]    
        # return area

# class Solution:
#     def trap(self, height: List[int]) -> int:

        # maxarea = 0
        # l = 0
        # r = len(height)-1
        # maxL = height[l]
        # maxR = height[r]
        # while l < r :
        #     if maxL < maxR :
        #         l+=1
        #         maxL = max(maxL,height[l])
        #         maxarea += maxL-height[l]
        #     else :
        #         r-=1
        #         maxR=max(maxR,height[r])
        #         maxarea += maxR-height[r]

        # return maxarea

        # totalarea = 0
        # l = 0
        # r = len(height)-1
        # maxL = height[l]
        # maxR = height[r]
        # while l < r :
        #     if maxL < maxR :
        #         l += 1
        #         maxL = max(maxL,height[l]) 
        #         totalarea += maxL - height[l]
                
        #     else :
        #         r -= 1
        #         maxR = max(maxR,height[r]) 
        #         totalarea += maxR - height[r]
                
        # return totalarea




# class Solution:
#     def trap(self, height: List[int]) -> int:
#         totalarea = 0
#         l = 0
#         maxl=height[l]
#         r = len(height)-1
#         maxr = height[r]
#         while l < r :

#             if maxl < maxr :
#                 l += 1
#                 maxl = max(maxl,height[l])
                
#                 totalarea += maxl - height[l] 
            
#             else :
#                 r -= 1
#                 maxr = max(maxr, height[r])
                
#                 totalarea += maxr - height[r]

#         return totalarea



class Solution:
    def trap(self, ht: List[int]) -> int:

        area=0
        l,r=0,len(ht)-1
        maxL,maxR=ht[l],ht[r]
        while l<r:

            if maxL<maxR:
                l+=1
                maxL=max(maxL,ht[l])
                area+=maxL-ht[l]
            else:
                r-=1
                maxR=max(maxR,ht[r])
                area+=maxR-ht[r]

        return area
        


            

































