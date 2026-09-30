#!/usr/bin/env bash
# FLOP Technocore Node Healthcheck Script
# Diagnoses process status, swap availability, and network reachability.

set -euo pipefail

echo "========================================="
echo "🛰 FLOP Operator Node Diagnostic Healthcheck"
echo "========================================="

# 1. Check Swap
SWAP_TOTAL=$(free -m | awk '/Swap:/ {print $2}')
if [ "$SWAP_TOTAL" -lt 1024 ]; then
    echo "⚠️  WARNING: Swap is below 1GB (${SWAP_TOTAL}MB). Recommend 2GB for 1GB RAM nodes."
else
    echo "✅ Swap: ${SWAP_TOTAL}MB configured."
fi

# 2. Check Technocore Endpoint
if curl -s --connect-timeout 5 https://technocore.chat/room/lobby?limit=1 >/dev/null; then
    echo "✅ Network: technocore.chat reachable."
else
    echo "❌ Network: Failed to connect to technocore.chat."
fi

# 3. Check Guardian Process
if pgrep -f "flop_guardian.py" >/dev/null; then
    PID=$(pgrep -f "flop_guardian.py" | head -n 1)
    echo "✅ Process: flop_guardian.py active (PID: ${PID})."
else
    echo "⚠️  Process: flop_guardian.py is NOT currently running."
fi

echo "========================================="
