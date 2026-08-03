/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let count = 0;
    let maxi = 0;
    const n = nums.length;
    for(let i=0; i<n;i++){
        if (nums[i]==1){
            count = count+1;
        }
        else{
            count=0;
        }
        if (count>maxi){
            maxi=count;
        }

    }
    return maxi;

};