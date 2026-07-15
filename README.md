# VC Comment Processing

Turns raw visual-complexity (VC) user comments into curated **phrases**, **sub-topics**,
and a final **keyword/stem dictionary**, combining LLM extraction, algorithmic
reduction, and human curation.

## Key numbers

| Quantity | Value |
|----------|-------|
| Comparison pairs (comments) | 699 (686 kept after `ToRemove`) |
| Unique images | 520 |
| VC topics / VisTypes | 7 / 9 |
| Curated phrases | 404 |
| Keywords entering reduction | 399 |
| Sub-topics after reduction | 19 (3/3/3/3/3/2/2 per topic) |
| Dictionary stems | 689 (668 user-comment + 21 literature) |

The 7 topics: Data Density / Image Clutter (DDIC), Visual Encoding Clarity (VEC),
Semantics / Text Legibility (STL), Schema (SCH), Color, Symbol, and Texture Details (CSTD),
Aesthetics Uncertainty (AU), Immediacy / Cognitive Load (ICL).

## Reading the data — two ways

The paired-comparison study table (and every other tab) can be read either from the
**master Google Sheet** or a **local copy** under `data_table/`:

```python
from data_loader import load_paired_comparison, load_sheet

df = load_paired_comparison(source="master")   # live Google Sheet
df = load_paired_comparison(source="local")    # local data_table/paired_comparison.csv

# any tab, by (spreadsheet_id, gid):
df = load_sheet(config.MASTER_SHEET_ID, "517808299", source="local")
```

The default source is `config.DATA_SOURCE` (set to `"master"`, or export
`VC_DATA_SOURCE=local`). Sheet IDs, the topic/VisType vocabulary, and folder
locations live in `config.py`.

## Pipeline

Run the notebooks in order; each writes its intermediate outputs to `data_processing/`.

| # | Notebook | Step | Main outputs |
|---|----------|------|--------------|
| 1 | `1_llm_extraction.ipynb` | LLM (GPT-5-mini) topic classification, phrase extraction, per-image split with `(+)/(-)` sentiment, keyword extraction, and image-level aggregation | `keyword_counts_by_vistype.csv`, `image_all_keywords_expanded.csv` |
| 2 | `2_phrase_curation.ipynb` | Regenerate the per-topic phrase mapping from all curated phrases; reconcile AI/Human curation | `term_mapping_regenerated.csv`, `phrase_pivot_regenerated.csv` |
| 3 | `3_phrase_reduction.ipynb` | Reduce 399 phrases → 19 named sub-topics (manual synonym groups + per-topic TF-IDF, universality scoring) | `phrase_shortlist.csv`, `subtopic_taxonomy.csv`, `phrase_reduction_tracking.csv` |
| 4 | `4_image_compilation.ipynb` | Compile the per-image master table (phrases, sentiments, stems, sub-topics) and build the stem dictionary | `image_compiled_phrases.csv`, `stem_dictionary.csv` |
| 5 | `5_keyword_extraction.ipynb` | Lemmatize curated phrases into words with POS (Original → AIcurated → HumanCurated) | `image_phrase_matching.csv`, `unique_words*.csv` |
| 6 | `6_keyword_stems.ipynb` | Stem-based extraction (SnowballStemmer) across Original → HumanCurated → FinalPhrase | `unique_stems*.csv` |

```
Stage 0  paired-comparison study (699 pairs)
   │
Stage 1  LLM topic/phrase/keyword extraction + sentiment split   → notebook 1
   │
Stage 2  human curation reconciled into phrase mapping           → notebook 2
   │
Stage 3  reduce 399 phrases → 19 sub-topics                      → notebook 3
   │
Stage 4  compile per-image master table + stem dictionary        → notebook 4
   │
Stage 5  keyword / stem dictionary (689 stems)                   → notebooks 5–6
```

## Layout

```
config.py            shared config: sheet IDs, topics, VisTypes, paths, data source
data_loader.py       load_sheet() / load_paired_comparison() — master or local
requirements.txt
data_table/          local CSV copies of key sheet tabs (offline read mode)
data_processing/     notebook outputs (git-ignored)
notebooks/           1..6 pipeline notebooks
```

## Setup

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Notebook 1 calls the OpenAI API — set `OPENAI_API_KEY` in your environment before running it.

## Notes

- Phrase reduction (notebook 3) uses **manual synonym groups + per-topic TF-IDF**, not a
  live LLM merge; the named sub-topics are the expert-curated result.
- Some tables (e.g., the AI/Human curation columns) originate from human curation in the
  master workbook; notebooks read them back from the sheet (or local copies).
- `data_processing/term_mapping.csv` (a phrase→sentiment lookup used by notebook 4) is an
  external input produced during phrase analysis; supply it or adapt the sentiment source.
