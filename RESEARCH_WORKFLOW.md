# From Participant Comments to a Visual-Complexity Vocabulary

## Background and purpose

When people compare visualization images, their explanations reveal what makes an image seem more or less complex: crowded marks, unclear encodings, unfamiliar forms, or the effort needed to interpret it. Organizing these explanations makes it possible to study perceived visual complexity (VC) while retaining the participants' own words.

This document describes that process: **AI-assisted extraction, expert curation, and image-level mapping**. AI proposes passages and assignments to seven predefined topics; researchers review the evidence, standardize equivalent expressions, and construct sub-topics. It is a guide to the research method, not a coding tutorial or an independent validation study.

The implementation and analysis materials are maintained in the [VC Comment Processing repository](https://github.com/mling216/vc_comment_processing) [1]. Reported counts follow its workflow documentation [2]. The main text can be read independently; the supplement supplies spreadsheet references and reproduction details.

## 1. Study materials and key numbers

Participants compared pairs of visualization images and explained why one appeared more or less visually complex.

| Study or processing quantity | Reported number |
| --- | --- |
| Nonempty comparison-pair records | 698 |
| Comparison-pair records retained after the exclusion flag was applied | 685 |
| Unique visualization images | 520 |
| Broad visual-complexity topics | 7 |
| Visualization types | 9 |
| Curated phrases | 404 |
| Keywords entering phrase reduction | 399 |
| Sub-topics after reduction | 19 |
| Dictionary stems | 689: 668 from participant comments and 21 from the literature |

These are reported workflow totals [2], not newly computed results. Comparison records are not participant counts. The 404 curated phrases and 399 reduction-input keywords describe different stages. The combined dictionary total includes literature contributions and is not a guaranteed output size on rerun.

### The seven topics

| Topic | What it captures, in plain language | Final sub-topics |
| --- | --- | --- |
| Data Density / Image Clutter (DDIC) | How much information is shown, how many elements appear, and whether they overlap or crowd one another | 3 |
| Visual Encoding Clarity (VEC) | How clearly graphical forms, positions, and other visual marks communicate the data | 3 |
| Semantics / Text Legibility (STL) | Whether labels, legends, text, and contextual information can be read and understood | 3 |
| Schema (SCH) | Familiarity with the domain or visual representation, including its structure and level of abstraction | 3 |
| Color, Symbol, and Texture Details (CSTD) | Color variety and contrast, graphical symbols, and texture | 2 |
| Aesthetics Uncertainty (AU) | Perceived disorganization or ambiguity in the image's appearance | 2 |
| Immediacy / Cognitive Load (ICL) | The difficulty, time, and mental effort involved in understanding the visualization | 3 |
| **Total** | | **19** |

## 2. Pipeline overview

![Pipeline from comparison comments through AI extraction and human review to sub-topics, image compilation, and word/stem tables](docs/vc_comment_pipeline.svg)

**Figure 1.** The core sequence includes three human-review checkpoints: contextual phrase review, vocabulary review, and consolidation/taxonomy review. After reduction, collaborators can choose image compilation, word/stem tables, or both. Arrows represent research handoffs, not automatic spreadsheet synchronization; downstream analysis also requires separately supplied inputs.

## 3. Research steps and spreadsheet checkpoints

Two primary spreadsheets organize the work: **PostquestionareAnalysisGPT5** holds source comments and earlier mappings; **ResultsStepByStep** holds reduction and per-image inputs. Both contain a **0.postquestionare_all** tab, so identify the spreadsheet as well as the tab. Auxiliary image-metadata and VC-score spreadsheets are listed in Supplement A.

### 1. Prepare the comment records

Use PostquestionareAnalysisGPT5 → **0.postquestionare_all**. Each record connects an image pair to the participant's explanation. Apply the study's exclusion flag, retaining **685 of 698** nonempty records. Preserve original comments, image identifiers, and the **index** record key when copying results back.

### 2. Extract topics and phrases with AI assistance

Assign comments to the seven predefined topics and extract **exact participant wording**. A passage may support multiple topics. Keep its image attribution and complexity direction: **(+) increased complexity; (-) decreased complexity**. These signs are not emotional sentiment and must be interpreted from the comment, not merely the image's comparison label. Return extraction fields to the source tab, matched by **index**.

### 3. Review phrases in context

In the same source tab, researchers check evidence, topic, image attribution, direction, and coverage against the original comment. Record approved assignments in **CuratePhrasesMoreComplex** and **CuratePhrasesLessComplex**. Complete this review before standardizing the vocabulary.

### 4. Review the standardized vocabulary

Review original-to-curated mappings in PostquestionareAnalysisGPT5 → **1.keyword.S&Y(AI+humanCuration)**, preserving the original wording as evidence. Refresh ResultsStepByStep → **2.curatedPhrases** with the approved phrase/count table. Its separate **1.phraseCuration** tab must also contain the intended mapping for per-image analysis. These are deliberate exports or copy-back steps, not automatic updates.

### 5. Consolidate phrases into 19 sub-topics

Starting from ResultsStepByStep → **2.curatedPhrases**, combine expert synonym groups, text-similarity suggestions, and semantic review. Rare expressions are initially merged rather than simply discarded; terms are not excluded merely for being specific to one visualization type.

The prioritization score is **phrase count × number of visualization types**. It summarizes frequency and breadth, not conceptual validity. Researchers inspect weak or forced merges, approve **19 sub-topics across seven topics**, and review the tracking table, including unmapped expressions [3]. Supplement B lists the sub-topics.

### 6. Link concepts to images and produce outputs

Per-image mapping uses ResultsStepByStep → **0.postquestionare_all**, **1.phraseCuration**, and **4.0.imageDataCompiled**. Check image identifiers, reference ordering, and phrase-to-image links.

- **Branch A: image compilation.** Assemble original/curated phrases, complexity directions, stems, and sub-topics for each image, with dictionary and optional reporting outputs. This branch uses PostquestionareAnalysisGPT5 → **5.1 imagePhraseCompile** for ordering.
- **Branch B: word and stem tables.** Extract words, match phrases to images, and group related word forms. A *stem* is a simplified form used to group words; shared stems do not necessarily imply identical meaning.

The branches can run separately or together, but require the intermediate inputs described in Supplement C. Optional spreadsheet summaries refresh PostquestionareAnalysisGPT5 → **5.imageTypeTopics** and **2.keyword.CountByVisTypes**.

## 4. Interpretation and reproducibility

The results describe **participants' expressed perceptions**, not causal or independently validated measures of image complexity. Distinguish original evidence from curated interpretations, AI suggestions from researcher decisions, and frequency from general importance. Keep participant-comment and literature dictionary contributions distinguishable.

Record the spreadsheet versions or saved snapshots used and retain phrase-reduction tracking. Spreadsheet edits do not automatically update local files; analysis outputs do not automatically update spreadsheets.

---

# Supplement: References and Reproduction Details

## A. Exact spreadsheet and tab references

The main text uses spreadsheet and tab names. The identifiers below allow collaborators to find the same tables even if a tab is later renamed.

### A1. PostquestionareAnalysisGPT5

**Spreadsheet ID:** `1gfeYdT-RxLq9tvNpfv_P8AIKg2eSz6-8bSv5zUJsWEc`

[Open PostquestionareAnalysisGPT5](https://docs.google.com/spreadsheets/d/1gfeYdT-RxLq9tvNpfv_P8AIKg2eSz6-8bSv5zUJsWEc/edit)

| Current tab name | Tab identifier (gid) | Role or historical label |
| --- | --- | --- |
| 0.postquestionare_all | `1103808983` | Source comparison records and phrase-review columns |
| 1.keyword.S&Y(AI+humanCuration) | `1166121277` | Earlier mapping table; historically labeled **1.phraseCuration** |
| Expired.1.keyword.Z&AA(AI+humanCuration) | `1841871821` | Historical keyword table, not the primary mapping checkpoint |
| 5.imageTypeTopics | `1390591889` | Image-topic summaries; historically labeled **6.imageTypeTopics** |
| 2.keyword.CountByVisTypes | `1160817631` | Visualization-type keyword counts; historically labeled **A.keyword.CountByVisTypes** |
| 5.1 imagePhraseCompile | `1429789806` | Image-order reference used by the compilation branch |

The image-order reference is in this same spreadsheet, not a separate workbook.

### A2. ResultsStepByStep

**Spreadsheet ID:** `1cVCOfBjHmcvsyrn7U0CbXoBSksF4JDRqWYm-ZJPbL4k`

[Open ResultsStepByStep](https://docs.google.com/spreadsheets/d/1cVCOfBjHmcvsyrn7U0CbXoBSksF4JDRqWYm-ZJPbL4k/edit)

| Current tab name | Tab identifier (gid) | Role |
| --- | --- | --- |
| 0.postquestionare_all | `1540814304` | Image-pair and reviewed-phrase input for the per-image section |
| 1.phraseCuration | `1455332435` | Mapping from reviewed original expressions to human-curated phrases |
| 2.curatedPhrases | `517808299` | Curated phrase-and-count input for reduction |
| 4.0.imageDataCompiled | `483858074` | Canonical image list for the reduction notebook's per-image output |

**Important:** ResultsStepByStep → 1.phraseCuration and PostquestionareAnalysisGPT5 → 1.keyword.S&Y(AI+humanCuration) are different tabs in different spreadsheets. The earlier mapping stage and the later per-image stage read different workbook contexts.

### A3. Sub.Vis2025VisComplexity.PerceivedScoreAndObjectiveMetrics

**Spreadsheet ID:** `1N6nK03QiPAM6AELb9kC3beETnKmG6u23`

[Open the VC score spreadsheet](https://docs.google.com/spreadsheets/d/1N6nK03QiPAM6AELb9kC3beETnKmG6u23/edit)

| Current tab name | Tab identifier (gid) | Role |
| --- | --- | --- |
| FormalExp1800Images | `67202923` | Normalized VC values used in downstream reporting |

A tab identifier is meaningful only together with its spreadsheet ID. Names above were checked against the live spreadsheets on November 23, 2026; the research counts remain the figures reported in the repository README.

### A4. VisComplexity.PerceivedScoreAndObjectiveMetrics

**Spreadsheet ID:** `1eJ3VUh2ZKZy6S6qo9nzF8h0rwwMNBhwuK42wdgeS54w`

[Open the image-metadata spreadsheet](https://docs.google.com/spreadsheets/d/1eJ3VUh2ZKZy6S6qo9nzF8h0rwwMNBhwuK42wdgeS54w/edit)

| Current tab name | Tab identifier (gid) | Role |
| --- | --- | --- |
| FormalExp1800Images | `1073958835` | Image metadata, including visualization types used by notebook 1's image-topic section |

This is a separate workbook from the similarly named VC-score reference in A3. Together with the two primary spreadsheets, these references make four workbook contexts in the implementation.

## B. The 19 sub-topics

These labels come from the expert-defined taxonomy in the phrase-reduction notebook [3].

| Broad topic | Named sub-topics |
| --- | --- |
| Data Density / Image Clutter | Information Volume; Element Quantity; Visual Clutter & Overlap |
| Visual Encoding Clarity | Graphical Forms & Primitives; Position, Scale & Organization; Encoding Interpretability |
| Semantics / Text Legibility | Annotations & Labels; Text Volume & Content; Typography & Readability |
| Schema | Domain Familiarity; Dimensionality & Structure; Abstraction Level |
| Color, Symbol, and Texture Details | Color Palette & Contrast; Symbols & Texture |
| Aesthetics Uncertainty | Visual Disorganization; Perceptual Ambiguity |
| Immediacy / Cognitive Load | Interpretive Difficulty; Semantic Clarity; Processing Time & Effort |

The nine visualization-type labels used in the implementation [1] are **Area, Bar, Cont.-ColorPatn, Glyph, Grid, Line, Node-link, Point, and Text**.

## C. Technical implementation and outputs

This section is for the analyst running the workflow. General readers do not need to run these notebooks.

| Research stage | Implementation | Main local outputs |
| --- | --- | --- |
| Topic and phrase extraction | [1_llm_extraction.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/1_llm_extraction.ipynb) | Extraction tables, including `extracted_*.csv` and `CuratedPhrasesCombined.csv`; additional keyword and image summaries |
| Phrase-mapping reconstruction | [2_phrase_curation.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/2_phrase_curation.ipynb) | `term_mapping_regenerated.csv`; `phrase_pivot_regenerated.csv` |
| Phrase reduction and sub-topic construction | [3_phrase_reduction.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/3_phrase_reduction.ipynb) | `phrase_shortlist.csv`; `subtopic_taxonomy.csv`; `phrase_reduction_tracking.csv`; `image_phrase_word_mapping.csv` |
| Branch A: image compilation | [4_image_compilation.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/4_image_compilation.ipynb) | `image_compiled_phrases.csv`; `stem_dictionary.csv`; optional reports |
| Branch B: word extraction and image matching | [5_keyword_extraction.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/5_keyword_extraction.ipynb) | `unique_words.csv`; `image_phrase_matching.csv`; visualization-type word tables |
| Branch B continuation: stem extraction | [6_keyword_stems.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/6_keyword_stems.ipynb) | `unique_stems*.csv`; optional phrase-lineage stem tables |

Notebook 3's per-image section is required for its full image-level handoff, but can be skipped when only the shortlist and tracking outputs are needed. Notebook 1 includes legacy analysis sections, and notebook 4 includes optional reporting sections; follow their execution guides rather than assuming every cell is required.

### Inputs that need a separate handoff

The current notebooks do not form a fully self-contained, one-click pipeline. Confirm these inputs are available in the local output folder before using the relevant downstream sections:

| Input file | Needed for | Handoff requirement |
| --- | --- | --- |
| `term_mapping.csv` | Notebooks 4 and 5 | Notebook 5 reads `Original`, `AIcurated`, and `HumanCurated`; notebook 4 core reads lowercase `original` and `OriginalSign`. A shared export needs both original-phrase spellings with identical values. Optional notebook 4 sentiment reports also use `HumanCuratedSign`. |
| `image_compiled_phrases.csv` | Notebook 4 | Existing image-level phrase table used as a compilation input, even though notebook 4 also writes an updated file with this name |
| `stem_dictionary.csv` | Notebook 4 core setup and dictionary cells | Existing or previously generated stem dictionary |
| `phrase_lineage_all_vistypes.csv` | Notebook 6's optional lineage section | Links `original_phrase` to `final_subtopic_phrase`; not produced by the current notebook 3 cells |

Notebook 2's `term_mapping_regenerated.csv` is a **wide, per-topic table**. It is not the long-format `term_mapping.csv` expected by notebooks 4 and 5. The analyst must adapt or export it into the required format before that handoff. The mapping review uses the column name `HumanCuration`, while the downstream file schema uses `HumanCurated`; these names should not be assumed identical.

Column names are case-sensitive; the notebooks do not automatically normalize `original` to `Original`. The reported combined dictionary total in Section 1 should also be distinguished from a rerun's comment-derived stem output: the implementation's optional literature-intersection report does not by itself guarantee that all 21 literature contributions are added to that output.

### Storage and synchronization

- The project's [data_table folder](https://github.com/mling216/vc_comment_processing/tree/HEAD/data_table) contains local snapshots of the source comparison records, earlier phrase mapping, and curated phrase table.
- The local `data_processing` folder holds generated analysis outputs and is excluded from version control.
- Spreadsheet edits require a corresponding local snapshot refresh if the analyst is using local data.
- Notebook outputs must be deliberately exported or copied back to the intended spreadsheet tabs.
- The source records' `index` key must be preserved during copy-back.

The data-loading mode named `master` means live Google Sheets, not that all inputs come from ResultsStepByStep. Local snapshot lookup is keyed by tab identifier only; it does not verify the supplied workbook ID. Use the workbook/tab pairs in Supplement A.

The reduction notebook uses TF-IDF, a text-weighting method, with cosine similarity to suggest phrase merges. Its rare-term consolidation treats phrases with counts of two or fewer as rare. Matching is primarily within a phrase's main topic, with a broader fallback when that topic has no surviving candidates; weak or unmatched cases can be force-merged. Those assignments merit particular attention during expert review.

The word-processing branch uses lemmatization to obtain word forms, followed by Snowball stemming in the stem-table notebook. The image-compilation branch also extracts stems from original phrases. These are text-processing operations, not semantic validation of the resulting dictionary.

For environment setup, data-loading options, and execution instructions, see the [project README](https://github.com/mling216/vc_comment_processing/blob/HEAD/README.md) [2]. Notebook 1 requires access to an LLM API; notebooks 4–6 require the documented language-processing model. These operational requirements are separate from the research review steps.

## D. References

1. **VC Comment Processing.** Implementation repository and analysis materials. https://github.com/mling216/vc_comment_processing
2. **VC Comment Processing: README.** Workflow, spreadsheet checkpoints, reported counts, and execution guidance. https://github.com/mling216/vc_comment_processing/blob/HEAD/README.md
3. **Phrase Reduction Pipeline.** Expert-defined taxonomy, consolidation, and phrase-tracking implementation. https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/3_phrase_reduction.ipynb

Spreadsheet names were checked on November 23, 2026. The references above point to the current project; a published study should additionally record the exact code revision and data snapshots used.
