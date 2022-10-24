import pandas
from dream_api_service.db import sqlalchemy_engine

def generate_hours(start, end):

    with sqlalchemy_engine.connect() as con:
        con.execution_options(isolation_level="AUTOCOMMIT")
        result = con.execute(
            """
            SELECT distinct xx::time::varchar
            from
                generate_series('2022-02-10 {}',
                                '2022-02-10 {}',
                                interval  '1 hour') xx
            order by xx
            """.format(start, end)
        )
    hours = []
    for r in result.all():
        hours.append(r[0])

    return hours

    