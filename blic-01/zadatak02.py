def func2(dict1, dict2):
    # assert isinstance(dict1, dict)
    # assert isinstance(dict2, dict)
    assert all(isinstance(n, list) for n in dict1)
    assert all(isinstance(n, list) for n in dict2)
    
    
print(func2({['GBP', 'USD', 'CZK']}, {['EUR', 'USD', 'CZK']}))