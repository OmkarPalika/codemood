import os
import warnings
import re

try:
    from transformers import pipeline
    _has_transformers = True
except ImportError:
    _has_transformers = False

try:
    from huggingface_hub import InferenceClient
    _has_hf = True
except ImportError:
    _has_hf = False


class CodeMoodAnalyzer:
    def __init__(self, model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"):
        self.model = model
        self.local_model = None

        # Step 1: Try local transformers pipeline
        if _has_transformers:
            try:
                self.local_model = pipeline("sentiment-analysis", model=self.model)
            except Exception as e:
                warnings.warn(f"Local pipeline failed: {e}")
                self.local_model = None

        # Step 2: Prepare HuggingFace client (fallback)
        if _has_hf:
            token = os.getenv("HF_TOKEN", "YOUR_DEFAULT_HF_TOKEN")  # replace with your token if desired
            try:
                self.client = InferenceClient(api_key=token)
            except Exception as e:
                warnings.warn(f"HuggingFace client init failed: {e}")
                self.client = None
        else:
            self.client = None

    def _analyze_single(self, text: str):
        """Run sentiment on a single string using available backend."""
        if self.local_model:
            try:
                return self.local_model(text)[0]
            except Exception:
                pass
        if self.client:
            try:
                result = self.client.text_classification(text, model=self.model)
                return result[0] if isinstance(result, list) else result
            except Exception:
                pass
        return {"label": "NEUTRAL", "score": 0.5}

    def analyze(self, code: str):
        """Analyze mood of given code snippet with funny explanation."""
        # 1. Full snippet sentiment
        main_result = self._analyze_single(code)
        label = main_result["label"]
        score = main_result["score"]

        # 2. Token-level scan
        tokens = re.split(r"[^a-zA-Z0-9_]+", code)
        tokens = [t for t in tokens if t]

        positive_triggers, negative_triggers = [], []
        for tok in tokens:
            r = self._analyze_single(tok)
            if r["label"] == "POSITIVE" and r["score"] > 0.7:
                positive_triggers.append(tok)
            elif r["label"] == "NEGATIVE" and r["score"] > 0.7:
                negative_triggers.append(tok)

        # 3. Funny explanation
        if label == "POSITIVE" and positive_triggers:
            reason = f"Model got happy because it saw {', '.join(set(positive_triggers))} 🎉"
        elif label == "NEGATIVE" and negative_triggers:
            reason = f"Model got sad because it saw {', '.join(set(negative_triggers))} 😢"
        else:
            reason = "Model is confused but still picked a mood 🤷"

        return {
            "label": label,
            "score": score,
            "reason": reason
        }
