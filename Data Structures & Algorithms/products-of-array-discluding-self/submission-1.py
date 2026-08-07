class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product_total = 1
        prefix_product = []
        for i in range(len(nums)):
            prefix_product_total *= nums[i]
            prefix_product.append(prefix_product_total)
        
        suffix_product = []
        suffix_product_total = 1
        for k in range(len(nums) - 1, -1, -1):
            suffix_product_total *= nums[k]
            suffix_product.append(suffix_product_total)
        suffix_product.reverse()

        for j in range(len(nums)):
            if j == 0:
                nums[j] = suffix_product[j+1]
            elif j == len(nums) - 1:
                nums[j] = prefix_product[j-1]
            else:
                nums[j] = prefix_product[j-1] * suffix_product[j+1]
        
        return nums