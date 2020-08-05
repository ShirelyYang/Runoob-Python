def log(pr):    # 将装饰函数传入
    def wrapper():
        print("************************")
        return pr()     # 执行被装饰的函数
    return wrapper      # 将装饰完之后的函数返回（返回的是函数名）

@log
def pr():
    print("I'm yang.")
    pass

pr()