"""
🟢 FizzBuzz
Classic programming challenge.
"""


def fizzbuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def fizzbuzz_extensible(n: int, mappings=None) -> list[str]:
    """Extensible FizzBuzz - easy to add new rules."""
    if mappings is None:
        mappings = [(3, "Fizz"), (5, "Buzz")]
    result = []
    for i in range(1, n + 1):
        output = ""
        for divisor, word in mappings:
            if i % divisor == 0:
                output += word
        result.append(output if output else str(i))
    return result


if __name__ == "__main__":
    for item in fizzbuzz(20):
        print(item)
