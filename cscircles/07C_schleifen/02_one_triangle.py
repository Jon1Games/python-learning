n=int(input())

if n <= 0:
   print("Negative int is not allowed")
else:
   for i in range(n,0,-1):
      s = input()
      space = i - 2
      if len(s) > space:
         s = s[0:space]
      else:
         while len(s) > space:
            s += "-"
      
      if i == n:
         print(i * "_")
      elif (i > 1):
         print("|" + (i-2) * "-" + "/")
      else:
         print("´")
