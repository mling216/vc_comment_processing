# From Participant Comments to a Visual-Complexity Vocabulary

## Background

Participants describe visual complexity in concrete terms: overlapping marks, hard-to-read labels, unfamiliar forms, or the time needed to understand an image. These comments help explain what a complexity judgment means to the person making it.

The analysis organizes those explanations into a vocabulary of perceived visual complexity (VC). A large language model (LLM) identifies relevant passages and proposes assignments to seven predefined topics. Researchers check the passages against the comments, bring similar expressions together, and group them into sub-topics. The resulting vocabulary remains linked to the original comments and images.

The code and selected data tables are available in [VC Comment Processing](https://github.com/mling216/vc_comment_processing) [1]. Its workflow documentation records the study and dictionary totals [2].

## 1. Study data and vocabulary

Participants compared pairs of visualization images and explained why one appeared more or less visually complex. Each comparison record contains the image pair and the associated comments. Of 698 nonempty records, 685 remain after the study's exclusion flag is applied.

| Quantity | Count |
| --- | --- |
| Nonempty comparison records | 698 |
| Retained comparison records | 685 |
| Images in the canonical reference list | 520 |
| Broad visual-complexity topics | 7 |
| Standard visualization-type categories used in summaries | 9 |
| Curated topic–phrase entries | 404 |
| Distinct curated phrases entering reduction | 399 |
| Named sub-topics | 19 |
| Reported combined dictionary stems | 689: 668 from participant comments and 21 from the literature |

These counts describe different units. A comparison record is not a participant. The 520-image canonical list provides a fixed reference for matching and ordering the image-level results; it is a subset of the images named in the source records. The curated table has 404 topic–phrase entries but 399 distinct phrases because five phrases each belong to two topics.

### The seven topics

| Topic | Aspect of visual complexity | Final sub-topics |
| --- | --- | --- |
| Data Density / Image Clutter (DDIC) | How much information is shown, how many elements appear, and whether they overlap or crowd one another | 3 |
| Visual Encoding Clarity (VEC) | How clearly graphical forms, positions, and other visual marks communicate the data | 3 |
| Semantics / Text Legibility (STL) | Whether labels, legends, text, and contextual information can be read and understood | 3 |
| Schema (SCH) | Familiarity with the domain or visual representation, including its structure and level of abstraction | 3 |
| Color, Symbol, and Texture Details (CSTD) | Color variety and contrast, graphical symbols, and texture | 2 |
| Aesthetics Uncertainty (AU) | Perceived disorganization or ambiguity in the image's appearance | 2 |
| Immediacy / Cognitive Load (ICL) | The difficulty, time, and mental effort involved in understanding the visualization | 3 |
| **Total** | | **19** |

## 2. From comments to image-level results

![Pipeline from comparison comments through AI extraction and human review to sub-topics, image compilation, and word/stem tables](docs/vc_comment_pipeline.svg)

**Figure 1.** Comments pass through extraction, phrase review, vocabulary curation, and sub-topic construction. Researchers review the original passages, the standardized wording, and the final groupings. The two downstream branches produce image-level summaries and word/stem tables. Files are transferred between stages; the arrows do not indicate automatic spreadsheet updates.

## 3. Processing steps

The work uses two main spreadsheets. PostquestionareAnalysisGPT5 holds the source comments and earlier phrase mappings. ResultsStepByStep holds the curated vocabulary and image-level reference tables. Both have a tab called 0.postquestionare_all, so the spreadsheet name matters. Supplement A lists the tables and the additional image-metadata and VC-score references.

### 1. Prepare the comment records

The starting point is PostquestionareAnalysisGPT5 → 0.postquestionare_all. Records marked for exclusion are removed before extraction. The remaining records retain the comments, image identifiers, and index key that connect each later annotation to its source.

### 2. Extract topics and phrases with AI assistance

The LLM identifies the topics discussed in each comment and extracts the relevant words or phrases without paraphrasing them. A passage may support more than one topic: a comment about overlapping labels, for example, may concern both clutter and text legibility.

Each passage is linked to the image it describes and marked (+) for increased complexity or (-) for decreased complexity. The sign records the participant's explanation, not whether the feature is generally good or bad. It also cannot be inferred solely from which image was chosen as more complex. Extraction results are copied back to the source tab using the index key.

### 3. Review phrases in context

Researchers read each extracted passage alongside the original comment. They check whether the words were quoted correctly, whether the topic assignment fits, and whether the image and complexity sign are correct. They also look for relevant wording that was missed.

Approved topic–phrase assignments are stored in CuratePhrasesMoreComplex and CuratePhrasesLessComplex in the source tab. This review comes before vocabulary curation, so the original wording is checked before expressions are combined or renamed.

### 4. Review the standardized vocabulary

Curation brings different expressions of the same idea under a consistent label. An original phrase is what the participant said; a curated phrase is the standardized wording used in the vocabulary. The mapping between them is retained so readers can trace a label back to the comments that support it.

Researchers review these mappings in PostquestionareAnalysisGPT5 → 1.keyword.S&Y(AI+humanCuration). The approved phrase and count table is then transferred to ResultsStepByStep → 2.curatedPhrases. For image-level analysis, that spreadsheet's separate 1.phraseCuration tab also needs the reviewed mapping.

### 5. Consolidate phrases into 19 sub-topics

Reduction begins with the 399 distinct phrases in ResultsStepByStep → 2.curatedPhrases. Expert-defined synonym groups combine closely related expressions. Text similarity is then used to match remaining rare phrases to more frequent candidates, usually within the same topic. Even weak matches can be assigned automatically, so those decisions need close review.

The reduction also removes empty entries and checks specified pairs of opposite expressions for redundancy. Phrases specific to one visualization type are retained when they describe a relevant visual property.

A phrase's ranking score multiplies its image-association count—the recorded links between that phrase and images—by the number of visualization types in which it appears. This favors phrases linked to many images and used across several types. The score helps order the vocabulary; researchers decide the conceptual groupings.

The taxonomy contains 19 named sub-topics across the seven broad topics [3]. A sub-topic groups related curated phrases under a concept such as Information Volume or Typography & Readability. The tracking table records merges, exclusions, and assignments, including phrases that remain unmapped. The full list of sub-topics appears in Supplement B.

### 6. Link concepts to images and produce outputs

The image-level stage connects each image to its original phrases, curated wording, and assigned sub-topics. It uses ResultsStepByStep → 0.postquestionare_all and 1.phraseCuration, then aligns the results to the 520-image reference list in 4.0.imageDataCompiled. Images on that list are retained even when no phrase mapping is available; a blank mapping should not be interpreted as evidence that the image lacks a particular property.

- **Image compilation (branch A)** combines the phrase mappings, complexity signs, sub-topics, and stems in an image-level table. It also produces a stem dictionary and optional reports. This branch uses PostquestionareAnalysisGPT5 → 5.1 imagePhraseCompile as its ordering reference.
- **Word and stem tables (branch B)** extracts words from the phrase vocabulary, matches phrases to images, and groups related word forms. A stem is a shortened form used for word matching. Related forms such as “color” and “colored” can be grouped, although sharing a stem does not always mean sharing a meaning.

The branches can be run separately or together. They require the intermediate files listed in Supplement C. Image-topic and visualization-type summaries can be copied back to PostquestionareAnalysisGPT5 → 5.imageTypeTopics and 2.keyword.CountByVisTypes.

## 4. Reading the results

The vocabulary describes what participants noticed and how they explained complexity. Original phrases provide the evidence; curated labels and sub-topics represent the researchers' interpretation. Neither a frequent phrase nor a high ranking score establishes that a feature causes complexity.

The combined dictionary is reported as 689 stems: 668 derived from participant comments and 21 from the literature [2]. Those sources should remain distinguishable. Word-level matching is useful for searching and summarizing the vocabulary, but the original comment is still needed to interpret a phrase's meaning and complexity sign.

Reproducing the analysis requires the code revision, the spreadsheet versions or saved snapshots, and the phrase-tracking table. Spreadsheet edits and local analysis files are synchronized by export or copy-back, not automatically.

---

# Supplement: References and Reproduction Details

## A. Exact spreadsheet and tab references

Spreadsheet titles and tab names were checked on November 23, 2026. A tab identifier (gid) locates a worksheet only within its spreadsheet; use both identifiers when reproducing a table reference.

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

### A2. ResultsStepByStep

**Spreadsheet ID:** `1cVCOfBjHmcvsyrn7U0CbXoBSksF4JDRqWYm-ZJPbL4k`

[Open ResultsStepByStep](https://docs.google.com/spreadsheets/d/1cVCOfBjHmcvsyrn7U0CbXoBSksF4JDRqWYm-ZJPbL4k/edit)

| Current tab name | Tab identifier (gid) | Role |
| --- | --- | --- |
| 0.postquestionare_all | `1540814304` | Image-pair and reviewed-phrase input for the per-image section |
| 1.phraseCuration | `1455332435` | Mapping from reviewed original expressions to human-curated phrases |
| 2.curatedPhrases | `517808299` | Curated phrase-and-count input for reduction |
| 4.0.imageDataCompiled | `483858074` | Canonical image list for the reduction notebook's per-image output |

ResultsStepByStep → 1.phraseCuration is the mapping used by the reduction notebook's image-level section. It is separate from PostquestionareAnalysisGPT5 → 1.keyword.S&Y(AI+humanCuration), which supplies the earlier mapping stage.

### A3. Sub.Vis2025VisComplexity.PerceivedScoreAndObjectiveMetrics

**Spreadsheet ID:** `1N6nK03QiPAM6AELb9kC3beETnKmG6u23`

[Open the VC score spreadsheet](https://docs.google.com/spreadsheets/d/1N6nK03QiPAM6AELb9kC3beETnKmG6u23/edit)

| Current tab name | Tab identifier (gid) | Role |
| --- | --- | --- |
| FormalExp1800Images | `67202923` | Normalized VC values used in downstream reporting |

### A4. VisComplexity.PerceivedScoreAndObjectiveMetrics

**Spreadsheet ID:** `1eJ3VUh2ZKZy6S6qo9nzF8h0rwwMNBhwuK42wdgeS54w`

[Open the image-metadata spreadsheet](https://docs.google.com/spreadsheets/d/1eJ3VUh2ZKZy6S6qo9nzF8h0rwwMNBhwuK42wdgeS54w/edit)

| Current tab name | Tab identifier (gid) | Role |
| --- | --- | --- |
| FormalExp1800Images | `1073958835` | Image metadata, including visualization types used by notebook 1's image-topic section |

The metadata and VC-score spreadsheets both contain a tab named FormalExp1800Images. They are separate reference tables.

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

The nine standard visualization-type labels used in summaries [1] are Area, Bar, Cont.-ColorPatn, Glyph, Grid, Line, Node-link, Point, and Text. Cont.-ColorPatn is the spreadsheet label used for Color/Pattern. Source records also include other and mixed-type labels; the nine categories are not a count of all labels in the raw study table.

## C. Technical implementation and outputs

| Research stage | Implementation | Main local outputs |
| --- | --- | --- |
| Topic and phrase extraction | [1_llm_extraction.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/1_llm_extraction.ipynb) | Extraction tables, including `extracted_*.csv` and `CuratedPhrasesCombined.csv`; additional keyword and image summaries |
| Phrase-mapping reconstruction | [2_phrase_curation.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/2_phrase_curation.ipynb) | `term_mapping_regenerated.csv`; `phrase_pivot_regenerated.csv` |
| Phrase reduction and sub-topic construction | [3_phrase_reduction.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/3_phrase_reduction.ipynb) | `phrase_shortlist.csv`; `subtopic_taxonomy.csv`; `phrase_reduction_tracking.csv`; `image_phrase_word_mapping.csv` |
| Branch A: image compilation | [4_image_compilation.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/4_image_compilation.ipynb) | `image_compiled_phrases.csv`; `stem_dictionary.csv`; optional reports |
| Branch B: word extraction and image matching | [5_keyword_extraction.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/5_keyword_extraction.ipynb) | `unique_words.csv`; `image_phrase_matching.csv`; visualization-type word tables |
| Branch B continuation: stem extraction | [6_keyword_stems.ipynb](https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/6_keyword_stems.ipynb) | `unique_stems*.csv`; optional phrase-lineage stem tables |

Notebook 3 produces the vocabulary tables before its image-level section. Notebook 4 adds image compilation and optional reports. Notebook 6's lineage section is optional and needs a separate lineage file. The execution guides identify the cells required for each output.

### Required intermediate files

Downstream analyses require the following separately supplied inputs in the local output folder:

| Input file | Needed for | Handoff requirement |
| --- | --- | --- |
| `term_mapping.csv` | Notebooks 4 and 5 | Notebook 5 reads `Original`, `AIcurated`, and `HumanCurated`; notebook 4 core reads lowercase `original` and `OriginalSign`. A shared export needs both original-phrase spellings with identical values. Optional notebook 4 sentiment reports also use `HumanCuratedSign`. |
| `image_compiled_phrases.csv` | Notebook 4 | Existing image-level phrase table used as a compilation input, even though notebook 4 also writes an updated file with this name |
| `stem_dictionary.csv` | Notebook 4 core setup and dictionary cells | Existing or previously generated stem dictionary |
| `phrase_lineage_all_vistypes.csv` | Notebook 6's optional lineage section | Links `original_phrase` to `final_subtopic_phrase`; not produced by the current notebook 3 cells |

Notebook 2's `term_mapping_regenerated.csv` is a **wide, per-topic table**. Export it into the long-format `term_mapping.csv` required by notebooks 4 and 5 before that handoff. The mapping review uses the column name `HumanCuration`, while the downstream file schema uses `HumanCurated`; these names require explicit conversion.

Column names are case-sensitive; the notebooks do not automatically convert `original` to `Original`.

The combined 689-stem dictionary and the comment-derived stem output are different products. The optional literature-intersection report compares vocabulary with literature factors; it does not automatically add all 21 literature-derived stems to the comment dictionary.

### Storage and synchronization

- The project's [data_table folder](https://github.com/mling216/vc_comment_processing/tree/HEAD/data_table) contains local snapshots of the source comparison records, earlier phrase mapping, and curated phrase table.
- The local `data_processing` folder holds generated analysis outputs and is excluded from version control.
- When using local data, refresh the snapshots after changing the spreadsheets.
- Notebook outputs must be deliberately exported or copied back to the intended spreadsheet tabs.
- The source records' `index` key must be preserved during copy-back.

The `master` data-loading mode reads live Google Sheets from the workbook specified for each input. Local snapshot lookup uses the tab identifier alone and does not verify the workbook ID, so the spreadsheet/tab pairs in Supplement A must be preserved.

### Reduction and word processing

The reduction count is the sum of `num_images` across the topic–phrase rows for a given phrase. An image associated with that phrase under more than one topic can therefore contribute more than once. It is not a participant or comment count. The ranking score multiplies this image-association count by the number of standard visualization types containing the phrase.

The reduction notebook treats counts below three as rare. After manual synonym merging, it uses TF-IDF to represent the remaining phrases by their words and word pairs, then compares those representations using cosine similarity. Matching normally stays within the assigned primary topic. If that topic has no more-frequent candidates, matching uses the wider candidate pool. Every remaining rare phrase receives its closest match, with low-similarity assignments recorded for review.

Word extraction uses lemmatization to obtain dictionary forms of words. The stem-table notebook then uses Snowball stemming to group related forms by a common stem. The image-compilation branch also stems words from the original phrases.

For environment setup, data-loading options, and execution instructions, see the [project README](https://github.com/mling216/vc_comment_processing/blob/HEAD/README.md) [2]. Notebook 1 requires access to an LLM API; notebooks 4–6 require the documented language-processing model.

## D. References

1. **VC Comment Processing.** Implementation repository and analysis materials. https://github.com/mling216/vc_comment_processing
2. **VC Comment Processing: README.** Workflow, spreadsheet checkpoints, reported counts, and execution guidance. https://github.com/mling216/vc_comment_processing/blob/HEAD/README.md
3. **Phrase Reduction Pipeline.** Expert-defined taxonomy, consolidation, and phrase-tracking implementation. https://github.com/mling216/vc_comment_processing/blob/HEAD/notebooks/3_phrase_reduction.ipynb
