License
=========================================

This porject is totally based on the entire `<CPython https://github.com/python/cpython>`_, 
so it is licensed under the terms of the PSF License Agreement.

See `LICENSE (https://github.com/thautwarm/flowpython/blob/master/LICENSE`_ for the details.


Additional Grammar Compatible to CPython 

==========================================


How to Get Flowpython
-----------------------

Go to release page...

VERSION
----------
flowpython  == 0.2.3

CPython == 3.6.x/3.5.x


Requirement
------------
CPython == 3.6.x/3.5.x

C/C++ Compiler 

- My version was built on clang-3.8.1/GCC-6.3.0 on linux-deepin


Grammar
------------

**with quite few new additional keywords here**

* **Where Syntax**

    .. code:: python

        (test) where:
            statements
        ...
        # "test" is the top one of expressions in Python Grammar.

- Take a look at here:
    the **where** blocks would be **executed before the expression at the head**, 
    but it should be **located at the end**.
- Q :Why did I bring "where" syntax into Python?
- A :For **combining the expressions and statements** in Python and enhanced the readability of procedure. 

- See the following codes:

    .. code:: python

        # 圆柱面积 / surface area of a cylinder 
        from math import pi
        r = 1  # the radius
        h = 10 # the height

        S = (2*S_top + S_side) where:
            S_top  = pi*r**2
            S_side = C * h where:
                C = 2*pi*r

- And where syntax makes it possible for **Lambda** in Python to do everything that **def** can do.

    .. code:: python

        # multi-row lambda in python
    
        lambda x:  someFunc(x) where:
            def someFunc(var):
               pass
    
        lambda x:  ret where:
            def someFunc(var):
               ...
            ret = someFunc(x)
    
However, in Flowpython, there are some other way more interesting supplied to define a "lambda" than "lambda x: f(x)" :

* **Lambda Syntax**

    .. code:: python

        # Lambda

        lambda x,y,z : lambda a,b,c : x*a + y*b + z*c
        # which equals to 
        .x,y,z -> .a,b,c ->  x*a + y*b + z*c
        # which equals to 
        as-with x,y,z def as a,b,c def x*a + y*b + z*c

        #look at this example:
    
        as-with x def as y def as z def x+y+z
        # which equals to 
        as-with x def as-with y def as-with z def x+y+z

And we know that there are some powerful tools in some FP languages, like 

* **Pattern matching**

    .. code:: python

        condef +[<] 1:
            case a:2   => 
                assert a == 1 and a < 2
            +(.x->type(x))
            case a:int =>
                assert a == 1 and type(a) == int
        condef 1:
            +(.x->2*x)
            case a:3   => 
                assert a == 1 and a*2 == 3
            +[is not]
            case a:2   =>
                assert a == 1 and a is not 2
            otherwise  =>
                ...
        
        # new syntax: matching filter
        condef[] [1,2,3] :
            +(type) 
            case (*a,b)->a:list =>
                assert type(a) == list
            otherwise           =>
                assert False,"emmmm"


There are more optional grammars, just see GitHub `Link  <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md>`_. 
        
More about Pattern Matching to see `TestFile <https://github.com/thautwarm/flowpython/blob/master/test/test_patm.py>`_
And `Distribute History <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md#powerful-pattern-matching>`_

Another useful tool in Flowpython is **Arrow Transform**, which enhances the readability greatly and makes it possible 
to **Avoid Prolix Parentheses**.  

* **Arrow Transform**
    
    .. code:: python

        range(100) -> reduce(.x,y->x+y, _) -> print(_) where:
            from functools import reduce

        [1,2,3] -> map(.x->x+1, _) -> list(_) -> print(_)

Read `Arrow Transform  <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md#arrow-transform>`_ to get a konwledge of this grammar.

            
    
Revision
------------

See `Distribution History <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md>`_  here.


Compile FlowPython For Yourself
--------------------------------------

**For Windows User**
    - You'd better use Visual Studio to make the Python project, and it must be the easiest thing in the world, I think.
    
    - I have tried with **Cygwin** but finally failed. 

**For Linux User**
    Firstly, you should have a C/C++ compiler like: 
    
    - https://gcc.gnu.org/
    
    - http://releases.llvm.org/

    To give some advice, you can easily get C/C++ compiler with    
    
    - **MinGW/Cygwin** on **windows** (Failed, please have a try with Visual Studio)

    - **sudo apt-get install gcc/clang** on **Ubuntu/Debian/Deepin** (maybe it also works for MacOS).

Next, you can get the Flowpython sources which can be directly compiled in the same way as CPython, because Flowpython is truly an adjustment about CPython.

The sources can be found at `ForCPython 3.5 <https://github.com/thautwarm/cpython/tree/3.5>`_  and `ForCPython 3.6 <https://github.com/thautwarm/cpython/tree/3.6>`_.
Clone them and just type command `./configure CC=clang` and `make` is okay.

.. code:: shell

    ./configure CC=clang
    make
    ...
    python
    Python 3.5.4+ (heads/3.5-dirty:0a8ff1b, Oct  8 2017, 13:56:29) 
    [GCC 4.2.1 Compatible Clang 3.8.0 (tags/RELEASE_380/final)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> .x -> x+1
    <function <lambda> at 0x7f159379aae8>

But for someone who want to get CPython source for yourself for some special reasons, 
there might be something useful in the following sections.

For Developers
---------------

You Could get a CPython distribution like Python-3.6.x and Python-3.5.x at
    
    - https://www.python.org/

And then you should **replace the files of the standard CPython distribution with those of Flowpython's** (They are at `flowpython/flowpython/$pythonVersion/`).

If you change the variable of **pythonDistPath** in the file **config.py** with  the path of your Python distribution, 

just run this command:

.. code:: shell

    ./conf commit -v try_flowPython

Everyting about Flowpython can be found in the directory "/flowpy".

Finally open the CMD/Terminal at the root of CPython distribution,

run the following commands:
    
.. code:: shell

    ./configure CC=<your C/C++ compiler>
    make regen-gramamr
    make regen-ast
    make
    ./python

If you change the variable of **pythonDistPath** in the file **config.py** with  the path of your Python distribution, 

just run this command:

.. code:: shell

    ./conf make -m all -pyv [py36 | py35]
    
And then you can enjoy Flowpython!


I wrote config.py as the project-manage tool of Flowpython.

It assembled the following modules:
    - make
    - customer version controler 
    - debug&unittest

It can be used like these way:

.. code:: shell

        ./conf commit -v <version_name> -pyv [py35 | py36]
        ./conf recover -pyv [py35 | py36]
        ./conf test -pyv [py35 | py36]
        ./conf make -m clean -pyv [py35 | py36]
        ./conf make -m ast   -pyv [py35 | py36]
        ...

It seems to be kind of complicated but it's quite easy to understand and operate in fact.












