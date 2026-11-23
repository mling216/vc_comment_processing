"""
Data loader — the single place that knows how to fetch a sheet/table.

Two ways to read the paired-comparison data (and any other tab):
  1. from the configured Google Sheets (``source="master"``, live)
  2. from a **local copy** under data_table/ (offline, reproducible)

Use `load_paired_comparison()` for the study table, or the generic
`load_sheet(spreadsheet_id, gid)` for any tab. The default source comes from
`config.DATA_SOURCE` and can be overridden per call.
"""
import os
import pandas as pd

import config


def _google_export_url(spreadsheet_id: str, gid: str) -> str:
    return (
        f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"
        f"/export?gid={gid}&format=csv"
    )


def load_sheet(spreadsheet_id: str, gid, source: str | None = None) -> pd.DataFrame:
    """Load one worksheet as a DataFrame.

    Parameters
    ----------
    spreadsheet_id : Google Sheet ID (ignored for local reads if a local copy
        is registered for the gid).
    gid : worksheet gid (int or str).
    source : "master" (Google) or "local" (data_table/ CSV). Defaults to
        ``config.DATA_SOURCE``.
    """
    gid = str(gid)
    source = source or config.DATA_SOURCE

    if source == "local":
        fname = config.LOCAL_SHEET_MAP.get(gid)
        if fname:
            path = os.path.join(config.DATA_TABLE, fname)
            if os.path.exists(path):
                return pd.read_csv(path)
        # No local copy registered/found -> fall back to the live sheet.
        print(f"[data_loader] no local copy for gid={gid}; reading from master")

    return pd.read_csv(_google_export_url(spreadsheet_id, gid))


def load_paired_comparison(source: str | None = None) -> pd.DataFrame:
    """Load PostquestionareAnalysisGPT5 / 0.postquestionare_all.

    Returns raw records; this loader does not apply the ToRemove exclusion.
    This is the entry point of the pipeline and demonstrates the two read
    modes: ``load_paired_comparison("master")`` vs ``load_paired_comparison("local")``.
    """
    return load_sheet(config.PAIRED_SHEET_ID, config.PAIRED_GID, source=source)
