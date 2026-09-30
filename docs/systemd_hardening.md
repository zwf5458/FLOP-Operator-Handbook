# Linux Systemd Hardening & Resource Isolation Guide

## 1. Overview
In multi-tenant cloud environments or low-tier VPS (1 CPU / 1GB RAM), background node processes frequently suffer from uncontained memory leaks or CPU starvation. This runbook establishes a production-grade Systemd configuration with hard kernel-level cgroups boundaries.

## 2. Unit Configuration (`flop-agent.service`)

Create `/etc/systemd/system/flop-agent.service`:

```ini
[Unit]
Description=FLOP Technocore Autonomous Operator Agent
After=network.target network-online.target
Wants=network-online.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/flop_agent
ExecStart=/root/flop_agent/venv/bin/python3 /root/flop_agent/flop_guardian.py
Restart=always
RestartSec=15

# Resource Isolation (Cgroups v2)
MemoryMax=650M
MemoryHigh=550M
CPUQuota=30%
TasksMax=64

# Security Sandboxing
NoNewPrivileges=true
ProtectSystem=full
ProtectHome=read-only
ReadWritePaths=/root/flop_agent

# Standard I/O Logging
StandardOutput=append:/root/flop_agent/agent_guardian.log
StandardError=append:/root/flop_agent/agent_guardian.log

[Install]
WantedBy=multi-user.target
```

## 3. Deployment Commands

```bash
# Reload unit definitions
sudo systemctl daemon-reload

# Enable service across reboots
sudo systemctl enable flop-agent.service

# Start the agent
sudo systemctl start flop-agent.service

# Verify real-time status and cgroup enforcement
sudo systemctl status flop-agent.service
```
