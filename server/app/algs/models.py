from sqlalchemy import Table, Column, String, Integer, ForeignKey

from database import metadata

requirement = Table(
    "requirement",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
)

algorithm = Table(
    "algorithm",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("description", String, default=""),
)

alg_req = Table(
    "alg_req",
    metadata,
    Column("pre_id", Integer, ForeignKey("requirement.id"), primary_key=True),
    Column("alg_id", Integer, ForeignKey("algorithm.id"), primary_key=True),
)

result = Table(
    "result",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, ForeignKey("user.username"), primary_key=True),
    Column("dataset_id", Integer, ForeignKey("dataset.id")),
    Column("pre_info", String),
    Column("name", String)
)

model = Table(
    "model",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("algorithm_id", Integer, ForeignKey("algorithm.id")),
    Column("hipers", String)
)

metric = Table(
    "metric",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)

split = Table(
    "split",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("strat", Integer),
    Column("test", Integer)
)

# metric_values = Table(
#     "metric_values",
#     metadata,
#     Column("result_id", Integer, ForeignKey(result.c.id), primary_key=True),
#     Column("split_id", Integer, ForeignKey(split.c.id), primary_key=True),
#     Column("metric_id", Integer, ForeignKey(metric.c.id), primary_key=True),
#     Column("model_id", Integer, ForeignKey(model.c.id), primary_key=True),
#     Column("value", Integer)
# )
