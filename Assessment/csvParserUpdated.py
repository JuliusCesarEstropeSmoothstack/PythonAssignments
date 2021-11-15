import logging
from openpyxl import load_workbook
from openpyxl.utils.cell import coordinate_from_string
from month_enum import Month
from Assessment import csvUtils

logging.basicConfig(level=logging.INFO, filename='csvParserLog.log')

validInput = False
while not validInput:

    workbookName = input('Enter the file name')

    try:

        workbook = load_workbook(workbookName)  # Attempt to load the workbook, throws FileExistsError if it doesn't

        logging.info(f'Attempting to parse {workbookName} for a month and year in filename')
        month = workbookName.split('_')[3]
        year = workbookName.split('_')[4].replace('.xlsx', '')

        monthNumber = Month[month].value  # convert month string into number using Month enum

        logging.info(f'Successfully parsed inputname for month and year: {month}, {year}')
        validInput = True
    except FileExistsError:
        message = f'Workbook {workbookName} does not exist. Enter a different name.'
        logging.fatal(message)
        print(message)
    except IndexError:
        message = "Failed to parse a month and year from the inputname. '_' not properly used. Retry."
        logging.warning(message)
        print(message)
    except ValueError:
        message = f'{month} could not be parsed as a month. Please format as lowercase full month name.'
        logging.warning(message)
        print(message)

try:
    sheetName = 'Summary Rolling MoM'  # grab sheet by name rather than the active sheet
    sheet = workbook[sheetName]

    # Attempt to find a cell with the corresponding year, knowing date-time format is: YYyy-MM-DD
    targetRegex = f"{year}-{monthNumber if monthNumber > 9 else f'0{monthNumber}'}"
    foundCell = csvUtils.find_in_column(sheet, 'A', targetRegex, False, 2, 13)

    if foundCell is None:  # unable to find specified month-year within specified rows of the sheet
        message = f'failed to find {Month(monthNumber)} {year} in column A of {workbookName}'
        logging.fatal(message)
        print(message)
        exit(-1)
    else:  # found the specified month-year, log and print out cell contents
        row = coordinate_from_string(foundCell)[1]  # extract numeral part of cell coordinate
        output = f"Calls offered: {sheet[f'B{row}'].value}"
        output += f"\n\tAbandon after 30s: {format(sheet[f'C{row}'].value * 100, '0.2f')}%"
        output += f"\n\tFCR: {format(sheet[f'D{row}'].value * 100, '0.2f')}%"
        output += f"\n\tDSAT: {format(sheet[f'E{row}'].value * 100, '0.2f')}%"
        output += f"\n\tCSAT: {format(sheet[f'F{row}'].value * 100, '0.2f')}%"
        logging.info(output)
        print(output)
except KeyError:
    message = f'{sheetName} not found in workbook {workbookName}. Skipping.'
    logging.warning(message)
    print(message)

try:
    sheetName = "VOC Rolling MoM"
    sheet = workbook[sheetName]

    # Attempt to find a cell with the corresponding year, knowing date-time format is: YYyy-MM-DD
    # Also allows use of full month name
    targetRegex = f"{year}-{monthNumber if monthNumber > 9 else f'0{monthNumber}'}|{month.lower()}"
    foundCell = csvUtils.find_in_row(sheet, 1, targetRegex, False, 2, 13)

    if foundCell is None:  # unable to find specified month-year within the specified columns of the sheet
        message = f'failed to find {Month(monthNumber)} {year} in row 1 of {workbookName}'
        logging.fatal(message)
        print(message)
        exit(-1)
    else:  # found the specified month-year, log and print out cell contents
        # Promoters is on row 4
        columnLetter = coordinate_from_string(foundCell)[0]  # extract alphabetic part of cell coordinate
        output = 'In Net Promoter Score : '
        output += f"\n\tPromoters { '>= 200 : good' if sheet[f'{columnLetter}4'].value >= 200 else '< 200 : bad'}"
        # Passives is on row 6
        output += f"\n\tPassives { '>= 200 : good' if sheet[f'{columnLetter}6'].value >= 100 else '< 100 : bad'}"
        # Detractors is on row 8
        output += f"\n\tDetractors { '>= 200 : good' if sheet[f'{columnLetter}8'].value >= 100 else '< 100 : bad'}"
        logging.info(output)
        print(output)
except KeyError:
    message = f'{sheetName} not found in workbook {workbookName}'
    logging.warning(message)
    print(message)
