class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new = -1
        for i in range(len(arr)-1, -1, -1): 
                
                newMax = max(new,arr[i])
                arr[i] = new
                new = newMax

                
            
                

        return arr
            
        