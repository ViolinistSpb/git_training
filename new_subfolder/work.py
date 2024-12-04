def my_summ(*args):
    total = 0
    count = 0
    for arg in args:
        total += arg
        count += 1
    return f'summ: {total}, number of args: {count}'
