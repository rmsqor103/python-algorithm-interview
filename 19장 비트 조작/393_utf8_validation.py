class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True



sol = Solution()
print(sol.validUtf8([197,130,1]))
print(sol.validUtf8([235,140,4]))


"""
Input: data = [197,130,1]
Output: true

Input: data = [235,140,4]
Output: false
"""
