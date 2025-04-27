def dig_pow(n: int, p:int) -> int:
    total = sum(int(digit) ** (p + i) for i, digit in enumerate(str(n)))
    return total // n if total % n == 0 else -1

def dig_pow1(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

def dig_pow3(n, p):
    sum = 0
    for c in str(n):
        sum += int(c) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1


if __name__ == "__main__":
    dig_pow(24234, 2)
