---
title: "Appendix: Substrate Context"
summary: "A bounded component of the Consullo public research program: Appendix: Substrate Context."
status: "specified but not implemented"
provenance: "derived from the owner-approved private Consullo design corpus; no artifact-specific public receipt has been issued"
claim_ids: ["CP-001"]
last_reviewed: "2026-08-12"
receipt: "none"
non_claims: ["Publication does not establish implementation or operational effectiveness.", "The implementation-evidence appendix records component evidence only and is not evidence of operational capability for this page."]
---
# Appendix: Substrate Context

This appendix holds infrastructure that supports the five theses without becoming a sixth thesis. These systems should be referenced by the master frame and imported by individual theses as needed.

## Purpose

The five theses are theory claims. Substrate context is enabling infrastructure. Keeping substrate context separate prevents alignment, economy, model routing, and prompt decomposition from being conflated.

## Substrate Areas

### Specialized LLM Ecosystem

Source:

- the Consullo agent-hierarchy narrative

Role:

- provider abstraction
- model routing
- specialized model selection
- fallback planning
- model capability tracking
- cost and latency tradeoff management

Primary imports:

- Thesis 2 imports model capability routing for cognitive agents.
- Thesis 4 imports model routing for code generation and repair.
- Thesis 1 imports cost and performance evidence for improvement evaluation.
- Thesis 5 imports model provenance and trust evidence for scoped permissioning.

### Atomic Prompt And Compiled-Code Orchestration

Sources:

- the Consullo agent-hierarchy narrative
- the internal atomic-prompt design note

Role:

- decomposition of monolithic prompts into smaller atomic prompts
- replacement of expensive LLM reasoning with compiled algorithms where appropriate
- token-cost reduction
- component-level validation
- reusable prompt and algorithm libraries

Primary imports:

- Thesis 4 imports this as software substrate.
- Thesis 2 imports it as cognitive decomposition support.
- Thesis 1 imports cost and reliability evidence for improvement evaluation.

### Rapid Knowledge Access

Source:

- the Consullo agent-hierarchy narrative

Role:

- retrieval
- indexing
- low-latency knowledge access
- context assembly
- memory-assisted reasoning

Primary imports:

- Thesis 2 imports this as cognitive substrate support.
- Thesis 1 imports it for evidence retrieval and method-memory reuse.
- Thesis 3 imports it for causal evidence and prior case retrieval.

### Internal Economy

Sources:

- the Consullo agent-hierarchy narrative
- the Consullo agent-hierarchy narrative
- an internal feature-design note
- an internal feature-design note
- an internal feature-design note

Role under single-owner Phase 1:

- internal resource accounting
- transfer pricing
- budgeting
- capital allocation
- service provision among company-owned agents and divisions
- cost measurement
- coordination overhead measurement

This is not independent market governance and is not an alignment mechanism. It is a resource-accounting and coordination substrate inside a single ownership boundary.

Primary imports:

- Thesis 1 imports cost of improvement and resource constraints.
- Thesis 3 imports economic objectives and causal analysis of resource allocation.
- Thesis 5 imports internal economy as a scope for trust and alignment review of economic actions.

## Substrate Invariant

No substrate system should be used as proof of capability, alignment, or superintelligence. Substrate systems provide mechanisms that must still be measured, governed, and validated through the relevant thesis.

## AAF Data Flow Reference

The Adversarial Alignment Function is owned by Thesis 5, but it imports substrate and cognitive mechanisms:

1. A high-stakes action or modification reaches a Thesis 1 acceptance gate.
2. The gate invokes `AdversarialAlignmentOrchestrator` when invariant I12 applies.
3. The AAF draws critique from rotating ethical personas, multi-model critique, theory-of-mind stakeholder simulations, and external review where available.
4. Theory-of-mind agents such as `BeliefModelingProcessor`, `IntentionRecognitionAnalyzer`, and `PerspectiveTakingModeler` support stakeholder simulation.
5. Critiques and dissent are preserved in the evidence ledger.
6. Severe unresolved objections trigger rejection, revision, or escalation to human authority.
7. If human authority overrides the objection, the override and rationale remain auditable.
