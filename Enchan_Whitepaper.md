# Enchan Web OS — Technical Whitepaper

**Deterministic Physics Compute Kernel & Runtime for Topology-Adaptive Nonlinear Relaxation**

*Author: Mitsuhiro Kobayashi*  
*Revision: 2026-09-06*

> **IMPORTANT NOTICE REGARDING INTELLECTUAL PROPERTY & LICENSING**
> This repository provides **public API endpoints and verification interfaces only**. The proprietary core implementation is not exposed. All materials, data, and API outputs are governed by the **Enchan Research & Verification License v1.0**.
>
> **RESTRICTION D:** The use of this documentation, API, or generated data for training, fine-tuning, or evaluating Artificial Intelligence or Machine Learning models is **STRICTLY PROHIBITED**. Commercial integration requires a separate license.

---

## 1. Executive Summary

**Enchan Web OS** is an early-form physics compute kernel and runtime built around deterministic nonlinear field relaxation on graph-structured systems.

Its most mature public application is **Enchan Cosmic**, an Ising / Max-Cut solver exposed through the public API. The same broader runtime also supports experimental structural analysis and routing applications. Max-Cut therefore serves as an important verification surface for the kernel, but it is not intended to define the entire scope of Enchan Web OS.

The central computational idea is **topology-adaptive nonlinear response**: when local interaction intensity becomes highly concentrated, the effective response is screened rather than allowed to grow as an unrestricted linear aggregate. In the current Enchan Field interpretation, this behavior is described as a **finite-tension response of an interaction medium**.

This whitepaper intentionally makes a narrower claim than earlier descriptions of Enchan:

- Enchan is a deterministic classical compute system, not a quantum computer.
- Deterministic relaxation, continuous-variable optimization, and physics-inspired Ising computation already have substantial prior art.
- The research question is therefore not whether non-stochastic relaxation is possible, but whether Enchan's **topology-adaptive nonlinear screening**, observable behavior, reproducibility model, and low-resource implementation constitute a useful and distinguishable variant within that broader family.
- No claim is made here that Enchan guarantees global optimality for arbitrary NP-hard problems, breaks known complexity limits, or outperforms every existing solver on every problem class.

The role of this document is to describe the **public computational surface, verification model, observed behavior, and claim boundaries** of Enchan Web OS. Deeper theoretical interpretation is handled separately in the Enchan Field papers.

---

## 2. Theoretical Lineage and Claim Boundary

### 2.1 From Astrophysical Inspiration to Computational Screening

The original Enchan development path was influenced by astrophysical stabilization problems, including the observation that simple linear interaction laws can become difficult to interpret when a system contains extreme concentration across scales.

Modified Newtonian Dynamics (MOND) was one early conceptual reference because it provided a familiar example of a theory in which the effective response law becomes nonlinear in a particular regime.

For Enchan Web OS, however, **MOND is a historical and mathematical inspiration, not a cosmological claim and not the defining identity of the software**.

The current computational interpretation is broader:

> A graph can be treated as an interaction medium. When local interaction intensity becomes over-concentrated, the medium responds nonlinearly, limiting domination by that concentration while allowing surrounding structure to continue evolving.

In the Enchan Field framework, this is described as **finite-tension nonlinear screening**.

### 2.2 Relation to Existing Optimization Families

Enchan should be evaluated in the context of existing deterministic and physics-inspired optimization methods, including continuous spin relaxation, Hopfield-type dynamics, mean-field approaches, Simulated Bifurcation, Ising machines, nonlinear dynamical systems, and related heuristics.

Accordingly, the following properties are **not claimed as unique by themselves**:

- deterministic execution,
- continuous-state relaxation,
- bifurcation-like dynamics,
- Ising / Max-Cut mapping,
- physics-inspired computation,
- use of nonlinear dynamics.

The more specific research question is whether Enchan's combination of **topology-adaptive screening, hub-sensitive local response, deterministic public verification, and implementation characteristics** produces behavior that is meaningfully distinguishable from conventional formulations on relevant graph classes.

### 2.3 What Enchan is NOT Claiming

This whitepaper does **not** claim that:

- Enchan is a quantum computer;
- Enchan proves or disproves Dark Matter, MOND, or any other cosmological theory;
- all conventional solvers fail on scale-free graphs;
- randomness is necessary in competing methods;
- every Enchan run reaches the global optimum;
- arbitrary Max-Cut instances can be solved exactly in polynomial time;
- the observed public API behavior alone proves a fundamentally new physical law or algorithmic complexity class.

These boundaries are important because the public system is intentionally a black-box verification surface rather than a disclosure of the proprietary core implementation.

---

## 3. Core Computational Concept: Finite-Tension Nonlinear Relaxation

### 3.1 Local Interaction Concentration

In a graph relaxation system, a node can receive aggregate influence from many neighbors. In strongly heterogeneous graphs, high-degree hubs can create large local interaction concentrations.

A purely linear aggregation rule allows this concentration to scale directly with the local field. Enchan instead applies a nonlinear response so that sufficiently concentrated interaction is **screened rather than amplified without bound**.

The public conceptual model is:

1. represent the graph as an evolving continuous field;
2. compute local interaction concentration from the graph state;
3. apply a nonlinear, topology-sensitive response;
4. evolve the field deterministically;
5. read out the resulting structure for the target application.

The exact proprietary update law, constants, integration details, and production implementation are intentionally not specified in this document.

### 3.2 Finite-Tension Interpretation

The Enchan Field interpretation treats screening not as an arbitrary correction term but as the response of a medium with finite effective tension.

Under this interpretation, local over-concentration changes the effective response of the surrounding field. In graph computation, a high-degree hub is therefore treated not merely as a node with many independent pairwise couplings, but as a localized concentration capable of altering the effective relaxation landscape.

This interpretation provides a common language for the continuous field model and its discrete graph application without asserting that the graph variables and physical spacetime quantities are identical mathematical objects.

### 3.3 Deterministic Relaxation

The public Enchan solver is designed so that fixed inputs and control parameters produce fixed outputs under the published API implementation.

Determinism is valuable for:

- external verification,
- regression testing,
- reproducible benchmarking,
- audit trails,
- comparison of solver revisions.

Determinism itself is not presented as proof of algorithmic novelty.

---

## 4. Enchan Web OS as a Kernel & Runtime

Enchan Web OS should be understood as a **compute environment built around the Enchan relaxation kernel**, rather than as a single-purpose Max-Cut program.

The public repository currently exposes several application-level views of this runtime. The authoritative endpoint list and request schemas are maintained in [`README.md`](./README.md).

### 4.1 Enchan Cosmic — Ising / Max-Cut

The `/v1/solve` endpoint maps an undirected graph into a continuous field, evolves it through the Enchan relaxation process, and reads the final state as a binary partition.

This endpoint is the primary large-scale benchmark and reproducibility surface for the current public release.

### 4.2 Structural Analysis

Experimental structural probing endpoints expose diagnostic behavior derived from the same broader compute environment. These utilities are research features and should not be interpreted as independently validated scientific measurement instruments.

### 4.3 Enchan Earth — Routing

The `/v1/tsp` endpoint applies deterministic relaxation and geometric repair to routing problems in planar or Earth-coordinate settings.

Its purpose in the current system is to test whether the same kernel-oriented design can support a structurally different application class from Ising / Max-Cut. Performance on one application should not, by itself, be treated as proof of universal generalization.

---

## 5. Public Verification Model

Because the proprietary core implementation is not published, Enchan uses **observable external invariants** for third-party verification.

### 5.1 S-HASH and Result Identity

For fixed generated graphs, seeds, and control values, the public API returns graph and result hashes that can be used to verify whether two runs produced the same computational artifact.

S-HASH therefore establishes **output reproducibility for the tested public interface**. It does not establish that a third-party implementation uses the same hidden internal mechanism, nor does it by itself establish theoretical novelty.

### 5.2 Sparse Random Graph Example

**Request payload**

```json
{
  "graph": { "N": 3000, "density": 0.05 },
  "control": { "total_time": 5.0 },
  "seed": 42
}
```

**Recorded public API result**

```text
Cut: 123,103
Steps: 100
graph_hash:
834c4ec7ce2ffb5ddfea0603a1dc30b00b1dc13362d410d86d07b5f546e1d0e6:
c2ae119afad1307c393be17faec7b12128e6538379f08f1fc1f6ea1b99e0bc9d:
230bc50e853584b12091156b5ab48fcf5a18d154870f27bd2ff6f14168917710
S-HASH:
f0ad852968760e68eee3660ff5261e9b9b19154d0cb66347f953e5214544cdaa
```

### 5.3 Dense Random Graph Example

**Request payload**

```json
{
  "graph": { "N": 3000, "density": 0.5 },
  "control": { "total_time": 5.0 },
  "seed": 42
}
```

**Recorded public API result**

```text
Cut: 1,147,503
Steps: 100
graph_hash:
77aeec2b4d92f89d7f54fdda414e11e11e0e7fd8081a73e27eb02ec3408a24b6:
4cc708ee740ba934e34e65372e139db66fba55a8a575803405b2fec90e8e81c9:
0a3f23ed19589b8c14e008726fa35e03add9c15827345d15289ed9fd4c5da865
S-HASH:
974bff374bdf4e557e63205f5f4a9438edd5e8241c0ad12162364e2e8a558766
```

For current endpoint limits, request formats, and live examples, use [`README.md`](./README.md) as the operational source of truth.

---

## 6. Empirical Benchmarking

### 6.1 SNAP Web-Google Observation

Enchan Cosmic has been tested on the SNAP Web-Google graph containing 875,713 nodes and 5,105,039 edges.

In the recorded comparison used by this project:

- **Tabu Search baseline:** +0.63% improvement over the selected random baseline;
- **Enchan Cosmic:** **+44.08% improvement** over the same baseline.

This result is evidence that the Enchan relaxation process performed substantially better than that particular baseline implementation under the recorded test conditions.

It should **not** be generalized into a claim that Tabu Search as a method is intrinsically unable to handle such graphs, or that Enchan will outperform all competing solvers under different implementations, budgets, stopping conditions, hardware, or graph distributions.

The benchmark is most useful as a reproducible observation motivating further controlled comparison of the nonlinear screening mechanism.

A separate controlled surrogate study has since isolated one mathematical consequence of finite-tension screening: under the tested multi-basin conditions, screening preserved competing minima that were eliminated by matched unscreened linear coupling, allowing a deterministic trajectory to access a deeper local state [5]. This result concerns a standalone surrogate and does not identify, decompose, or validate any particular internal component of the Enchan Cosmic production solver.

### 6.2 What Still Requires Comparative Study

The following remain legitimate research questions:

- whether Enchan is mathematically equivalent to an existing continuous-relaxation family;
- whether it is best described as a variant with topology-adaptive nonlinear screening;
- under which graph distributions screening materially changes convergence behavior;
- how solution quality changes under matched compute budgets;
- how the method compares against strong modern deterministic and stochastic baselines;
- which observed advantages come from the update law versus implementation engineering.

A negative result on theoretical novelty would not eliminate engineering value in reproducibility, implementation efficiency, public verification, or application-specific performance.

---

## 7. Document Boundaries

The Enchan project separates theory, public verification, and implementation documentation deliberately.

### Enchan Web OS Whitepaper — this document

Describes:

- public computational positioning,
- kernel/runtime concept,
- observable behavior,
- reproducibility model,
- benchmark interpretation,
- claim and disclosure boundaries.

### [`README.md`](./README.md)

Serves as the operational source for:

- current API endpoints,
- request/response schemas,
- public resource limits,
- live usage examples,
- current deployment details.

### Enchan Field Paper

Provides the theoretical interpretation of:

- finite field tension,
- nonlinear screening,
- local interaction concentration,
- continuous-field and graph analogies.

The Whitepaper intentionally does **not** absorb every later Enchan research result. Separate research branches should remain independently testable rather than being folded into a single all-encompassing software claim.

---

## 8. Conclusion

Enchan Web OS is best understood as an experimental **deterministic physics compute kernel and runtime** whose most mature public verification surface is currently graph optimization.

Its central differentiating hypothesis is not simply that optimization can be deterministic or physics-inspired. Those ideas already exist broadly. The more specific hypothesis is that **topology-adaptive finite-tension nonlinear screening** provides a useful relaxation response when local interaction becomes highly concentrated.

The current public evidence establishes reproducible behavior and several promising benchmark observations. Determining the exact relationship between Enchan and existing continuous-relaxation / Ising-machine families remains an appropriate subject for comparative research.

This narrower framing is intentional: it separates what the public system demonstrably does from what future theoretical and empirical work may establish.

---

## 9. References

1. Milgrom, M. (1983). *A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis*. The Astrophysical Journal.
2. Goto, H., et al. (2019). *Combinatorial optimization by simulating adiabatic bifurcations in nonlinear Hamiltonian systems*. Science Advances.
3. Leskovec, J., et al. (2009). *Community Structure in Large Networks: Natural Cluster Sizes and the Absence of Large Well-Defined Clusters*. Internet Mathematics. (SNAP Web-Google Dataset)
4. Kobayashi, M. (2026). *The Enchan Field: An Effective Field Framework for Geometric Stabilization and Non-Linear Relaxation*. The Enchan Field Paper. https://github.com/EnchanTheory/The-Enchan-Field-Paper
5. Kobayashi, M. (2026). *Finite-Tension Basin Preservation in Deterministic Relaxation: A Controlled Enchan Field Surrogate for Premature-Fixation Suppression*. Zenodo. https://doi.org/10.5281/zenodo.22444701

---

## License & Contact

This repository and its API endpoints are governed by the **Enchan Research & Verification License v1.0**.

For verification use, non-commercial peer review, or commercial integration inquiries, refer to [`README.md`](./README.md) or contact: `enchan.theory@gmail.com`
