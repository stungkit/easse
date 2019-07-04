from pathlib import Path


# Paths
REPO_DIR = Path(__file__).resolve().parent.parent.parent
TOOLS_DIR = REPO_DIR / 'tools'
DATA_DIR = REPO_DIR / 'data'
STANFORD_CORENLP_DIR = TOOLS_DIR / 'stanford-corenlp-full-2018-10-05'
UCCA_DIR = TOOLS_DIR / 'ucca-bilstm-1.3.10'
UCCA_PARSER_PATH = UCCA_DIR / 'models/ucca-bilstm'

# Constants
VALID_TEST_SETS = ['turk', 'turk_valid', 'pwkp', 'hsplit']
VALID_METRICS = ['bleu', 'sari', 'samsa', 'fkgl']
DEFAULT_METRICS = [m for m in VALID_METRICS if m != 'samsa']  # HACK: SAMSA is too long to compute