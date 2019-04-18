import numpy as np
import csv

""" 
Class to represent graph

Arguments:
	num_vertices: number of vertices
	mat: A matrix, [i, j] is the distance from vertex i to vertex j
"""
class Graph_global:
	def __init__(self, num_vertices, mat, compare_mat):
		self.V = num_vertices # number of vertices
		self.graph = []
		self.mat = mat
		self.compare_mat = compare_mat
		self.__create_graph()
	

	# Add edge to the graph
	def __addEdge(self, u, v, w):
		self.graph.append((u, v, w))

	# create the graph
	def __create_graph(self):
		for i in range(self.mat.shape[0]):
			for j in range(self.mat.shape[1]):
				# avoid adding loop (edge from one vertex to itself)
				if(i != j):
					# avoid adding edge not existing
					if(~np.isnan(self.mat[i, j])):
						self.__addEdge(i, j, self.mat[i, j])

	"""
	function to display the path and distance from a starting station to a destination station
	Arguments:
		starting: index of the starting vertex
		ending: index of the ending vertex
	Returns:
		: shortest distance from starting to ending
		: shortest path in list style
	"""
	def show_path_dist(self, starting, ending):
		dist, parent = self.BellmanFord(starting)
		if(dist[ending] == float("Inf")):
			return [], float("Inf"), float("Inf")
		else:
			path = []
			path.append(ending)
			current = ending
			while(parent[current] != "NIL"):
				path.append(parent[current])
				current = parent[current]
			path.reverse()
			
			# calculate another one (time / distance)
			compare_dist = 0
			for i in range(len(path) - 1):
				if(np.isnan(self.compare_mat[path[i], path[i+1]])):
					compare_dist = float("Inf")
					break
				compare_dist += self.compare_mat[path[i], path[i+1]]

			return path, dist[ending], compare_dist
			# if(path[-1] == starting):
			# 	path.reverse()
			# 	return path
			pass

	# main function that finds the shortest path from src to all other vertices using Bellman-Ford algorithm
	# return distance list and parent list
	# Notice: in our problem, there is no negative weight for edge, so we do not check if there is a negative cycle in the graph
	def BellmanFord(self, src):
		dist = [float("Inf")] * self.V
		dist[src] = 0
		# initialize a list to record the parent of a vertex in the shortest path
		parent = ["NIL"] * self.V
		for i in range(self.V - 1):
			for u, v, w in self.graph:
				if(dist[u] != float("Inf") and (dist[u] + w)<dist[v]):
					dist[v] = dist[u] + w
					parent[v] = u
		return dist, parent




if __name__ == "__main__":
	np.random.seed(2)
	mat = np.random.normal(10, 3, size=(6, 6))
	g = Graph_global(6, mat)
	dist, parent = g.BellmanFord(0)
	print("orignial mat")
	print(mat)
	print("shortest distance from 0")
	print(dist)
	s_p, d, comp_d = g.show_path_dist(0, 3)
	print("shortest path and distance from 0 to 3")
	print(s_p, d, comp_d)
