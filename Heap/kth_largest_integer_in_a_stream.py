# https://neetcode.io/problems/kth-largest-integer-in-a-stream

# Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
# Implement the following methods:
#     constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
#     int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
   
# Input:
# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
# Output:
# [null, 3, 3, 3, 5, 6]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        # A min-heap requires that the parent be less than or equal to its children
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
