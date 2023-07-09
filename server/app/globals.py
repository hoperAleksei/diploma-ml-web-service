from typing import Dict

from state_manager.schemas import UserState, State, Prepro, Split, Autofit
from pandas import DataFrame

datasets : Dict[int, DataFrame] = {}

state : Dict[str, UserState] = {}
