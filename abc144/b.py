def check():
  n = int(input())
  if n <= 9:
    return 'Yes'
  elif n > 81:
    return 'No'
  else:
    for i in range(2, 9):
      if n % i == 0 and n / i <= 9:
        return 'Yes'
    return 'No'

print(check())
