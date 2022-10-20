def add(*args):
    print(args[0])
    sum = 0
    for number in args:
        sum += number
    return sum


print(add(1,3,2,5))



def calculate(n,**kwargs):               #keywordarguments
    print(kwargs)
    # for key , value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)

    print(kwargs["add"])

calculate(2, add = 3 ,multiply = 6)



class car:

    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")



my_car = car(make ="Nissan")
print(my_car.model)