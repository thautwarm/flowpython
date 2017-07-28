

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

1. where expression

.. code:: flowpy

    (test) where:
        as <caseClass> => test
        ...
        as-def <function> => test
        ...
        with-in
            statements
            ...
        with-def

    # "test" is the top one of expression in Python Grammar.

*Take a look at here*:

the **with-in-with-def** blocks would be **executed before the other parts** in "where" syntax, 
but it should be **located as the end**.

- Q :Why did I bring "where" syntax into Python?
- A :For **combined the expressions and statements** in Python and enhanced the readability of procedure. 

See the following codes:

.. code:: flowpy

    # 圆柱面积 / surface area of a cylinder 
    from math import pi
    r = 1 # the radius
    h =   # the height

    S = (2*S_top + S_side) where:
        with-in
            S_top  = pi*r**2
            S_side = C * h where:
                with-in
                        C = 2*pi*r
                with-def
        with-def
    








