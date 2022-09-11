def f(func):
    def wrapper(*args, **kwargs):
        print("Started")

        v = func(*args, **kwargs)
        print("Stopped")
        return v

    return wrapper
@f
def f1(a):
    print(a,"Is Better")
f1('hibrahim')

print("------------------------")
@f
def f2(x,y):
    print("the sum of: ", x , " and ", y ," = ", x+y)

f2(2, 8)

print("------------------------")

@f
def add(x, y):
    return x+y
print(add(4,5))