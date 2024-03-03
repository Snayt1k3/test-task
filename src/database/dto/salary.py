import dataclasses
import datetime

@dataclasses.dataclass
class Salary:
    value: int
    dt: datetime.datetime
