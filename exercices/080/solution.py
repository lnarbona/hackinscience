b = ("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
a = b.split(",")
for i in a:
    for j in a:
        if (i<j):
            print(str(i) + str(j))
