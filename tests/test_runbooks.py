#!/usr/bin/env python3
"""
Diagnostic test suite for FLOP Operator Handbook runbooks and scripts.
"""

import os
import subprocess
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()


class TestOperatorHandbook(unittest.TestCase):

    def test_runbook_files_exist(self):
        required_docs = [
            REPO_ROOT / "docs" / "systemd_hardening.md",
            REPO_ROOT / "docs" / "troubleshooting_runbook.md",
            REPO_ROOT / "scripts" / "node_healthcheck.sh",
            REPO_ROOT / "SECURITY.md",
            REPO_ROOT / "README.md",
        ]
        for doc in required_docs:
            self.assertTrue(doc.exists(), f"Missing required documentation/script: {doc}")
            self.assertGreater(doc.stat().st_size, 100, f"File {doc} is suspiciously small")

    def test_healthcheck_script_syntax(self):
        script_path = REPO_ROOT / "scripts" / "node_healthcheck.sh"
        self.assertTrue(script_path.exists())
        # Bash syntax check (-n)
        res = subprocess.run(["bash", "-n", str(script_path)], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, f"Bash syntax check failed: {res.stderr}")

    def test_systemd_unit_template_validity(self):
        systemd_doc = (REPO_ROOT / "docs" / "systemd_hardening.md").read_text(encoding="utf-8")
        self.assertIn("[Unit]", systemd_doc)
        self.assertIn("[Service]", systemd_doc)
        self.assertIn("CPUQuota=30%", systemd_doc)
        self.assertIn("MemoryMax=650M", systemd_doc)
        self.assertIn("NoNewPrivileges=true", systemd_doc)


if __name__ == "__main__":
    unittest.main()
