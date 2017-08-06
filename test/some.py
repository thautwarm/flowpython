print("FlowPython as-with-def Lambda")
t=as-with a,b,c def as d,e,f  def as g,h,i def ret_value where:
        middle_value1 = a*e*i + b*f*g + c*d*h
        middle_value2 = g*e*c + h*f*a + i*d*b
        ret_value = middle_value1 - middle_value2 
print(t (1,2,3)\
        (0,2,1)\
        (0,0,3) == 6)


t=.a,b,c -> .d,e,f -> .g,h,i -> ret_value where:
        middle_value1 = a*e*i + b*f*g + c*d*h
        middle_value2 = g*e*c + h*f*a + i*d*b
        ret_value = middle_value1 - middle_value2 
print(t (1,2,3)\
        (0,2,1)\
        (0,0,3) == 6)

print("Original CPython Lambda")
t=lambda a,b,c : lambda d,e,f  : lambda g,h,i : ret_value where:
        middle_value1 = a*e*i + b*f*g + c*d*h
        middle_value2 = g*e*c + h*f*a + i*d*b
        ret_value = middle_value1 - middle_value2 
print(t (1,2,3)\
        (0,2,1)\
        (0,0,3) == 6)
        

