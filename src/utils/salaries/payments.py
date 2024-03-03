import datetime
from collections import defaultdict
from src.database.dto.salary import Salary


async def aggregate_payments(
    dt_from: datetime.datetime,
    dt_upto: datetime.datetime,
    group_type: str,
    payments_data: list[Salary],
):
    # try:
    #     aggregated_payments = defaultdict(dict)
    #     for payment in payments_data:
    #         if dt_from <= payment.dt <= dt_upto:
    #             aggregated_payments[group_type][].append(payment.value)
    #
    #     return aggregated_payments[group_type]
    # except Exception as e:
    #     print(e)
    pass