class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=0;mid=0;high=len(nums)-1
        while(mid<=high):
            if(nums[mid]==0):
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1;low+=1
            elif(nums[mid]==2):
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
            else:
                mid+=1
                