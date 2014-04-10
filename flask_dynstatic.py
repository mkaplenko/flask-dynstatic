from functools import wraps
import os

static_root = os.path.join(os.path.dirname(__file__), 'static')

views = []


def to_static_html(path):
    def decorator(func):
        if func not in views:
                views.append((path, func))

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


def construct_html():
    for view in views:
        with open(os.path.join(static_root, view[0]), 'w') as html_file:
            html_file.write(view[1]())
