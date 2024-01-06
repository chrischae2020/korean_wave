import sqlite3

import numpy as np
import scipy.stats as stats

# Connect to the database
conn = sqlite3.connect('/Users/anishansupradhan/Desktop/DataScience/final-project-the-korean-wave/data/kpop.db')

###### FOR HYPOTHESIS #1 ######
# Get the data for boy groups and girl groups
boy_groups = conn.execute('SELECT views FROM boy_mvs WHERE views IS NOT NULL').fetchall()
girl_groups = conn.execute('SELECT views FROM girl_mvs WHERE views IS NOT NULL').fetchall()

# Convert the data to NumPy arrays
boy_views = np.array(boy_groups)
girl_views = np.array(girl_groups)

# Conduct the t-test
tstats, pvalue = stats.ttest_ind(boy_views, girl_views, equal_var=True)

# Print the results
print("T-statistics: ", tstats)
print("P-value: ", pvalue)

# Interpretation
if pvalue < 0.05:
  print('The hypothesis #1 results are statistically significant.')
else:
  print('The hypothesis #1 results are not statistically significant.')


###### FOR HYPOTHESIS #2 ######
# Get the data for views and percent_english (associaton between views and percent_english => Maybe Chi squared test?)
views, percent_english = zip(*conn.execute('SELECT views, percent_english FROM mvs where views IS NOT NULL and percent_english is NOT NULL').fetchall())

# Convert the data to NumPy arrays
views = np.array(views)
percent_english = np.array(percent_english)

# Conduct the correlation test - Need to be checked
correlation, pvalue = stats.pearsonr(views, percent_english)

# Print the results
print("Correlation coefficient: ", correlation)
print("P-value: ", pvalue)

# Interpretation
if pvalue < 0.05:
  print('The hypothesis #2 results are statistically significant.')
else:
  print('The hypothesis #2 results are not statistically significant.')




###### FOR HYPOTHESIS #3 ######
# Conduct the independent two sample t-test
date, views_before =  zip(*conn.execute('SELECT release_date, views FROM mvs  where views IS NOT NULL AND release_date < "2010-01-01"').fetchall())
date2, views_after =  zip(*conn.execute('SELECT release_date, views FROM mvs  where views IS NOT NULL AND release_date > "2010-01-01"').fetchall())

views_before = np.array(views_before)
views_after = np.array(views_after)
correlation, pvalue = stats.ttest_ind(views_before, views_after)

# Print the results
print("T-statistics:: ", correlation)
print("P-value: ", pvalue)


# Interpretation
if pvalue < 0.05:
  print('The hypothesis #3 results are statistically significant.')
else:
  print('The hypothesis #3 results are not statistically significant.')


###### FOR HYPOTHESIS #4 ######
# Conduct the independent two sample t-test
views_boyg =  conn.execute('SELECT views FROM boy_mvs WHERE views NOT NULL').fetchall()
views_girlg =  conn.execute('SELECT views FROM girl_mvs WHERE views NOT NULL').fetchall()
views_solo =  conn.execute('SELECT views FROM solo_mvs WHERE views NOT NULL').fetchall()

views_group = [i[0] for i in views_boyg] + [i[0] for i in views_girlg]
views_solo = [i[0] for i in views_solo]
views_group = np.array(views_group)
views_solo = np.array(views_solo)
correlation, pvalue = stats.ttest_ind(views_group, views_solo)

# Print the results
print("T-statistics:: ", correlation)
print("P-value: ", pvalue)


# Interpretation
if pvalue < 0.05:
  print('The hypothesis #4 results are statistically significant.')
else:
  print('The hypothesis #4 results are not statistically significant.')


# Close the connection to the database
conn.close()