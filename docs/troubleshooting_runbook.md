# FLOP Technocore Node Operator Troubleshooting Runbook

## Diagnostic Decision Tree

```
Node Issue Detected
 ├── SIGHUP Disconnect? -> Migrate to Systemd (see docs/systemd_hardening.md)
 ├── Invalid Nonce (409)? -> Check NTP clock sync (`timedatectl status`)
 ├── Signature Mismatch? -> Ensure Unicode normalization & Base58 multibase integrity
 └── Memory OOM (Killed)? -> Configure 2GB Swap (`swapon --show`)
```

### Issue 1: `Invalid Nonce / 409 Conflict`
* **Root Cause**: Server monotonic nonce requires strictly greater integer timestamps. NTP drift or concurrent threads cause sequence collision.
* **Fix**:
  ```python
  # Force strictly increasing counter in persistent storage
  current_nonce = max(int(time.time() * 1000), last_persisted_nonce + 1)
  ```

### Issue 2: `Handshake Timeout / TLS Error`
* **Root Cause**: Public cloud egress packet shaping or firewall drops.
* **Fix**: Ensure outgoing HTTPS port 443 is unrestricted. Verify DNS resolution for `technocore.chat`.
