from numpy import zeros, float16, float32, float64
from time import perf_counter
import matplotlib.pylab as plt


#Tamaño
N = 1000

Ns = [1, 10 ,100, 1000, 2000, 2100, 2200, 2400, 2500 ,3000, 3400, 3500, 4000, 4400, 4500, 5000, 7500, 10000]
#Ns = [1, 25, 50, 100, 500, 1500]
dts = []
mems = []

fid = open("rendimiento.txt","w")
i = 0
while i < 10:
	for N in Ns:
		uso_memoria_total = 0

		A = zeros((N, N), dtype = float16)+1



		B = zeros((N, N))+2



		t1 = perf_counter()
		C = A@B
		t2 = perf_counter()

		uso_memoria_total = A.nbytes + B.nbytes +C.nbytes

		dt = t2 - t1
		dts.append(dt)
		mems.append (uso_memoria_total)
		print(f"N = {N} dt = {dt} s. mem = {uso_memoria_total} bytes. flops = {N**3/dt} flops/s")
		fid.write(f"{N} {dt} {uso_memoria_total}\n" )


	i += 1

fid.close()

