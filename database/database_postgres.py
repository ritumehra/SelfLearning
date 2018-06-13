import psycopg2

class rrf_database_settings:

    db_conn = None
    db_cursor = None

    def __init__(self):
        print("DB Initialized")
        if self.db_conn is not None:
            raise ValueError("An instantiation already exists!")
            # do your init stuff

    def __del__(self):
        print("tearDown called")
        rrf_database_settings.db_conn = None
        rrf_database_settings.db_cursor = None

    @classmethod
    def get_db_instance(cls):
        if cls.db_conn is None:
            try:

                dbname = "postgres"
                user = "postgres"
                host = "localhost"
                password = "heer"
                port = 5432

                config_string = "dbname='%s' user='%s' host='%s' password='%s' port='%s'" \
                                % (dbname, user, host, password, port)

                conn = psycopg2.connect(config_string)
                cls.db_conn = conn
                cls.db_cursor = conn.cursor()
                print ("POSTGRES DB INSTANCE CREATED")

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)



        return cls.db_conn, cls.db_cursor






