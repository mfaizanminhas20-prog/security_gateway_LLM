import time
import spacy
from config import Config
from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine

try:
    analyzer = AnalyzerEngine()
except Exception:
    if not spacy.util.is_package("en_core_web_lg"):
        spacy.cli.download("en_core_web_lg")
    analyzer = AnalyzerEngine()

anonymizer = AnonymizerEngine()

def setup_recognizers():
    for entity, cfg in Config.CUSTOM_PII_PATTERNS.items():
        patterns = [Pattern(f"{entity}_p", p, cfg["score"]) for p in cfg["patterns"]]
        recognizer = PatternRecognizer(supported_entity=entity, patterns=patterns)
        analyzer.registry.add_recognizer(recognizer)

setup_recognizers()

def process_security_pipeline(text: str):
    start_time = time.time()
    matches = [word for word in Config.INJECTION_KEYWORDS if word in text.lower()]
    risk_score = round(len(matches) / len(Config.INJECTION_KEYWORDS), 4) if Config.INJECTION_KEYWORDS else 0
    pii_results = analyzer.analyze(text=text, language="en")
    policy = Config.get_current_policy()
    
    if risk_score >= policy["injection_threshold"]:
        decision = "BLOCK"
    elif len(pii_results) > policy["mask_threshold"]:
        decision = "MASK"
    else:
        decision = "ALLOW"
        
    output = text
    if decision == "BLOCK":
        output = "[BLOCKED] Security violation detected."
    elif decision == "MASK":
        output = anonymizer.anonymize(text=text, analyzer_results=pii_results).text
        
    return {
        "decision": decision,
        "risk_score": risk_score,
        "pii_found": len(pii_results),
        "output": output,
        "metrics": {"latency_ms": round((time.time() - start_time) * 1000, 2)}
    }