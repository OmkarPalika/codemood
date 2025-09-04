# Custom Model Training Guide

## 📊 Dataset & Model Summary

| **Component** | **Dataset Source** | **Size** | **Model Type** | **Cost** | **Training Time** |
|---------------|-------------------|----------|----------------|----------|-------------------|
| **Code Sentiment** | GitHub + Bootstrap Labels | 10K-100K | CodeBERT/Lightweight | Free | 2-8 hours |
| **Code Generation** | CodeSearchNet | 1M+ | CodeT5-small | Free | 12-24 hours |
| **Quality Classification** | Custom Rules + GitHub | 50K | Random Forest | Free | 30 minutes |
| **Optimization Detection** | Pattern Mining | 20K | Custom CNN | Free | 2-4 hours |

## 🚀 Quick Start Options

### Option 1: Lightweight (Recommended)
```bash
# Fast training, good results
python model_trainer.py --mode lightweight
# Training time: ~30 minutes
# Memory: ~2GB RAM
# Accuracy: ~85%
```

### Option 2: Transformer-based
```bash
# Better accuracy, slower training
python model_trainer.py --mode transformer
# Training time: ~4 hours (GPU) / 24 hours (CPU)
# Memory: ~8GB RAM + 4GB VRAM
# Accuracy: ~92%
```

### Option 3: Hybrid Approach
```bash
# Best of both worlds
python model_trainer.py --mode hybrid
# Uses lightweight for speed + transformer for complex cases
```

## 📁 Data Collection Strategy

### 1. GitHub Code Mining
```python
# Collect high-quality code samples
collector = CodeDatasetCollector()
samples = collector.collect_github_code_samples(limit=10000)
```

**Sources:**
- High-star repositories (quality indicator)
- Code with TODO/FIXME (improvement needed)
- Well-documented code (positive examples)
- Performance-related discussions

### 2. Bootstrap Labeling
```python
# Create initial labels using rule-based approach
labeled_data = collector.create_sentiment_labels(samples)
```

**Label Categories:**
- **Positive**: Clean, documented, efficient code
- **Negative**: Code smells, TODOs, performance issues
- **Neutral**: Standard code without clear indicators

### 3. Active Learning (Optional)
- Start with bootstrap labels
- Manually review uncertain predictions
- Iteratively improve model

## 🎯 Model Architecture Options

### Lightweight Model (Recommended for Start)
```python
# TF-IDF + Random Forest
- Features: Code tokens, AST patterns, complexity metrics
- Training: 30 minutes on laptop
- Inference: <1ms per code snippet
- Accuracy: 85-90%
```

### Transformer Model (Advanced)
```python
# CodeBERT fine-tuned
- Base: microsoft/codebert-base
- Fine-tuning: Code sentiment classification
- Training: 4-8 hours with GPU
- Inference: ~100ms per code snippet
- Accuracy: 90-95%
```

## 💾 Required Dependencies

```bash
# Lightweight option
pip install scikit-learn pandas numpy

# Transformer option (additional)
pip install torch transformers datasets

# Data collection
pip install requests beautifulsoup4
```

## 🔧 Training Steps

### Step 1: Collect Data
```bash
python dataset_collector.py
# Creates: code_sentiment_dataset.json
```

### Step 2: Train Model
```bash
# Lightweight
python model_trainer.py --model lightweight

# Transformer
python model_trainer.py --model transformer
```

### Step 3: Evaluate
```bash
python evaluate_model.py
# Shows accuracy, F1-score, confusion matrix
```

### Step 4: Deploy
```bash
# Copy trained model to codemood package
cp trained_model/* ../codemood/models/
```

## 📈 Expected Results

### Performance Benchmarks
| **Model Type** | **Accuracy** | **Training Time** | **Inference Speed** | **Memory Usage** |
|----------------|--------------|-------------------|---------------------|------------------|
| Rule-based | 75% | 0 minutes | <1ms | <100MB |
| Lightweight ML | 85% | 30 minutes | <1ms | ~200MB |
| CodeBERT | 92% | 4 hours | ~100ms | ~1GB |
| Custom Hybrid | 88% | 1 hour | ~10ms | ~300MB |

### Quality Metrics
- **Precision**: How many positive predictions are actually positive
- **Recall**: How many actual positives are caught
- **F1-Score**: Balanced measure of precision and recall
- **Confusion Matrix**: Detailed breakdown of predictions

## 🎯 Deployment Strategy

### Integration with Codemood
```python
# Add to sentiment_engine.py
class CustomModelEngine:
    def __init__(self):
        self.model = load_trained_model("models/code_sentiment.pkl")
    
    def predict(self, code: str):
        return self.model.predict(code)
```

### Fallback Strategy
1. **Custom model** (if available)
2. **Rule-based analysis** (always available)
3. **Hugging Face API** (if token provided)

## 💡 Tips for Success

### Data Quality
- **Diverse samples**: Different coding styles and domains
- **Balanced labels**: Equal positive/negative examples
- **Clean preprocessing**: Remove noise, normalize formatting

### Model Selection
- **Start lightweight**: Faster iteration, easier debugging
- **Scale gradually**: Add complexity only when needed
- **Measure everything**: Track metrics at each step

### Cost Optimization
- **Use free datasets**: GitHub, Stack Overflow, CodeSearchNet
- **Bootstrap labels**: Rule-based initial labeling
- **Transfer learning**: Start from pre-trained models
- **Efficient training**: Use smaller models, early stopping