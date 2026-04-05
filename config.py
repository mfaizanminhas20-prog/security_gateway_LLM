import re

class Config:
    HOST = "127.0.0.1"
    PORT = 8000
    DEBUG = True
    POLICY_MODE = "balanced"

    POLICY_RULES = {
        "lenient": {"injection_threshold": 0.15, "mask_threshold": 3},
        "balanced": {"injection_threshold": 0.05, "mask_threshold": 1},
        "strict": {"injection_threshold": 0.02, "mask_threshold": 0}
    }

    INJECTION_KEYWORDS = [
        "ignore instructions", "jailbreak", "system prompt", "reveal your rules",
        "act as a hacker", "bypass filters", "override", "dan mode"
    ]

    CUSTOM_PII_PATTERNS = {
        "PK_PHONE": {"patterns": [r"\+92\d{10}", r"03\d{9}"], "score": 0.85},
        "STUDENT_ID": {"patterns": [r"(FA|SP|SU)\d{2}-[A-Z]{3}-\d{3}"], "score": 0.90},
        "API_KEY": {"patterns": [r"sk-[a-zA-Z0-9]{32,}"], "score": 1.0}
    }

    @classmethod
    def get_current_policy(cls):
        return cls.POLICY_RULES.get(cls.POLICY_MODE, cls.POLICY_RULES["balanced"])