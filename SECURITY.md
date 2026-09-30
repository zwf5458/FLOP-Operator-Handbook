# Security Policy for FLOP Node Operators

## Threat Model: Headless Server Deployments

This security policy applies to server operators running autonomous node instances for FLOP Technocore.

### Operator Hardening Checkpoints:
1. **Unprivileged Execution**:
   - Production daemons should be restricted from acquiring new privileges via `NoNewPrivileges=true` in systemd.
2. **Key Isolation**:
   - `identity.pem` permissions must be strictly `0600` (`-rw-------`).
   - Store operator master DIDs in offline storage; run headless bots with secondary worker DIDs.
3. **Environment Security**:
   - Never pass passphrases as command-line arguments (visible via `ps aux`). Always use environment variables or stdin.

### Vulnerability Reporting
For security disclosures regarding node operator scripts, email the repository owner or open an encrypted communication using Technocore DID.
