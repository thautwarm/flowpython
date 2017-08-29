# Install & Uninstall

- Support Windows 32bit/64bit and Linux 64bit for CPython 3.6.x/3.5.x.
- Will support CPython 3.7 sooner.
- Will never support CPython 2.x :)


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



# **Flowpython Project**

- Version : 0.2.3

- See [Flowpython project](/flowpython/ReadMe.rst) here. 




# **History**


## Feature - List
- [Old-Works](#old-works)
- [Add-where-syntax](#add-where-syntax)
- [Fix-lambda-closure](#fix-where-syntax-in-lambda-closure)
- [Fix-keyword-conflictions](#fix-keyword-conflictions)
- [Powerful-pattern-matching](#powerful-pattern-matching)
- [Arrow-Transform](#arrow-transform)
- [Matching-Filter](#matching-filter)
- [Library fp.py](#fp-module)
- [Branches](#branches)
- [Pipeline/Monad](#pipeline)
- [Logs](#logs)
- [Auto Compose](#auto-compose)


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
    

### Auto Compose

    ```python
    from flowpython.composing import auto_logger, auto_compose, flow_map, flow_filter
    auto_logger(__builtin__.__dict__)
    
    >> sum.filter(.x->x,[0,1,2,3,0])
    >> 6
    ``` 

### Fix Where Syntax in Lambda Closure
- Particularly, fixed **where** syntax for *lambda*, to make the **scope** of statements in *where* syntax to be the **closure of the innermost lambda**.  
    You can write following codes:
    ```python
    as-with x def as y def as z def ret_value where:
        ret_value = x + y +z
    ```
    instead of:
    ```python
    as-with x def as y def as z def tmp(x+y+z) where:
        def tmp(x,y,z):
            return x +y +z
    ```
    Does it seem to be currying?
    ```
    .x->.y->.z-> ret where:
        ret = x +y +z
    ```
  
### Fix Keyword Conflictions
* **fix-keyword**
* **switch-case-otherwise -> condef-case-otherwise**

    Some new keywords brought by Flowpython, such as **where, condef, case, otherwise**, used to conflict with **Standard Library**
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
        condef 1:
            case case => case 
            otherwise => otherwise
    ```

    Take care that each syntax in [ **where, case, otherwise** ] are not real keywords, and **condef** is.

    ```python
        condef = 1
        >>> SyntaxError: invalid syntax
    ```

### Powerful Pattern Matching

* **pattern-matching**

    There are four kinds of matching rules in Flowpython:
    1. **comparing operator matching**
    ```C

        condef [ == ] expr:
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
    **Giving a mode followed by *condef* keyword means giving a default mode.**  
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
    condef (f) expr:
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
    condef {f} expr:
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
    condef +[>] 1:
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
    condef [1,2,3]:
        ...
    condef {1,2,3}:
        ...
    condef (1,2,3):
        ...
    ```
    it will lead to **syntax Error**. But you can use this instead:
    ```C
    condef() [1,2,3]:
        ...
    condef[] {1,2,3}:
        ...
    condef{} (1,2,3):
        ...
    ```

#### Conclusion for Pattern Matching
<center>

| Matching Method                    | Identity      |       
| -------------                      |:-------------:| 
| comparing operator matching        | [`operator`]  | 
| callable object matching           | (`callable`)  | 
| dual callable comparing matching   | {`callable`}  | 
| python pattern matching(comparing) | +[`operator`] | 
| python pattern matching(callable)  | +(`callable`) |          
</center>

### Arrow Transform

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

    ```C
        condef[] [1,2,3]:
            +(type)
            case (*a,b) -> a:list => 
                print("just match 'a' with 'list' ")
            
            otherwise           =>
                print("emmmmmm,,")

    ```

### FP Module

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
fastmap(.x -> x+1, [1,2,3]) -> list(_)
# -> [2,3,4]

strict_flat_map(.x->x+1, [1,2,3]) # -> [2,3,4] 

# flatten
flatten([1,2,[3,4],[[5],[6]]]) -> list(_)
# -> [1,2,3,4,5,6]

# compose : Callable->Callable->Any
f1 -> compose(f2)(_)

# andThen : Callable->Callable->Any
f1 -> andThen(f2)(_)

# foreach : Callable->Callable->Any
range(20) -> foreach(print)(_) 
# -> 0 \n 1 \n 2 ...


# fold : Dual Callable->(zero:Any)->Iterator->Any
foldr # (not recommended)
foldl # (not recommended)

range(20) -> foldr(. x,y -> print(x) or x+y)(0)(_) 
range(20) -> foldr(. x,y -> print(y) or x+y)(0)(_)

# flat_map : Iterator -> Callable -> Iterator
# default lazy
flat_map(.x->x+1)([[1,2,[3,4],[5,6]],[7,8]]) -> list(_)
# -> [2,3,4,5,6,7,8,9]

# object in norecursion class use no recursive methods.
norec_flatten([[1,[2],[[3]],[[[4]]]]] -> list(_) 



```

### Branches
 
An easy way to define `if-elif-else` statements:  
( It's not `guard` in Haskell ! )
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


## Pipeline

Sorry for the shortage of documents for new gramamr, and I'm busy with my new semester.   
It would be completed as sooner as possible.
```python
    
    >> 1 ->> .x -> x*10 => .x-> x+1 
    >> 11

```

```python

    >> range(100)  ->> f1 \
                    => f2 \
                    => groupby(.x->x)  \
                    => lambda Dict: map(.key->(key,len(Dict[key])), Dict) \
                    => dict \
                    => print where:
                    from flowpython.fp import groupby
                    f1 = . seq -> map(.x->x%2, seq)
                    f2 = . seq -> filter(.x -> x, seq)
    >> {1:50}

```



## Logs
- date : before 2017-07-30
- date : 2017-07-30
    - Add **where** syntax
- date: 2017-08-06
    - Fix `closure` for `where` syntax in case of **Lambda Definition**.
- date: 2017-08-07
    - Add `switch syntax`.
- date: 2017-08-08
    - Fix the keyword conflicts against the standard libraries and the packages from Third Party.
    - Change the grammar of `switch` syntax.  
        `switch-case-otherwise -> condef-case-otherwise`
- date: 2017-08-10
    - Add `pattern matching` syntax.
    - Add arrow transform expression.
    - Remove `switch` syntax(which can be totally replaced by `pattern matching`).
- date: 2017-08-10
    - Add matching filter syntax for `pattern matching` .
- date: 2017-08-13
    - Add module `fp.py`.
- date: 2017-08-15  
    - Add `branches` grammar.
- data: 2017-08-25
    - Add `pipeline` grammar.
    - Change keyword for pattern matching from `condic` to `condef`.



            
            





           






