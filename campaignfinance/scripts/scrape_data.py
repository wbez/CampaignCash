import scraper, argparse, csv, StringIO
from datetime import date

parser = argparse.ArgumentParser()
parser.add_argument('--start', '-s', help='Start date for scraping' )
parser.add_argument('--end', '-e', help='End date for scraping' )
parser.add_argument('--type', '-t', help='Type of file to get (Receipts or Expenditures). Must be uppercased' )
args = parser.parse_args()

scrape_type = args.type
start_date = args.start
end_date = args.end

today = date.today().strftime('%Y%m%d')

def scrape():

	print "Scraping from %s to %s" % (start_date,end_date)
	data = scraper.fetch_data(dl_type=scrape_type,start_date=start_date,end_date=end_date)

	# years=range(startyear,endyear+1)
	# for i in range(len(years)):
	# 	year  = str(years[i])
	# 	if year == today.year:
	# 		print "Scraping from %s to " % (start_date,end_date)
	# 		data = scraper.fetch_data(dl_type=scrape_type,start_date=str(year)+'0101',end_date=str(year)+'1231')
	# 	else:
	# 		print "Scraping %s" % str(year)
	# 		data = scraper.fetch_data(dl_type=scrape_type,start_date=start_date,end_date=today)

	write_to_csv(data)

def write_to_csv(data_string):
	f = StringIO.StringIO(data_string)
	reader = csv.reader(f, delimiter='\t')
	raw = open('scripts/output/%s-to-%s-%s-raw.csv' % (start_date,end_date,scrape_type), 'w')
	raw.write(data_string)
	raw.close()

	output = open('scripts/output/%s-to-%s-%s.csv' % (start_date,end_date,scrape_type), 'w')
	errors = open('scripts/output/%s-to-%s-%s-errors.csv' % (start_date,end_date,scrape_type), 'w')
	output_writer = csv.writer(output)
	error_writer = csv.writer(errors)
	header = reader.next()
	output_writer.writerow(header)
	error_writer.writerow(header)

	for row in reader:
		if len(row) == len(header):
			output_writer.writerow(row)
		else:
			error_writer.writerow(row)

if __name__ == '__main__':
	scrape()