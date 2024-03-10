import datetime
from collections import defaultdict
from src.database.dto.salary import Salary
import pandas as pd


async def aggregate_payments(
    dt_from: datetime.datetime,
    dt_upto: datetime.datetime,
    group_type: str,
    payments_data: list[Salary],
):
    aggregated_payments = defaultdict(int)
    for payment in payments_data:
        if dt_from <= payment.dt <= dt_upto:
            if group_type == "day":
                aggregated_payments[payment.dt.day] += payment.value
            elif group_type == "month":
                aggregated_payments[payment.dt.month] += payment.value
            elif group_type == "hour":
                aggregated_payments[payment.dt.hour] += payment.value

    if group_type == "hour":
        date_range = pd.date_range(start=dt_from, end=dt_upto, freq="H")
    elif group_type == "day":
        date_range = pd.date_range(start=dt_from, end=dt_upto, freq="D")
    elif group_type == "month":
        date_range = pd.date_range(start=dt_from, end=dt_upto, freq="MS")

    return {"labels": [date.strftime("%Y-%m-%dT%H:%M:%S") for date in date_range], "dataset": [value for _, value in aggregated_payments.items()]}
    # return aggregated_payments
