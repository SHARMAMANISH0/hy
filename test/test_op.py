from src.math_operation import multi, add

def test_multi():
    assert multi(2,3)== 6
    assert multi(5,2)== 10

def test_add():
    assert add(2,3)==5
    assert add(4,3)==7
    assert add(3,3)==6
    assert add(2,2)==4
