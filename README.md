# DLML — Deterministic Layered Manifest Language  
### *A 5-layer, hash-verified, zero-drift manifest format for reproducible AI agents.*

[![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)]()
[![Spec](https://img.shields.io/badge/spec-v1.0.0-green.svg)]()
[![Status](https://img.shields.io/badge/status-experimental-yellow.svg)]()
[![YAML](https://img.shields.io/badge/based_on-YAML-blue)]()

**DLML** is a new, open, portable manifest format that packages the **identity**,  
**context**, **state**, **intent**, and **payload** of an AI agent or microservice  
into a single multi-document, hash-verifiable bundle.

DLML solves the hardest problem in emerging AI systems:

> **“How do you reconstruct an agent’s full operational state deterministically  
> across machines, time, and environments — without hallucination or drift?”**

Features:
- 5 canonical layers  
- 11 structural limits  
- Zero-inference rules  
- Cryptographic SHA-256 footer hash  
- Portable seed arcs for agent reconstruction  
- Lightweight YAML-based format

The full specification is available in `SPEC.md`.
