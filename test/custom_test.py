import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import dla_simulation as dla

# --- User-configurable parameters ---
N = 256
N_SEEDS = 1
N_WALKERS = 5_000
MAX_STEPS = 200_000
REINJECT_TIMEOUT = 1000
INJ_MODE = "random"
INJ_RADIUS = None
# ------------------------------------

print("=" * 60)
print("Custom DLA test")
print(f"  N={N}, n_seeds={N_SEEDS}, n_walkers={N_WALKERS}")
print(f"  max_steps={MAX_STEPS}, reinject_timeout={REINJECT_TIMEOUT}")
print(f"  inj_mode={INJ_MODE}, inj_radius={INJ_RADIUS}")
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
print(f"  Expected Df ≈ 1.71 (single cluster, avoid boundary effects)")
