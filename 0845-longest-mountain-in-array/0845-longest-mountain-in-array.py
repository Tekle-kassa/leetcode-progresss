class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        i = 1
        while i < n - 1:
            # Check if current element is the starting point of a mountain
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left, right = i, i

                # Expand mountain to the left
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                # Expand mountain to the right
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Check if a mountain is found
                ans = max(ans, right - left + 1)

                # Move to next element after the mountain
                i = right
            else:
                # Move to next element
                i += 1

        return ans
