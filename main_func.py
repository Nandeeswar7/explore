def git_tube(x,y,p):

    if p==1:
        return (x+y)**2

    elif p==2:
        return (x+y)**3

    else:
        return "invalid p"


x = int(input("x : "))
y = int(input("y : "))
p = int(input("p(1 or 2) : "))

o = git_tube(x,y,p)

print(o)
    
