class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        prefix_product_array = []
        for i in range(len(nums)):
            if i == 0:
                prefix_product_array.append(1)
                prefix_product *= nums[i]
            else:
                prefix_product_array.append(prefix_product)
                prefix_product *= nums[i]
        
        suffix_product = 1
        suffix_product_array = []
        for j in range(len(prefix_product_array)-1, -1, -1):
            if j == len(prefix_product_array) - 1:
                prefix_product_array[j] *= 1
                suffix_product *= nums[j]
            else:
                prefix_product_array[j] *= suffix_product
                suffix_product *= nums[j]

        return prefix_product_array
            
            