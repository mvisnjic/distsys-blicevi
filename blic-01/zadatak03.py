def func3(li):
    assert isinstance(li, list)
    assert all(isinstance(n, dict) for n in li)
    return {elem['kategorija']: sum([elem["ocjena"] for elem in li])}
    # return {}
    
print(func3([{"naziv": "Burek", "kategorija":"pite", "ocjena": 1}, {"naziv": "Ramstek", "kategorija":"steak", "ocjena": 9}, {"naziv": "Ribeye", "kategorija":"steak", "ocjena": 4}, {"naziv": "Sirnica", "kategorija":"pite", "ocjena": 5}]))