"""
Flask-DynStatic
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-DynStatic',
    version='0.0.1',
    url='https://github.com/mkaplenko/flask-page-to-static',
    license='BSD',
    author='Mikhail Kaplenko',
    author_email='mkaplenko@brpr.ru',
    description='Grab flask dynamic pages to static html pages',
    long_description=__doc__,
    py_modules=['flask_dynstatic'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)