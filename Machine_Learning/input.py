import numpy as np
import pandas as pd

borrowers = ["A", "B", "C", "D", "E"]
lenders = ["L1", "L2", "L3", "L4", "L5"]

data_matrix = np.zeros((len(lenders),len(borrowers)))

while True:
	print("Please select one user: ")
	print(lenders)
	k = input()
	if k == "exit":
		break
	for i in range(0,len(lenders)):
		if lenders[i] == k:
			break
	while True:
		print("Please select one borrowers: ")
		print(borrowers)
		p = input()
		if p == "exit":
			break
		for m in range(0,len(borrowers)):
			if borrowers[m] == p:
				break
		print("Please input your rating")
		rate = int(input())
		data_matrix[i][m] = rate

for i in data_matrix:
	print(i)

from sklearn.metrics.pairwise import pairwise_distances
user_similarity = pairwise_distances(data_matrix, metric='cosine')
item_similarity = pairwise_distances(data_matrix.T, metric='cosine')

def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        #You use np.newaxis so that mean_user_rating has same format as ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
    return pred

item_prediction = predict(data_matrix, item_similarity, type='item')
user_prediction = predict(data_matrix, user_similarity, type='user')

print(user_prediction)
