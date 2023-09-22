from pathlib import Path

from gsuid_core.data_store import get_res_path

BG_PATH = Path(__file__).parent / 'bg'
MAIN_PATH = get_res_path('BlueArchiveUID')
GUIDE_PATH = MAIN_PATH / 'guide'
EVENT_PATH = MAIN_PATH / 'event'
CHAR_PATH = MAIN_PATH / 'char'


def init_dir():
    for i in [
        MAIN_PATH,
        GUIDE_PATH,
        EVENT_PATH,
        CHAR_PATH,
    ]:
        i.mkdir(parents=True, exist_ok=True)


init_dir()
