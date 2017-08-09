condic (.x->2*x) 1:
    case 2 => 
            print("(1*2) == 2")
            assert (1*2) == 2
    otherwise =>
        assert False, "cannot match"

condic[>] 1:
    case 0 => 
        print('1 > 0')
        assert 1 > 0
    otherwise =>
        assert False, "cannot match"

condic[<] 10:
    case 5 => 
        assert 10 < 5, "Error Match: 10 < 5"
    otherwise =>
        print("10 > 5")
        assert 10 > 5


condic +[==] 1:
    case a:1 => 
            print(" 'a == 1' and  can do assignment 'a = 1' ")
            assert a==1
    otherwise =>
        assert False, "cannot match"

condic +() [1,2,3]:
    case (a,b) =>
            print("can do assignment (a,b) = [1,2,3]")
            assert [a,b] == [1,2,3]
    case (*a,b) =>
            print("can do assignment '(*a,b) = [1,2,3]' ")
            assert [*a,b] == [1,2,3]
    otherwise =>
        assert False, "cannot match"

condic () [1,2,3]:
    +(type) case a:list =>
            print("can do assignment 'a = [1,2,3]' and 'type(a) == list'")
            assert( type(a) == list and a == [1,2,3] )
    otherwise =>
        assert False, "cannot match"

tomap = .f -> .var -> ret where:
    ret = list(map(f, var))


condic +(tomap(type)) [1,2,3]:
    case (*a,b):[int]*3 =>
            print("can do assignment '(*a,b) = [1,2,3]' and tomap(type)((*a,b)) == [int]*3 ")
            assert [*a,b] == [1,2,3] and tomap(type)((*a,b)) == [int]*3
    otherwise =>
            assert False, "+(tomap(type)) case (*a,b):[int]*3 \n cannot match [1,2,3]!"



