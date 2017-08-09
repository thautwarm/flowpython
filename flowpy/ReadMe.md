# **History**

## Feature - List
- [Add-where-syntax](#add-where-syntax)
- [Fix-lambda-closure](#fix-where-syntax-in-lambda-closure)
- [Add-switch-syntax](#add-switch-syntax)
- [Fix-keyword-conflictions](#fix-keyword-conflictions)
- [Powerful-pattern-matching](#powerful-pattern-matching)

----

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
            found the function `ast_for_stmt`, `ast_for_expr_stmt`,`ast_for_flow_stmt`,`ast_for_assert_stmt`, change it as what I did in **flowpy/Python/ast.c**. It tells the Python compiler how to get the data structure from the parsed codes.
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
        a = ret where:
            ret = where
        
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
            [>] case test1 =>
                    <body1>
            case     test2 => 
                    <body2>
            otherwise =>
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
        case      test1 => 
            <body1>
        [!=] case test2 =>
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
        case         a:2   =>
            <body1>
        +(type) case a:int =>
            <body2>
    ```
    The codes above can be explained as following process:  
    1. `if` we can do assignment `a = 1` and expression `a > 2` can be satisfied, then do `<body1>`.
    2. `else if` we can do assignment `a = 1` and expression `type(a) == int` can be satisfied, then do `<body2>`.  
    - There are much more ways to use **Pattern Matching**, take a look
    at [**test_patm.py**](https://github.com/thautwarm/flowpython/blob/master/test/test_patm.py)

#### Conclusion for Pattern Matching

| Matching Method                    | Identity      |       
| -------------                      |:-------------:| 
| comparing operator matching        | [`operator`]  | 
| callable object matching           | (`callable`)  | 
| dual callable comparing matching   | {`callable`}  | 
| python pattern matching(comparing) | +[`operator`] | 
| python pattern matching(callable)  | +(`callable`) |          

        
    

















            
            





           






