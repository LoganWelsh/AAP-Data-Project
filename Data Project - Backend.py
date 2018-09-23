# This program accepts data CSV files of two types of data: Home Sales or Construction Permits.

# This program filters the data file for either Home Sales or Construction Permits and writes
# the filtered data to a new text CSV file in a 'Data Quarry' folder on the users desktop.
# It also counts the number of occurrences of wanted data for each month of each year since
# the start year set by the user and writes this information in a table on a separate
# text file in the 'Data Quarry' folder.

# Filter parameters are hard-coded in and can be changed by request to the developer, Logan Welsh.

# Data text CSV files must be named either 'Web_Sales_View.txt' for Home Sales or 'Web_Permits_View.txt'
# for Construction Permits.

import os


def permits_processing ():
    def filter_data(filename):
        global monthly_permits, count, start_year, end_year
        valid_years = False
        while not valid_years:
            start_year, end_year = input('Filter data from (year): '), input('to (year): ')
            try:
                int(end_year) and int(start_year)
            except:
                print('Invalid year!')
                continue
            if int(end_year) > 2017 or int(start_year) > 2017:
                print('Invalid year!')
            elif len(end_year) != 4 or len(start_year) != 4:
                print('Invalid year!')
            else:
                valid_years = True
        file = open(filename, 'r')
        for year in range(int(start_year), int(end_year) + 1):
            monthly_permits[year] = []
            for month in range(1, 13):
                monthly_permits[year].append(0)
        data = file.readlines()
        refined_data = []
        descriptions = ['SINGLE FAMILY-DETACH', 'SINGLE FAMILY']
        for line in data:
            new_line = line.strip().split(',')
            if len(new_line) < 6:
                continue
            for index in range(2, 6):
                new_line[index] = new_line[index].strip('"')
            alt_key, roll_year, permit_number, issue_date, completion_date, description = new_line[0], new_line[1], \
                                                                                          new_line[2], new_line[3], \
                                                                                          new_line[4], new_line[5]
            new_line.insert(2, issue_date[0:4])
            try:
                if int(issue_date[0:4]) in range(int(start_year), int(end_year) + 1):
                    if description in descriptions:
                        monthly_permits[int(issue_date[0:4])][int(issue_date[4:6]) - 1] += 1
                        count += 1
                        refined_data.append(new_line)
            except ValueError:
                continue
        file.close()
        return (refined_data)

    def write_data_1(filename):
        file = open(filename, 'w')
        data = filter_data('Web_Permits_View.txt')
        global count
        file.write('Alt_Key, Roll_Year, Issue_Year, Permit_Numb, Issue_Date, Completion_Date, Description \n')
        for line in data:
            string = line[0]
            for element in range(1, 7):
                string = string + ',' + line[element]
            string = string + '\n'
            file.write(string)
        file.close()

    def write_data_2(filename):
        file = open(filename, 'w')
        file.write('Number of single-family home construction permits: {} \n'.format(count))
        file.write(
            '{:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} \n'.format('Year', 'Jan',
                                                                                                      'Feb',
                                                                                                      'Mar', 'Apr',
                                                                                                      'May',
                                                                                                      'June', 'July',
                                                                                                      'Aug',
                                                                                                      'Sept', 'Oct',
                                                                                                      'Nov',
                                                                                                      'Dec'))
        for year in range(int(start_year), int(end_year) + 1):
            file.write(
                '{:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} \n'.format(year,
                                                                                             monthly_permits[year][0],
                                                                                             monthly_permits[year][1],
                                                                                             monthly_permits[year][2],
                                                                                             monthly_permits[year][3],
                                                                                             monthly_permits[year][4],
                                                                                             monthly_permits[year][5],
                                                                                             monthly_permits[year][6],
                                                                                             monthly_permits[year][7],
                                                                                             monthly_permits[year][8],
                                                                                             monthly_permits[year][9],
                                                                                             monthly_permits[year][10],
                                                                                             monthly_permits[year][11]))
        file.close()

    global count, monthly_permits

    count = 0
    monthly_permits = {}

    while not os.path.exists(os.path.join(os.getcwd(), 'Web_Permits_View.txt')):
        print("Error: Unable to locate 'Web_Permits_View.txt' file.")
        input("Please make sure your data file is in the program folder and named properly, then press enter.")
    write_data_1('Filtered Single-Family Permits.txt')
    write_data_2('Single-Family Permits Count.txt')
    for path in ['Filtered Single-Family Permits.txt', 'Single-Family Permits Count.txt']:
        new_path = os.path.join(os.environ['HOMEPATH'], 'Desktop')
        new_path = os.path.join(new_path, 'Data Quarry')
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        new_path = os.path.join(new_path, path)
        try:
            os.rename(path, new_path)
        except FileExistsError:
            os.remove(new_path)
            os.rename(path, new_path)

    print('Finished! Your new files are in your data quarry on your desktop!')
    input("Please click close to exit, or press enter")


# The function below is specifically for Volusia County Home Sales Data

def home_sales_processing ():
    # This function filters the input data from file
    def filter_data(filename):
        global monthly_sales, count, start_year, end_year, start_month
        # First, we take user inputted criteria to filter the data on
        # User inputted range of years to filter data.
        valid_years = False
        while not valid_years:
            start_year, end_year = input('Filter data from (year): '), input('to (year): ')
            try:
                int(end_year) and int(start_year)
            except:
                print('Invalid year!')
                continue
            if int(end_year) > 2018 or int(start_year) > 2018:
                print('Invalid year!')
            elif len(end_year) != 4 or len(start_year) != 4:
                print('Invalid year!')
            else:
                valid_years = True
        # User inputted start month for the start year specified above
        valid_month = False
        while not valid_month:
            start_month = input('Filter data from {} starting in month (mm):'.format(start_year))
            start_month = start_month.strip()
            try:
                int(start_month)
            except:
                print('Invalid month!')
                continue
            if int(start_month) < 1 or int(start_month) > 12:
                print('Invalid month!')
                continue
            else:
                valid_month = True
        # User inputted threshold sale price of homes
        valid_price = False
        while not valid_price:
            threshold_price = input('Enter minimum sale price of home sales you want to find (enter 0 if no minimum): ')
            try:
                int(threshold_price)
            except:
                print('Invalid price!')
                continue
            if int(threshold_price) < 0:
                print('Invalid price!')
                continue
            else:
                valid_price = True
        #if start_year[3] == '0':
        #    start_year = start_year[2:4]
        #else:
        #    start_year = start_year[2:4].strip('0')
        #end_year = end_year[2:4].strip('0')
        #print(start_year, end_year)

        # This little bit is using a secondary data file to grab the altkeys of all valid homes on the working tax roll
        temp_file = open('VCPA_CAMA_RES_BLDG.txt', 'r')
        temp_data = temp_file.readlines()
        home_keys = []
        for line in temp_data:
            new_line = line.split(',')
            home_keys.append(new_line[0][0:7])
        temp_file.close()


        # Open home sales file
        file = open(filename, 'r')
        # Creating table for monthly sales count for each year in range
        for year in range(int(start_year), int(end_year) + 1):
            monthly_sales[year] = []
            for month in range(1, 13):
                monthly_sales[year].append(0)
        data = file.readlines()
        refined_data = []
        qualify = ['Q', '01', '02']  # These are codes that qualify sales as real home sales in the database
        print('Processing...')
        for line in data: # Iterating over each line in the data
            new_line = line.strip().split(',') # Splitting lines by the delimiter ','
            if new_line[2] == '':
                print(new_line)
                quit()
                continue
            else:
                # Stripping off extra quotations on data
                for index in range(0, 13):
                    new_line[index] = new_line[index].strip('"')
                # Assigning variables to important data criteria
                alt_key, sale_month, sale_year, sale_instrumt, sale_qualify, sale_price, sale_date = new_line[0][0:7], int(new_line[2][0:new_line[2].find('/')]), int(new_line[2][new_line[2].find(' ') - 4:new_line[2].find(' ')]), new_line[6], new_line[10], new_line[8], new_line[2]
                # Filtering data on criteria
                if sale_year in range(int(start_year) + 1, int(end_year) + 1):
                    if alt_key in home_keys:
                        if sale_qualify in qualify:
                            if sale_instrumt == 'WD':
                                if float(sale_price) >= int(threshold_price):
                                    monthly_sales[sale_year][sale_month - 1] += 1
                                    count += 1
                                    print(count)
                                    refined_data.append(new_line)
                elif sale_year == int(start_year):
                    if alt_key in home_keys:
                        if sale_month >= int(start_month):
                            if sale_qualify in qualify:
                                if sale_instrumt == 'WD':
                                    if float(sale_price) >= int(threshold_price):
                                        monthly_sales[sale_year][sale_month - 1] += 1
                                        count += 1
                                        print(count)
                                        refined_data.append(new_line)
        file.close()
        print('Done Processing!')
        return (refined_data)

    def write_data_1(filename):
        global old_file, data
        file = open(filename, 'w')
        data = filter_data('VCPA_CAMA_SALES.txt')
        global count
        print('Writing...')
        file.write("ALT_KEY,SALE_MONTH,SALE_YEAR,SALE_INSTRUMT,SALE_QUALIFY,SALES_PRICE,SALE_DATE\n")
        for line in data:
            string = line[0]
            for element in range(1, 9):
                string = string + ',' + str(line[element])
            string = string + '\n'
            file.write(string)
        file.close()

    def write_data_2(filename):
        file = open(filename, 'w')
        file.write('Number of home sales: {} \n'.format(count))
        file.write('{:>4} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4}\n'.format('Year', 'Jan',
                                                                                                      'Feb',
                                                                                                      'Mar', 'Apr',
                                                                                                      'May',
                                                                                                      'June', 'July',
                                                                                                      'Aug',
                                                                                                      'Sept', 'Oct',
                                                                                                      'Nov',
                                                                                                      'Dec'))
        for year in range(int(start_year), int(end_year) + 1):
            file.write('{:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}\n'.format(year,
                                                                                             monthly_sales[year][0],
                                                                                             monthly_sales[year][1],
                                                                                             monthly_sales[year][2],
                                                                                             monthly_sales[year][3],
                                                                                             monthly_sales[year][4],
                                                                                             monthly_sales[year][5],
                                                                                             monthly_sales[year][6],
                                                                                             monthly_sales[year][7],
                                                                                             monthly_sales[year][8],
                                                                                             monthly_sales[year][9],
                                                                                             monthly_sales[year][10],
                                                                                             monthly_sales[year][11]))
        file.close()

    def write_data_3(filename):
        file = open(filename, 'w')
        file.write('Number of home sales found: {} \n'.format(count))
        file.write('{:10} {:10}\n'.format('Alt Key', 'Sale Price'))
        for line in data:
            file.write('{:10} ${:10}\n'.format(line[0], line[6]))
        file.close()

    global count, monthly_sales

    count = 0
    monthly_sales = {}

    while not os.path.exists(os.path.join(os.getcwd(), 'VCPA_CAMA_SALES.txt')):
        print("Error: Unable to locate 'Web_Sales_View.txt' file.")
        input("Please make sure your data file is in the program folder and named properly, then press enter.")
    write_data_1('Filtered Home Sales.txt')
    write_data_2('Home Sales Count.txt')
    write_data_3('Alt Keys.txt')
    for path in ['Filtered Home Sales.txt', 'Home Sales Count.txt', 'Alt Keys.txt']:
        new_path = os.path.join(os.environ['HOMEPATH'], 'Desktop')
        new_path = os.path.join(new_path, 'Data Quarry')
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        new_path = os.path.join(new_path, path)
        try:
            os.rename(path, new_path)
        except FileExistsError:
            os.remove(new_path)
            os.rename(path, new_path)

    print('Finished! Your new files are in your data quarry on your desktop!')
    input("Please click close to exit, or press enter")


print('This program filters two types of data: Home Sales or Permits. These data files are massive and date back to\n'
      'the 1950s. Only a few types of entries in these data files qualify as real home sales or real home permits.\n'
      'Copies of these two types of unfiltered data files are included in this folder, so you can view them to see \n'
      'the full, unfiltered files. They are called: Web_Sales_View.txt and Web_Permits_View.txt\n'
      'This program creates two new files, one with filtered data (either Home Sales or Permits) and one with a \n'
      'count of qualified data entries found.\n'
      "The new files are placed in a newly created folder called 'Data Quarry' on your desktop.\n"
      '\n'
      'The data is filtered on parameters that find only real home sales and real home permits.\n'
      "Don't forget to view the produced files in the 'Data Quarry' on your desktop!")

input('Press enter to begin a test of my program! (This one may take a few seconds to process)')
print('-------------------------------------------------------------------------------------------------------------\n')

valid = False
while valid == False:
    data_type = input('What data are you wanting to filter/update? (Home Sales, Permits): ')
    if data_type.lower() == 'permits':
        valid = True
        permits_processing()
    elif data_type.lower() == 'home sales':
        valid = True
        home_sales_processing()
    else:
        print('Invalid data option!')

