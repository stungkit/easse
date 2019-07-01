from pathlib import Path


REPO_DIR = Path(__file__).resolve().parent.parent.parent
TOOLS_DIR = REPO_DIR / 'tools'
DATA_DIR = REPO_DIR / 'data'
STANFORD_CORENLP_PATH = TOOLS_DIR / 'stanford-corenlp-full-2018-10-05'