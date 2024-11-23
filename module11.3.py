import inspect

def introspection_info(obj):
    dict = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': getattr(obj, 'module', None)
    }
    return dict

number_info = introspection_info(42)
print(number_info)