import psycopg2

conn_string = "host='localhost' dbname='catalogdb' user='www-data' password='bcr0072'"

def application(environ, start_response):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("select * from Items")
    records = cursor.fetchall()
    output = records[0][1]
    status = '200 OK'

    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]