/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let l=0;
    const n = nums.length;
    for (let r=0;r<n;r++){
        if(nums[r] !== 0){
            ;[nums[r],nums[l]]=[nums[l],nums[r]];
            l=l+1;
        }
    }
    return nums;
    
};