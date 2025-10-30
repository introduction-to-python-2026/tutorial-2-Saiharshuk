def find_max_number(num1, num2, num3):
    if num1 > num2 >= num3:
      return num1
    elif num2 > num1 >= num3:
      return num2
    if num3 > num2 >= num1:
      return num3     
   
