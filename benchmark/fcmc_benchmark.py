import requests
import time
import json

# --- Enchan API: Quantum-Transcendence Challenge ---
API_URL = "https://enchan-api-82345546010.us-central1.run.app/v1/solve"

def run_extreme_challenge():
    # ══════════════════════════════════════════════════
    #  ENCHAN EXTREME BENCHMARK CONFIGURATION
    # ══════════════════════════════════════════════════
    N = 2000
    DENSITY = 1.0
    TOTAL_TIME = 35.0

    payload = {
        "graph": {"N": N, "density": DENSITY},
        "control": {"total_time": TOTAL_TIME}, 
        "seed": 777
    }

    total_edges = int(N * (N - 1) / 2)

    print(f"🔥 Launching Extreme Challenge: N={N} (Fully Connected)...")
    print(f"📡 Processing {total_edges:,} interactions on Cloud Run...")
    
    start_wall = time.perf_counter()
    
    try:
        response = requests.post(API_URL, json=payload, timeout=300)
        response.raise_for_status()
        
        end_wall = time.perf_counter()
        
        # --- data extraction ---
        data = response.json()

        # ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
        # View raw data from the server
        print("\n=== [DEBUG] RAW SERVER RESPONSE (PROOF OF TRUTH) ===")
        debug_view = {
            "metrics": data.get("metrics"),
            # If the server returns any graph information, it will be displayed here
            "graph_summary": data.get("graph", "Not included in response"),
            "TIMING": data.get("TIMING"),
            "audit": data.get("audit")
        }
        print(json.dumps(debug_view, indent=2))
        print("====================================================\n")
        # ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲

        metrics = data.get("metrics", {})
        timing = data.get("TIMING", {})
        env_root = data.get("ENV", {})
        runtime = env_root.get("runtime", {})
        audit = data.get("audit", {})
        audit_env = audit.get("ENV", {}) 

        # --- calculation ---
        total_latency = end_wall - start_wall
        pure_solve_time = timing.get("total_wall_time", 0.0)
        overhead = total_latency - pure_solve_time
        
        cut_score = int(metrics.get("cut", 0))
        expected_random = total_edges * 0.5
        gain_percent = 0.0
        if expected_random > 0:
            gain_percent = (cut_score / expected_random * 100) - 100

        # plastic surgery
        mem_used = runtime.get("memory_used_MB", "N/A")
        mem_total = runtime.get("memory_total_MB", "N/A")
        mem_str = f"{mem_used} / {mem_total} MB" if mem_used != "N/A" else "N/A"
        cpu_count = runtime.get("cpu_count", "N/A")
        numpy_ver = audit_env.get("numpy", "Hidden")
        numba_ver = audit_env.get("numba", "Hidden")
        s_hash = audit.get("HASH", {}).get("S", "Hidden")

        # --- 📝 THE ARTIFACT REPORT ---
        print("\n" + "═" * 55)
        print("   ENCHAN ADVANCED SYSTEM & PHYSICS REPORT (Extreme)")
        print("═" * 55)
        
        print(f" [MODEL]       Ising / QUBO (Max-Cut Formulation)")
        print(f" [NODES]       {N:,} nodes")
        print(f" [DENSITY]     {DENSITY*100:.1f}% (Full Mesh)")
        print(f" [EDGES]       {total_edges:,} edges")
        print(f" [TOTAL TIME]  {TOTAL_TIME:.1f} virtual sec")
        print("-" * 55)

        print(f" [PYTHON]      {runtime.get('python_version', 'N/A')}")
        print(f" [PLATFORM]    {runtime.get('os_info', 'Cloud Run')}")
        print(f" [NUMPY]       {numpy_ver}")
        print(f" [NUMBA]       {numba_ver}")
        print(f" [CPU]         {cpu_count} vCPU")
        print(f" [MEMORY]      {mem_str}")
        print("-" * 55)

        print(f" [LATENCY]     {total_latency:.3f}s (Round Trip)")
        print(f" [SOLVE TIME]  {pure_solve_time:.3f}s (Core Physics Engine)")
        print(f" [OVERHEAD]    {overhead:.3f}s (Network/IO)")
        print("-" * 55)

        print(f" [RESULT]      Max-Cut Score: {cut_score:,}")
        print(f" [GAIN]        {gain_percent:+.2f}% vs expected baseline")
        print(f" [S-HASH]      {s_hash}")
        print("═" * 55 + "\n")

    except Exception as e:
        print(f"\n❌ Benchmark Failed: {e}")

if __name__ == "__main__":
    run_extreme_challenge()