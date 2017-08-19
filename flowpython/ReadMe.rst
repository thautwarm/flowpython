
Additional Grammar Compatible to CPython 
==========================================


How to Get Flowpython
-----------------------

- Intsall 

.. code:: shell
    
    pip install flowpython


- Enable/Disable Flowpython grammar

.. code:: shell

    python -m flowpython -m enable/disable


VERSION
----------
flowpython  == 0.2.1

CPython == 3.6.2


Requirement
------------
CPython == 3.6

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

        condic +[<] 1:
            case a:2   => 
                assert a == 1 and a < 2
            +(.x->type(x))
            case a:int =>
                assert a == 1 and type(a) == int
        condic 1:
            +(.x->2*x)
            case a:3   => 
                assert a == 1 and a*2 == 3
            +[is not]
            case a:2   =>
                assert a == 1 and a is not 2
            otherwise  =>
                ...
        
        # new syntax: matching filter
        condic[] [1,2,3] :
            +(type) 
            case (*a,b)->a:list =>
                assert type(a) == list
            otherwise           =>
                assert False,"emmmm"

        
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

More `Distribution History <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md>`_  here.

- date: 2017-07-28
    * **where**  syntax 

    **with-in-with-def** => **with-in-with-break**

- date: 2017-07-29
    * fix **test if else test**

    * **where** syntax 
        * **with-in-with-def** => **where - syntax**

    * **lambda**
        * add two new methods to define "lambda".

- date: 2017-08-06
    * **switch-case-otherwise**
- date: 2017-08-07
    * **fix-keyword**
    * **switch-case-otherwise -> condic-case-otherwise**
    * See `fix-keyword-contradictions <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md#fix-keyword-conflictions>`_

- date: 2017-08-09
    * **add-pattern-matching-syntax**
    * See `Powerful Pattern Matching <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md#powerful-pattern-matching>`_
- date: 2017-08-10
    * **add-arrow-transform(strict form of lambda)**
    * See `Arrow Transform <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md#arrow-transform>`_
    * add a new syntax to pattern matching : `Matching Filter <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md#matching-filter>`_

- date: 2017-08-13
    * add a module named **flowpython.fp** to give basic support to Functional Programming.

- date: 2017-08-15
    * add a new way to define **if-elif-else** statements.
    * See `Branches <https://github.com/thautwarm/flowpython/blob/master/ReadMe.md#branches>`_

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
        ./conf test 
        ./conf make -m clean
        ./conf make -m ast
        ...

It seems to be kind of complicated but it's quite easy to understand and operate in fact.












