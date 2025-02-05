inp = input()
inp = inp.replace("+", " + ")
inp = inp.replace("/", " / ")
inp = inp.replace("-", " - ")
inp = inp.replace("*", " * ")
inp = inp.split(" ")
result = 0
first = True
add = False
divide = False
multiplay = False
substract = False
for a in inp:
   if first:
      result = float(a)
      first = False
      continue
   elif add:
      result += float(a)
      add = False
      continue
   elif substract:
      result -= float(a)
      substract = False
      continue
   elif divide:
      result /= float(a)
      divide = False
      continue
   elif multiplay:
      result *= float(a)
      multiplay = False
      continue
   elif a == "+":
      add = True
   elif a == "/":
      divide = True
   elif a == "*":
      multiplay = True
   elif a == "-":
      substract = True
   
print(result)