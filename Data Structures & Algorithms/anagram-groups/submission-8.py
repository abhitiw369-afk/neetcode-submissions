# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # res = defaultdict(list)

        
        
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c)-ord('a')] +=1  #a->0,b->1,...z->25
                

        #     res[tuple(count)].append(s)

        # return list(res.values())

        # hmap = defaultdict(list)

        # for s in strs:
        #     count = [0]*26

        #     for c in s:
        #         count[ord(c)-ord("a")] += 1

        #     hmap[tuple(count)].append(s)  #dict[key].append(value)

        # return list(hmap.values())

        # seen = {}

        # for s in strs:
        #     key = "".join(sorted(s))

        #     if key not in seen:
        #         seen[key] = []

        #     seen[key].append(s)

        # return list(seen.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}

        for s in strs :
            
            key = " ".join(sorted(s))
            if key not in seen :
                seen[key] = []
            
            seen[key].append(s)

        return list(seen.values())




































