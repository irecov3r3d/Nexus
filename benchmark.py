import timeit
from nexus_lm.core.reasoning import REEREngine

def benchmark():
    engine = REEREngine(max_iterations=1000)
    engine.search("Benchmark Query")

if __name__ == "__main__":
    t = timeit.timeit(benchmark, number=100)
    print(f"Execution time: {t:.6f} seconds")
