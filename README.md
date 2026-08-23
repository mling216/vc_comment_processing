# VC Comment Processing

Turns raw visual-complexity (VC) user comments into curated phrases, sub-topics,
and a final keyword/stem dictionary. The workflow combines LLM extraction,
spreadsheet-based human curation, algorithmic phrase reduction, and per-image
compilation.

## Workbook, tab, and GID convention

Each Google Sheets workbook has a **spreadsheet ID**. Each tab inside that
workbook has a **gid** (the numeric tab identifier). A gid is only meaningful
together with its spreadsheet ID; the same number in another workbook is a
different tab. In the notebooks, variables named `sheet_id` or
`sheet_*_id` contain a gid, not a workbook ID.

For clarity, this README writes `gid` before every tab number. The equivalent
loader call is:

```python
df = load_sheet(spreadsheet_id, gid)
```

The repository currently uses these workbook contexts:

| Workbook context | Spreadsheet ID | Tabs used |
| --- | --- | --- |
| Source and legacy keyword workbook | `1gfeYdT-RxLq9tvNpfv_P8AIKg2eSz6-8bSv5zUJsWEc` | `gid 1103808983` source pairs; `gid 1166121277` phrase/keyword mapping; `gid 1841871821` prior keyword table; `gid 1390591889` image topics; `gid 1160817631` keyword counts |
| Current reduction workbook | `1cVCOfBjHmcvsyrn7U0CbXoBSksF4JDRqWYm-ZJPbL4k` | `gid 517808299` curated phrases; `gid 1455332435` term mapping; `gid 1540814304` image pairs; `gid 483858074` canonical image list |
| Image order workbook | `1gfeYdT-RxLq9tvNpfv_P8AIKg2eSz6-8bSv5zUJsWEc` | `gid 1429789806` canonical order used by notebook 4 |
| VC score workbook | `1N6nK03QiPAM6AELb9kC3beETnKmG6u23` | `gid 67202923` normalized VC values |

The first two contexts are not interchangeable just because a tab number looks
similar. When adding a new reference, record both the spreadsheet ID and the
gid, and prefer the variable name `gid` in new code.

## Pipeline at a glance

Run the core path in order, pausing for the spreadsheet curation checkpoints.
After phrase reduction, choose the downstream branch or run both. Notebooks
write CSV outputs under `data_processing/`; they do not automatically upload
those files back to Google Sheets.

```text
CORE PATH

0. Source study data
   Read:  0.postquestionare_all (gid `1103808983`)
   Local: data_table/paired_comparison.csv
      |
      v
1. LLM extraction: notebook 1
   Write local extraction files, then paste the generated extraction columns
   back into 0.postquestionare_all, preserving the `index` row key.
      |
      v
2. HUMAN CURATION CHECKPOINT
   Edit in 0.postquestionare_all (gid `1103808983`):
     CuratePhrasesMoreComplex
     CuratePhrasesLessComplex
   Review topic assignments, phrase wording, and (+)/(-) sentiment.
      |
      v
3. Phrase mapping: notebook 2
   Read:  0.postquestionare_all (gid `1103808983`)
      1.phraseCuration (gid `1166121277`) for existing mappings
   Write: data_processing/term_mapping_regenerated.csv
      data_processing/phrase_pivot_regenerated.csv
   Review and refresh 1.phraseCuration, especially `AIcurated` and
   `HumanCuration`, then refresh 2.curatedPhrases (gid `517808299`).
      |
      v
4. Phrase reduction: notebook 3
   Read:  2.curatedPhrases (gid `517808299`), plus reduction-workbook tabs
      when running the per-image section.
   Review the manual synonym groups, shortlist, and sub-topic taxonomy.
   Write: phrase_shortlist.csv, subtopic_taxonomy.csv,
      phrase_reduction_tracking.csv, image_phrase_word_mapping.csv

DOWNSTREAM BRANCH A: IMAGE COMPILATION

5A. notebook 4
    Requires the notebook 3 outputs plus external
    data_processing/image_compiled_phrases.csv,
    data_processing/term_mapping.csv, and (for some cells) a prior
    data_processing/stem_dictionary.csv. See "External artifacts" below.
    Write: image_compiled_phrases.csv, stem_dictionary.csv, and reports.

DOWNSTREAM BRANCH B: WORD AND STEM TABLES

5B. notebook 5
    Requires data_processing/term_mapping.csv. Its later cells also read
    source tabs `gid 1103808983` and `gid 1166121277` to build image matching.
    Write: unique_words.csv, image_phrase_matching.csv, unique_words_by_*.csv
      |
      v
6B. notebook 6
    Read:  image_phrase_matching.csv and, for the lineage section,
       phrase_lineage_all_vistypes.csv.
    Write: unique_stems*.csv.

OPTIONAL WORKBOOK HANDOFF

Refresh 6.imageTypeTopics (gid `1390591889`) from compiled per-image results,
then refresh A.keyword.CountByVisTypes (gid `1160817631`) when needed.
```

## Human curation checkpoints

Human curation happens after the first notebook has produced or refreshed the AI
extraction fields and before phrase reduction:

1. In `0.postquestionare_all` (`1103808983`), review the extracted phrases for
   each more-complex and less-complex image. Store the reviewed topic-to-phrase
   JSON in `CuratePhrasesMoreComplex` and `CuratePhrasesLessComplex`.
2. Run `2_phrase_curation.ipynb`. It collects all reviewed phrases from the
   source tab and preserves existing mappings from `1.phraseCuration`.
3. Review the generated `HumanCuration` labels in `1.phraseCuration`
   (gid `1166121277`). This is the mapping from each original phrase to the final
   human-curated phrase used downstream.
4. Refresh `2.curatedPhrases` (gid `517808299`) with the curated phrase table before
   running `3_phrase_reduction.ipynb`.
5. During notebook 3, review manual synonym groups, the phrase shortlist, and
   the sub-topic taxonomy. Do not treat the TF-IDF suggestions as a substitute
   for expert review.

### What to extract and where to put it

| Stage | Extract/read from | Manually write or paste back | Local artifact |
| --- | --- | --- | --- |
| Raw study data | `0.postquestionare_all`, gid `1103808983` | None before notebook 1 | `data_table/paired_comparison.csv` |
| AI phrase extraction | Source rows and comment columns in `0.postquestionare_all` | AI extraction columns in the same source tab, aligned by `index` | `data_processing/extracted_*.csv`, `CuratedPhrasesCombined.csv` |
| Human phrase review | `CuratePhrasesMoreComplex` and `CuratePhrasesLessComplex` in `0.postquestionare_all` | Reviewed JSON phrase assignments in those same columns | `data_processing/term_mapping_regenerated.csv` |
| Phrase mapping review | `1.phraseCuration`, gid `1166121277` | `AIcurated` and `HumanCuration` values | `data_table/phrase_curation.csv` for the shipped local copy |
| Reduction input | `2.curatedPhrases`, gid `517808299` | Refresh the curated phrase/count table | `data_table/curated_phrases.csv` for the shipped local copy |
| Per-image workbook refresh | Compiled outputs from notebooks 3-4 | Optional refresh of `6.imageTypeTopics`, gid `1390591889` | `image_compiled_phrases.csv` and summaries |

## External artifacts

The repository intentionally does not include every historical intermediate CSV.
Before running the downstream branches, confirm that these files exist under
`data_processing/`:

| File | Consumed by | Required columns or role |
| --- | --- | --- |
| `term_mapping.csv` | notebooks 4 and 5 | Phrase mapping with `Original`, `AIcurated`, `HumanCurated`; notebook 4 also uses `OriginalSign` for sentiment lookup |
| `image_compiled_phrases.csv` | notebook 4 | Existing per-image phrase table used as the compilation source |
| `stem_dictionary.csv` | notebook 4 setup and later dictionary cells | Existing or previously generated original-stem dictionary |
| `phrase_lineage_all_vistypes.csv` | notebook 6 lineage section | Mapping from `original_phrase` to `final_subtopic_phrase` |

Notebook 2 creates `term_mapping_regenerated.csv`, a wide per-topic table. It
does not create the long-format `term_mapping.csv` expected by notebooks 4 and
5. Adapt or export the regenerated table into that schema before using those
notebooks. Likewise, `phrase_lineage_all_vistypes.csv` is not produced by the
current notebook 3 cells and must be supplied if the notebook 6 lineage report
is needed.

When using local mode, update the corresponding CSV under `data_table/` after
making a spreadsheet change. `data_processing/` is ignored by Git because its
contents are regenerated by the notebooks.

## Key numbers

| Quantity | Value |
| --- | --- |
| Comparison pairs (comments) | 699 (686 kept after `ToRemove`) |
| Unique images | 520 |
| VC topics / VisTypes | 7 / 9 |
| Curated phrases | 404 |
| Keywords entering reduction | 399 |
| Sub-topics after reduction | 19 (3/3/3/3/3/2/2 per topic) |
| Dictionary stems | 689 (668 user-comment + 21 literature) |

The 7 topics are Data Density / Image Clutter (DDIC), Visual Encoding Clarity
(VEC), Semantics / Text Legibility (STL), Schema (SCH), Color, Symbol, and
Texture Details (CSTD), Aesthetics Uncertainty (AU), and Immediacy / Cognitive
Load (ICL).

## Reading the data: two ways

The paired-comparison study table and other supported tabs can be read from the
master Google Sheet or from local CSV copies:

```python
import config
from data_loader import load_paired_comparison, load_sheet

# Live Google Sheet
pairs = load_paired_comparison(source="master")

# Local copy under data_table/
pairs = load_paired_comparison(source="local")

# Any tab by spreadsheet ID and gid. Only the three tabs listed in
# config.LOCAL_SHEET_MAP are available locally; other gids fall back online.
df = load_sheet(config.MASTER_SHEET_ID, "517808299", source="local")
```

The default source is `config.DATA_SOURCE` (`"master"`). Set
`VC_DATA_SOURCE=local` to use the shipped CSV snapshots where available; an
unmapped or missing local tab prints a message and falls back to the live
Google Sheet. Sheet IDs, tab mappings, topic names, VisTypes, and folder
locations are defined in `config.py`.

## Notebook summary

| # | Notebook | Purpose | Main outputs |
| --- | --- | --- | --- |
| 1 | `1_llm_extraction.ipynb` | Classify topics, extract phrases/effects, split sentiment, and aggregate keywords by image | `keyword_counts_by_vistype.csv`, `image_all_keywords_expanded.csv` |
| 2 | `2_phrase_curation.ipynb` | Rebuild the phrase mapping from all reviewed source-tab phrases | `term_mapping_regenerated.csv`, `phrase_pivot_regenerated.csv` |
| 3 | `3_phrase_reduction.ipynb` | Reduce the reviewed vocabulary into named sub-topics | `phrase_shortlist.csv`, `subtopic_taxonomy.csv`, `phrase_reduction_tracking.csv` |
| 4 | `4_image_compilation.ipynb` | Downstream branch A: compile per-image phrases, sentiments, stems, sub-topics, and reporting tables | `image_compiled_phrases.csv`, `stem_dictionary.csv` |
| 5 | `5_keyword_extraction.ipynb` | Downstream branch B: create lemmatized word tables and image phrase matching | `unique_words*.csv`, `image_phrase_matching.csv` |
| 6 | `6_keyword_stems.ipynb` | Continue branch B with Snowball stem tables; the final-phrase lineage section needs an additional lineage CSV | `unique_stems*.csv` |

## Layout

```text
config.py            shared config: sheet IDs, topics, VisTypes, paths, data source
data_loader.py       load_sheet() / load_paired_comparison()
requirements.txt
data_table/          local CSV copies of key Google Sheet tabs
data_processing/     notebook outputs (Git-ignored)
notebooks/           1..6 pipeline notebooks
```

## Setup

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Run notebooks from the repository root, or use the portable setup cell included
in each notebook. Notebook 1 calls the OpenAI API; set `OPENAI_API_KEY` in your
environment before running the LLM cells. The spaCy model is required by
notebooks 4-6. Internet access is required for live Google Sheet reads and
OpenAI calls.

## Notes

- Notebook 3 uses manual synonym groups plus per-topic TF-IDF and universality
  scoring. The final named sub-topics require expert review.
- Keep the `index` column as the row key when copying notebook results back into
  the source study tab.
- Notebook 1 contains legacy keyword-curation and image-analysis sections; use
   the execution guide in the notebook to select the relevant branch.
- Notebook 4 contains optional pivots, sentiment reports, top-k reports, and
   literature-factor analysis after its core compilation cells.
- The local CSV files are snapshots, not automatic two-way synchronizations with
  Google Sheets.
