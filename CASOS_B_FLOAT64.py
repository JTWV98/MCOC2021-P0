import numpy as np
from numpy import matrix
from numpy import transpose
from numpy import mean
from numpy import linalg
from numpy import zeros
from scipy import linalg
from time import perf_counter
from scipy.linalg import inv,eigh
from scipy.linalg import solve
from numpy import ones
#from laplaciana import laplaciana
from numpy import float64, float64
import matplotlib.pylab as plt

def laplaciana(N, dtype):
    A = zeros((N,N) , dtype=dtype)
    
    for i in range(N):
        A[i,i] = 2
        for j in range(max(0,i-2),i):
            if abs(i-j) == 1:
                A[i,j] = -1
                A[j,i] = -1
        
        
    return(A)

def vector(N):
    vector=[]
    for i in range(N):
        vector.append(1)
    b = np.array(vector)
    return b

#B_CASO_1_FLOAT_64

Ns= [1, 10, 100,500,1000, 1200, 1300,1500, 2000, 2200, 2300, 2500, 3000, 3500,4000]
time=[]


fid = open("B_1_FLOAT64.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float64)
        b=ones(N)
        # print(A)
        t1=perf_counter()
        w, h=eigh(A)
        #print(Am1)

        t2=perf_counter()
        
        dt_ =t2-t1
        print()
        print("N =",N)
        print("Tiempo :", dt_,"[seg]")
        
        time.append(dt_)
        #fid.write(f"{N}     {dt_}\n" )
           
    i +=1 
   

# print (time)


dt_s=[]

def split_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

dt_s = list(split_list(time,len(Ns)))
# print(dt_s)


dt_prom=[]

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex=mean(transpuesta[i])
    dt_prom.append(cex)

    

    fid.write(f"{Ns[i]}     {cex}\n" )

fid.close()
 
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot()
plt.title("Desempeño B C1 FLOAT64")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño B C1 FLOAT64")
plt.show()



# #B_CASO_2_FLOAT_64_ev_overwrite_a=True

Ns= [1, 10, 100,500,1000, 1200, 1300,1500, 2000, 2200, 2300, 2500, 3000, 3500,4000]
time=[]


fid = open("B_2_FLOAT64_ev_overwrite_a=True.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float64)
        b=ones(N)
        # print(A)
        t1=perf_counter()
        w, h=eigh(A, driver='ev', overwrite_a=True)
        #print(Am1)

        t2=perf_counter()
        
        dt_ =t2-t1
        print()
        print("N =",N)
        print("Tiempo :", dt_,"[seg]")
        
        time.append(dt_)
        #fid.write(f"{N}     {dt_}\n" )
           
    i +=1 
   

# print (time)


dt_s=[]

def split_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

dt_s = list(split_list(time,len(Ns)))
# print(dt_s)


dt_prom=[]

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex=mean(transpuesta[i])
    dt_prom.append(cex)

    

    fid.write(f"{Ns[i]}     {cex}\n" )

fid.close()
 
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot()
plt.title("Desempeño B C2 FLOAT64 EV OVERWRITE TRUE")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño B C2 FLOAT64 EV OVERWRITE TRUE")
plt.show()



# #B_CASO_2_FLOAT_64_ev_overwrite_a=False

Ns= [1, 10, 100,500,1000, 1200, 1300,1500, 2000, 2200, 2300, 2500, 3000, 3500,4000]
time=[]


fid = open("B_2_FLOAT64_ev_overwrite_a=False.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float64)
        b=ones(N)
        # print(A)
        t1=perf_counter()
        w, h=eigh(A, driver='ev', overwrite_a=False)
        #print(Am1)

        t2=perf_counter()
        
        dt_ =t2-t1
        print()
        print("N =",N)
        print("Tiempo :", dt_,"[seg]")
        
        time.append(dt_)
        #fid.write(f"{N}     {dt_}\n" )
           
    i +=1 
   

# print (time)


dt_s=[]

def split_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

dt_s = list(split_list(time,len(Ns)))
# print(dt_s)


dt_prom=[]

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex=mean(transpuesta[i])
    dt_prom.append(cex)

    

    fid.write(f"{Ns[i]}     {cex}\n" )

fid.close()
 
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot()
plt.title("Desempeño B C2 FLOAT64 EV OVERWRITE FALSE")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño B C2 FLOAT64 EV OVERWRITE FALSE")
plt.show()


# #B_CASO_3_FLOAT_64_evd_overwrite_a=True

Ns= [1, 10, 100,500,1000, 1200, 1300,1500, 2000, 2200, 2300, 2500, 3000, 3500,4000]
time=[]


fid = open("B_3_FLOAT64_evd_overwrite_a=True.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float64)
        b=ones(N)
        # print(A)
        t1=perf_counter()
        w, h=eigh(A, turbo='evd', overwrite_a=True)
        #print(Am1)

        t2=perf_counter()
        
        dt_ =t2-t1
        print()
        print("N =",N)
        print("Tiempo :", dt_,"[seg]")
        
        time.append(dt_)
        #fid.write(f"{N}     {dt_}\n" )
           
    i +=1 
   

# print (time)


dt_s=[]

def split_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

dt_s = list(split_list(time,len(Ns)))
# print(dt_s)


dt_prom=[]

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex=mean(transpuesta[i])
    dt_prom.append(cex)

    

    fid.write(f"{Ns[i]}     {cex}\n" )

fid.close()
 
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot()
plt.title("Desempeño B C3 FLOAT64 EVD OVERWRITE TRUE")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño B C3 FLOAT64 EVD OVERWRITE TRUE")
plt.show()



# #B_CASO_3_FLOAT_64_evd_overwrite_a=False

Ns= [1, 10, 100,500,1000, 1200, 1300,1500, 2000, 2200, 2300, 2500, 3000, 3500,4000]
time=[]


fid = open("B_3_FLOAT64_evd_overwrite_a=False.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float64)
        b=ones(N)
        # print(A)
        t1=perf_counter()
        w, h=eigh(A, turbo='evd', overwrite_a=False)
        #print(Am1)

        t2=perf_counter()
        
        dt_ =t2-t1
        print()
        print("N =",N)
        print("Tiempo :", dt_,"[seg]")
        
        time.append(dt_)
        #fid.write(f"{N}     {dt_}\n" )
           
    i +=1 
   

# print (time)


dt_s=[]

def split_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

dt_s = list(split_list(time,len(Ns)))
# print(dt_s)


dt_prom=[]

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex=mean(transpuesta[i])
    dt_prom.append(cex)

    

    fid.write(f"{Ns[i]}     {cex}\n" )

fid.close()
 
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot()
plt.title("Desempeño B C3 FLOAT64 EVD OVERWRITE FALSE")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño B C3 FLOAT64 EVD OVERWRITE FALSE")
plt.show()


# #B_CASO_4_FLOAT_64_evr_overwrite_a=True

Ns= [1, 10, 100,500,1000, 1200, 1300,1500, 2000, 2200, 2300, 2500, 3000, 3500,4000]
time=[]


fid = open("B_4_FLOAT64_evr_overwrite_a=True.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float64)
        b=ones(N)
        # print(A)
        t1=perf_counter()
        w, h=eigh(A, driver='evr', overwrite_a=True)
        #print(Am1)

        t2=perf_counter()
        
        dt_ =t2-t1
        print()
        print("N =",N)
        print("Tiempo :", dt_,"[seg]")
        
        time.append(dt_)
        #fid.write(f"{N}     {dt_}\n" )
           
    i +=1 
   

# print (time)


dt_s=[]

def split_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

dt_s = list(split_list(time,len(Ns)))
# print(dt_s)


dt_prom=[]

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex=mean(transpuesta[i])
    dt_prom.append(cex)

    

    fid.write(f"{Ns[i]}     {cex}\n" )

fid.close()
 
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot()
plt.title("Desempeño B C4 FLOAT64 EVR OVERWRITE TRUE")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño B C4 FLOAT64 EVR OVERWRITE TRUE")
plt.show()



# #B_CASO_4_FLOAT_64_evr_overwrite_a=False

Ns= [1, 10, 100,500,1000, 1200, 1300,1500, 2000, 2200, 2300, 2500, 3000, 3500,4000]
time=[]


fid = open("B_4_FLOAT64_evr_overwrite_a=False.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float64)
        b=ones(N)
        # print(A)
        t1=perf_counter()
        w, h=eigh(A, driver='evr', overwrite_a=False)
        #print(Am1)

        t2=perf_counter()
        
        dt_ =t2-t1
        print()
        print("N =",N)
        print("Tiempo :", dt_,"[seg]")
        
        time.append(dt_)
        #fid.write(f"{N}     {dt_}\n" )
           
    i +=1 
   

# print (time)


dt_s=[]

def split_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

dt_s = list(split_list(time,len(Ns)))
# print(dt_s)


dt_prom=[]

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex=mean(transpuesta[i])
    dt_prom.append(cex)

    

    fid.write(f"{Ns[i]}     {cex}\n" )

fid.close()
 
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot()
plt.title("Desempeño B C4 FLOAT64 EVR OVERWRITE FALSE")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño B C4 FLOAT64 EVR OVERWRITE FALSE")
plt.show()



# #B_CASO_5_FLOAT_64_evx_overwrite_a=True

Ns= [1, 10, 100,500,1000, 1200, 1300,1500, 2000, 2200, 2300, 2500, 3000, 3500,4000]
time=[]


fid = open("B_5_FLOAT64_evx_overwrite_a=True.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float64)
        b=ones(N)
        # print(A)
        t1=perf_counter()
        w, h=eigh(A, driver='evx', overwrite_a=True)
        #print(Am1)

        t2=perf_counter()
        
        dt_ =t2-t1
        print()
        print("N =",N)
        print("Tiempo :", dt_,"[seg]")
        
        time.append(dt_)
        #fid.write(f"{N}     {dt_}\n" )
           
    i +=1 
   

# print (time)


dt_s=[]

def split_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

dt_s = list(split_list(time,len(Ns)))
# print(dt_s)


dt_prom=[]

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex=mean(transpuesta[i])
    dt_prom.append(cex)

    

    fid.write(f"{Ns[i]}     {cex}\n" )

fid.close()
 
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot()
plt.title("Desempeño B C5 FLOAT64 EVX OVERWRITE TRUE")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño B C5 FLOAT64 EVX OVERWRITE TRUE")
plt.show()



# #B_CASO_4_FLOAT_64_evr_overwrite_a=False

Ns= [1, 10, 100,500,1000, 1200, 1300,1500, 2000, 2200, 2300, 2500, 3000, 3500,4000]
time=[]


fid = open("B_5_FLOAT64_evx_overwrite_a=False.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float64)
        b=ones(N)
        # print(A)
        t1=perf_counter()
        w, h=eigh(A, driver='evx', overwrite_a=False)
        #print(Am1)

        t2=perf_counter()
        
        dt_ =t2-t1
        print()
        print("N =",N)
        print("Tiempo :", dt_,"[seg]")
        
        time.append(dt_)
        #fid.write(f"{N}     {dt_}\n" )
           
    i +=1 
   

# print (time)


dt_s=[]

def split_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

dt_s = list(split_list(time,len(Ns)))
# print(dt_s)


dt_prom=[]

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex=mean(transpuesta[i])
    dt_prom.append(cex)

    

    fid.write(f"{Ns[i]}     {cex}\n" )

fid.close()
 
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot()
plt.title("Desempeño B C5 FLOAT64 EVX OVERWRITE FALSE")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño B C5 FLOAT64 EVX OVERWRITE FALSE")
plt.show()
