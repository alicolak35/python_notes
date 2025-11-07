from dataclasses import dataclass


"""
5 november: "field is not defined" error I received. with @dataclass decorator, i dont need to initilize variables with "def __init__():"

"""
@dataclass#  @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
          #  match_args=True, kw_only=False, slots=False, weakref_slot=False) by default
class Cla():
    var_a : int 
    var_b : str 
    # var_c : list = field(default_factory=list) #[ 2, 4]

    """ equivalent to
    def __init__(self, var_a : int = 4, var_b : str, var_c : list):
        self.var_a = var_a
        self.var_b = var_b
        self.var_c = var_c
    """


ass = Cla(5, "sss")

# @dataclass
# class C:
#     mylist: list[int] = field(default_factory=list)

# c = C()
# c.mylist += [1, 2, 3]


def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

# say_hello = my_decorator(say_hello) : first, my_decorator uses say_hello(). Then, my_decorator returns a wrappper function nd assigns it to the variable say_hello. Now, say_hello variable points wrapped function
# it will call wrapper() after it include func() inside it with "return wrapper"
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# say_hello()

# def wrapper() :
#     print("Before")
#     # func()
#     print("After")

#     return wrapper

# hi = wrapper()

# hi()

a = 3

