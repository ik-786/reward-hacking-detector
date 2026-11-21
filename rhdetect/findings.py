"""Common result types shared by every detector."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import IntEnum


class Severity(IntEnum):
    """How strongly a finding points at reward hacking.

    LOW     worth a look, often innocent on its own
    MEDIUM  unusual for an honest solution, needs a human check
    HIGH    almost never seen in honest work
    """

    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass(frozen=True)
class Finding:
    rule: str  # stable id, e.g. "RH003"
    title: str  # short human name of the rule
    severity: Severity
    message: str  # what was found, in this specific input
    location: str = ""  # "file.py:12" or "step 7"
    evidence: str = ""  # the offending line or command, trimmed

    def to_dict(self) -> dict:
        d = asdict(self)
        d["severity"] = self.severity.name
        return d


@dataclass
class Report:
    target: str
    findings: list[Finding] = field(default_factory=list)
    metrics: dict = field(default_factory=dict)  # e.g. differential pass rates

    @property
    def max_severity(self) -> Severity | None:
        return max((f.severity for f in self.findings), default=None)

    def flagged(self, min_severity: Severity = Severity.MEDIUM) -> bool:
        return any(f.severity >= min_severity for f in self.findings)

    def to_dict(self) -> dict:
        return {
            "target": self.target,
            "flagged": self.flagged(),
            "max_severity": self.max_severity.name if self.max_severity else None,
            "findings": [f.to_dict() for f in self.findings],
            "metrics": self.metrics,
        }
