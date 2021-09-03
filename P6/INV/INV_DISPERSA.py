from numpy import double
import scipy.sparse as sp
import scipy.sparse as sparse
from time import perf_counter
from scipy.sparse.linalg import inv

def laplaciana_dispersa(N,dtype):
    return 2*sparse.eye(N,dtype=dtype)-sparse.eye(N,N,1,dtype=dtype)-sparse.eye(N,N,-1,dtype=dtype)


Ns = [1, 10 ,100, 1000, 2000, 2100, 2200, 2400, 2500 ,3000, 3400, 3500, 4000, 4400, 4500, 5000, 7500, 10000]


dte=[]
dti=[]

fid = open("INV_DISPERSA.txt","w")
i = 0
while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
        t1=perf_counter()
        A= laplaciana_dispersa(N, dtype = double)
        Acsr = sp.csr_matrix(A)
        # print(A)
        t2=perf_counter()
        Am1 = inv(Acsr)
        #print(Am1)
        t3=perf_counter()
        dt_ensamblaje = t2-t1
        dt_inversion = t3-t2
   
        dte.append(dt_ensamblaje)
        dti.append(dt_inversion)
        
        print()
        print("N =",N)
        print("Tiempo ensamblaje:", dt_ensamblaje,"[seg]")
        print("Tiempo inversión:", dt_inversion,"[seg]")
       
        fid.write(f"{N}     {dt_ensamblaje}    {dt_inversion}\n" )
           
    i +=1 

fid.close()


import matplotlib.pylab as plt

Ns =[]
dte = []
dti=[]


fid = open("INV_DISPERSA.txt","r")

for line in fid:
    
    s1 = line.split() 
    N = int(s1[0])
    dt_ensamblaje = float(s1[1])
    dt_inversion = float(s1[2])
   
    Ns.append(N)
    dte.append(dt_ensamblaje)
    dti.append(dt_inversion)

fid.close()
ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_ = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

ygraf2 = ["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf2_ = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]
Ns_ = [1, 10 ,100, 1000, 2000, 2100, 2200, 2400, 2500 ,3000, 3400, 3500, 4000, 4400, 4500, 5000, 7500, 10000]
plt.figure(1)

plt.subplot(2,1,1)
plt.title("RENDIMIENTO INV DISPERSA")

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
	
	plt.subplot(2,1,2).loglog(Ns[i*18:(i+1)*18], dti[i*18:(i+1)*18], "o-", color="lightgray")
# 	print(f"{Ns[i*18:(i+1)*18], dti[i*18:(i+1)*18]}")
	#print (Ns[i])
plt.ylabel("Tiempo inversión")
plt.xlim(right = 20000)
plt.yticks(ygraf2_, ygraf2)
plt.xticks(eje_x, eje_x, rotation=45)
plt.plot(Ns_ ,[max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti),max(dti)],linestyle = "--",color ="blue", label="CONSTANTE")
plt.plot([3,Ns[-1]],[dti[0],max(dti)],linestyle = "--", color="orange", label="O(N)")
plt.plot([10,Ns[-1]],[dti[0]**2,max(dti)],linestyle = "--", color="green", label="O(N^2)")
plt.plot([100,Ns[-1]],[dti[0]**3,max(dti)],linestyle = "--",color="red", label="O(N^3)")
plt.plot([400,Ns[-1]],[dti[0]**4,max(dti)],linestyle = "--",color="purple", label="O(N^4)")
plt.axis([0,20000,0.0001, 600])
plt.legend(loc="lower left")
plt.grid()


plt.xlabel("Tamaño matriz N")

plt.savefig("RENDIMIENTO INV DISPERSA")

plt.show()
