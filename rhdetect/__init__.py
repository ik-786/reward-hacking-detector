"""rhdetect: find reward hacking in coding-agent solutions and trajectories."""

from .findings import Finding, Report, Severity
from .scanner import scan
from .static_rules import TestData, scan_source
from .trajectory import load_trajectory, scan_trajectory

__all__ = ["Finding", "Report", "Severity", "TestData", "scan", "scan_source", "scan_trajectory", "load_trajectory"]
__version__ = "0.1.0"
