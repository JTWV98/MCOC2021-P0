from time import perf_counter
from scipy.linalg import inv
from laplaciana import laplaciana
from numpy import float16

# #HALF
Ns = [1, 10 ,100, 1000, 2000, 2100, 2200, 2400, 2500 ,3000, 3400, 3500, 4000, 4400, 4500, 5000, 7500, 10000]
dt_ensamblaje_ = []
dt_inversion_=[]
bytes_total_=[]


fid = open("timing_inv_caso_3_half.txt","w")
i = 0
# fid.write("Tamaño   Ensamblaje[s]           Inversión[s]        Memoria[bytes] \n")
while i < 10:
    print()
    print()
    print("Ciclo Nº", i+1)
    for N in Ns:
 		 
        t1=perf_counter()
        A= laplaciana(N, dtype = float16)
        # print(A)
        t2=perf_counter()
        Am1 = inv(A, overwrite_a=True)
        #print(Am1)
        t3=perf_counter()
        
        dt_ensamblaje = t2-t1
        dt_inversion = t3-t2
        bytes_total = A.nbytes + Am1.nbytes
        
        dt_ensamblaje_.append(dt_ensamblaje)
        dt_inversion_.append(dt_inversion)
        bytes_total_.append(bytes_total)
        print()
        print("N =",N)
        print("Tiempo ensamblaje:", dt_ensamblaje,"[seg]")
        print("Tiempo inversión:", dt_inversion,"[seg]")
        print(bytes_total, "[bytes]")
        fid.write(f"{N}     {dt_ensamblaje}    {dt_inversion}    {bytes_total}\n" )
           
    i +=1 
   
fid.close()



import matplotlib.pylab as plt

Ns =[]
dt_ensamblaje_h1 = []
dt_inversion_h1=[]
bytes_total_h1=[]

fid = open("timing_inv_caso_3_half.txt","r")

for line in fid:
    
    s1 = line.split() 
    N = int(s1[0])
    dt_ensamblaje = float(s1[1])
    dt_inversion = float(s1[2])
    bytes_total = int(s1[3])
    
    Ns.append(N)
    dt_ensamblaje_h1.append(dt_ensamblaje)
    dt_inversion_h1.append(dt_inversion)
    bytes_total_h1.append(bytes_total)

fid.close()

ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

ygraf3 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf3_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

ygraf2 = ["1KB", "10KB", "100KB", "1MB", "10MB", "100MB", "1GB", "10GB"]
ygraf2_mem = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]

plt.figure(1)

plt.subplot(2,1,1)
plt.title("Rendimiento caso_3_half")

for i in range(len(Ns)):

    plt.subplot(2,1,1).loglog(Ns[i*18:(i+1)*18], dt_ensamblaje_h1[i*18:(i+1)*18], "o-")
    # print(f"{Ns[i*18:(i+1)*18], dt_ensamblaje_h1[i*18:(i+1)*18]}")
 	#print (Ns[0])
plt.ylabel("Tiempo ensamblaje")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, [])
plt.grid()
plt.show()

plt.subplot(2,1,1.5)
plt.title("Rendimiento caso_3_half")
for j in range(len(Ns)):

    plt.subplot(2,1,1.5).loglog(Ns[j*18:(j+1)*18], dt_inversion_h1[j*18:(j+1)*18], "o-")
    # print(f"{Ns[j*18:(j+1)*18], dt_inversion_h1[j*18:(j+1)*18]}")
plt.ylabel("Tiempo inversion")
plt.xlabel("Tamaño matriz N")
plt.xlim(right = 20000)
plt.yticks(ygraf3_seg, ygraf3)
plt.xticks(eje_x, [])
plt.grid()
plt.show()

plt.subplot(2,1,2)
plt.title("Rendimiento caso_3_half")
plt.subplot(2, 1, 2)
plt.hlines(y = 10000000000, xmin = 0, xmax = 20000, linestyle = "--")
plt.loglog(Ns, bytes_total_h1, "o-")
plt.xlim(right = 20000)
plt.yticks(ygraf2_mem, ygraf2)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()

plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria")
plt.savefig("RENDIMIENTO caso 3 half")
plt.show()