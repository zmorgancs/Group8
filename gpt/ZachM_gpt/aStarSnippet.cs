// Code snippet obtained from this public repo: https://github.com/LostTrainDude/astar-pathfinding-unity/blob/master/Assets/Scripts/AStar.cs
using System.Collections.Generic;
using Priority_Queue;
using UnityEngine;

/// <summary>
/// Implementation of Amit Patel's A* Pathfinding algorithm studies
/// https://www.redblobgames.com/pathfinding/a-star/introduction.html
/// </summary>
public static class AStar
{
    /// <summary>
    /// Finds the best path from start to goal on the given graph.
    /// </summary>
    /// <param name="graph">The graph to search.</param>
    /// <param name="start">The starting node.</param>
    /// <param name="goal">The goal node.</param>
    /// <returns>The best path from start to goal.</returns>
    public static List<Node> FindPath(GridGraph graph, Node start, Node goal)
    {
        // Dictionary to store the parent nodes for each node in the path.
        Dictionary<Node, Node> parentNodes = new Dictionary<Node, Node>();
        
        // Dictionary to store the cost to reach each node from the start node.
        Dictionary<Node, float> costToReach = new Dictionary<Node, float>();

        // List to store the final path.
        List<Node> path = new List<Node>();

        // Priority queue to store nodes to be explored, with their priorities.
        SimplePriorityQueue<Node> frontier = new SimplePriorityQueue<Node>();

        // Enqueue the start node with a priority of 0.
        frontier.Enqueue(start, 0);

        // Initialize the start node's parent and cost to reach.
        parentNodes[start] = start;
        costToReach[start] = 0;

        // Loop until there are nodes to explore.
        Node current = new Node(0, 0);
        while (frontier.Count > 0)
        {
            // Dequeue the node with the lowest priority.
            current = frontier.Dequeue();

            // If the current node is the goal, exit the loop.
            if (current == goal)
                break;

            // Explore the neighbors of the current node.
            foreach (Node next in graph.GetNeighbors(current))
            {
                // Calculate the new cost to reach the neighbor.
                float newCost = costToReach[current] + graph.GetCost(current, next);

                // If the neighbor hasn't been visited or the new cost is lower than the previous cost,
                // update its parent and cost, and enqueue it with a priority based on the total cost.
                if (!costToReach.ContainsKey(next) || newCost < costToReach[next])
                {
                    costToReach[next] = newCost;
                    parentNodes[next] = current;
                    float priority = newCost + Heuristic(next, goal);
                    frontier.Enqueue(next, priority);
                }
            }
        }

        // If the goal is unreachable, log an error and return an empty path.
        if (current != goal)
        {
            Debug.LogError("Goal is unreachable!");
            return path;
        }

        // Reconstruct the path from the goal node to the start node.
        while (current != start)
        {
            path.Insert(0, current); // Insert the current node at the beginning of the path.
            current = parentNodes[current]; // Move to the parent node.
        }
        path.Insert(0, start); // Insert the start node at the beginning of the path.

        return path;
    }

    /// <summary>
    /// Calculates the Manhattan distance heuristic between two nodes.
    /// </summary>
    /// <param name="a">The first node.</param>
    /// <param name="b">The second node.</param>
    /// <returns>The Manhattan distance between the two nodes.</returns>
    public static float Heuristic(Node a, Node b)
    {
        // Calculate the Manhattan distance between the two nodes.
        return Mathf.Abs(a.Position.x - b.Position.x) + Mathf.Abs(a.Position.y - b.Position.y);
    }
}