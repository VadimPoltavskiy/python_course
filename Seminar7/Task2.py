def sam_by(func, list_obj: list) -> bool:
    result =[]
    for obj in list_obj:
        result.append(func(obj))
    if len(set(result)) == 1:
        return True
    return False

print (sam_by(lambda x: x%2==0, [2,5,6,8,10]))