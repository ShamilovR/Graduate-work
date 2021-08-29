def check_length(string):
    return len(str(string)) <= 4

def is_number(str):
    if str.isdigit():
        return True
    else:
        try:
            float(str)
            return True
        except:
            return False

def discard_zeros(array):
    result = []
    for num in array:
        if num - int(num) == 0.0:
            result.append(int(num))
        else:
            result.append(float('{0:.5f}'.format(num).rstrip('0').rstrip('.')))
    return result