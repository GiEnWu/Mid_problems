from src.problem4_sol import problem4

black = '黑色'
white = '白色'

def test_problem4():
  assert problem4(1,1) == black
  assert problem4(2,6) == black
  assert problem4(8,8) == black
  assert problem4(4,4) == black
  assert problem4(7,8) == white
  assert problem4(1,8) == white
  assert problem4(8,1) == white