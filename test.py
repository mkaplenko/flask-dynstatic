import unittest
from flask.ext.testing import TestCase
from flask import Flask
from flask_dynstatic import DynStatic
import os


class DynStaticTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['DYNSTATIC_ROOT'] = os.path.dirname(__file__)
        self.dn = DynStatic(app)
        self.app = app
        return app

    def test_to_static_html(self):
        create_view = self.dn.to_static_html(path='index.html')(self.create_view())
        self.assertEqual(create_view(), 'test_html')
        self.assertEqual(len(self.dn.views), 1)

    def create_view(self):
        @self.app.route('/')
        def index():
            return 'test_html'
        return index

dynstatic_testsuite = unittest.defaultTestLoader.loadTestsFromTestCase(DynStaticTestCase)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(dynstatic_testsuite)