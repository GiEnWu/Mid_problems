'''
 棋盤如 圖4 所示。
 程式有兩個參數 1到8 - 棋盤的列號和行號，指定棋盤中的格子。
 若該格為黑色，印出答案黑色回傳，否則印出答案白色回傳
'''

def problem4(r, c):
  if(r+c)%2==0:
      return"black"
  else:
    return"white"
    
print(f"{problem4(1,1)}")

