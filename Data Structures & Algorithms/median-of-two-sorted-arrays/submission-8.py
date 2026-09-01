class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A,B = nums1, nums2
        total = len(A)+len(B)
        half = total//2

        if len(A)>len(B) :
            A, B=B, A
        
        l, r = 0, len(A)-1
        while True: #not l<=r bcz: in this problem, the correct partition may require: l = 0, r = -1,(for example when A is empty).
            midA = (l+r)//2
            midB = half - midA - 2 

            Aleft = A[midA] if midA >= 0 else float('-inf')
            Aright = A[midA + 1] if (midA+1) < len(A) else float('inf')
            Bleft = B[midB] if midB >= 0 else float('-inf')
            Bright = B[midB + 1] if (midB+1) < len(B) else float('inf')

            # is partitioning correct??
            if Aleft <= Bright and Bleft <= Aright :

                # if we have odd nos in total
                if total%2: #total%2 is True, i.e 1
                    return min(Aright,Bright)
                # if we have even nos in total
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft > Bright :
                r = midA - 1
            else :
                l = midA + 1
        













class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        total=len(A)+len(B)
        half=total//2
        
        if len(A)>len(B):
            A,B=B,A #as we process on smaller of A,B. so let's A be shorter
        l,r=0,len(A)-1

        while True:
        #instead of l<=r,True bcz A can be empty too,so to handle each edge case
        #We use while True because a valid partition is guaranteed to exist.
        #This also naturally handles cases where A is empty.
            midA=(l+r)//2
            midB=half-midA-2
            #why(-2)? bcz both A,B starts from 0th indx

            #setup for normal and edge cases
            Aleft=A[midA] if midA>=0 else float("-inf")
            Bleft=B[midB] if midB>=0 else float("-inf")
            Aright=A[midA+1] if (midA+1) < len(A) else float("inf")
            Bright=B[midB+1] if (midB+1) < len(B) else float("inf")

            #now check is our partition is correct or not?
            if Aleft <= Bright and Bleft<=Aright:

                #if partioning is correct we've to compute median
                #if total is odd
                if total%2 : #total%2==1,i.e True
                    return min(Aright,Bright)
                else: #if total is even
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Bleft>Aright: #and Aleft<=Bright
                l=midA+1
            else: #Aleft>Bright and Bleft<Aright
                r=midA-1




























        