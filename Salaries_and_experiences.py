import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict, OrderedDict
salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7),
(76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
(48000, 1.9), (63000,4.2)]
# If you want to see the scatter plot, uncomment the following lines of codes
# salaries_and_tenures_arr = np.asarray(salaries_and_tenures)
# plt.scatter(salaries_and_tenures_arr[:,1], salaries_and_tenures_arr[:,0], color = 'r')
# plt.xlabel('Years Experience')
# plt.ylabel('Salary')
# plt.title('Salary by Years Experience')
# plt.show()

## Keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
	salary_by_tenure[tenure].append(salary)
# Keys are years, each value is average salary for that tenure
average_salary_by_tenure =  {tenure: sum(salaries) / len(salaries) for tenure, salaries in salary_by_tenure.items()}

print('AVerage Salary by Tenure : ', OrderedDict(sorted(average_salary_by_tenure.items())))

'''Bucket the tenures'''
def tenure_bucket(tenure):
	if tenure < 2:
		return "less than two"
	elif tenure < 5:
		return "between two and five"
	else: 
		return "more than five"
# Key are tenure buckets, values are list of salaries to each bucket
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
	bucket = tenure_bucket(tenure)
	salary_by_tenure_bucket[bucket].append(salary)
print('Salary by tenure bucket : ', salary_by_tenure_bucket)

# compute the average
salary_by_tenure_bucket = {tenure_bucket : sum(salaries) / len(salaries) 
for tenure_bucket, salaries in salary_by_tenure_bucket.items()}
print('Salaries by tenure bucket : ', salary_by_tenure_bucket) 