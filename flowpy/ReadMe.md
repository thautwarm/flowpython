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
            1. Add a param `stmt* where` at the end for data structure in the following list,  
            which can be found at Grammar/Grammar.  
                1. Assign
                2. AugAssign
                3. AnnAssign
                4. Raise
                5. Assert
             
        - **AST**:
            - change Python/ast.c
                1. found the function `ast_for_stmt`, `ast_for_expr_stmt`,`ast_for_flow_stmt`,`ast_for_assert_stmt`, change it as what I did in **flowpy/Python/ast.c**. It tells the Python compiler how to get the data structure from the parsed codes.
                


    - P.S:
        - **[1]** we don't need gramamr like these:  
            ```
            raise where:
                ...
            break where:
                ...
            ```










            
            





           






