from collections import defaultdict, Counter
users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]
interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
#print(interests)
# to find users with the same interest
def data_scientists_who_like(target_interest):
	'''Find the ids of all users who like the target interest'''
	return [user_id for user_id, user_interest in interests if user_interest==target_interest]
print('user id who showed interest in Big data : ', data_scientists_who_like('Big Data'))

# Key interests, values are listed user_ids, with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
	user_ids_by_interest[interest].append(user_id)

#print('Users by interest : ', user_ids_by_interest)

## keys are user ids, values are lists of interests for the user id
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
	interests_by_user_id[user_id].append(interest)
#print('Interest by user ID : ',  interests_by_user_id)
'''Who hs the most common interest'''
def most_common_interests_with(user):
	return Counter(interested_user_id for interest in interests_by_user_id[user['id']] 
		for interested_user_id in user_ids_by_interest[interest] if interested_user_id!=user['id'])
# For example
print(most_common_interests_with(users[0]))