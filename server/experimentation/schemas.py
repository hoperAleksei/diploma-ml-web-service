from pydantic import BaseModel


# experiment.run_experiment
# input
class Param(BaseModel):
    name: str
    type: str
    min: float | None = None
    max: float | None = None
    values: list[str] | None = None
    decs: str | None = None


class ExperimentResultInput(BaseModel):
    alg_name: str
    n_steps: int
    params: list[Param]


# output

class MetricsResult(BaseModel):
    accuracy: float | None = None
    error_rate: float | None = None
    precision: float | None = None
    recall: float | None = None
    f1: float | None = None
    roc_auc: float | None = None


class CurExperimentResult(BaseModel):
    hyperparams: dict  # приходит каждый раз разный словарик
    metrics: MetricsResult


class ExperimentResultOutput(BaseModel):
    alg_name: str
    hyperparams_names: list[str]
    experiment: list[CurExperimentResult]


# alg_test.parse
# output

class ParseOut(BaseModel):
    status: bool
    details: str
    name: str
    desc: str
    pre: list


parseOut = \
    {
        "status": True,
        "details": "SUCCESS",
        "name": "Decision Tree",
        "desc": "Дерево решений — классификатор, построенный на основе решающих правил вида «если, то», упорядоченных в древовидную иерархическую структуру.",
        "pre": [
            "not null"
        ]
    }

# print(ParseOut.parse_obj(parseOut))


# loader.get_all_alg


class get_all_alg_output(BaseModel):
    name: str
    params: list[Param]

