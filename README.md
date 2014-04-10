flask-dynstatic
===============
Simple decorator for generating static HTML files (error pages for example) from flask views.

Installation
------------
The simplest and recommended way to install Flask-DynStatic is installation via pip:

```bash
pip install git+git://github.com/mkaplenko/flask-dynstatic
```

How to use
----------

```python
from flask_dynstatic import DynStatic

app = Flask(__name__)
app.debug = True
app.config['DYNSTATIC_ROOT'] = os.path.join(os.path.dirname(__file__), 'static')
dn = DynStatic(app)

@app.route('/')
@dn.to_static_html(path='404.html')
def not_found():
    return render_template('404.html')


@app.route('/test/')
@dn.to_static_html(path='test.html')
def test():
    return 'Func arr'
```

Decorator required path to the outputting HTML file related to the DYNSTATIC_ROOT DIRECTORY.

Register managment command
--------------------------

```python
from flask_dynstatic import GetStatic

manager.add_command('statichtml', GetStatic())
```
Then you can generate static HTML files from outputting by decorated views to the DYNSTATIC_ROOT DIRECTORY by use manage command:

```bash
./manage.py statichtml
```

Testing
-------
For testing you need to install flask-testing extension.
Simplest way to install flask-testing is installation via pip:
```bash
pip install flask-testing
```

You can test Flask-DynStatic by run test cases from directory which Flask-DynStatic has been installed:

```bash
python test.py
```
