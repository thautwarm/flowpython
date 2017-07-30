.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/thautwarm/flowpython/blob/master/LICENSE

Additional Grammar Compatible to CPython 
==========================================

VERSION
----------
flowpy  == 0.1

CPython == 3.6.2


Requirement
------------
CPython == 3.6

C/C++ Compiler 

- My version was built on clang-3.8.1/GCC-6.3.0 on linux-deepin


Grammar
------------

**with quite few new additional keywords here**

* where syntax

.. code:: python

    (test) where:
        statements
        ...

    # "test" is the top one of expressions in Python Grammar.

*Take a look at here*:

the **where** blocks would be **executed before the expression at the head**, 
but it should be **located at the end**.

- Q :Why did I bring "where" syntax into Python?
- A :For **combining the expressions and statements** in Python and enhanced the readability of procedure. 

See the following codes:

.. code:: python

    # 圆柱面积 / surface area of a cylinder 
    from math import pi
    r = 1  # the radius
    h = 10 # the height

    S = (2*S_top + S_side) where:
        S_top  = pi*r**2
        S_side = C * h where:
            C = 2*pi*r

And where syntax makes it possible for **Lambda** in Python to do everything **def** can do.

.. code:: python

    # multi-row lambda in python
    
    lambda x:  someFunc(x) where:
        def someFunc(var):
            pass
    

However, in Flowpython, there are some other way more interesting supplied to define a "lambda" than "lambda x: f(x)" :

.. code:: python

    # Lambda

    lambda x,y,z : lambda a,b,c : x*a + y*b + z*c
    # which equals to 
    .x,y,z -> .a,b,c ->  x*a + y*b + z*c
    # which equals to 
    as-with x,y,z def as a,b,c def x*a + y*b + z*c

    #look at this example:
    as-with x def as y def as z def x+y+z
    # which is equals to 
    as-with x def as-with y def as-with z def x+y+z




Revision
------------


- date: 2017-07-28
    * **where**  syntax 

    **with-in-with-def** => **with-in-with-break**

- date: 2017-7-29
    * **test if else test**
        * make a change to support like
        
        .. code:: python

            ret  =  e1 if j1 else
                    e2 if j2 else
                    e3 
    
        instead of

        .. code:: python

            ret  =  e1 if j1 else \
                    e2 if j2 else \
                    e3 

    * **where** syntax 
        * **with-in-with-def** => **where - syntax**

    * **lambda**
        * add two new methods to define "lambda".

        .. code:: python

             .x -> x+1
             as-with x def x+1
             as-with x def as y def x+y



How To Get FlowPy
--------------

Firstly, you should have a C/C++ compiler like: 
    
    - https://gcc.gnu.org/
    
    - http://releases.llvm.org/

To give some advice, you can easily get C/C++ compiler with    
    
    - **MinGW/Cygwin** on **windows**

    - **sudo apt-get install gcc/clang** on **Ubuntu/Debian/Deepin** (maybe it also works for MacOS).

And then you should have a CPython distribution like Python-3.6.2, like:
    
    - https://www.python.org/

And then you should replace the files of the standard CPython distribution with Flowpython.

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

    ./conf make -m all
    
And then you can enjoy Flowpython!


For Developers
---------------

I wrote config.py as the project-manage tool of Flowpython.

It assembled the following modules:
    - make
    - git
    - customer version controler 
    - debug&unittest

It can be used like these way:

.. code:: shell

        ./conf commit -v <version_name>
        ./conf recover 
        ./conf debug -f test_where
        ./conf make -m clean
        ./conf make -m ast
        ...

It seems to be kind of complicated but it's quite easy to understand and operate in fact.












