"""
Central configuration for the VC comment-processing pipeline.

Everything that varies between environments (data source, sheet IDs, folder
locations, the canonical topic/VisType vocabulary) lives here so the notebooks
stay clean and portable.
"""
import os

# ---------------------------------------------------------------------------
# Repository layout
# ---------------------------------------------------------------------------
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(REPO_ROOT, "data_processing")   # notebook outputs
DATA_TABLE = os.path.join(REPO_ROOT, "data_table")      # local sheet copies
os.makedirs(DATA_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Where to read the input tables from
#   "master" -> live Google Sheet (needs internet; always current)
#   "local"  -> local CSV copies under data_table/ (offline, reproducible)
# Override per-call with load_sheet(..., source="master"|"local").
# ---------------------------------------------------------------------------
DATA_SOURCE = os.environ.get("VC_DATA_SOURCE", "master")

# ResultsStepByStep: current reduction workbook, not the initial comment source.
MASTER_SHEET_ID = "1cVCOfBjHmcvsyrn7U0CbXoBSksF4JDRqWYm-ZJPbL4k"

# PostquestionareAnalysisGPT5 / 0.postquestionare_all: initial comment source.
# ResultsStepByStep has a separate tab with this name (gid 1540814304).
PAIRED_SHEET_ID = "1gfeYdT-RxLq9tvNpfv_P8AIKg2eSz6-8bSv5zUJsWEc"
PAIRED_GID = "1103808983"

# Map a sheet gid -> local CSV filename (under data_table/) for offline reads.
# Only tabs that have a shipped local copy need to appear here; everything else
# falls back to the Google export URL automatically.
LOCAL_SHEET_MAP = {
    "1103808983": "paired_comparison.csv",   # PostquestionareAnalysisGPT5 / 0.postquestionare_all
    "517808299":  "curated_phrases.csv",     # ResultsStepByStep / 2.curatedPhrases
    "1166121277": "phrase_curation.csv",     # PostquestionareAnalysisGPT5 / 1.keyword.S&Y(AI+humanCuration)
}

# ---------------------------------------------------------------------------
# Canonical vocabulary shared across the whole pipeline
# ---------------------------------------------------------------------------
TOPICS = [
    "Data Density / Image Clutter",
    "Visual Encoding Clarity",
    "Semantics / Text Legibility",
    "Schema",
    "Color, Symbol, and Texture Details",
    "Aesthetics Uncertainty",
    "Immediacy / Cognitive Load",
]

TOPIC_ABBREV = {
    "Data Density / Image Clutter": "DDIC",
    "Visual Encoding Clarity": "VEC",
    "Semantics / Text Legibility": "STL",
    "Schema": "SCH",
    "Color, Symbol, and Texture Details": "CSTD",
    "Aesthetics Uncertainty": "AU",
    "Immediacy / Cognitive Load": "ICL",
}

VIS_TYPES = [
    "Area", "Bar", "Cont.-ColorPatn", "Glyph", "Grid",
    "Line", "Node-link", "Point", "Text",
]
