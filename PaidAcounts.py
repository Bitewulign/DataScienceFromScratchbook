from collections import defaultdict, OrderedDict


def predict_paid_or_unpaid(years_experience):
	if years_experience < 3.0:
		return 'Paid'
	elif years_experience < 8.5:
		return 'Unpaid'
	else:
		return 'Paid'
salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7),
(76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
(48000, 1.9), (63000,4.2)]

Paid_or_Unpaid = defaultdict(list)

for salary, experience in salaries_and_tenures:
	predict_PU = predict_paid_or_unpaid(experience)
	Paid_or_Unpaid[experience].append(predict_PU)
print('Paid or unpaid? ', OrderedDict(sorted(Paid_or_Unpaid.items())))
