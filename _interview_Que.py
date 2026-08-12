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

class UserProfile:
    def __init__(self, user_id: int, username: str, role: str):
        self.user_id = user_id
        self.username = username
        self.role = role

def fetch_user_role(user: UserProfile) -> str:
    if user.role == "admin":
        return "Access level: Full Console Access"
    return "Access level: Limited Viewer Access"

print(fetch_user_role(UserProfile(101, "sarthak_dev", "admin")))


from typing import TypeVar, Generic, Union

T = TypeVar('T')

class APIResponse(Generic[T]):
    def __init__(self, status: str, data: T, code: int):
        self.status = status
        self.data = data
        self.code = code

def handle_api_response(response: APIResponse[T]) -> Union[T, str]:
    if response.code == 200:
        return response.data
    return "Error: System failed to fetch records."

print(handle_api_response(APIResponse("success", ["item1", "item2"], 200)))


class OperationalConfig:
    def __init__(self, api_key: str, endpoints: list[str], timeout: int = None):
        self._api_key = api_key
        self.endpoints = endpoints
        self.timeout = timeout

def initialize_system(config: OperationalConfig) -> str:
    time_limit = config.timeout if config.timeout is not None else 30
    return f"System loaded with API key reference using {time_limit}s fallback delay."

print(initialize_system(OperationalConfig("secret_abc123", ["/v1/status"])))


def render_network_ui(state: dict) -> str:
    status = state.get("status")
    if status == "success":
        return f"Render items count: {len(state['records'])}"
    elif status == "error":
        return f"Alert dialogue error box: {state['message']}"
    return "Unknown state"

print(render_network_ui({"status": "success", "records": ["user1", "user2"]}))


def extract_dict_keys(obj: dict, keys: list) -> list:
    return [obj[key] for key in keys if key in obj]

product_data = {"sku": "LAP-102", "price": 1200, "stock": 45}
print(extract_dict_keys(product_data, ["price", "stock"]))

def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], index]
        lookup[num] = index
    return []

print(two_sum([2, 7, 11, 15], 9))


def group_anagrams(words: list[str]) -> list[list[str]]:
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


def valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(valid_parentheses("()[]{}"))


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def product_except_self(nums: list[int]) -> list[int]:
    length = len(nums)
    answer = [1] * length
    
    left_product = 1
    for i in range(length):
        answer[i] = left_product
        left_product *= nums[i]
        
    right_product = 1
    for i in reversed(range(length)):
        answer[i] *= right_product
        right_product *= nums[i]
        
    return answer

print(product_except_self([1, 2, 3, 4]))


def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit_val = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit_val:
            max_profit_val = price - min_price
    return max_profit_val

print(max_profit([7, 1, 5, 3, 6, 4]))


def is_palindrome(s: str) -> bool:
    clean_str = "".join(char.lower() for char in s if char.isalnum())
    return clean_str == clean_str[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


def reverse_string(text: str) -> str:
    if len(text) == 0:
        return text
    return text[-1] + reverse_string(text[:-1])

print(reverse_string("hello"))


def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], index]
        lookup[num] = index
    return []

print(two_sum([2, 7, 11, 15], 9))


def group_anagrams(words: list[str]) -> list[list[str]]:
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

def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], index]
        lookup[num] = index
    return []

print(two_sum([2, 7, 11, 15], 9))
                                             
def group_anagrams(words: list[str]) -> list[list[str]]:
    cache = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in cache:
            cache[sorted_word] = []
        cache[sorted_word].append(word)
    return list(cache.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
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
def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit_val = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit_val:
            max_profit_val = price - min_price
    return max_profit_val

print(max_profit([7, 1, 5, 3, 6, 4]))

def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], index]
        lookup[num] = index
    return []

print(two_sum([2, 7, 11, 15], 9))


def group_anagrams(words: list[str]) -> list[list[str]]:
    cache = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in cache:
            cache[sorted_word] = []
        cache[sorted_word].append(word)
    return list(cache.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(valid_parentheses("()[]{}"))


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


def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit_val = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit_val:
            max_profit_val = price - min_price
    return max_profit_val

print(max_profit([7, 1, 5, 3, 6, 4]))

def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], index]
        lookup[num] = index
    return []

print(two_sum([2, 7, 11, 15], 9))


def group_anagrams(words: list[str]) -> list[list[str]]:
    cache = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in cache:
            cache[sorted_word] = []
        cache[sorted_word].append(word)
    return list(cache.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(valid_parentheses("()[]{}"))


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


def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit_val = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit_val:
            max_profit_val = price - min_price
    return max_profit_val

print(max_profit([7, 1, 5, 3, 6, 4]))
