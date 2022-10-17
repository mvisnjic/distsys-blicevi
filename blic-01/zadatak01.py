def func1(listOfStrings):
    assert isinstance(listOfStrings, list)
    assert all(isinstance(n, str) for n in listOfStrings)
    # return {keys[k]:v if v>=5 and v<=10 else -1 for k,v in enumerate(listOfStrings)}
    return {k:elem[::-1] for k,elem in enumerate(listOfStrings)}

print(func1(['Stol', 'Stolica', 'Krevet', 'Fotelja']))    