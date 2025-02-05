# https://neetcode.io/problems/evaluate-reverse-polish-notation
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

#     The operands may be integers or the results of other operations.
#     The operators include '+', '-', '*', and '/'.
#     Assume that division between integers always truncates toward zero.

# Input: tokens = ["1","2","+","3","*","4","-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    stack.append(int(first / second))
        return stack.pop()
