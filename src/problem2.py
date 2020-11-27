'''
 回文是一個數字，向前讀取的內容與向後讀取的內容相同。
 給定一個四位數的整數，如果是回文，則回傳 YES，否則回傳 NO。
 1221 -> YES
 1231 -> NO
'''

def problem2(num):
  a=num//1000
  b=(num-1000*a)//1000
  c=(num-1000*a-100*b)//10
  d=(num-1000*a-100*b-10*c)
  if a==d & b==c:
    return "Yes"
  else:
    return"No"


print(f"{problem2(1234)}")