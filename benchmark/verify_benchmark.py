import requests
import time

# --- Configuration ---
API_URL = "https://enchan-api-82345546010.us-central1.run.app/v1/solve"

def run_benchmark():
    # Parameters for Server-Side Graph Generation
    N = 2000
    DENSITY = 0.005  # ≈ 10,000 edges

    payload = {
        "graph": {"N": N, "density": DENSITY},
        "control": {"total_time": 35.0},
        "seed": 42
    }

    print(f"1. Triggering Server-Side Generation (N={N}, density={DENSITY})...")
    start_wall = time.time()

    try:
        # Public preview: no authentication required
        response = requests.post(API_URL, json=payload, timeout=60)
        response.raise_for_status()
        end_wall = time.time()

        try:
            data = response.json()
        except ValueError:
            print("[ERROR] Invalid JSON response from server.")
            print(response.text[:200])
            return

        metrics = data.get("metrics", {})
        timing = data.get("TIMING", {})
        env = data.get("ENV", {}).get("runtime", {})

        total_latency = end_wall - start_wall
        pure_solve_time = timing.get("total_wall_time", 0.0)

        print("\n" + "═" * 55)
        print("   ENCHAN ADVANCED SYSTEM & PHYSICS REPORT")
        print("═" * 55)
        
        # --- 0. Problem Scale (Added) ---
        print(f" [NODES]       {N} nodes")
        print(f" [DENSITY]     {DENSITY*100:.2f}%")
        print(f" [SIM TIME]    {payload['control']['total_time']:.1f} virtual sec")
        print("-" * 55)

        # --- 1. System Environment Proof ---
        print(f" [PYTHON]      {env.get('python_version', 'N/A')}")
        print(f" [CPU CORES]   {env.get('cpu_count', 'N/A')} cores")
        print(f" [CPU FREQ]    {env.get('cpu_freq', 'N/A')} MHz")
        print(f" [MEMORY]      {env.get('memory_used_MB')} / {env.get('memory_total_MB')} MB")
        print(f" [INSTANCE ID] {env.get('container_id', 'N/A')}")
        print("-" * 55)

        # --- 2. Performance Metrics ---
        print(f" [LATENCY]     {total_latency:.3f}s (Round Trip)")
        print(f" [SOLVE TIME]  {pure_solve_time:.3f}s (Core Physics Engine)")
        print(f" [OVERHEAD]    {total_latency - pure_solve_time:.3f}s (Network/Cold Start)")
        print("-" * 55)

        # --- 3. Physics Results ---
        cut = metrics.get("cut", 0)
        edges_expected = N * (N - 1) / 2 * DENSITY  # dynamic normalization
        gain = (cut / edges_expected * 100 - 50)

        print(f" [RESULT]      Max-Cut Score: {int(cut)}")
        print(f" [GAIN]        {gain:+.2f}% vs expected baseline")
        print("═" * 55 + "\n")

    except requests.exceptions.Timeout:
        print("\n[ERROR] Request timed out. Try reducing N or increasing timeout.")
    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] Benchmark Failed: {e}")

if __name__ == "__main__":
    run_benchmark()