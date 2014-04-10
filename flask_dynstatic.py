from flask import current_app
from functools import wraps
from flask.ext.script import Command
import os


class DynStatic(object):
    views = []

    def __init__(self, app=None):
        self.app = app

    @staticmethod
    def construct_html():
        for view in DynStatic.views:
            with open(os.path.join(current_app.config['DYNSTATIC_ROOT'], view[0]), 'w') as html_file:
                html_file.write(view[1]())
                print('{0} done\n'.format(html_file.name))

    @staticmethod
    def to_static_html(path):
        def decorator(func):
            if func not in DynStatic.views:
                    DynStatic.views.append((path, func))

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator


class GetStatic(Command):
    def run(self):
        DynStatic.construct_html()
        print("Static html constructed\n")
