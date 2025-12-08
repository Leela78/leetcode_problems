# 3Sum

## Difficulty
Medium

## Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1:
- **Input:** `nums = [-1,0,1,2,-1,-4]`
- **Output:** `[[-1,-1,2],[-1,0,1]]`
- **Explanation:** The triplets that sum to zero are [-1,-1,2] and [-1,0,1]

### Example 2:
- **Input:** `nums = [0]`
- **Output:** `[]`

### Example 3:
- **Input:** `nums = [-2,0,1,1,2]`
- **Output:** `[[-2,0,2],[-2,1,1]]`

## Constraints
- `0 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`
