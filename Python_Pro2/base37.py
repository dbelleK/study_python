try:
    a=10
    b=0
    c=a/b
except Exception as e:
    print(e)


try:
    a=10
    b='zero'
    c=a/b
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
