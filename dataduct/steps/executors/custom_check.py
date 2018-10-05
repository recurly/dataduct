import pandas.io.sql as pdsql

from dataduct.data_access import redshift_connection


def get_redshift_data(sql):
    connection = redshift_connection()
    data = pdsql.read_sql(sql, connection)
    connection.close()
    return data.iloc[0][0]


def validate_redshift_result(sql, min_result, max_result):
    result = get_redshift_data(sql)

    if min_result and result < min_result:
        raise Exception("result {0} is less than min {1}".format(result, min_result))
    if max_result and result > max_result:
        raise Exception("result {0} is greater than max {1}".format(result, max_result))

    print result
