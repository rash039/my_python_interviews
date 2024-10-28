#decorators for exception handling

def decorator_exception(logic):
    try:
        return logic
    except Exception as e:
        return e
  
@decorator_exception     
def new_using_decorator(logic):
    logic = a[0]
    print(logic)
    

