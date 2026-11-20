"""
🟡 Evaluate Reverse Polish Notation
Evaluate an arithmetic expression in Reverse Polish Notation.

Time:  O(n)
Space: O(n)
"""


def eval_rpn(tokens: list[str]) -> int:
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


if __name__ == "__main__":
    print(eval_rpn(["2","1","+","3","*"]))          # 9
    print(eval_rpn(["4","13","5","/","+"]))          # 6
