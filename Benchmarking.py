from os import write
from typing import List, Tuple, Optional, Dict, Callable, Any
import time, csv, numpy as np, matplotlib.pyplot as plt
from random import randint
import Quick_Sort_Implementations 

#Dealing with the input
#OptTuple3i = Optional[Tuple[int,int,int]]
FunType = Callable[[List[int]], List[int]]



#Time
def measure(f: Callable[[], Any])->float:
    start: float = time.time()
    f()
    end: float = time.time()
    return end - start



def benchmark(f: FunType, args: List[List[int]], N: int)->np.ndarray:
    m: int = len(args)
    M: np.ndarray = np.zeros((m,N))
    for i in range(len(args)):
        arg: List[int] = args[i]
        for j in range(N):
            M[i,j] = measure(lambda: f(arg))
    means = np.mean(M, axis=1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof=1).reshape(m, 1)
    return np.hstack([means, stdevs])



#NEED TO MAKE NEW INPUT GENERATION METHOD - This is a temporary attempt with random ints.

def generate_input(n: int)->List[int]:
    list = []
    for i in range(1,n+1):
        list.append(randint(0, 1000))
    return list






#The full test:

ns: List[int]
args: List[List[int]]
res_classic: np.ndarray
result_dual: np.ndarray
max_i: int = 12 #was 12
N: int = 5 #was 5
ns = [int(30*1.41**i) for i in range(max_i)]
args = [generate_input(n) for n in ns]

#Uncopy Code to Run the full test
res_classic = benchmark(Quick_Sort_Implementations.classic_quicksort, args, N)
res_dual = benchmark(Quick_Sort_Implementations.dual_quicksort, args, N)

print(res_classic)
print(res_dual)





def write_csv(ns: List[int], res: np.ndarray, filename: str):
    with open(filename,'w') as f:
        writer = csv.writer(f)
        for i in range(len(ns)):
            writer = csv. writer(f)
            for i in range(len(ns)):
                writer.writerow([ns[i]] + res[i,:].tolist())


def write_latex_tabular(ns: List[int], res:  np.ndarray, filename: str):
    with open(filename, 'w') as f:
        f.write(r'\begin{tabular}{rrr}' + '\n')
        f.write(r'$n$ & Average & Standard deviation')
        f.write(r'\\\hline' + '\n')
        for i in range(len(ns)):
            fields = [str(ns[i]), 
                '{:.6f}'.format(res[i,0]),
                '{:.6f}'.format(res[i,1])]
            f.write(' & '.join(fields) + r'\\' + '\n')
        f.write(r'\end{tabular}' + '\n') 



# FILL IN THE RIGHT INFORMATION:
write_csv(ns, res_classic, "classic_performance.csv")
write_latex_tabular(ns, res_classic, "classic_quicksort_tabular.tex")

write_csv(ns, res_dual, "dual_quicksort_performance.csv")
write_latex_tabular(ns, res_dual, "dual_quicksort_tabular.tex")

#Making the plot presenting the performance

fig = plt.figure()
ax = fig.gca()

#Changed to relevant information
ax.errorbar(ns, res_classic[:,0], res_classic[:,1], capsize = 3.0, marker = 'o')
ax.errorbar(ns, res_dual[:,0], res_dual[:,1], capsize = 3.0, marker = 'o')

ax.set_xlabel('Number of elements $n$')
ax.set_ylabel('Time (s)')
ax.set_yscale('log')


ax.legend(['Classic_QuickSort', 'Dual_Pivot_QuickSort'])
plt.savefig('plot_Classic_vs_Dual.pdf')

