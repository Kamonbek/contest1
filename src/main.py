from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1
kwargsAcceptFun(name="John", age=25, city="New York") 
typeBasedTransformer(name="John", age=25, city="New York", wives=['kate','angela','julia'])
decorator_1(kwargsAcceptFun)(name="John", age=25, city="New York")

