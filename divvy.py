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
					if mat_dist[i, j] and mat_time[i, j]:
						self.__addEdge(i, j, mat_dist[i, j], mat_time[i, j])

	# main function that finds the shortest path from src to all other vertices
	# return distance and parent list
	def Divvy_GJLS(self, src, end):
		

