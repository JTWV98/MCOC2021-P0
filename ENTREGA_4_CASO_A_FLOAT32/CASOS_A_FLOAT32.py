import numpy as np
from numpy import matrix
from numpy import transpose
from numpy import mean
from numpy import linalg
from numpy import zeros
from scipy import linalg
from time import perf_counter
from scipy.linalg import inv
from scipy.linalg import solve
#from laplaciana import laplaciana
from numpy import float32, float64
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

#A_CASO_1_FLOAT_32

Ns= [1, 10, 100,500,1000, 1500, 2000, 2500, 3000, 3500,4000, 5000 ,5500, 6000,10000]
time=[]


fid = open("A_1_FLOAT32.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float32)
        # print(A)
        t1=perf_counter()
        Am1 = inv(A)
        #print(Am1)
        x = Am1*vector(N)
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
plt.title("Desempeño A C1 FLOAT32")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño A C1 FLOAT32")
plt.show()



#A_CASO_2_FLOAT_32

Ns= [1, 10, 100,500,1000, 1500, 2000, 2500, 3000, 3500,4000, 5000 ,5500, 6000,10000]
time=[]


fid = open("A_2_FLOAT32.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float32)
        # print(A)
        t1=perf_counter()

        #print(Am1)
        x = linalg.solve(A,vector(N),assume_a='pos')
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
plt.title("Desempeño A C2 FLOAT32")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño A C2 FLOAT32")
plt.show()




#A_CASO_3_FLOAT_32

Ns= [1, 10, 100,500,1000, 1500, 2000, 2500, 3000, 3500,4000, 5000 ,5500, 6000,10000]
time=[]


fid = open("A_3_FLOAT32.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float32)
        # print(A)
        t1=perf_counter()

        #print(Am1)
        x = linalg.solve(A,vector(N),assume_a='sym')
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
plt.title("Desempeño A C3 FLOAT32")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño A C3 FLOAT32")
plt.show()

#A_CASO_4_FLOAT_32

Ns= [1, 10, 100,500,1000, 1500, 2000, 2500, 3000, 3500,4000, 5000 ,5500, 6000,10000]
time=[]


fid = open("A_4_FLOAT32.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float32)
        # print(A)
        t1=perf_counter()

        #print(Am1)
        x = linalg.solve(A,vector(N),overwrite_a=True)
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
plt.title("Desempeño A C4 FLOAT32")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño A C4 FLOAT32")
plt.show()



#A_CASO_5_FLOAT_32

Ns= [1, 10, 100,500,1000, 1500, 2000, 2500, 3000, 3500,4000, 5000 ,5500, 6000,10000]
time=[]


fid = open("A_5_FLOAT32.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float32)
        # print(A)
        t1=perf_counter()

        #print(Am1)
        x = linalg.solve(A,vector(N),overwrite_b=True)
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
plt.title("Desempeño A C5 FLOAT32")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño A C5 FLOAT32")
plt.show()


#A_CASO_6_FLOAT_32

Ns= [1, 10, 100,500,1000, 1500, 2000, 2500, 3000, 3500,4000, 5000 ,5500, 6000,10000]
time=[]


fid = open("A_6_FLOAT32.txt","w")
i = 0

while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        
        A= laplaciana(N, dtype = float32)
        # print(A)
        t1=perf_counter()

        #print(Am1)
        x = linalg.solve(A,vector(N),overwrite_b=True, overwrite_a=True)
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
plt.title("Desempeño A C6 FLOAT32")

for i in range(len(Ns)):

    plt.subplot().loglog(Ns[i*15:(i+1)*15], dt_prom[i*15:(i+1)*15], "o-")
    
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()
plt.savefig("Desempeño A C6 FLOAT32")
plt.show()


