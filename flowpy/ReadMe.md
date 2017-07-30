# **History**

- *before 2017-07-30*
    - add **where** syntax
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
                1. found the function `ast_for_stmt`, `ast_for_expr_stmt`,`ast_for_flow_stmt`,`ast_for_assert_stmt`, change it as what I did in **flowpy/Python/ast.c**. It tells the Python compiler how to get the data structure from the parsed codes.
        - **Compile&Interpret**
            - change Python/compile.c  
                This part is kind of complicated to bring out, and I think that you'd better use *version controler* to detect out what's the differences between Flowpython and CPython 3.6.2.
            - change Python/symtable.c  
                Quite similar to *compile.c*. 
            
            - P.S for *Compile&Interpret*  
                If your want to get a complete knowledge about how Python works, you should understand how the two C Module works firstly.

- *2017-07-30*
    - Particularly, fixed **where** syntax for *lambda*, to make the **scope** of statements in *where* syntax to be the **closure of the innermost lambda**.  
    You can write following codes:
    ```python
    as-with x def as y def as z def ret_value where:
        ret_value = x + y +z
    ```
    instead of:
    ```
    as-with x def as y def as z def ret_value where:
        def tmp(x,y,z):
            return x +y +z
        ret_value = tmp(x+y+z) 
    ```
    Does it seem to be currying?
    ```
    .x->.y->.z-> ret where:
        ret = x +y +z
    ```













            
            





           






