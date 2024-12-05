
# # def solve(n, x):
# #     count = 0
# #     for k in range(n):
# #         if (n ^ k) & x == 0:
# #             count += 1
# #     return count

# # print(solve(127, 6))
   


# # def find_starting_shop(n, candies, demands):
# #     total_candies = 0
# #     total_demands = 0
# #     current_balance = 0
# #     start_index = 0

# #     for i in range(n):
# #         total_candies += candies[i]
# #         total_demands += demands[i]
# #         current_balance += candies[i] - demands[i]

# #         # If balance is negative, reset start index and balance
# #         if current_balance < 0:
# #             start_index = i + 1
# #             current_balance = 0

# #     # If total candies are less than total demands, it's impossible
# #     if total_candies < total_demands:
# #         return -1
# #     return start_index



# # class Solution:
# #     def canCompleteCircuit(gas, cost) -> int:
# #         if sum(gas) < sum(cost):
# #             return -1
                
# #         curernt_gas = 0
# #         start = 0
# #         for i in range(len(gas)):
# #             curernt_gas += gas[i] - cost[i]
# #             if curernt_gas < 0:
# #                 curernt_gas = 0
# #                 start = i + 1

# #         return start



# # # Example usage
# # n = int(input("Enter the number of candy shops: "))
# # candies = list(map(int, input("Enter the candies at each shop: ").split()))
# # demands = list(map(int, input("Enter the demands at each shop: ").split()))
# # print(canCompleteCircuit(n, candies, demands))


# def min_speed_to_eat_all(arr, k):
#     # Helper function to calculate total hours required with a given speed T
#     def hours_needed(T):
#         hours = 0
#         for apples in arr:
#             hours += -(-apples // T)  # Equivalent to ceil(apples / T)
#         return hours

#     # Binary search for the minimum T
#     left, right = 1, max(arr)
#     while left < right:
#         mid = (left + right) // 2
#         if hours_needed(mid) <= k:
#             right = mid
#         else:
#             left = mid + 1
#     return left

# # Example usage
# n = int(input("Enter the size of the array: "))
# arr = [int(input()) for _ in range(n)]
# k = int(input("Enter the number of hours: "))
# print(min_speed_to_eat_all(arr, k))


import math
def minEatingSpeed(arr, k):
    def canEatAll(speed):
        hours = 0
        for apples in arr:
            # Math.ceil equivalent using integer division
            hours += math.ceil(apples + speed - 1) // speed
        return hours <= k

    left = 1
    right = max(arr)
    
    while left < right:
        mid = (left + right) // 2
        if canEatAll(mid):
            right = mid
        else:
            left = mid + 1
            
    return left


print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))












