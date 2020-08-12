def is_armstrong(n: int) -> bool:
    input = n
    total = 0
    num_dig = len(str(input))
    if not isinstance(input, int):
        return False

    if n // 10 == 0:
        return True
    else:
        while n // 10 > 0:
            dig = n % 10
            total += dig ** num_dig
            n = n // 10
        dig = n % 10
        total += dig ** num_dig

    if total == input:
        return True
    else:
        return False
