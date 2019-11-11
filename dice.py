import re
from collections import Counter
def dice1(user_input):
  result = re.findall(r'(^(66)[^6]|[^6](66)[^6]|[^6]66$)', user_input)
def dice2(user_input):
  result = re.split("6", user_input)
  return max(len(a) for a in result)
def dice3(user_input):
  result = re.split(r'[^56]', user_input)
  result_len = [len(a) for a in result if a !='']
  if(not result_len): return 0
  most_freq = Counter(result_len)
  return max([a for a in most_freq if most_freq[a] == max(most_freq.values())])
def dice(user_input):
  print(dice1(user_input))
  print(dice2(user_input))
  print(dice4(user_input))
def checker(func, user_input, output):
  try:
    assert func(str(user_input)) == (output)
    print(f'Assertion of {func.__name__} on {user_input} passed')
  except AssertionError as err:
    print(f'Assertion of {func.__name__} on {user_input} failed', err)
if __name__ == "__main__":
  checker(dice1, 56611166626634416, 2)
  checker(dice1, 666666, 0)
  checker(dice2, 666166666766, 1)
  checker(dice2, 66423612345654, 5)
  checker(dice2, 6123123456, 8)
  checker(dice3, 6556665, 7)
  checker(dice3, 5533661656, 2)
  checker(dice3, 456116513656124566, 3)
  checker(dice3, 12345, 0)
  print("done with tests")
  while 1:
    number_of_throws = input("Enter the number of throws: ")
    throws_result = input("Enter the result of throws: ")
    dice(throws_result)
