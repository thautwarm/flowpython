
f = .x -> r where:
    condic x:
        [==]
        case []             =>  r = 0

        +[==]
        case (a,*b) -> b:[] =>  r = a

        otherwise           =>  r= a + f(b)

