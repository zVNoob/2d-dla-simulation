import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import dla_simulation as dla

N = 512
N_WALKERS = 25_000
MAX_STEPS = 500_000
REINJECT_TIMEOUT = 2000
INJ_MODE = "radial"
INJ_RADIUS = 180

print("=" * 60)
print("Test Config 4: single seed, radial injection, high density")
print(f"  N={N}, n_walkers={N_WALKERS}, inj_mode={INJ_MODE}, inj_radius={INJ_RADIUS}")
print("=" * 60)

start = time.time()
result = dla.simulation(
    N=N, n_seeds=1, n_walkers=N_WALKERS,
    max_steps=MAX_STEPS, reinject_timeout=REINJECT_TIMEOUT,
    inj_mode=INJ_MODE, inj_radius=INJ_RADIUS,
)
elapsed = time.time() - start

print(f"\n  Fractal dimension Df = {result['fractal_dimension']:.4f}")
print(f"  Particles glued       = {result['n_particles']}")
print(f"  Number of aggregates  = {result['n_aggregate']}")
print(f"  Simulation time       = {elapsed:.1f}s")
print(f"  Expected: Df may overestimate 1.71 due to finite-size saturation")
if result['fractal_dimension'] > 1.8:
    print("  NOTE: Elevated Df — cluster likely fills significant portion of lattice")
