import cv2
import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import csv

def ngbr(a,n):
    x=a[0]
    y=a[1]
    l=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    ll=[]
    for i in range (4):
        if(l[i][0]>=0 and l[i][1]>=0 and l[i][0]<n and l[i][1]<n):
            ll.append(l[i])
            
    return ll

def drunkers_walk_grid(n):
    if(n<=35):
        size_of_node=20
    elif(n<=50):
        size_of_node=10
    else:
        size_of_node=1



    return_path=1
    project_name="Random_Walker_"+str(n)
    inl_image_name="Traversal_Grid_Size"+str(n)
    image_name="Traversal_Grid_Size"+str(n)
    g= nx.grid_2d_graph(n,n)
    l=list(g.nodes())

    pos = dict( (xx, xx) for xx in g.nodes() )
    a=random.choice(l)
    ba=random.choice(ngbr(a,n))
    destination=random.choice(l)
    while(a==destination):
        destination=random.choice(l)

    kola=["green"]*len(l)
    kola[(n*a[0])+a[1]]="blue"
    kola[(n*destination[0])+destination[1]]="orange"
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
    found=0
    play=1
    start_time = time.time()
    total_time_taken=0
    time_ptr=0
    while True:
        if(done==1):
            lll=ngbr(a,n)
            done=0
        #return_path=1
        if(found==1 and time_ptr==0):
            time_ptr=1
            end_time = time.time()
            total_time_taken=end_time - start_time
            print("Time taken is ",total_time_taken)
        for i in range (len(lll)):
            element=lll[i]
            if(kola[(n*element[0])+element[1]]!="red"):
                #return_path=0
                break
        if (total_edges<final_edges and found==0 and play==1):
            ba=random.choice(lll)
            mad=0
            while ba==a:
                ba=random.choice(lll)
            if a!=ba:
                #print(a,ba,"ng of a is ",ngbr(a,n))
                if  kola[(n*ba[0])+ba[1]]=="green":
                    done=1
                    kola[(n*ba[0])+ba[1]]="red"
                    g.add_edge(a,ba)
                    total_edges=total_edges+1
                    covered=covered+1
                    i=i-1
                    a=ba
                    mad=1
                elif kola[(n*ba[0])+ba[1]]=="orange":
                    done=1
                    g.add_edge(a,ba)
                    total_edges=total_edges+1
                    covered=covered+1
                    i=i-1
                    a=ba
                    mad=1
                    print("Destination found by drunker")
                    found=1

                elif (g.has_edge(a, ba)):
                    if(return_path==1):
                        #return_path=0
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
        elif special_key==32:
            if(play==1):
                play=0
                break_time=time.time()
            else:
                start_time=start_time+(time.time()-break_time)
                play=1
            print("play toggled")
        elif special_key==ord("r"):
            print("r is now pressed")       
            found=0     
            time_ptr=0
            a=random.choice(l)
            ba=random.choice(ngbr(a,n))
            kola=["green"]*len(l)
            kola[(n*a[0])+a[1]]="blue"
            destination=random.choice(l)
            while(a==destination):
                destination=random.choice(l)
            kola[(n*destination[0])+destination[1]]="orange"
            gola={}
            i=len(l)-1
            edg=list(g.edges())
            for i in range (len(edg)):
                gola[edg[i]]="green"
            g.remove_edges_from(edg)
            total_edges=0
            covered=1
            done=1
            start_time = time.time()
    cv2.destroyAllWindows()
    return total_time_taken

n=10
no_of_attempts=3
#ans_time=drunkers_walk_grid(n)
#n=int(input("enter the value of n ,It will make a n*n grid "))


fields = ['Value of N(Grid Crossection)'] 
    
# data rows of csv file 
rows = [] 
for i in range (n):
    rows.append([i+1])

for i in range (no_of_attempts):
    fields.append("Time in Attempt "+str(i+1))
fields.append("Average Time")
for i in range (n):
    suum=0
    for j in range (no_of_attempts):
        if((i+1)<2):
            ans_time=0
        else:
            ans_time=drunkers_walk_grid(i+1)
        rows[i].append(ans_time)
        suum=suum+ans_time
    if(no_of_attempts==0):
        rows[i].append(0)
    else:
        rows[i].append(suum/no_of_attempts)
    
# name of csv file 
filename = "Grid_size_VS_Time.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)