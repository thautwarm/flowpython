# Install & Uninstall

- Just for Windows 32bit/64bit and Linux 64bit for CPython 3.6.2.
- Will support CPython 3.5.2 and CPython 3.7 sooner.


- use `setup.py`
```	
	python setup.py install
```

- use `pip`
```
	pip install flowpython -i <mirror-url>
```

- enable/disable Flowpython grammar
```
	python -m flowpython -m enable/disable
```



# **Flowpython Porject**

See [Flowpython project](/flowpython/ReadMe.rst) here. 

# **History**


## Feature - List
- [Old-Works](#old-works)
- [Add-where-syntax](#add-where-syntax)
- [Fix-lambda-closure](#fix-where-syntax-in-lambda-closure)
- [Add-switch-syntax](#add-switch-syntax)
- [Fix-keyword-conflictions](#fix-keyword-conflictions)
- [Powerful-pattern-matching](#powerful-pattern-matching)
- [Arrow-Transform](#arrow-transform)
- [Matching-Filter](#matching-filter)
- [Library fp.py](#fp-module)
- [Branches](#branches)

----

### Old Works

fix `if-expr` and add some new ways to define `lambda`.

- `if-expr`  
    you can write
    ```python

            ret  =  e1 if j1 else
                    e2 if j2 else
                    e3 
    ```
    instead of

    ```python

            ret  =  e1 if j1 else \
                    e2 if j2 else \
                    e3 
    ```
- `lambda`  

    ```python
             .x -> x+1
             as-with x def x+1
             as-with x def as y def x+y
    ```

### Add Where Syntax  
    
- add **where** syntax
- date : before 2017-07-30
- principle:
    - **Parse**:
        - change Grammar/Grammar
            1. Firstly, add a new grammar *where_stmt*.  
            &emsp;&emsp;``where_stmt: 'where' ':' suite``  
            add this grammar to `compound_stmt`
            2. Then change the end of *simple_stmt*,replace *NEWLINE* with   
            &emsp;&emsp;``(NEWLINE | where_stmt)``
        - change Parser/Python.asdl
            1. Add a data structure *Where* as a kind of *expr*  
            ```
            Where(expr target, stmt* body)
            ```
             
    - **AST**:
        - change Python/ast.c
            found the function `ast_for_stmt`, `ast_for_expr_stmt`,`ast_for_flow_stmt`,`ast_for_assert_stmt`, change it as what I did in **flowpython/Python/ast.c**. It tells the Python compiler how to get the data structure from the parsed codes.
    - **Compile&Interpret**
        - change Python/compile.c  
                This part is kind of complicated to bring out, and I think that you'd better use *version controler* to detect out what's the differences between Flowpython and CPython 3.6.2.
        - change Python/symtable.c  
                Quite similar to *compile.c*. 
            
        - P.S for *Compile&Interpret*  
                If your want to get a complete knowledge about how Python works, you should understand how the two C Module works firstly.
    


### Fix Where Syntax in Lambda Closure
- date : 2017-07-30
    - Particularly, fixed **where** syntax for *lambda*, to make the **scope** of statements in *where* syntax to be the **closure of the innermost lambda**.  
    You can write following codes:
    ```python
    as-with x def as y def as z def ret_value where:
        ret_value = x + y +z
    ```
    instead of:
    ```
    as-with x def as y def as z def tmp(x+y+z) where:
        def tmp(x,y,z):
            return x +y +z
    ```
    Does it seem to be currying?
    ```
    .x->.y->.z-> ret where:
        ret = x +y +z
    ```
  

### Add Switch Syntax
- date: 2017-08-06
- To give some support for Pattern Matching to Python.
- principle:
    the principle of following codes  
    ```C  
        switch (this):
            case <case1> : 
                ...
            case <case2> :
                ...
            ...
            otherwise:
                ...
    ```
    works similar to
    ```python
        if this == <case1>:
            ...
        else:
            if this == <case2>:
                ...
            else:
                ...
                else:
                    ...
    ```
    Finally, I'd like to tell you that, in Python,
    the **ast** of **if-elif-else** will be transformed to that of **if-else-[if-else]**, which I don't think to be a good way to generate **ast**. 

### Fix Keyword Conflictions
- date: 2017-08-07
* **fix-keyword**
* **switch-case-otherwise -> condic-case-otherwise**

    Some new keywords brought by FlowPy, such as **where, switch, case, otherwise**, used to conflict with **Standard Library**
    and some important Libaraies from **Third Party**.

    I fixed these conflictions with making the Parser module to ignore some grammar structures which would be checked in AST module.   

    So you can write these codes now:

    ```python
        # no confliction
        
        where = 1
        where += where where:
            where += where
        
        case = 1
        otherwise = 2
        condic 1:
            case case => case 
            otherwise => otherwise
    ```

    Take care that each syntax in [ **where, case, otherwise** ] are not real keywords, and **condic** is.

    ```python
        condic = 1
        >>> SyntaxError: invalid syntax
    ```

### Powerful Pattern Matching
- date: 2017-08-08
* **pattern-matching**

    There are four kinds of matching rules in Flowpy:
    1. **comparing operator matching**
    ```C

        condic [ == ] expr:
            [>] 
            case test1 =>
                    <body1>
            case test2 => 
                    <body2>
            otherwise  =>
                    <body3>
    ```
    which equals to 
    ```python

        if (expr > test1 )
            <body1>
        elif (expr == test2 )
            <body2>
        else:
            <body3>
    ```
    Each in `[], (), +(), +[], {} ` are called the **operator comparing mode**.     
    **Giving a mode followed by *condic* keyword means giving a default mode.**  
    The relus are concluded [here](#conclusion-for-pattern-matching)  
    
        for operator comparing mode "[<optional>]"
        <optional> can be
        ==      
        >
        <
        >=
        <=
        in
        not in
        is 
        is not
    
    2. **callable object matching**
    ```C
    condic (f) expr:
        case test1 => 
            <body1>
        [!=] 
        case test2 =>
            <body2>
    ```
    equals
    ```python
    if (f(expr) == test1):
        <body1>
    elif expr != test2:
        <body2>
    ```

    3. **dual callable comparing matching**

    ```C
    condic {f} expr:
        case test1 => 
            <body1>
    ```
    equals
    ```python
    if f(expr, test1):
        <body1>
    ```

    4. **Python Pattern Matching**
    - This one is the implementation for traditional pattern matching in CPython.
    ```C
    condic +[>] 1:
        case a:2   =>
            <body1>
        +(type) 
        case a:int =>
            <body2>
    ```
    The codes above can be explained as following process:  
    1. `if` we can do assignment `a = 1` and expression `a > 2` can be satisfied, then do `<body1>`.
    2. `else if` we can do assignment `a = 1` and expression `type(a) == int` can be satisfied, then do `<body2>`.  
    - There are much more ways to use **Pattern Matching**, take a look
    at [**test_patm.py**](https://github.com/thautwarm/flowpython/blob/master/test/test_patm.py)
    3. **Take care**  
    if you write the following codes without default mode,
    ```C
    condic [1,2,3]:
        ...
    condic {1,2,3}:
        ...
    condic (1,2,3):
        ...
    ```
    it will lead to **syntax Error**. But you can use this instead:
    ```C
    condic() [1,2,3]:
        ...
    condic[] {1,2,3}:
        ...
    condic{} (1,2,3):
        ...
    ```

#### Conclusion for Pattern Matching

| Matching Method                    | Identity      |       
| -------------                      |:-------------:| 
| comparing operator matching        | [`operator`]  | 
| callable object matching           | (`callable`)  | 
| dual callable comparing matching   | {`callable`}  | 
| python pattern matching(comparing) | +[`operator`] | 
| python pattern matching(callable)  | +(`callable`) |          

### Arrow Transform
- date: 2017-08-10
- **arrow transform expression**  
    This one looks like **lambda**, and they have quite a lot of features in common.  
    Look at this example:  
    - `arrow transform`
    ```C
    >> 1 -> _+1
    >> 2
    >> x = [1,2,3]
    >> x -> map(.x->x+1, _) ->  list(_)
    >> [2,3,4]
    ```
    - `lambda`
    ```python
    >> .x -> x
    >> _(1)
    >> 1
    >> var = [1,2,3]
    >> .x -> map(.x->x+1, x) -> list(_)
    >> _(var)
    >> [2,3,4]
    ```
    To conclude, `lambda` is the `lazy` form of `arrow transform`.  
    The grammar identity `.` means **Take It As Lazy**

### Matching Filter
- date: 2017-08-10
    ```C
        condic[] [1,2,3]:
            +(type)
            case (*a,b) -> a:list => 
                print("just match 'a' with 'list' ")
            
            otherwise           =>
                print("emmmmmm,,")

    ```

### FP Module
- date: 2017-08-13
- library: fp.py

To support some basic operations in Functional Programming, here are methods implemented in `flowpython.fp`.

```C
from flowpython.fp import compose, andThen, foldr, foldl, flat_map, flatten
from flowpython.fp import strict, norecursion

strict_flatten = strict.flatten
strict_fastmap = strict.fastmap 
strict_flat_map= strict.flat_map  
norec_flatten  =  norecursion.lazy.flatten


# fastmap( use generator instead of map in original Python )
fastmap([1,2,3], .x -> x+1) -> list(_)
# -> [2,3,4]

strict_flat_map([1,2,3], .x->x+1) # -> [2,3,4] 

# flatten
flatten([1,2,[3,4],[[5],[6]]]) -> list(_)
# -> [1,2,3,4,5,6]

# compose : Callable->Callable->Any
f1 -> compose(_)(f2)

# andThen : Callable->Callable->Any
f1 -> andThen(_)(f2)

# foreach : Callable->Callable->Any
range(20) -> foreach(_)(print) 
# -> 0 \n 1 \n 2 ...


# fold : Dual Callable->(zero:Any)->Iterator->Any
foldr # (not recommended)
foldl # (not recommended)

range(20) -> foldr(. x,y -> print(x) or x+y)(0)(_) 
range(20) -> foldr(. x,y -> print(y) or x+y)(0)(_)

# flat_map : flat_map -> Iterator -> Callable -> Iterator
# default lazy
flat_map([[1,2,[3,4],[5,6]],[7,8]])(.x->x+1) -> list(_)
# -> [2,3,4,5,6,7,8,9]

# object in norecursion class use no recursive methods.
norec_flatten([[1,[2],[[3]],[[[4]]]]] -> list(_) 



```

### Branches
- date: 2017-08-15
An easy way to define `if-elif-else` statements:

```python

    otherwise = True

    | x == 1           => x += 1
    | type(x) is str   => x = int(x) 
    | otherwise        =>
            x = 2*x
            y = 1
    def defined(key):
        return key in globals()

    print(x)
    print(defined("y")) 

    func = .x -> ret where:
        otherwise = True
        | x is 0                => ret = 0.0
        | type(x) in (str,int)  => ret = float(x)
        | otherwise             => ret = x
        
```








            
            





           






