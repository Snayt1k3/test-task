import datetime

import pandas as pd

from src.database.repositories.base import BaseRepository


class AggregatePayments:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def execute(
            self,
            dt_from: datetime.datetime,
            dt_upto: datetime.datetime,
            group_type: str,
    ):
        payments_data = await self.repository.get_all_salaries("user_salaries")
        aggregated_payments = {}

        if group_type == "hour":
            date_range = pd.date_range(start=dt_from, end=dt_upto, freq="H")
        elif group_type == "day":
            date_range = pd.date_range(start=dt_from, end=dt_upto, freq="D")
        elif group_type == "month":
            date_range = pd.date_range(start=dt_from, end=dt_upto, freq="MS")

        labels = [date.strftime("%Y-%m-%dT%H:%M:%S") for date in date_range]

        # формируем словарь с ключами
        for label in labels:
            aggregated_payments[label] = 0

        payments_data.sort(key=lambda a: a.dt)

        for payment in payments_data:
            if dt_from <= payment.dt <= dt_upto:
                if group_type == "day":
                    aggregated_payments[
                        datetime.datetime(
                            day=payment.dt.day, month=payment.dt.month, year=payment.dt.year
                        ).strftime("%Y-%m-%dT%H:%M:%S")
                    ] += payment.value

                elif group_type == "month":
                    aggregated_payments[
                        datetime.datetime(
                            month=payment.dt.month, year=payment.dt.year, day=1
                        ).strftime("%Y-%m-%dT%H:%M:%S")
                    ] += payment.value

                elif group_type == "hour":
                    aggregated_payments[
                        datetime.datetime(
                            hour=payment.dt.hour,
                            day=payment.dt.day,
                            month=payment.dt.month,
                            year=payment.dt.year,
                        ).strftime("%Y-%m-%dT%H:%M:%S")
                    ] += payment.value

        return {
            "labels": labels,
            "dataset": [value for _, value in aggregated_payments.items()],
        }
