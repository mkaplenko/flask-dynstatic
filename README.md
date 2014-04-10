flask-dynstatic
===============
Simple decorator for generating static HTML files (for error pages) from flask views.

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
