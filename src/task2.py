from task3 import decorator_1
@decorator_1
def typeBasedTransformer(**kwargs):
    transformed = {}
    
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  
            transformed[key] = value ** 2
        elif isinstance(value, bool):  
            transformed[key] = not value
        elif isinstance(value, (list, tuple, str)): 
            transformed[key] = value[::-1]
        elif isinstance(value, dict):  
            if len(value) == len(set(value.values())):  
                transformed[key] = {v: k for k, v in value.items()}
            else:
                transformed[key] = value 

    print(transformed) 
