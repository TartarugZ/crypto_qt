def check_int(data):
    try:
        inf = int(data)
    except ValueError:
        return False
    if inf <= 0:
        return False
    return True
