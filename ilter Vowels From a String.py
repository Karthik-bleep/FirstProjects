#Filter Vowels From a String
str = input("Enter your name: ")
list=["a","e","i","o","u"]
def vowel(str):
  for ch in str:
    if ch in list:
      return True

obj_filtered = filter(vowel,str)
for x in obj_filtered:
  print(x)
