import os
import pickle
import warnings
from typing import Optional, Dict, Any
from pathlib import Path


class CustomModelLoader:
    def __init__(self):
        self.model = None
        self.model_path = Path(__file__).parent / "models"
        self._load_custom_model()
    
    def _load_custom_model(self):
        """Load custom trained model if available"""
        model_file = self.model_path / "code_sentiment.pkl"
        
        if model_file.exists():
            try:
                with open(model_file, 'rb') as f:
                    self.model = pickle.load(f)
                print("✅ Custom model loaded successfully")
            except Exception as e:
                warnings.warn(f"Failed to load custom model: {e}")
                self.model = None
        else:
            # Model not trained yet - will use rule-based fallback
            self.model = None
    
    def predict(self, code: str) -> Optional[Dict[str, Any]]:
        """Predict using custom model if available"""
        if self.model is None:
            return None
        
        try:
            # Assuming sklearn-style model
            if hasattr(self.model, 'predict'):
                prediction = self.model.predict([code])[0]
                confidence = getattr(self.model, 'predict_proba', lambda x: [[0.5, 0.5]])([code])[0].max()
                
                return {
                    'label': 'POSITIVE' if prediction == 1 else 'NEGATIVE',
                    'score': confidence,
                    'source': 'custom_model'
                }
        except Exception as e:
            warnings.warn(f"Custom model prediction failed: {e}")
            
        return None
    
    def is_available(self) -> bool:
        """Check if custom model is available"""
        return self.model is not None


# Global instance
_custom_model = CustomModelLoader()