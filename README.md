# 📚 NLP Project: Moroccan Legal System Analysis & RAG Architectures

**Author**: EL-GHARIB MAHMOUD  
**Professor**: Ikram BEN ABDEL OUAHAB  
**Course**: Natural Language Processing (NLP) — 2026  
**Language**: Python 3 + Jupyter Notebooks  

---

## 🎯 Project Overview

This project implements a complete **NLP pipeline** for Arabic text processing and **Retrieval-Augmented Generation (RAG)** systems applied to Moroccan legal documents. The work progresses across **4 weeks**, from basic NLP processing to advanced RAG architecture comparison.

### Key Objectives

✅ Build complete 5-stage NLP pipeline for Arabic text  
✅ Extract and structure legal documents from PDF  
✅ Implement RAG system for legal Q&A in Arabic/French  
✅ Compare 7 different RAG architectures with quantitative evaluation  
✅ Create interactive web interface for legal consultation  

---

## 📂 Project Structure

```
NLP-DEVOIRS-EL-GHARIB-MAHMOUD-master/
│
├── 📄 README.md                                    [This file]
├── 📄 RAPPORT_NLP_PIPELINE_WEEK_1.md              [Week 1 Report]
├── 📄 RAPPORT_EXTRACTION_WEEK_2.md                [Week 2 Report]
├── 📄 RAPPORT_RAG_SYSTEM_WEEK_3.md                [Week 3 Report]
├── 📄 RAPPORT_RAG_ARCHITECTURES_WEEK_4.md         [Week 4 Report]
├── 📄 documents_juridiques_arabes.txt             [Source corpus]
│
├── Week_1/
│   └── 📓 nlp_pipeline_week_1.ipynb               [5-stage NLP pipeline]
│
├── Week_2/
│   ├── 📓 devoir2.ipynb                           [PDF extraction & structuration]
│   └── Data/
│       └── extracted_legal_documents.csv          [Extracted articles]
│
├── Week_3/
│   ├── 📓 devoir3_rag_droit_marocain.ipynb       [RAG system implementation]
│   └── Data/
│       └── code_route.csv                         [Traffic code corpus]
│
└── Week_4/
    ├── 📓 devoir4_rag_droit_marocain.ipynb       [7 RAG architectures compared]
    ├── Data/
    │   ├── corpus_juridique_marocain.csv          [73 legal articles]
    │   └── create_csv.py                          [Corpus generator]
    └── Generated/
        ├── corpus_juridique_maroc.json            [JSON export]
        ├── graph_rag_knowledge.png                [Knowledge graph]
        ├── rag_evaluation_heatmap.png             [Metrics heatmap]
        └── rag_comparison_bars.png                [Architecture comparison]
```

---

## 📖 Week-by-Week Breakdown

### Week 1: NLP Pipeline for Arabic Text Processing

**Objective**: Build a complete 5-stage NLP pipeline for processing Arabic legal documents.

**Notebook**: `Week_1/nlp_pipeline_week_1.ipynb`

#### Pipeline Stages

| Stage | Component | Input | Output | Technologies |
|-------|-----------|-------|--------|---------------|
| **1** | Data Collection | PDF files | Raw text | PyPDF2 |
| **2** | Preprocessing | Raw Arabic text | Normalized tokens | PyArabic, NLTK |
| **3** | Syntactic Analysis | Tokens | POS tags + parse trees | Rule-based tagger |
| **4** | Semantic Analysis | Tagged tokens | Named entities | Pattern-based NER |
| **5** | Vectorization | Text | TF-IDF vectors | scikit-learn |

#### Key Features

- ✅ Arabic text normalization (diacritics removal, hamza normalization, ta forms)
- ✅ Tokenization with Arabic-specific rules
- ✅ POS tagging (6 categories: VERB, NOUN, ADJ, ADP, CONJ, PRON)
- ✅ NER extraction (6 entity types: PERSON, LOC, ORG, DATE, TECH, MISC)
- ✅ TF-IDF vectorization with cosine similarity
- ✅ Document clustering (KMeans, k=5)

#### Output Report

📊 **[RAPPORT_NLP_PIPELINE_WEEK_1.md](RAPPORT_NLP_PIPELINE_WEEK_1.md)**
- 5-stage architecture diagram
- Implementation details
- Processing pipeline visualization
- Performance metrics

---

### Week 2: PDF Extraction & Legal Document Structuration

**Objective**: Extract Moroccan traffic code from PDF and structure into analyzable dataset.

**Notebook**: `Week_2/devoir2.ipynb`

#### Processing Steps

1. **PDF Extraction**: PyMuPDF + Tesseract OCR
2. **Arabic Normalization**: Remove diacritics, normalize hamza/ta forms
3. **Hierarchical Parsing**: Book → Section → Chapter → Article
4. **NER Extraction**: Fines, points, vehicle categories, keywords
5. **ML Processing**: TF-IDF clustering, BERT embeddings
6. **Output Generation**: CSV, JSON, embeddings

#### Output Data

- 📊 **142 infractions** extracted
- 📋 **14 columns** per infraction (article_id, description, fine, points, etc.)
- 🔗 **Hierarchical structure** preserved
- 💾 **Multiple formats**: CSV, JSON, .npy embeddings

#### Extracted Features

| Feature | Type | Example |
|---------|------|---------|
| Article ID | String | `ART_42` |
| Description | Arabic | `تجاوز السرعة المحددة...` |
| Fine Range | Float | 300-1500 MAD |
| Points Deducted | Int | 2-6 points |
| Vehicle Category | Enum | Motorcycle, SUV, Heavy truck |
| Violation Keywords | List | Speed, parking, alcohol |

#### Output Report

📊 **[RAPPORT_EXTRACTION_WEEK_2.md](RAPPORT_EXTRACTION_WEEK_2.md)**
- PDF extraction pipeline
- Normalization techniques
- Hierarchical structuring
- NER patterns
- ML clustering results
- Data statistics

---

### Week 3: RAG System for Legal Q&A

**Objective**: Implement complete RAG system for answering questions about Moroccan traffic code.

**Notebook**: `Week_3/devoir3_rag_droit_marocain.ipynb`

#### RAG Architecture

```
User Question (Arabic/French)
         ↓
    Preprocessing
         ↓
 Embedding Generation
  (Sentence-Transformers)
         ↓
 FAISS Semantic Search
      (Top-3 docs)
         ↓
  Out-of-Domain Check
  (Score threshold 0.25)
         ↓
  Prompt Engineering
  (Context + instruction)
         ↓
 LLM Generation
  (Qwen2.5-0.5B)
         ↓
  Post-processing
  (Extract answer)
         ↓
 Source Citation
  (Article references)
         ↓
  Interactive Response
```

#### Key Components

| Component | Technology | Details |
|-----------|-----------|---------|
| **Embeddings** | Sentence-Transformers | paraphrase-multilingual-MiniLM-L12-v2 (384-dim) |
| **Indexing** | FAISS | IndexFlatIP with L2 normalization |
| **Retrieval** | Semantic search | Top-k cosine similarity |
| **OOD Detection** | Threshold-based | Score < 0.25 → reject |
| **LLM** | Qwen2.5 | 0.5B-Instruct (Arabic-capable) |
| **Interface** | Gradio | Web UI with examples |

#### Performance Metrics

- ⚡ Retrieval: ~50ms
- 🧠 Generation: ~150ms
- 🚀 Total: ~200ms per question
- 📈 OOD Detection F1: ~0.94

#### Output Report

📊 **[RAPPORT_RAG_SYSTEM_WEEK_3.md](RAPPORT_RAG_SYSTEM_WEEK_3.md)**
- Complete architecture diagram
- 6-stage pipeline breakdown
- Component specifications
- Performance analysis
- Test results (5 queries)
- Interface documentation

---

### Week 4: Comparison of 7 RAG Architectures

**Objective**: Implement, evaluate, and compare 7 different RAG architectures using standardized metrics.

**Notebook**: `Week_4/devoir4_rag_droit_marocain.ipynb`

#### 7 Architectures Implemented

| # | Architecture | Description | Strengths | Latency |
|---|--------------|-------------|-----------|---------|
| **1** | **LLM (Baseline)** | No retrieval, knowledge-based rules | Fast, baseline | 0.1s |
| **2** | **RAG Classique** | Dense retrieval only | Simple, clear | 0.5s |
| **3** | **RAG + Re-ranking** | Dense + lexical re-scoring | Better recall | 0.7s |
| **4** | **RAG Hybride** | Dense + BM25 + RRF fusion | **Best balance** | 0.8s |
| **5** | **Multi-hop RAG** | Iterative retrieval + reformulation | Complex queries | 1.5s |
| **6** | **Graph RAG** | Knowledge graph exploration | Relations captured | 0.9s |
| **7** | **🏆 Agentic RAG** | **Best overall** | Adaptive, robust | 1.2s |

#### Evaluation Metrics (8 total)

```
┌──────────────────────────────────────────────┐
│         METRIC COMPARISON (Test on 5 Q&A)    │
├──────────────────────────────────────────────┤
│ Architecture    │ P@3  │ R@3  │ F1   │ Faith│
├─────────────────┼──────┼──────┼──────┼──────┤
│ Agentic RAG     │ 0.87 │ 0.78 │ 0.82 │ 0.92 │
│ RAG Hybride     │ 0.85 │ 0.76 │ 0.80 │ 0.90 │
│ Graph RAG       │ 0.82 │ 0.74 │ 0.78 │ 0.88 │
│ Multi-hop RAG   │ 0.80 │ 0.72 │ 0.76 │ 0.85 │
│ RAG + Re-rank   │ 0.78 │ 0.70 │ 0.74 │ 0.83 │
│ RAG Classique   │ 0.72 │ 0.65 │ 0.68 │ 0.78 │
│ LLM (Baseline)  │ 0.45 │ 0.38 │ 0.41 │ 0.52 │
└──────────────────────────────────────────────┘

Legend:
  P@3 = Precision@3 (% top-3 relevant)
  R@3 = Recall@3 (% relevant docs found)
  F1  = F1-score (harmonic mean P, R)
  Faith = Faithfulness (% answer in context)
```

#### Corpus: 73 Moroccan Legal Articles

| Domain | Count | Type |
|--------|-------|------|
| 🚗 Code de la Route | 19 | Traffic violations |
| ⚖️ Droit Pénal | 15 | Criminal law |
| 👨‍👩‍👧 Moudawwana | 18 | Family law |
| 📋 Obligations & Contrats | 12 | Contract law |
| 🏛️ Système Judiciaire | 15 | Court procedures |
| 🤝 Droit Commercial | 8 | Commercial law |
| **TOTAL** | **73** | **Multiple domains** |

#### Generated Visualizations

- 📊 t-SNE embeddings (73 documents in 2D space)
- 🔥 Heatmap metrics (7 architectures × 8 metrics)
- 📈 Bar chart comparisons (P@3, R@3, MRR, NDCG, F1)
- 📍 Latency vs Performance scatter plot
- 🕸️ Knowledge graph (79 nodes, 235 edges)

#### Output Report

📊 **[RAPPORT_RAG_ARCHITECTURES_WEEK_4.md](RAPPORT_RAG_ARCHITECTURES_WEEK_4.md)**
- 7 architectures detailed
- Evaluation methodology
- Performance comparison tables
- Critical analysis
- Recommendations (short/medium/long term)
- Deployment roadmap

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8+
python3 --version

# Install dependencies
pip install -r requirements.txt
```

### Required Libraries

```
# NLP & Text Processing
pandas>=2.0
numpy>=1.24
nltk>=3.8
pyarabic>=0.6.15
sentence-transformers>=2.2.0

# ML & Embeddings
scikit-learn>=1.3.0
torch>=2.0.0
transformers>=4.30.0

# Retrieval & Search
faiss-cpu>=1.7.4  # or faiss-gpu for GPU support
rank-bm25>=0.2.2

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
networkx>=3.1
plotly>=5.14.0

# Graph & Parsing
networkx>=3.1

# Interface
gradio>=3.40.0

# Development
jupyter>=1.0.0
ipython>=8.12.0

# PDF Processing (Week 2 only)
pymupdf>=1.23.0
pdf2image>=1.16.3
pytesseract>=0.3.10  # Requires Tesseract OCR installed

# Evaluation
rouge-score>=0.1.2
bert-score>=0.3.13
```

### Installation

```bash
# Clone repository
git clone https://github.com/mahmoud-ath/NLP-DEVOIRS-EL-GHARIB-MAHMOUD-master.git
cd NLP-DEVOIRS-EL-GHARIB-MAHMOUD-master

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python3 -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
```

### Running Notebooks

```bash
# Start Jupyter
jupyter notebook

# Open desired week:
# - Week_1/nlp_pipeline_week_1.ipynb
# - Week_2/devoir2.ipynb
# - Week_3/devoir3_rag_droit_marocain.ipynb
# - Week_4/devoir4_rag_droit_marocain.ipynb
```

### Running Gradio Interfaces

**Week 3 RAG System**:
```bash
cd Week_3
jupyter notebook devoir3_rag_droit_marocain.ipynb
# Run last cell → Gradio interface launches on http://localhost:7860
```

**Week 4 RAG Comparison**:
```bash
cd Week_4
jupyter notebook devoir4_rag_droit_marocain.ipynb
# Run Gradio cell → Compare 7 architectures on http://localhost:7860
```

---

## 📊 Report Summaries

### Week 1: NLP Pipeline
**Duration**: 5 stages of text processing  
**Key Output**: 5-stage architecture diagram  
**Report**: [RAPPORT_NLP_PIPELINE_WEEK_1.md](RAPPORT_NLP_PIPELINE_WEEK_1.md)

```
Preprocessing → Syntactic Analysis → Semantic Analysis → 
Vectorization → Clustering
```

---

### Week 2: PDF Extraction
**Duration**: Extract 142 infractions from PDF  
**Key Output**: CSV with 14 columns + JSON + embeddings  
**Report**: [RAPPORT_EXTRACTION_WEEK_2.md](RAPPORT_EXTRACTION_WEEK_2.md)

```
PDF Extraction → Normalization → Hierarchical Parsing → 
NER → ML Processing → Export
```

---

### Week 3: RAG System
**Duration**: Single RAG implementation  
**Key Output**: 11-step pipeline + Gradio UI  
**Report**: [RAPPORT_RAG_SYSTEM_WEEK_3.md](RAPPORT_RAG_SYSTEM_WEEK_3.md)

```
Query → Embedding → FAISS Search → OOD Check → 
Prompt Engineering → LLM → Post-processing → Sources
```

---

### Week 4: 7 RAG Architectures
**Duration**: Compare 7 implementations  
**Key Output**: Performance tables + visualizations  
**Report**: [RAPPORT_RAG_ARCHITECTURES_WEEK_4.md](RAPPORT_RAG_ARCHITECTURES_WEEK_4.md)

```
Baseline vs Classical vs Re-ranking vs Hybrid vs 
Multi-hop vs Graph vs Agentic
```

---

## 🏆 Key Results

### Week 1-2: Data Processing
- ✅ 142 traffic infractions extracted
- ✅ 73 legal articles structured
- ✅ Arabic preprocessing pipeline

### Week 3: Single RAG
- ✅ 200ms response time
- ✅ 94% OOD detection F1
- ✅ Multilingue support (Arabic/French)

### Week 4: Architecture Comparison
- ✅ Agentic RAG: 0.82 F1-score
- ✅ RAG Hybrid: 0.80 F1 + best latency trade-off
- ✅ 8 metrics evaluated on 5 test queries

---

## 🔍 Corpus Information

### Moroccan Legal Domains

| Domain | Articles | Focus |
|--------|----------|-------|
| **Traffic Code (52-05)** | 19 | Speed limits, alcohol, equipment |
| **Criminal Law** | 15 | Theft, violence, fraud |
| **Family Law (Moudawwana 70-03)** | 18 | Marriage, divorce, inheritance |
| **Contract Law** | 12 | Formation, liability, damages |
| **Judicial System (96-51)** | 15 | Courts, procedures, appeals |
| **Commercial Law** | 8 | Merchants, commercial acts |

### Data Format (CSV)

```csv
id,type_loi,numero_loi,texte_legal,texte_fr,explication,exemple,amende,points,peine_min_ans,peine_max_ans,prison_mois,suspension_mois
CR_001,قانون السير,52-05,يُحدد الحد الأقصى للسرعة...,La vitesse maximale...,تجاوز السرعة يُعرّض...,سائق بلغت سرعته 69...,300,2,,,,
```

---

## 📈 Performance Comparison

### Latency Analysis

```
Execution Time Breakdown:
  LLM (Baseline):     0.1s  (instant)
  RAG Classique:      0.5s  (dense search)
  RAG + Re-rank:      0.7s  (+ rerank)
  RAG Hybride:        0.8s  (+ BM25)
  Graph RAG:          0.9s  (+ exploration)
  Agentic RAG:        1.2s  (+ classify + loop)
  Multi-hop RAG:      1.5s  (x2 retrieve)
```

### Quality Metrics

```
F1-Score Ranking:
  1. Agentic RAG:     0.82 🏆
  2. RAG Hybride:     0.80
  3. Graph RAG:       0.78
  4. Multi-hop RAG:   0.76
  5. RAG + Re-rank:   0.74
  6. RAG Classique:   0.68
  7. LLM (Baseline):  0.41
```

---

## 💡 Key Technologies

### NLP & Embeddings
- **PyArabic**: Arabic text normalization
- **NLTK**: Tokenization, POS tagging
- **Sentence-Transformers**: Multilingual embeddings (384-dim)

### Retrieval & Search
- **FAISS**: Vector indexing (IndexFlatIP with L2 norm)
- **BM25Okapi**: Sparse lexical retrieval
- **NetworkX**: Knowledge graph construction

### LLM & Generation
- **Qwen2.5-0.5B-Instruct**: Arabic-capable lightweight LLM
- **Transformers**: Model loading and inference
- **Gradio**: Interactive web interface

### Evaluation
- **scikit-learn**: Precision, Recall, F1 metrics
- **ROUGE-score**: Lexical overlap
- **Custom metrics**: Faithfulness, OOD detection

---

## 📝 Usage Examples

### Example 1: Run Week 1 Pipeline

```python
# Load and process Arabic text
from Week_1.nlp_pipeline import preprocess, extract_ner, vectorize

text = "يُحدد الحد الأقصى للسرعة داخل المدينة بـ60 كيلومتر"

# Process through pipeline
tokens = preprocess(text)
entities = extract_ner(tokens)
vectors = vectorize(text)
```

### Example 2: Query Week 3 RAG

```python
# Question in Arabic
query = "ما هي عقوبة تجاوز السرعة في الطريق السيار؟"

# RAG pipeline
retrieved_docs = retrieve(query, k=3)
answer = generate_response(query, retrieved_docs)

# Output: Answer with source articles
print(answer)
# "وفقاً للمادة 2، الحد الأقصى للسرعة... Art.2 (score: 0.88)"
```

### Example 3: Compare Week 4 Architectures

```python
# Test different RAG architectures
architectures = {
    'classic': rag_classic,
    'hybrid': rag_hybrid,
    'agentic': agentic_rag,
}

for name, func in architectures.items():
    response = func(query)
    score = evaluate(response)
    print(f"{name}: F1={score['f1']:.2f}, Latency={score['latency']:.2f}s")
```

---

## 🐛 Troubleshooting

### Issue: FAISS Installation Failed
```bash
# Try CPU version
pip install faiss-cpu

# Or GPU version (CUDA 11.x)
pip install faiss-gpu
```

### Issue: Tesseract Not Found (Week 2)
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract

# Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
```

### Issue: Arabic Text Display Issues
```bash
# Ensure UTF-8 encoding
# Add to notebook top:
%env LC_ALL=C.UTF-8
%env LANG=C.UTF-8
```

### Issue: Out of Memory (Embedding Generation)
```python
# Process in batches
embeddings = model.encode(texts, batch_size=32, show_progress_bar=True)
```

---

## 📚 Academic References

- **Moroccan Legal System**: 
  - Loi 52-05 (Code de la Route)
  - Loi 70-03 (Moudawwana - Family Law)
  - Loi 51-96 (Judicial Organization)

- **NLP Techniques**:
  - Preprocessing: PyArabic library documentation
  - Embeddings: Sentence-Transformers (2022)
  - RAG: Lewis et al. (2020) "Retrieval-Augmented Generation"

- **Evaluation Metrics**:
  - NDCG: Järvelin & Kekäläinen (2002)
  - MRR: Mean Reciprocal Rank (IR evaluation)
  - ROUGE: Lin (2004) for automatic summarization evaluation

---

## 📄 License

This project is for **academic purposes** as part of NLP coursework.

**Disclaimer**: Legal information provided is for educational purposes only. Not intended as legal advice. Consult qualified legal professionals for real legal matters.

---

## ✍️ Author Notes

### Progression Overview

```
Week 1: Foundation (Basic NLP)
  ↓
Week 2: Data Extraction (Structured Processing)
  ↓
Week 3: Single RAG (Complete Pipeline)
  ↓
Week 4: Comparison (Architecture Evaluation)
```

### Lessons Learned

1. **Arabic NLP Complexity**: Requires careful normalization (diacritics, hamza, ta forms)
2. **Embeddings Quality**: Multilingual models trade-off with domain-specific performance
3. **RAG Benefits**: Retrieval+Generation combo outperforms LLM alone by 2x (F1: 0.82 vs 0.41)
4. **Hybrid Approach**: Dense + sparse complementary (different strengths)
5. **Evaluation Critical**: Metrics show trade-offs (latency vs quality)

### Future Improvements

- ✅ Fine-tune embeddings on Moroccan legal domain
- ✅ Implement multi-turn conversational RAG
- ✅ Add automatic relation extraction for graph RAG
- ✅ Deploy as production API with monitoring
- ✅ Integrate jurisprudence and precedent cases

---

## 🔗 Resources

- **Notebooks**: See `/Week_*/*.ipynb`
- **Reports**: See `/RAPPORT_*.md`
- **Data**: See `/Week_*/Data/`
- **Visualizations**: See `/Week_4/Generated/`

---

## 📞 Contact & Support

**Author**: EL-GHARIB MAHMOUD  
**Course**: Natural Language Processing — 2026  

**Questions?** See detailed reports for each week.

---

**Last Updated**: 13 May 2026  
**Status**: ✅ Complete (All 4 weeks finished)  
**Files**: 4 notebooks + 4 reports + corpus data + visualizations

