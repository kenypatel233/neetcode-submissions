class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(list)
        n = len(nums)
        for i in nums:
            if i in result:
                result[i]+=1
            else:
                result[i]=1
        freq = [[] for i in range(n+1)]
        for numbr, count in result.items():
            freq[count].append(numbr)

        top_k = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                top_k.append(num)
                if len(top_k)==k:
                    return top_k