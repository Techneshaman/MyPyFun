# there's like really everything in here

d = {'three_args': (0,1,2),
     'two_args': (0,1)}


def three_arg_func(a,b,c):
    print [a,b,c]


def two_arg_func(a,b):
    print [a,b]

expected_args = len(d['three_args'])
