def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], index]
        lookup[num] = index
    return []

print(two_sum([2, 7, 11, 15], 9))def group_anagrams(words: list[str]) -> list[list[str]]:
    cache = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in cache:
            cache[sorted_word] = []
        cache[sorted_word].append(word)
    return list(cache.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

def length_of_longest_substring(s: str) -> int:
    seen_chars = set()
    left = 0
    max_size = 0
    for right in range(len(s)):
        while s[right] in seen_chars:
            seen_chars.remove(s[left])
            left += 1
        seen_chars.add(s[right])
        max_size = max(max_size, right - left + 1)
    return max_size

print(length_of_longest_substring("abcabcbb"))
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = current
        if curr_start <= prev_end:
            merged[-1][1] = max(prev_end, curr_end)
        else:
            merged.append(current)
    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
def max_sub_array(nums: list[int]) -> int:
    max_current = nums[0]
    max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
