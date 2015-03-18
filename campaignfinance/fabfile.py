from fabric.api import local

from datetime import date, timedelta
import psycopg2

conn = psycopg2.connect("dbname=electionmoney user=chris")
cur = conn.cursor()
cur.execute("""SELECT max("RcvDate") FROM receipts""")
start = cur.fetchone()[0]-timedelta(days=1)

today = date.today().strftime('%Y%m%d')
start_sql = start.strftime('%Y-%m-%d')
start_string = start.strftime('%Y%m%d')

def update_finance_db():
	print "deleting records from %s" % start_string
	cur.execute("""DELETE from receipts where "RcvDate" >= '%s' ;""" % start_sql)

	local("python scripts/scrape_data.py -s %s -e %s -t Receipts" % (start_string, today))
	output = open('scripts/output/%s-to-%s-%s.csv' % (start_string,today,'Receipts'), 'r')
	sql = "COPY receipts FROM STDIN CSV HEADER;"	
	cur.copy_expert(sql=sql, file=output)
	

	conn.commit()
	cur.close()
	conn.close()

	local('python manage.py staticsitegen')

def check_date():
	print start

# DELETE from receipts where "RcvDate" >= '2015-02-20';
# python scrape_data.py
# psql electionmoney -c "COPY receipts FROM '`pwd`/receipts2015.csv' CSV HEADER;"
# python manage.py staticsitegen