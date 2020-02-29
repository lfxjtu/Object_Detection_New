# import xlsxwriter module
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('car_detection_coordinates.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
worksheet.write(1, 0, 'ISBT DEHRADUN')
worksheet.write(2, 0, 'SHASTRADHARA')
worksheet.write(3, 0, 'CLEMEN TOWN')
worksheet.write(4, 0, 'RAJPUR ROAD')
worksheet.write(5, 0, 'CLOCK TOWER')
worksheet.write(0, 1, 'ISBT DEHRADUN')
worksheet.write(0, 2, 'SHASTRADHARA')
worksheet.write(0, 3, 'CLEMEN TOWN')
worksheet.write(0, 4, 'RAJPUR ROAD')
worksheet.write(0, 5, 'CLOCK TOWER')

# Finally, close the Excel file
# via the close() method.
workbook.close()