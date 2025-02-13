def kwargsAcceptFun(**kwargs):
    print("Received keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
