import os
import pickle

import aiofiles

import globals

PERSISTENCE_PATH = os.path.join(os.path.abspath("."), "persistence")
DATA_STATE = "data_state"
DATA_DS = "data_ds"


async def load():
    # проверка на наличие директории с постоянными данными
    if not (os.path.exists(PERSISTENCE_PATH) and os.path.isdir(PERSISTENCE_PATH)):
        os.mkdir(PERSISTENCE_PATH)
    else:
        if os.path.exists(os.path.join(PERSISTENCE_PATH, DATA_STATE)) and os.path.exists(
                os.path.join(PERSISTENCE_PATH, DATA_DS)):
            with open(os.path.join(PERSISTENCE_PATH, DATA_STATE), "rb") as file:
                globals.state = pickle.load(file)
            with open(os.path.join(PERSISTENCE_PATH, DATA_DS), "rb") as file:
                globals.datasets = pickle.load(file)


async def save():
    # проверка на наличие директории с постоянными данными
    if not (os.path.exists(PERSISTENCE_PATH) and os.path.isdir(PERSISTENCE_PATH)):
        os.mkdir(PERSISTENCE_PATH)
    else:
        with open(os.path.join(PERSISTENCE_PATH, DATA_STATE), "wb") as file:
            pickle.dump(globals.state, file)
        with open(os.path.join(PERSISTENCE_PATH, DATA_DS), "wb") as file:
            pickle.dump(globals.datasets, file)
