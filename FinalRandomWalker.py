import cv2
import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def ngbr(a,n):
    x=a[0]
    y=a[1]
    l=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    ll=[]
    for i in range (4):
        if(l[i][0]>=0 and l[i][1]>=0 and l[i][0]<n and l[i][1]<n):
            ll.append(l[i])
            
    return ll
        

n=5
n=int(input("enter the value of n ,It will make a n*n grid "))
if(n<=35):
    size_of_node=20
elif(n<=50):
    size_of_node=10
else:
    size_of_node=1



return_path=0
project_name="Random_Walker_"+str(n)
inl_image_name="books_read"+str(n)
image_name="books_read"+str(n)
g= nx.grid_2d_graph(n,n)
l=list(g.nodes())

pos = dict( (xx, xx) for xx in g.nodes() )
a=random.choice(l)
ba=random.choice(ngbr(a,n))
kola=["green"]*len(l)
kola[(n*a[0])+a[1]]="blue"
gola={}
i=len(l)-1
edg=list(g.edges())
for i in range (len(edg)):
    gola[edg[i]]="green"
g.remove_edges_from(edg)
covered=1
max_covered=0

strange=0
total_edges=0
final_edges=(n*n)-1
done=1
while True:
    if(done==1):
        lll=ngbr(a,n)
        done=0
    return_path=1
    for i in range (len(lll)):
        element=lll[i]
        if(kola[(n*element[0])+element[1]]=="green"):
            #return_path=0
            break
    if total_edges<final_edges:
        ba=random.choice(lll)
        mad=0
        while ba==a:
            ba=random.choice(lll)
        if a!=ba:
            print(a,ba,"ng of a is ",ngbr(a,n))
            if  kola[(n*ba[0])+ba[1]]=="green":
                done=1
                kola[(n*ba[0])+ba[1]]="red"
                g.add_edge(a,ba)
                total_edges=total_edges+1
                covered=covered+1
                i=i-1
                a=ba
                mad=1
                done=1
            elif (g.has_edge(a, ba)):
                if(return_path==1):
                    return_path=1
                    g.remove_edge(a,ba)
                    total_edges=total_edges-1
                    covered=covered-1
                    kola[(n*a[0])+a[1]]="green"
                    a=ba
                    done=1
            else:
                lll.remove(ba)
        nx.draw(g,pos,node_color=kola,node_size=size_of_node)
        if mad==1:
            mad=1
        #plt.plot(g)
        plt.savefig(image_name+".png")
        if(max_covered<covered):
            max_covered=covered
            #plt.savefig("max_coverage = "+str(float((100*covered)/(final_edges+1)))+".png")
        plt.clf()
    god=cv2.imread(image_name+".png")
    god=cv2.resize(god,None,fx=1.3,fy=1.3,interpolation=cv2.INTER_CUBIC)
    cv2.imshow(project_name,god)
    
    special_key=cv2.waitKey(5)
    if special_key==27:
        print("escape is pressed")
        break
    elif special_key==ord("r"):
        print("r is now pressed")            
        a=random.choice(l)
        ba=random.choice(ngbr(a,n))
        kola=["green"]*len(l)
        kola[(n*a[0])+a[1]]="blue"
        gola={}
        i=len(l)-1
        edg=list(g.edges())
        for i in range (len(edg)):
            gola[edg[i]]="green"
        g.remove_edges_from(edg)
        total_edges=0
        covered=1
        done=1
cv2.destroyAllWindows()
