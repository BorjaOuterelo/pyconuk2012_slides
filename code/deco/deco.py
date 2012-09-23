# simple memoize cache
def memoize(f, cache={}, *args, **kwargs):
    def _memoize(*args, **kwargs):
        key = (args, str(kwargs))
        if not key in cache:
            cache[key] = f(*args, **kwargs)

        return cache[key]

    return _memoize

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

@memoize
def fib_memoized(n):
    if n <= 1:
        return 1
    return fib_memoized(n-1) + fib_memoized(n-2)


print(fib_memoized(100))


# two standard way to define a decorator
def decorator(func):
    def _decorator(*args, **kwargs):
        # something before the function is run
        ret = func(*args, **kwargs)
        # something after the function is run
        return ret

    return _decorator

# and we use it in this way
# def to_decorate():
#     print("Hello world")

@decorator
def to_decorate():
    print("Hello world")


to_decorate = decorator(to_decorate)

def param_deco(func):
    def _param_deco(arg1, arg2):
         def __param_deco(*args, **kwargs):
             pass

         return __param_deco
    return _param_deco


class call_decorator:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        def _decorator(*args, **kwargs):
            ret = func(*args, **kwargs)
            return ret

        return _decorator


def class_decorator(cls):
    def new_meth(self):
        return 100

    cls.new_meth = new_meth
    return cls


@class_decorator
class C1:
    pass

c = C1()
print(c.new_meth())
