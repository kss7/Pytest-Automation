
## Python Automation Testing With Pytest
<a href="https://www.udemy.com/course/python-automation-pytest/?referralCode=14154874C63EEAE25028"><img src="./PytestFramework_Course_pic.JPG" alt="Pytest Framework" style="width:200px;height:100px;"></a>

### Pytest Usage

https://docs.pytest.org/

```
pytest [options] [file_or_dir] [file_or_dir] ...
```

Help:

    pytest --help

### Some commonly used options

```
 -s                    Show Output, do not caputure
 -x                    Stop after first failure
 -k "expression"       Only run tests that match file-name-expession
 -m "MARKEXPR:         Only run tests matching given mark expression.
 -rs                   Show extra summary info for SKIPPED
 -r chars              Show extra test summary info as specified by chars:
                       (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed
                       (w)pytest-warnings (p)passed, (P)passed with output,
                       (a)all except pP.

 -v                    Verbose
 -q, --quiet           Less verbose
 -l, --showlocals      Show local variables in tracebacks
```

### Shorter tracebacks, python tracebacks

    pytest --tb=short
    pytest --tb=line # even shorter


### Output capturing, display print statements

    pytest -s # disable all capturing

https://pytest.org/latest/capture.html#capturing-of-the-stdout-stderr-output

### Print a message after the test

The text is printed always, even in silent mode. See https://stackoverflow.com/a/38806934/362951

    def report():
      print("""This is printed AFTER the test""")
    import atexit
    atexit.register(report)

### Collect information only / dry run

    pytest --collect-only -q

(will not display fixture code but fixture code will be run always)

### Output verbose messages

    pytest test_sample.py -v  

### Run a single test, specify file.py::testName

    pytest -q -s test_file.py::testName

(fixture code will also run)

### Ignore / exclude certain files or directories

    --ignore=lib/foo/bar.py --ignore=lib/hello/

### Call pytest through python

    python -m pytest -q test_sample.py  

### Call pytest from python

Calling pytest programmatically / from code:

    import pytest
    # put all arguments into a string. example:
    pytest.main("g/src/app/art/__init_unit.py")    
    # another example:
    pytest.main("-x mytestdir")
    # or pass in a list of arguments:
    pytest.main(['-x', 'mytestdir'])

### Show available markers

    pytest --markers  

### Create a reusable marker

content of pytest.ini:

```
[pytest]
markers =
   webtest: mark a test as a webtest.
```

### Only run tests with names that match the "string expression"

    pytest -k "TestClass and not test_one" 

(fixture code will also run)

### Only run tests that match the node ID

    pytest test_server.py::TestClass::test_method  

(fixture code will also run)

### Stop after

```
py.test -x  # stop after first failure
py.test --maxfail=2  # stop after two failures
py.test --maxfail=2 -rf  # exit after 2 failures, report fail info.
```

### Show local variables in tracebacks

```
py.test --showlocals 
py.test -l  # (shortcut)

py.test --tb=long  # the default informative traceback formatting
py.test --tb=native  # the Python standard library formatting
py.test --tb=short  # a shorter traceback format
py.test --tb=line  # only one line per failure
py.test --tb=no  # no tracebak output
```

### List of the slowest 10 test durations.

    pytest --durations=10  

### Send tests to multiple CPUs

    pytest -n 4  

### Run tests with decorator "slowest"

Run tests with decorator @pytest.mark.slowest or slowest = pytest.mark.slowest; @slowest

    pytest -m slowest  

### Show active plugins

Find out which plugins are active in your environment

    pytest --traceconfig  

### Instafail

if pytest-instafail is installed, show errors and failures instantly instead of waiting until the end of test suite:

    pytest --instafail  

### Expected exceptions

See https://pytest.org/latest/assert.html#assertions-about-expected-exceptions

Example:

```python
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)
```

More usage examples: http://stackoverflow.com/a/15152283/362951

Excinfo is a py.code.ExceptionInfo instance: http://pylib.readthedocs.org/en/latest/code.html#py-code-exceptioninfo

Its main attributes are type (the exception class), value (the current instance), and traceback (see http://pylib.readthedocs.org/en/latest/code.html#py.code.Traceback) - 

Also see https://docs.python.org/3.4/library/sys.html#sys.exc_info

### Skip

Simple use:

```python
import pytest

@pytest.mark.skip(reason="Skipping for no reason specified")
@pytest.mark.skipif(condition)
```
Skip a whole module:

```
import pytest
pytestmark=pytest.mark.skipif(condition)
```


Show skip reasons / info:

```
pytest -rs
```


Advanced: https://pytest.org/latest/skipping.html

### Test using parametrize

```python
import pytest

@pytest.mark.parametrize(
   ('n', 'expected'), [
       (1, 2),
       (2, 3),
       (3, 4),
       (4, 5),
       pytest.mark.xfail((1, 0)),
       pytest.mark.xfail(reason="some bug")((1, 0)),
       pytest.mark.skipif('sys.version_info >= (3,0)')((10, 11)),
   ]
)
def test_increment(n, expected):
   assert n + 1 == expected
```

### Configuration

See https://docs.pytest.org/en/latest/customize.html

Check if there are unexpected pytest.ini, tox.ini or setup.cfg somewhere in the project.

### Known issues

#### assert error with python 3.5

`TypeError: Call constructor takes either 0 or 3 positional arguments`

Workaround: add the parameter `--assert=plain` to the pytest command

#### pytest.ini

Put a section marker at the top:

```
[pytest]
```

##### Line continuation

indent continued line by 2 spaces:*

```
norecursedirs = 
  .git
  .idea
```

##### norecursedir

Allows only simple directory names or patterns wihtout `/`, they are always applied in all subdirectories. For individual directories use: 'addopts --ignore='!

##### addopts

Example:
```
addopts = 
  --ignore=./some/dir
  --ignore=./some/other/dir
  --ignore=./dir1/some.file
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks!)

   [Ref1]: <https://gist.github.com/kwmiebach/3fd49612ef7a52b5ce3a>
