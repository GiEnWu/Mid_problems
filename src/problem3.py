'''
 定兩個整數A和B，如下所示算出AB之間所有整數的平方。
   請將答案印出並加人 ans 後回傳，'*'和'='中間沒有空格。
 A=4 B=5 
 4*4=16
 5*5=25

 A=20 B=20
 20*20=400

'''

def problem3(A, B):
  ans =[]
  rangenum = B - A + 1
  for i in range(rangenum):
    a = A+i
    ansstr =a*a
    print(ansstr)
    ans.append(ansstr)
  return ans    

s58 = ['5*5=25', '6*6=36', '7*7=49', '8*8=64']

print(f"\n{problem3(5,8)}") 

