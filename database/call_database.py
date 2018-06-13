import psycopg2
# https://trvrm.github.io/bulk-psycopg2-inserts.html
import json

from database.database_postgres_uri import *

# rrf_database_settings_obj = rrf_database_settings()
conn, cursor = rrf_database_settings.get_db_instance()

# # cursor.execute("""SELECT * from python_concepts.pythonconcepts""")
# try:
#     # cursor.execute("""SELECT * from rrf_ref_source_config""")
#     cursor.execute("""select source_id from rrf_schema.rrf_ref_source_config where io_extractor_id = '2fd2cc84-0545-426f-bddb-fc4460e7ad90'""")
#     # result = cursor.fetchall() # returns a list of tuple
#     result_one = cursor.fetchone()
#     # result_fetchmany = cursor.fetchmany(2)
#     # result_fetchmany1 = cursor.fetchmany(2)
#     # print("FetchAll : {}".format(result))
#
#     print(len(result_one))
#     print("FetchOne: {}".format(result_one[0]))
#
#     # print("FetchMany: {}".format(result_fetchmany))
#     # print("FetchMany1: {}".format(result_fetchmany1))
# except (Exception, psycopg2.DatabaseError) as error:
#     print("error.pgcode:", error.pgcode, "error.pgerror:", error.pgerror)

rrf_database_settings.teardown()
work_flow_id = '2fd2cc84-0545-426f-bddb-fc4460e7ad90'
query = """select source_id from rrf_ref_source_config where io_extractor_id = %s"""

conn, cursor = rrf_database_settings.get_db_instance()

try:
    cursor.execute(query, (work_flow_id,))
    result_one = cursor.fetchone()
    print("Result: {}".format(result_one))
    if len(result_one) == 1:
        source_id = result_one[0]
        print("Source ID: {}".format(source_id))
except (Exception, psycopg2.DatabaseError) as e:
    conn.rollback()
    rrf_database_settings.teardown()
    print(e.pgerror)
    raise e




