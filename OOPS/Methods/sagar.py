#^-----------------------------------------------------------------------------------------
#!ArithmeticCalOops.py
# class Calculator:
#      def getvals(self):
#           self.a = int(input("Enter First Values : "))
#           self.b = int(input("Enter Second Values : "))
#           self.op = input("Enter Arithmetic Operator : ")

# class Result:
#      @staticmethod
#      def dispvals(obj):
#         match(obj.op):
#              case "+":
#                   print(f"sum = ({obj.a},{obj.b}) = {obj.a+obj.b}")
#              case "-":
#                   print(f"sub = ({obj.a},{obj.b}) = {obj.a-obj.b}")
#              case "*":
#                   print(f"mul = ({obj.a},{obj.b}) = {obj.a*obj.b}")
#              case "/":
#                   print(f"div = ({obj.a},{obj.b}) = {obj.a/obj.b}")
#              case "//":
#                   print(f"div = ({obj.a},{obj.b}) = {obj.a//obj.b}")
#              case "%":
#                   print(f"Modulodiv = ({obj.a},{obj.b}) = {obj.a%obj.b}")
#              case "":
#                   print(f"Pow = ({obj.a},{obj.b}) = {obj.a**obj.b}")
#              case _:
#                   print(f"{obj.op} is not a Arithmethic Operator")


# co = Calculator()
# while True:
#  try:
#   co.getvals()
#   Result.dispvals(co)
#  except ValueError:
#         print("Don't enter alnums,strs and symbols--try again")
#  else:
#       ch = input("do you want to do another operation-(yes,no) :").lower()
#       if ch == "no":
#        break
#^-----------------------------------------------------------------------------------------
#!ArithmeticCalOops2.py
# class Calculator:
#      def getvals(self):
#           self.a = int(input("Enter First Values : "))
#           self.b = int(input("Enter Second Values : "))
#           self.op = input("Enter Arithmetic Operator : ")

# class Result:
#      @staticmethod
#      def dispvals(obj):
#         match(obj._dict_['op']):
#              case "+":
#                   print(f"sum = ({obj._dict['a']},{obj.dict['b']}) = {obj.dict['a']+obj.dict_['b']}")
#              case "-":
#                   print(f"sub = ({obj._dict['a']},{obj.dict['b']}) = {obj.dict['a']-obj.dict_['b']}")
#              case "*":
#                   print(f"mul = ({obj._dict['a']},{obj.dict['b']}) = {obj.dict['a']*obj.dict_['b']}")
#              case "/":
#                   print(f"div = (({obj._dict['a']},{obj.dict['b']}) = {obj.dict['a']/obj.dict_['b']}")
#              case "//":
#                   print(f"div = ({obj._dict.get('a')},{obj.dict.get('b')}) = {obj.dict.get('a')//obj.dict_.get('b')}")
#              case "%":
#                   print(f"Modulodiv = ({obj._dict.get('a')},{obj.dict.get('b')}) = {obj.dict.get('a')%obj.dict_.get('b')}")
#              case "":
#                   print(f"Pow = ({obj._dict.get('a')},{obj.dict.get('b')}) = {obj.dict.get('a')**obj.dict_.get('b')}")
#              case _:
#                   print(f"{obj.op} is not a Arithmethic Operator")


# co = Calculator()
# while True:
#  try:
#   co.getvals()
#   Result.dispvals(co)
#  except ValueError:
#         print("Don't enter alnums,strs and symbols--try again")
#  else:
#       ch = input("do you want to do another operation-(yes,no) :").lower()
     #  if ch == "no":
     #   break
#^-----------------------------------------------------------------------------------------
#!ArithmeticCalOops1.py and #!ArithmeticCalOops2.py
# class Calculator:
#      def getvals(self):
#           self.a = int(input("Enter First Values : "))
#           self.b = int(input("Enter Second Values : "))
#           self.op = input("Enter Arithmetic Operator : ")

# class Result:
#      @staticmethod
#      def dispvals(obj):
#         match(obj.op or obj.dict['op']):
#              case "+":
#                   print(f"sum = ({obj.a},{obj.b}) = {obj.a+obj.b}")
#              case "-":
#                   print(f"sub = ({obj.dict['a']},{obj.dict['b']}) = {obj.dict['a']-obj.dict['b']}")
#              case "*":
#                   print(f"mul = ({obj.dict['a']},{obj.dict['b']}) = {obj.dict['a']*obj.dict['b']}")
#              case "/":
#                   print(f"div = (({obj.dict['a']},{obj.dict['b']}) = {obj.dict['a']/obj.dict['b']}")
#              case "//":
#                   print(f"div = ({obj.dict.get('a')},{obj.dict.get('b')}) = {obj.dict.get('a')//obj.dict.get('b')}")
#              case "%":
#                   print(f"Modulodiv = ({obj.a},{obj.b}) = {obj.a%obj.b}")
#              case "":
#                   print(f"Pow = ({obj.a},{obj.b}) = {obj.a**obj.b}")
#              case _:
#                   print(f"{obj.op} is not a Arithmethic Operator")


# co = Calculator()
# while True:
#  try:
#   co.getvals()
#   Result.dispvals(co)
#  except ValueError:
#         print("Don't enter alnums,strs and symbols--try again")
#  else:
#       ch = input("do you want to do another operation-(yes,no) :").lower()
#       if ch == "no":
#        break
#^-----------------------------------------------------------------------------------------
# class Linear:
#      def getvals(self):
#           lst = [int(i) for i in input("Enter Comma Seprated Value : ").split()]
#           return lst
          
#      def search(self,lst):
#           lst.sort()
#           print(f"Sorted list : {lst}")
#           skey = int(input("Enter Search Key : "))
#           ski = -1
#           for i in range(len(lst)):
#                if skey == lst[i]:
#                     ski = i
#                     break
#           if ski== -1:
#                print(f"{skey} value does not exist in list : ")
#                print("Search in Un-Successfull")
#           else:
#                print(f"The index of value {skey} in list is {ski}")
#                print("Search is Successfull")


# lo = Linear()

# lst=  lo.getvals()
# if len(lst) == 0:
#      print(f"List is Empty : {lst}")
# else:
#      lo.search(lst)
#^-----------------------------------------------------------------------------------------