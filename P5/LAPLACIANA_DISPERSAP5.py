from time import perf_counter
import numpy as np
import scipy.sparse as sparse
from numpy import eye, zeros
import scipy.sparse as sparce
from numpy import float16, float32
import matplotlib.pylab as plt

# def laplaciana(N, dtype):
#     A = zeros((N,N) , dtype=dtype)
    
#     for i in range(N):
#         A[i,i] = 2
#         for j in range(max(0,i-2),i):
#             if abs(i-j) == 1:
#                 A[i,j] = -1
#                 A[j,i] = -1
        
        
#     return(A)

# print (laplaciana(19,float32))




def matriz_laplaciana_dispersa(N,dtype):
    return 2*sparse.eye(N,dtype=dtype)-sparse.eye(N,N,1,dtype=dtype)-sparse.eye(N,N,-1,dtype=dtype)





# Ns = [1, 10 ,100, 1000, 2000, 2100, 2200, 2400, 2500 ,2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000]
Ns = [1,100, 1000, 2000,3500, 4000, 4500, 5000, 10000, 20000, 50000, 100000, 200000,500000,1000000, 5000000,10000000,20000000]
# Ns = [1, 25, 50, 100, 500, 200000]

dts = []
dts_ = []


fid = open("laplaciana_dispersa.txt","w")
i = 0
while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
        
        t1 = perf_counter()
        A = (matriz_laplaciana_dispersa(N,float32))
        B = (matriz_laplaciana_dispersa(N,float32))
        
        Acsr = sparse.csr_matrix(A)
        Bcsr = sparse.csr_matrix(B)
        

        t2 = perf_counter()

        C=Acsr@Bcsr
        
        t3 = perf_counter()
        
        dt_ensamblado = t2 - t1
        dt_solucion = t3 - t2
        
        dts.append(dt_ensamblado)
        dts_.append(dt_solucion)
       
        print(f"N = {N}         Tiempo ensamblado = {dt_ensamblado} s.         Tiempo solucion = {dt_solucion} s.")
        fid.write(f"{N} {dt_ensamblado} {dt_solucion}\n" )


    i += 1

fid.close()


Ns =[]
dte = []
dts = []
fid = open("laplaciana_dispersa.txt", "r")

for line in fid:
	s1 = line.split()
	N = int(s1[0])
	dt_ensamblado = float(s1[1])
	dt_solucion =float(s1[2])

	Ns.append(N)
	dte.append(dt_ensamblado)
	dts.append(dt_solucion)

fid.close()

ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_ = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

ygraf2 = ["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf2_ = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000,500000, 1000000, 5000000,10000000,20000000]
Ns_ = [1 ,100, 1000, 2000,3500, 4000, 4500, 5000, 10000, 20000, 50000, 100000, 200000,500000,1000000, 5000000,10000000,20000000]
plt.figure(1)

plt.subplot(2,1,1)
plt.title("Rendimiento Dispersa")

for i in range(len(Ns)):
	
	plt.subplot(2,1,1).loglog(Ns[i*18:(i+1)*18], dte[i*18:(i+1)*18], "o-")
# 	print(f"{Ns[i*18:(i+1)*18], dte[i*18:(i+1)*18]}")
	#print (Ns[i])
plt.ylabel("Tiempo ensamblado")
plt.xlim(right = 20000)
plt.yticks(ygraf1_, ygraf1)
plt.plot(Ns_ ,[max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte),max(dte)],linestyle = "--",color ="blue", label="CONSTANTE")               
plt.plot([3,20000000],[dte[0],max(dte)],linestyle = "--", color="orange", label="O(N)")
plt.plot([10,20000000],[dte[0]**2,max(dte)],linestyle = "--", color="green", label="O(N^2)")
plt.plot([100,20000000],[dte[0]**3,max(dte)],linestyle = "--",color="red", label="O(N^3)")
plt.plot([400,20000000],[dte[0]**4,max(dte)],linestyle = "--",color="purple", label="O(N^3)")
plt.axis([0,Ns[-1],0.0001, 60])
plt.xticks(eje_x, [])
plt.grid()



for i in range(len(Ns)):
	
	plt.subplot(2,1,2).loglog(Ns[i*18:(i+1)*18], dts[i*18:(i+1)*18], "o-")
# 	print(f"{Ns[i*18:(i+1)*18], dts[i*18:(i+1)*18]}")
	#print (Ns[i])
plt.ylabel("Tiempo solución")
plt.xlim(right = 20000)
plt.yticks(ygraf2_, ygraf2)
plt.xticks(eje_x, eje_x, rotation=45)
plt.plot(Ns_ ,[max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts),max(dts)],linestyle = "--",color ="blue", label="CONSTANTE")
plt.plot([3,20000000],[dts[0],max(dts)],linestyle = "--", color="orange", label="O(N)")
plt.plot([10,20000000],[dts[0]**2,max(dts)],linestyle = "--", color="green", label="O(N^2)")
plt.plot([100,20000000],[dts[0]**3,max(dts)],linestyle = "--",color="red", label="O(N^3)")
plt.plot([400,20000000],[dts[0]**4,max(dts)],linestyle = "--",color="purple", label="O(N^4)")
plt.axis([0,Ns[-1],0.0001, 60])
plt.legend(loc="lower left")
plt.grid()

plt.xlabel("Tamaño matriz N")

plt.savefig("laplaciana_dispersa")

plt.show()





































































































































































































































# def matriz_laplaciana(N,t=np.float32):
#     e =np.eye(N)-np.eye(N,N,1)
    
#     return t(e+e.T)
    
# N=4

# A= matriz_laplaciana(N)
# print (f"A= \n {A}") 
   
# Acsr = sparse.csr_matrix(A)
# print (f"Acsr= \n {Acsr}") 

# Acsc = sparse.csc_matrix(A)
# print (f"Acsc= \n {Acsc}")

# Acoo = sparse.coo_matrix(A)    
# print (f"Acoo= \n {Acoo}")

# Adia = sparse.dia_matrix(A)
# print (f"Adia= \n {Adia}")

# Alil= sparse.lil_matrix(A)    
# print (f"Alil= \n {Alil}")

# # (index based formar)
# # idice 0, 0 hay un 2
# # indice 0 1 hay un -1
# # indice 1 0 hay un -1
# # indice 1 1 hay un 2

# # CSR(hartos ceros y matriz bambeada)

# # para esta se mustra el primer f

# # 0 0 2



# # CSC

# # #diagonal

# # N=4
# # b=1
# # 2 2 2 2 -1 -1 