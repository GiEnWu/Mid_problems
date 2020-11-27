''''
 給一個四位數的整數，將其循環旋轉兩位數，如下面的測試所示
 1234 -> 3412
 5678 -> 7856
'''

def problem1(num) :
  a =num%100
  b =num//100
  return a*100+b


print(f"{problem1(1234)}")
