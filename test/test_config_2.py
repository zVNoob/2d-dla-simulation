import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import dla_simulation as dla

N = 512
N_SEEDS = 12
N_WALKERS = 15_000
MAX_STEPS = 500_000
REINJECT_TIMEOUT = 2000
INJ_MODE = "random"
INJ_RADIUS = None

print("=" * 60)
print("Test Config 2: multi-seed, random injection")
print(f"  N={N}, n_seeds={N_SEEDS}, n_walkers={N_WALKERS}, inj_mode={INJ_MODE}")
print("=" * 60)

start = time.time()
result = dla.simulation(
    N=N, n_seeds=N_SEEDS, n_walkers=N_WALKERS,
    max_steps=MAX_STEPS, reinject_timeout=REINJECT_TIMEOUT,
    inj_mode=INJ_MODE, inj_radius=INJ_RADIUS,
)
elapsed = time.time() - start

print(f"\n  Fractal dimension Df = {result['fractal_dimension']:.4f}")
print(f"  Particles glued       = {result['n_particles']}")
print(f"  Number of aggregates  = {result['n_aggregate']}")
print(f"  Simulation time       = {elapsed:.1f}s")
print(f"  Expected: Df lower than 1.71 due to multi-cluster effects")
print(f"  Expected: {N_SEEDS}+ separate aggregates (fragmentation likely)")
if result['n_aggregate'] > N_SEEDS:
    print("  NOTE: More aggregates than seeds — fragmentation occurred")
