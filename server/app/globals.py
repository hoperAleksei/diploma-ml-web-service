from typing import Dict

from state_manager.schemas import UserState, State, Split, Autofit
from pandas import DataFrame

datasets: Dict[int, DataFrame] = {}

state: Dict[str, UserState] = {}

results: Dict[str, [UserState]] = {}
