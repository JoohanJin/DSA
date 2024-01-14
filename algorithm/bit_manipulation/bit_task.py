'''
'''
def get_bit(num: int, i: int):
    return (num & (i << i))


'''
'''
def set_bit(num: int, i: int):
    return (num | (i << i))


'''
'''
def clear_bit(num: int, i: int):
    mask  = ~(1 << i)
    return (num & mask)