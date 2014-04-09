__author__ = 'mkaplenko'


views = []


def to_static_html(func):
    def wrapper(*args, **kwargs):
        if func not in views:
            views.append(func)
            print views
        return func(*args, **kwargs)
    return wrapper
