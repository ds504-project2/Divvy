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
	def __init__(self, num_vertices, mat_dist, mat_time):
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
					if(~np.isnan(self.mat_dist[i, j]) and ~np.isnan(self.mat_time[i, j])):
						self.__addEdge(i, j, self.mat_dist[i, j], self.mat_time[i, j])

	# main function that finds the shortest path from src to end
	# return path, distance list and time list
	def Divvy_GJLS(self, src, end, time_span=30):
		path_list = [src]
		dist_list = []
		time_list = []
		next_v = src
		while(next_v != end):
			next_v, next_dist, next_time = self.next_vertex(next_v, end, time_span=time_span)
			# print(next_v)

			# try to avoid going back and force or going in a circle
			# Is there a better way to handle this problem?
			# Following is just a naive method to avoid this situation
			if(next_v in path_list):
				circle_v_loc_idx = path_list.index(next_v)
				path_list = path_list[:circle_v_loc_idx+1]
				dist_list = dist_list[:circle_v_loc_idx]
				time_list = time_list[:circle_v_loc_idx]
				path_list.append(end)
				dist_list.append(self.mat_dist[next_v, end])
				time_list.append(self.mat_time[next_v, end])
				break
			
			path_list.append(next_v)
			dist_list.append(next_dist)
			time_list.append(next_time)
		return path_list, dist_list, time_list


	def next_vertex(self, start, end, time_span=30):
		in_30_list = []
		# distance from every vertex to the end vertex
		current_dist_vec = self.mat_dist[:, end]
		# time from start to every vertex
		current_time_vec = self.mat_time[start, :]

		# assume that time is represented by minutes

		# first check if the end vertex can be reached in 30 minutes from start
		if(current_time_vec[end] <= time_span):
			# return start, end
			return end, self.mat_dist[start, end], self.mat_time[start, end]

		for v in range(len(current_time_vec)):
			if(v != start and current_time_vec[v] <= time_span):
				in_30_list.append(v)

		# find the nearest station to the end
		dist_vec = [current_dist_vec[x] for x in in_30_list]
		# when all the other stations are not in 30-min circle, return the end station directly
		if not dist_vec:
			return end, self.mat_dist[start, end], self.mat_time[start, end]
		min_dist = dist_vec[0]
		next_v = in_30_list[0]
		# consider if more than 1 vertices are nearest to the end
		other_v = []
		for i in range(1, len(dist_vec)):
			if(dist_vec[i] == min_dist):
				other_v.append(in_30_list[i])
			elif(dist_vec[i] < min_dist):
				min_dist = dist_vec[i]
				next_v = in_30_list[i]
				other_v = []
			else:
				continue
		# if not other_v:
		# 	# return start, next_v
		# 	return next_v
		if other_v:
			other_v.append(next_v)
			other_time = [current_time_vec[x] for x in other_v]
			next_v = other_v[other_time.index(max(other_time))]
			# return start, next_v
		return next_v, self.mat_dist[start, next_v], self.mat_time[start, next_v]

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

if __name__ == "__main__":
	np.random.seed(2)
	d_m = np.random.normal(10, 3, size=(6, 6))
	t_m = np.random.normal(35, 10, size=(6, 6))
	g = Graph_Divvy(6, d_m, t_m)
	# next_v, d, t = g.next_vertex(0, 3)
	path_l, dist_l, time_l = g.Divvy_GJLS(0, 3, time_span=30)

	print("\ndistance mat")
	print(d_m)
	print("\ntime mat")
	print(t_m)
	# print("\nnext step from 0 to 3 (distance and time)")
	# print(next_v, d, t)
	print("\npath from 0 to 3 is")
	print(path_l)
	print("distance list is")
	print(dist_l)
	print("time list is")
	print(time_l)
