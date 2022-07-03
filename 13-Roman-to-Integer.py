"""
SINS - Given a string of Roman number we need to convert that in integer form.

Solution - Make a hashmap and store all the roman numbers according to their values, now make two pointers one for the curr instance and another for the last instance. Now iterate through the string and for each character check if it's present in the hashmap, if yes, check if the last pointer value is greater than the curr pointer value then subtract that character from the curr pointer value else if it's not present then add that character to the curr pointer value then add that character to the curr pointer value or remove the last pointer value twice and increment value in curr pointer. 

Time Complexity - O(n) where n is the length of the string.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        arr = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = arr[s[0]]
        last = arr[s[0]]
        for idx, curr in enumerate(s):
            if idx > 0:
                if last < arr[curr]:
                    res += arr[curr] - 2*last
                else:
                    res += arr[curr]
            last = arr[curr]
        return res


print("sol", Solution.romanToInt("", "LVIII"))
