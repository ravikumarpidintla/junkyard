def per_diff(x,y=0):
    result = 0
    result = ((x - y)/((x + y)/2)) * 100
    print('percent diff between', x, y, 'is:')
    return result
per_diff(1797.12, 1658.88)
