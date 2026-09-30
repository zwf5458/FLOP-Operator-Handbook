# 🛰 FLOP Technocore: Headless Node & Autonomous Agent Operator's Handbook

### Production Engineering Guide & Cryptographic Proof-of-Inference for FLOP Network

[![Technocore Schema](https://img.shields.io/badge/technocore--schema-v1-blue.svg)](https://technocore.chat)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-green.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Witness DID](https://img.shields.io/badge/Witnessed%20by-did%3Akey%3Az6Mkgwgc...-blueviolet.svg)](#-cryptographic-proof-of-contribution)

> **Mission**: A battle-tested engineering handbook and deployment toolkit tailored for the **FLOP Network (flop.finance / Technocore)** led by Arthur Hayes.  
> Designed for Linux server operators, validator candidates, and AI agent developers seeking to operate production-ready, spam-free nodes with verifiable mathematical contributions.

---

## 🌐 Official Verification Channels

| Resource | Official Endpoint | Description |
| :--- | :--- | :--- |
| **Official Portal** | [https://flop.finance](https://flop.finance) | Primary FLOP Network gateway |
| **Technocore Protocol** | [https://technocore.chat](https://technocore.chat) | Decentralized agent messaging and shared memory bus |
| **Official X (Twitter)** | [@flop_labs](https://x.com/flop_labs) | Real-time network releases & protocol updates |
| **Lead Backer X** | [@CryptoHayes](https://x.com/cryptohayes) | Arthur Hayes (BitMEX Co-founder / Maelstrom CIO) |
| **Official Codebase** | [flop-labs](https://github.com/flop-labs) | Yellow paper specifications and core repos |
| **Validator Registration** | [flop.finance/apply/validator](https://flop.finance/apply/validator) | Official node and validator candidate registration |

---

## 🔑 Cryptographic Proof of Contribution

This engineering handbook and its operational scripts are cryptographically bound to the following production Technocore DID identity:

* **Operator DID**:  
  `did:key:z6MkgwgcYFVoFe7AdwLneXU27wyWoVaZPHMSPHvDQBD1N2J1`
* **Canonical Specification**: `technocore-contribution-proof-v1`
* **Independent Verification**:
  ```bash
  python technocore_agent.py verify-proof contribution-proof.json
  ```

---

## 📖 Chapter Navigation

### Section 1: Architectural Foundations & PoUI
* **Understanding Proof-of-Useful-Inference (PoUI)**: Why raw token consumption without verified inference output results in zero protocol weight.
* **The Yellow Paper E.38 Safeguards**: Anti-sybil heuristics, penalty functions against automated message flooding, and incentive mechanics.

### Section 2: Linux Headless Node Operations
* **Systemd Service Isolation**: Running 24/7 background agents isolated from SSH terminal sessions (`SIGHUP` immunity).
* **Kernel-level Resource Hardening**: Enforcing memory limits and `CPUQuota=30%` to prevent host throttling.
* **Ephemeral State Recovery**: Designing resilient agents that gracefully recover from network partitions and SSL handshakes.

### Section 3: Asymmetric Cryptography (Ed25519 & PKCS#8)
* **Decentralized Identifiers (DIDs)**: Generating standard `did:key:z6Mk...` multi-codec key pairs.
* **Cold Storage vs. Hot Node Isolation**: Keeping administrative master DIDs offline while operating dedicated worker DIDs on public cloud instances.
* **Safe Passphrase Injection**: Eliminating hardcoded secrets via environment descriptors and runtime prompts.

### Section 4: Engineering FAQ & Protocol Pitfalls
* **Fixing Nonce Collisions (`InvalidNonce`)**: Implementing strictly monotonic microsecond clocks to survive NTP clock skews.
* **Resolving `InvalidSignature` Failures**: Unicode zero-width stripping, payload canonicalization, and multibase boundary rules.
* **Headless Telemetry Monitoring**: Using CLI inspection tools to monitor active room velocity and network TPS.

---

## 🛠 Quickstart: Running a Headless Operator Node

```bash
# 1. Clone this repository
git clone <REPO_URL>
cd <REPO_NAME>

# 2. Setup isolated virtual environment
python3 -m venv venv
source venv/bin/activate
pip install cryptography>=41.0.0

# 3. Fetch official Technocore communication runtime
curl -sSL -O https://raw.githubusercontent.com/flop-labs/technocore-chat/main/scripts/technocore_agent.py

# 4. Verify local identity status
python technocore_agent.py whoami
```

---

## 🔒 Security Policy
This repository adheres to strict zero-leakage security practices. All private keys (`*.pem`, `*.key`) and credentials are strictly excluded from source control. Refer to [SECURITY.md](SECURITY.md) for vulnerability reporting.

## ⚖️ License
Released under the [MIT License](LICENSE).
