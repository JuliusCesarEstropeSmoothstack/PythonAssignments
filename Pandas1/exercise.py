import pandas as pd

df = pd.read_csv('2_pandas_Salaries.csv')

print(df)

# Question 1
print('Headers:')
print(df.head())

# Question 2
print('Info:')
print(df.info())

# Question 3
print('Average of first 10000 in BasePay:')
print(df['BasePay'][:10001].mean())

# Question 4
print('Highest Value in TotalPayBenefits')
print(df['TotalPayBenefits'].max())

# Question 5
print('Job Title of JOSEPH DRISCOLL')
print(df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

# Question 6
joseph_df = df[df['EmployeeName'] == 'JOSEPH DRISCOLL']
print('Earnings of JOSEPH DRISCOLL')
print(joseph_df['BasePay'] + joseph_df['TotalPayBenefits'])

# Question 7
df['TotalPay'] = df['BasePay'] + df['TotalPayBenefits']
print('Highest Paid Employee Including Benefits:')
print(df[df['TotalPay'] == df['TotalPay'].max()]['EmployeeName'])

# Question 8
df['TotalPay'] = df['BasePay'] + df['TotalPayBenefits']
print('Lowest Paid Employee Including Benefits:')
print(df[df['TotalPay'] == df['TotalPay'].min()][['EmployeeName', 'BasePay', 'TotalPayBenefits']])  # Negative benefits

# Question 9
print('Mean TotalPay per Year:')
print(df.groupby('Year').mean()['TotalPay'])

# Question 10
print('Unique Job Titles:')
print(len(df['JobTitle'].unique()))

# Question 11
print('Top 7 Most Common Jobs:')
print(df['JobTitle'].value_counts()[:7])

# Question 12
print('Number of Job Titles with 1 occurrence in 2013:')
print(len(df[df['Year'] == 2013]['JobTitle'].unique()))

# Question 13
df['Chief'] = df['JobTitle'].str.extract(r'(Chief)')
print("Number of people with 'Chief' in their job title")
print(len(df[df['Chief'] == 'Chief']))

# Question 14
print('Is there a correlation between JobTitle length and Salary?')
print(df[['TotalPay', 'JobTitle']].corr())
