# AAP-Data-Project
This is a data analysis program meant to be fed Volusia County home sales and permits data.
This was created by Logan Welsh in 2017.
Since initial development, the format of the input data files has changed, so updates may be necessary.

This program accepts data CSV files of two types: Home Sales or Construction Permits.
Current data files of this type can be downloaded here: http://vcpa.vcgov.org/database.html
Data files must be placed in the same PATH as the source code.
CSV files must be named 'Web_Sales_View.txt' or 'Web_Permits_View.txt' for Home Sales or Permits,
  respectively.

This program outputs filtered data (Home Sales or Permits) to a new CSV file in a created 'Data Quarry'
  folder on the user's desktop. It also outputs a table containing the counted occurrences of wanted
  data for each month of each year in time interval.
  
Run the program with data files, named properly, and follow input prompts to choose data type, time 
  interval, and threshold price if home sales. Filter parameters are hard-coded.
