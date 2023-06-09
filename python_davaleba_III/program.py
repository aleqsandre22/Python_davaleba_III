import math

def is_pol(str):
  """აბრუნებს True-ს, თუ მოცემული სტრიქონი პოლინდრომი, წინააღმდეგ შემთხვევაში, False."""
  for i in range(len(str) // 2):
    if str[i] != str[len(str) - 1 - i]:
      return False
  return True

def is_anagram(str1, str2):
  """აბრუნებს True-ს, თუ მოცემული სტრიქონები ერთმანეთის ანაგრამებია, წინააღმდეგ შემთხვევაში False."""
  if len(str1) != len(str2):
    return False
  for char in str1:
    if char not in str2:
      return False
  return True

def count_vow(str):
  """აბჯუნებს ხმოვანთა რაოდენობას მოცემულ სტრიქონში."""
  vowels = "aeiou"
  count = 0
  for char in str:
    if char in vowels:
      count += 1
  return count

def is_per(num):
  """აბჯუნებს True-ს, თუ მოცემული რიცხვი არის სრულყოფილი, False-ს წინააღმდეგ შემთხვევაში."""
  sum_of_divisors = 0
  for i in range(1, num):
    if num % i == 0:
      sum_of_divisors += i
  return sum_of_divisors == num

def to_rom(number):
  """აქცევს მოცემულ რიცხვს რომაულ ციფრებში."""
  rom_numerals = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
  }
  rom_number = ""
  for value, rom_numeral in rom_numerals.items():
    while number >= value:
      rom_number += rom_numeral
      number -= value
  return rom_number

def g_c_s(str1, str2):
  """აბრუნებს მოცემული სტრიქონების უდიდეს საერთო ქვესტრიქონს."""
  table = [[0 for i in range(len(str2))] for j in range(len(str1))]
  for i in range(len(str1)):
    for j in range(len(str2)):
      if str1[i] == str2[j]:
        table[i][j] = 1 + table[i - 1][j - 1] if i > 0 and j > 0 else 1
  max_len = 0
  max_start = 0
  for i in range(len(table)):
    for j in range(len(table[i])):
      if table[i][j] > max_len:
        max_len = table[i][j]
        max_start = i
  return str1[max_start:max_start + max_len]

def main():
  """მთავარი ფუნქცია."""
  while True:
    print("აირჩიეთ მოქმედება:")
    print("1. შეამოწმეთ არის თუ არა სტრიქონი პოლინდრომი")
    print("2. შეამოწმეთ არის თუ არა ორი სტრიქონი ერთმანეთის ანაგრამა")
    print("3. დათვალეთ ხმოვანთა რაოდენობა სტრიქონში (მხოლოდ ინგლისური)")
    print("4. შეამოწმეთ არის თუ არა რიცხვი სრულყოფილი")
    print("5. გადაიყვანეთ რიცხვი რომაულ ციფრებში")
    print("6. გამოყავით ყველაზე დიდი საერთო ქვესტრიქონი ორი სტრიქონისაგან")
    print("7. გასვლა")

    choice = int(input())

    if choice == 1:
      str = input("შეიყვანეთ სტრიქონი: ")
      if is_pol(str):
        print("მოცემული სტრიქონი პოლინდრომი")
      else:
        print("მოცემული სტრიქონი არ არის პოლინდრომი")
    elif choice == 2:
      str1 = input("შეიყვანეთ პირველი სტრიქონი: ")
      str2 = input("შეიყვანეთ მეორე სტრიქონი: ")
      if is_anagram(str1, str2):
        print("ორი სტრიქონი ერთმანეთის ანაგრამებია")
      else:
        print("ორი სტრიქონი არ არის ერთმანეთის ანაგრამები")
    elif choice == 3:
      str = input("შეიყვანეთ სტრიქონი: ")
      print(f"ხმოვანთა რაოდენობა სტრიქონში '{str}' არის {count_vow(str)}")
    elif choice == 4:
      num = int(input("შეიყვანეთ რიცხვი: "))
      if is_per(num):
        print(f"რიცხვი '{num}' მშვენიერია")
      else:
        print(f"რიცხვი '{num}' არ არის სრულყოფილი")
    elif choice == 5:
      num = int(input("შეიყვანეთ რიცხვი: "))
      print(to_rom(num))
    elif choice == 6:
      str1 = input("შეიყვანეთ პირველი სტრიქონი: ")
      str2 = input("შეიყვანეთ მეორე სტრიქონი: ")
      g_c_s = g_c_s(str1, str2)
      print(f"ყველაზე დიდი საერთო ქვესტრიქონი '{str1}' და '{str2}' არის '{g_c_s}'")
    else:
      break

if __name__ == "__main__":
  main()