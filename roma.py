def numberOfNumeral(n):
ns = str(input("Enter a roman numeral"))
while ns:
   firstNum = numberOfNumeral(ns[0])
   secondNum = numberOfNumeral(ns[1]) if len(ns) > 1 else -1
   if firstNum is at least secondNum:
      ns = ns[1:] 
   else:
      ns = ns[2:]
