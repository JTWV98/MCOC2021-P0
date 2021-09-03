import numpy as np
from numpy import zeros
from time import perf_counter
from scipy.linalg import solve
from numpy import double
import matplotlib.pylab as plt


def laplaciana_llena(N, dtype):
    A = zeros((N,N) , dtype=dtype)
    
    for i in range(N):
        A[i,i] = 2
        for j in range(max(0,i-2),i):
            if abs(i-j) == 1:
                A[i,j] = -1
                A[j,i] = -1
        
        
    return(A)
print (laplaciana_llena(5, double))

def vector(N,dtype=double):
    vector=[]
    for i in range(N):
        vector.append(1)
    b = np.array(vector)
    return b    
            


# print (vector(4, dtype=double).T)      
Ns = [1, 10 ,100, 1000, 2000, 2100, 2200, 2400, 2500 ,3000, 3400, 3500, 4000, 4400, 4500, 5000, 7500, 10000]

dte=[]
dts=[]

fid = open("SOLVE_LLENA.txt","w")
i = 0
while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
        t1=perf_counter()
        A= laplaciana_llena(N, dtype = double)
        b= vector(N,dtype=double)
        t2=perf_counter()
        x= solve(A,b)
        t3=perf_counter()
        dt_ensamblaje = t2-t1
        dt_solucion = t3-t2
    
        
        dte.append(dt_ensamblaje)
        dts.append(dt_solucion)
        
        print()
        print()
        print("N =",N)
        print("Tiempo ensamblaje:", dt_ensamblaje,"[seg]")
        print("Tiempo solucion:", dt_solucion,"[seg]")
     
       
        fid.write(f"{N}     {dt_ensamblaje}    {dt_solucion}\n" )
           
    i +=1 

fid.close()

Ns =[]
dte = []
dts=[]


fid = open("SOLVE_LLENA.txt","r")

for line in fid:
    
    s1 = line.split() 
    N = int(s1[0])
    dt_ensamblaje = float(s1[1])
    dt_inversion = float(s1[2])
   
    Ns.append(N)
    dte.append(dt_ensamblaje)
    dts.append(dt_inversion)

fid.close()
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_ = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

ygraf2 = ["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf2_ = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]
Ns_ =[1, 10 ,100, 1000, 2000, 2100, 2200, 2400, 2500 ,3000, 3400, 3500, 4000, 4400, 4500, 5000, 7500, 10000]
plt.figure(1)

plt.subplot(2,1,1)
plt.title("RENDIMIENTO SOLVE LLENA")

for i in range(len(Ns)):
	
	plt.subplot(2,1,1).loglog(Ns[i*18:(i+1)*18], dte[i*18:(i+1)*18], "o-", color="lightgray")
# 	print(f"{Ns[i*18:(i+1)*18], dte[i*18:(i+1)*18]}")
	#print (Ns[i])
plt.ylabel("Tiempo ensamblado")
plt.xlim(right = 20000)
plt.yticks(ygraf1_, ygraf1)
plt.plot(Ns_ ,[max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte)],linestyle = "--",color ="blue", label="CONSTANTE")               
plt.plot([3,Ns[-1]],[dte[0],max(dte)],linestyle = "--", color="orange", label="O(N)")
plt.plot([10,Ns[-1]],[dte[0]**2,max(dte)],linestyle = "--", color="green", label="O(N^2)")
plt.plot([100,Ns[-1]],[dte[0]**3,max(dte)],linestyle = "--",color="red", label="O(N^3)")
plt.plot([400,Ns[-1]],[dte[0]**4,max(dte)],linestyle = "--",color="purple", label="O(N^3)")
plt.axis([0,Ns[-1],0.0001, 600])
plt.xticks(eje_x, [])
plt.grid()



for i in range(len(Ns)):
	
	plt.subplot(2,1,2).loglog(Ns[i*18:(i+1)*18], dts[i*18:(i+1)*18], "o-", color="lightgray")
# 	print(f"{Ns[i*18:(i+1)*18], dts[i*18:(i+1)*18]}")
	#print (Ns[i])
plt.ylabel("Tiempo solución")
plt.xlim(right = 20000)
plt.yticks(ygraf2_, ygraf2)
plt.xticks(eje_x, eje_x, rotation=45)
plt.plot(Ns_ ,[max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts)],linestyle = "--",color ="blue", label="CONSTANTE")
plt.plot([3,Ns[-1]],[dts[0],max(dts)],linestyle = "--", color="orange", label="O(N)")
plt.plot([10,Ns[-1]],[dts[0]**2,max(dts)],linestyle = "--", color="green", label="O(N^2)")
plt.plot([100,Ns[-1]],[dts[0]**3,max(dts)],linestyle = "--",color="red", label="O(N^3)")
plt.plot([400,Ns[-1]],[dts[0]**4,max(dts)],linestyle = "--",color="purple", label="O(N^4)")
plt.axis([0,20000,0.0001, 600])
plt.legend(loc="lower left")
plt.grid()


plt.xlabel("Tamaño matriz N")

plt.savefig("RENDIMIENTO SOLVE LLENA")

plt.show()








