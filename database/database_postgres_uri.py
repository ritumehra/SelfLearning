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
    def tearDown(self):
        rrf_database_settings.db_conn = None
        rrf_database_settings.db_cursor = None

    @classmethod
    def get_db_instance(cls):
        if cls.db_conn is None:
            try:

                dbname = "rapidredflagDB"
                user = "rrfqaadmin"
                host = "rapidredflag-qa-cluster.cluster-corycqk2nwkx.us-east-1.rds.amazonaws.com"
                password = "NuytIvtyEFUe"
                port = 5432
                sslmode = "require"

                config_string = "dbname='%s' user='%s' host='%s' password='%s' port='%s' sslmode='%s'" \
                                % (dbname, user, host, password, port,sslmode)
                conn = psycopg2.connect(config_string)

                # conn = psycopg2.connect("postgresql:///postgres?host=localhost&port=5432&user=postgres&password=heer")
                # conn = psycopg2.connect(
                #     "postgresql:///rapidredflagDB?host=rapidredflag-qa-cluster.cluster-corycqk2nwkx.us-east-1.rds.amazonaws.com&port=5432&user=rrfqaadmin&password=NuytIvtyEFUe")
                # conn = psycopg2.connect("postgresql:///rapidredflagDB?host=rapidredflagclstr-1.cluster-corycqk2nwkx.us-east-1.rds.amazonaws.com&port=5432&user=rrfdevadmin&password=NuytIvtyEFUe")
                cls.db_conn = conn
                cls.db_cursor = conn.cursor()
                print ("POSTGRES DB INSTANCE CREATED")

            except (Exception, psycopg2.DatabaseError) as error:
                print("error.pgcode:",error.pgcode, "error.pgerror:",error.pgerror)



        return cls.db_conn, cls.db_cursor






