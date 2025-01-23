# https://neetcode.io/problems/string-encode-and-decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# During encoding, we convert the length of the string into a fixed 4-digit string, add the string itself, and append it to the result string in sequence.

# During decoding, we first take the first four digits of the string to get the length,
# and then cut the following string according to the length. We cut it in sequence until we get the list of strings.

class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for item in strs:
            res.append("{:4}".format(len(item)) + item)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i, total_size = 0, len(s)
        res = []
        while i < total_size:
            length = int(s[i : i + 4])
            i += 4
            string = s[i : i + length]
            res.append(string)
            i += length
        return res


        
