import sys
import numpy as np
import os

from global_optimal import Graph_global
from divvy import Graph_Divvy
from pipline import load_data

from itertools import permutations

# evaluation method:
# 1. calculate all the pairs of 2 stations (with order)
# 2. for each pair, calculate the related data according to divvy shortest path method
# 3. for each pair, calculate the shortest distance and corresponding time according to global method
# 4. for each pair, calculate the shortest time and corresponding distance according to global method
# 5. calculate the avg difference between GJLS and global method (both time and distacne)

TIME_MATRIX, DIST_MATRIX = load_data()

def all_pairs(num_vert):
	ls = list(range(num_vert))
	return list(permutations(ls, 2))

def evaluate(time_matrix, dist_matrix):
	num_vert = dist_matrix.shape[0]
	pair_ls = all_pairs(num_vert)
	num_pair = len(pair_ls)

	# create 3 graphs
	global_graph_dist = Graph_global(num_vert, dist_matrix, time_matrix)
	global_graph_time = Graph_global(num_vert, time_matrix, dist_matrix)
	divvy_graph = Graph_Divvy(num_vert, dist_matrix, time_matrix)

	# gd: global distance, gt: global time
	dv_gd_time_diff, dv_gd_dist_diff, dv_gt_time_diff, dv_gt_dist_diff = 0 

	# for debug
	counter = 0
	for pair in pair_ls:
		# for debug
		counter += 1
		print(counter)
		
		# GJLS
		_, dv_dist, dv_time = divvy_graph.Divvy_GJLS(pair[0], pair[1])
		# Global Dist, g_d_d is the shortest distance, g_d_t is the time according to shortest distance
		_, g_d_d, g_d_t = global_graph_dist.show_path_dist(pair[0], pair[1])
		# Global Time, 
		_, g_t_t, g_t_d = global_graph_time.show_path_dist(pair[0], pair[1])

		# Compare GJLS with global dist
		dv_gd_dist_diff += (sum(dv_dist) - g_d_d)
		dv_gd_time_diff += (sum(dv_time) - g_d_t)
		# Compare GJLS with global time
		dv_gt_dist_diff += (sum(dv_dist) - g_t_d)
		dv_gt_time_diff += (sum(dv_time) - g_t_t)

	# Avg
	dv_gd_time_diff, dv_gd_dist_diff, dv_gt_time_diff, dv_gt_dist_diff = dv_gd_time_diff/num_pair, dv_gd_dist_diff/num_pair, dv_gt_time_diff/num_pair, dv_gt_dist_diff/num_pair

	return dv_gd_time_diff, dv_gd_dist_diff, dv_gt_time_diff, dv_gt_dist_diff


if __name__ == "__main__":
	# pairs = all_pairs(3)
	# print(pairs)
	gd_time, gd_dist, gt_time, gt_dist = evaluate(TIME_MATRIX, DIST_MATRIX)
	print("\nCompare with global distance")
	print("Avg distance difference")
	print(gd_dist)
	print("Avg time difference")
	print(gd_time)
	print("\nCompare with global time")
	print("Avg distance difference")
	print(gt_dist)
	print("Avg time difference")
	print(gt_time)

