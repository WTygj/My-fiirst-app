def visitors():
	counter_read_file = open("count.txt","r")
	visitors_count = int(counter_read_file.read()) counter_read_file.close()

# Increment the count
	visitors_count = visitors_count + 1\

# Overwrite the count

	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()
	print('Total visitors: visitors_count')


def covid_stats():

	country_code = input('Enter country Name:')
	corona_data = ''+country_code print(corona_data)