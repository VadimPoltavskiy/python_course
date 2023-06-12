def is_simple(number: int) -> bool:
    if number in [1,2]:
        return True
    if not number % 2 == 0:
        return False
    for dev in range(3, number//2 + 1, 2):
      if number % dev == 0:
            return False
    return True

print(is_simple (199))