from src.problem2_sol import problem2

def test_problem1():
  assert problem2(1221) == "YES"
  assert problem2(5678) == "NO"
  assert problem2(1111) == "YES"
  assert problem2(2332) == "YES" 
  assert problem2(8070) == "NO"