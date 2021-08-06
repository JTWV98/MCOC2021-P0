import matplotlib.pylab as plt

Ns =[]
dts = []
mems = []
fid = open("rendimiento.txt", "r")
datos =fid.read()
for line in fid:
	s1 = line.split()
	N = int(s1[0])
	dt = float(s1[1])
	mem = int(s1[2])

	Ns.append(N)
	dts.append(dt)
	mems.append(mem)

print(Ns)
print (dts)
print(mems)


fid.close()

N = len(datos)/10
N = int(N)

ygraf1 =["0.1 ms", "1 ms", "10ms", "0.1s", "1 seg", "10 seg", "1 min", "10 min"]
ygraf1_seg = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

ygraf2 = ["1KB", "10KB", "100KB", "1MB", "10MB", "100MB", "1GB", "10GB"]
ygraf2_mem = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]

eje_x=[10, 20, 50,100, 200, 500, 1000, 2000, 5000, 10000, 20000]
plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
r=0
t=0
while r < 10:
    while t < len(datos):
        plt.loglog(Ns[t:t+30],dts[t:t+30], "o-")
        t+=N
    r+=1
    
plt.ylabel("Tiempo transcurrido")
plt.xlim(right = 20000)
plt.yticks(ygraf1_seg, ygraf1)
plt.xticks(eje_x, [])
plt.grid()

plt.subplot(2, 1, 2)
plt.hlines(y = 10000000000, xmin = 0, xmax = 20000, linestyle = "--")
plt.loglog(Ns, mems, "o-")
plt.xlim(right = 20000)
plt.yticks(ygraf2_mem, ygraf2)
plt.xticks(eje_x, eje_x, rotation=45)
plt.grid()

plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria")
plt.savefig("RENDIMIENTOA@B")
plt.show()
