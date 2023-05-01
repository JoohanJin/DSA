/*
Two Sum Problem from Leetcode
source: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/
// Two pointers method
// Time Complexity: O(n^2)
// Space Complexity: O(1)

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++){
            for (int j = i + 1; j < nums.size(); j++){
                if (nums[i] + nums[j] == target){
                    return {i, j};
                }
            }
        }
        return {};
    }
};

int main(){
    vector<vector<int>> nums = {
                                {2,7,11,15},
                                {3,2,4},
                                {3,3}
                                };
    int targets[3] = {9, 6, 6};
    Solution a;
    for (int i = 0; i < 3; i++){
        vector<int> ans = a.twoSum(nums[i], targets[i]);
        for (int j = 0; j < 2; j++){
            if (j == 0){
                cout << ans[j] << ", ";
            }
            else {
                cout << ans[j] << "\n";
            }
        }
    }
    
    
    return 0;
}