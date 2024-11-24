class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for _ in range(abs(b)):
            result = result + abs(a)
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = 0
        abs_a, abs_b = abs(a), abs(b)
        while abs_a >= abs_b:
            abs_a -= abs_b
            result += 1
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            result = -result
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        abs_a, abs_b = abs(a), abs(b)
        while abs_a >= abs_b:
            abs_a -= abs_b
        return abs_a if a >= 0 else -abs_a
