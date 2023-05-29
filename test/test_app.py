from app import login

def test_login():
    assert login().__contains__('<!DOCTYPE html>')
