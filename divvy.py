import numpy as np
import csv

""" 
Class to represent graph

Arguments:
	num_vertices: number of vertices
	mat_dist: A matrix, [i, j] is the distance from vertex i to vertex j
	mat_time: A matrix, [i, j] is the travel time from vertex i to vertex j
"""
class Graph_Divvy:
	def __init__(self, num_vertices, mat_time, mat_dist):
		self.V = num_vertices # number of vertices
		self.graph = []
		self.mat_dist = mat_dist
		self.mat_time = mat_time
		self.__create_graph()

	# Add edge to the graph
	def __addEdge(self, u, v, d, t):
		self.graph.append((u, v, d, t))

	# create the graph
	def __create_graph(self):
		assert self.mat_dist.shape == self.mat_time.shape, "Time matrix and distance matrix should have the same shape"
		# assert self.mat_dist.shape[0] == self.mat_dist.shape[1], "Matrix should be square matrix"
		# n = self.mat_dist.shape[0]
		for i in range(self.mat_dist.shape[0]):
			for j in range(self.mat_dist.shape[1]):
				# avoid adding loop (edge from one vertex to itself)
				if(i != j):
					# avoid adding edge not existing
					if(~np.isnan(mat_dist[i, j]) and ~np.isnan(mat_time[i, j])):
						self.__addEdge(i, j, mat_dist[i, j], mat_time[i, j])

	# main function that finds the shortest path from src to all other vertices
	# return distance and parent list
	def Divvy_GJLS(self, src, end, time_span=30):
		pass

	def next_vertex(self, start, end, time_span=30):
		in_30_list = []
		# distance from every vertex to the end vertex
		current_dist_vec = self.mat_dist[:, end]
		# time from start to every vertex
		current_time_vec = self.mat_time[start, :]

		# assume that time is represented by minutes

		# first check if the end vertex can be reached in 30 minutes from start
		if(current_time_vec[end] <= 30):
			return start, end

		for v in range(len(current_time_vec)):
			if(v != start and current_time_vec[v] <= time_span):
				in_30_list.append(v)

		# find the nearest station to the end
		dist_vec = [current_dist_vec[x] for x in in_30_list]
		# consider if more than 1 vertices are nearest to the end
		other_v = []
		min_dist = dist_vec[0]
		next_v = in_30_list[0]
		for i in range(1, len(dist_vec)):
			if(dist_vec[i] == min_dist):
				other_v.append(in_30_list[i])
			elif(dist_vec[i] < min_dist):
				min_dist = dist_vec[i]
				next_v = in_30_list[i]
				other_v = []
			else:
				continue
		if not other_v:
			return start, next_v
		else:
			other_v.append(next_v)
			other_time = [current_time_vec[x] for x in other_v]
			next_v = other_v[other_time.index(max(other_time))]
			return start, next_v

		# # if the start vertex is the nearest one to the end, go stright from start to the end
		# if(current_dist_vec[start] <= min(dist_vec)):
		# 	return start, None

		# next_v = in_30_list[dist_vec.index(min(dist_vec))]
		# consider the vertices which have the same distances to the end
		# next_v = start
		# min_dist = current_dist_vec[start]
		# other_v = []
		# for i in range(len(dist_vec)):
		# 	if(dist_vec[i] == min_dist):
		# 		other_v.append(i)
		# 	elif(dist_vec[i] < min_dist):
		# 		min_dist = dist_vec[i]
		# 		next_v = in_30_list[i]
		# 		other_v = []
		# 	else:
		# 		continue
		# # handle the case that more than 1 vertices are nearest to the end
		# if not other_v:
		# 	other_v.append(next_v)
		# 	other_time = [current_time_vec[x] for x in other_v]
		# 	return start,other_v[other_time.index(max(other_time))]
		# else:
		# 	return start, next_v