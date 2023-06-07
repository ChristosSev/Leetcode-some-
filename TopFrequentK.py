import heapq
from collections import Counter

def topKFrequent(nums, k):
    # Step 1: Create dictionary to store frequency counts
    freq_count = Counter(nums)

    # Step 2: Create priority queue (heap)
    heap = []

    # Step 3: Push elements into heap using frequency count as sorting key
    for num, freq in freq_count.items():
        heapq.heappush(heap, (freq, num))

        # Step 4: If heap size exceeds k, pop the smallest element
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 5: Create result list by popping elements from heap
    result = [num for freq, num in heap]
    # Step 6: Reverse the result list for descending order of frequency
    return result[::-1]
