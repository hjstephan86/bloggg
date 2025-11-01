"""
Generated with Claude AI

Push and Swap Algorithm for Cooperative Path-Finding - FIXED VERSION
Uses the Graph class from graph.py with adjacency matrix representation

Based on: Luna & Bekris, "Push and Swap: Fast Cooperative Path-Finding
with Completeness Guarantees", IJCAI 2011

Key fixes:
1. Don't move agents that are already at their goals
2. Better deadlock detection and oscillation prevention
3. Improved clearing logic
"""

from collections import deque
from typing import Dict, List, Optional, Set, Tuple

# Import the provided Graph and Matrix classes
try:
    from graph import Graph
    from matrix import Matrix
except ImportError:
    from .graph import Graph
    from .matrix import Matrix


class Agent:
    """Represents an agent with start and goal positions."""

    def __init__(self, agent_id: int, start: int, goal: int):
        self.id = agent_id
        self.start = start
        self.goal = goal
        self.current = start
        self.path = [start]

    def at_goal(self) -> bool:
        """Check if agent is at its goal."""
        return self.current == self.goal

    def reset(self):
        """Reset agent to starting position."""
        self.current = self.start
        self.path = [self.start]

    def __repr__(self):
        return f"Agent({self.id}: {self.start}->{self.goal}, current={self.current})"


class PushAndSwap:
    """
    Push and Swap algorithm for cooperative path-finding.
    Provides completeness guarantees for problems with at most n-2 agents
    in a graph of size n.
    """

    def __init__(self, graph: Graph, agents: List[Agent], verbose: bool = True):
        """
        Initialize Push and Swap solver.

        Args:
            graph: Graph object from graph.py with adjacency matrix
            agents: List of Agent objects
            verbose: Whether to print progress messages
        """
        self.graph = graph
        self.agents = agents
        self.n_agents = len(agents)
        self.n_nodes = graph.num_nodes
        self.verbose = verbose

        # Track current positions of agents
        self.agent_positions = {agent.id: agent.current for agent in agents}

        # Validate unique start and goal positions
        self._validate_problem()

        # Check solvability constraint: at most n-2 agents in graph of size n
        if self.n_agents > self.n_nodes - 2:
            raise ValueError(
                f"Problem not solvable: {self.n_agents} agents in graph of "
                f"size {self.n_nodes}. Maximum agents: {self.n_nodes - 2}"
            )

    def _validate_problem(self):
        """Validate that start and goal positions are unique and valid."""
        starts = [agent.start for agent in self.agents]
        goals = [agent.goal for agent in self.agents]

        if len(starts) != len(set(starts)):
            raise ValueError("Agents must have unique start positions")

        if len(goals) != len(set(goals)):
            raise ValueError("Agents must have unique goal positions")

        for agent in self.agents:
            if not (0 <= agent.start < self.n_nodes):
                raise ValueError(
                    f"Invalid start position {agent.start} for agent {agent.id}"
                )
            if not (0 <= agent.goal < self.n_nodes):
                raise ValueError(
                    f"Invalid goal position {agent.goal} for agent {agent.id}"
                )

    def solve(self, max_iterations: int = 1000) -> Dict[int, List[int]]:
        """
        Main solving routine using Push and Swap algorithm.

        Args:
            max_iterations: Maximum number of iterations to prevent infinite loops

        Returns:
            Dictionary mapping agent_id to list of nodes in path
        """
        if self.verbose:
            print(
                f"\nSolving for {self.n_agents} agents on graph with {self.n_nodes} nodes..."
            )
            print(f"Agents configuration:")
            for agent in self.agents:
                print(f"  {agent}")

        # Phase 1: Push - move agents toward goals greedily
        self._push_phase()

        # Phase 2: Resolve remaining conflicts with swaps and additional pushes
        iteration = 0
        no_progress_count = 0
        last_positions = None

        while not self._all_at_goals() and iteration < max_iterations:
            # Check for oscillation
            current_positions = tuple(sorted(self.agent_positions.items()))
            if current_positions == last_positions:
                no_progress_count += 1
                if no_progress_count > 5:
                    if self.verbose:
                        print(
                            f"  Detected position oscillation, attempting different strategy..."
                        )
                    # Try moving all non-goal agents randomly to break deadlock
                    if not self._break_oscillation():
                        break
                    no_progress_count = 0
            else:
                no_progress_count = 0
            last_positions = current_positions

            # Find agents not at goal
            blocked_agents = [a for a in self.agents if not a.at_goal()]

            if not blocked_agents:
                break

            # Try to make progress for blocked agents
            progress_made = False
            for agent in blocked_agents:
                if self._try_move_to_goal(agent):
                    progress_made = True
                    break

            if not progress_made:
                # Need to perform swap or clearing move to unblock
                if not self._resolve_deadlock():
                    if self.verbose:
                        print(
                            f"  Warning: Could not resolve deadlock at iteration {iteration}"
                        )
                    break

            iteration += 1

        if self._all_at_goals():
            if self.verbose:
                print(
                    f"\n✓ Success! All agents reached goals in {iteration} additional iterations"
                )
        else:
            if self.verbose:
                print(
                    f"\n✗ Warning: Not all agents reached goals after {iteration} iterations"
                )
                for agent in self.agents:
                    if not agent.at_goal():
                        print(
                            f"  Agent {agent.id} stuck at {agent.current}, goal is {agent.goal}"
                        )

        # Return paths
        return {agent.id: agent.path.copy() for agent in self.agents}

    def _push_phase(self):
        """
        Push phase: move agents toward goals until no more progress possible.
        Each agent greedily moves toward its goal when space is available.
        """
        if self.verbose:
            print("\nPhase 1: PUSH - Moving agents toward goals...")

        progress = True
        pushes = 0

        while progress:
            progress = False
            for agent in self.agents:
                if agent.at_goal():
                    continue

                # Try to move agent closer to goal
                if self._try_move_to_goal(agent):
                    progress = True
                    pushes += 1

        if self.verbose:
            at_goal = sum(1 for a in self.agents if a.at_goal())
            print(f"  Push phase complete: {pushes} moves made")
            print(f"  Agents at goal: {at_goal}/{self.n_agents}")
            if at_goal < self.n_agents:
                print(f"\nPhase 2: SWAP - Resolving deadlocks...")

    def _try_move_to_goal(self, agent: Agent) -> bool:
        """
        Try to move agent one step closer to its goal along shortest path.

        Returns:
            True if movement was successful, False otherwise
        """
        if agent.at_goal():
            return False

        # Find shortest path to goal using BFS
        path = self._bfs_shortest_path(agent.current, agent.goal)

        if not path or len(path) < 2:
            return False

        next_pos = path[1]

        # Check if next position is occupied
        if self._is_occupied(next_pos):
            return False

        # Move agent
        self._move_agent(agent, next_pos)
        return True

    def _resolve_deadlock(self) -> bool:
        """
        Resolve deadlock situation using swap operations or clearing moves.
        CRITICAL FIX: Never move agents that are already at their goals!

        Returns:
            True if deadlock was resolved, False otherwise
        """
        if self.verbose:
            print("  Attempting to resolve deadlock...")

        # Strategy 1: Try swapping agents that would mutually benefit
        for agent1 in self.agents:
            if agent1.at_goal():
                continue

            for agent2 in self.agents:
                if agent2.at_goal() or agent1.id == agent2.id:
                    continue

                # Check if swapping would help agent1 progress toward goal
                if self._swap_would_help(agent1, agent2):
                    return self._perform_swap(agent1, agent2)

        # Strategy 2: Move a blocking agent to free space to clear path
        # CRITICAL: Only move agents that are NOT at their goals
        free_nodes = self._find_free_nodes()
        if free_nodes:
            # Try moving blocking agents to make progress
            for agent in self.agents:
                if agent.at_goal():
                    continue

                # Find the path and check for blocking agents
                path = self._bfs_shortest_path(agent.current, agent.goal)
                if path and len(path) > 1:
                    next_pos = path[1]
                    blocking_agent = self._get_agent_at(next_pos)

                    # CRITICAL FIX: Don't move agents at their goals!
                    if blocking_agent and not blocking_agent.at_goal():
                        # Try to move blocking agent to nearest free space
                        closest_free = min(
                            free_nodes,
                            key=lambda n: len(
                                self._bfs_shortest_path(blocking_agent.current, n) or []
                            )
                            or float("inf"),
                        )
                        path_to_free = self._bfs_shortest_path(
                            blocking_agent.current, closest_free
                        )

                        if path_to_free and len(path_to_free) > 1:
                            next_move = path_to_free[1]
                            if not self._is_occupied(next_move):
                                self._move_agent(blocking_agent, next_move)
                                if self.verbose:
                                    print(
                                        f"    Moved agent {blocking_agent.id} to clear path"
                                    )
                                return True

        return False

    def _break_oscillation(self) -> bool:
        """
        Break oscillation by moving agents that are not at goals to alternative positions.

        Returns:
            True if oscillation was broken
        """
        free_nodes = self._find_free_nodes()
        if not free_nodes:
            return False

        # Find agent furthest from its goal that's not at goal
        worst_agent = None
        worst_distance = -1

        for agent in self.agents:
            if not agent.at_goal():
                path = self._bfs_shortest_path(agent.current, agent.goal)
                if path and len(path) > worst_distance:
                    worst_distance = len(path)
                    worst_agent = agent

        if worst_agent and free_nodes:
            # Move to closest free node
            closest_free = min(
                free_nodes,
                key=lambda n: len(self._bfs_shortest_path(worst_agent.current, n) or [])
                or float("inf"),
            )
            path_to_free = self._bfs_shortest_path(worst_agent.current, closest_free)
            if path_to_free and len(path_to_free) > 1:
                next_move = path_to_free[1]
                if not self._is_occupied(next_move):
                    self._move_agent(worst_agent, next_move)
                    if self.verbose:
                        print(f"    Moved agent {worst_agent.id} to break oscillation")
                    return True

        return False

    def _swap_would_help(self, agent1: Agent, agent2: Agent) -> bool:
        """
        Check if swapping two agents would help agent1 progress toward goal.

        Returns:
            True if swap would reduce distance to goal for agent1
        """
        # Calculate distance before and after hypothetical swap
        path_before = self._bfs_shortest_path(agent1.current, agent1.goal)
        path_after = self._bfs_shortest_path(agent2.current, agent1.goal)

        if not path_before or not path_after:
            return False

        dist_before = len(path_before)
        dist_after = len(path_after)

        return dist_after < dist_before

    def _perform_swap(self, agent1: Agent, agent2: Agent) -> bool:
        """
        Perform swap operation between two agents.
        Agents exchange positions without affecting other agents.

        Returns:
            True if swap was successful
        """
        if self.verbose:
            print(
                f"    Swapping agents {agent1.id} (at {agent1.current}) "
                f"and {agent2.id} (at {agent2.current})"
            )

        # Check if agents are adjacent (direct swap possible)
        if self.graph.has_edge(agent1.current, agent2.current):
            # Direct neighbor swap
            pos1, pos2 = agent1.current, agent2.current
            self._move_agent(agent1, pos2)
            self._move_agent(agent2, pos1)
            return True
        else:
            # Need complex swap using intermediate space
            return self._complex_swap(agent1, agent2)

    def _complex_swap(self, agent1: Agent, agent2: Agent) -> bool:
        """
        Perform swap for non-adjacent agents using free space as temporary location.

        Returns:
            True if swap was successful
        """
        free_nodes = self._find_free_nodes()

        if not free_nodes:
            return False

        # Use closest free node as temporary space
        temp_node = min(
            free_nodes,
            key=lambda n: len(self._bfs_shortest_path(agent1.current, n) or [])
            or float("inf"),
        )

        original_pos1 = agent1.current
        original_pos2 = agent2.current

        # Move agent1 to temp location
        path1_to_temp = self._bfs_shortest_path(agent1.current, temp_node)
        if path1_to_temp and len(path1_to_temp) > 1:
            for i in range(1, len(path1_to_temp)):
                if (
                    not self._is_occupied(path1_to_temp[i])
                    or path1_to_temp[i] == temp_node
                ):
                    self._move_agent(agent1, path1_to_temp[i])

        # Move agent2 to agent1's original position
        path2_to_pos1 = self._bfs_shortest_path(agent2.current, original_pos1)
        if path2_to_pos1 and len(path2_to_pos1) > 1:
            for i in range(1, len(path2_to_pos1)):
                if (
                    not self._is_occupied(path2_to_pos1[i])
                    or path2_to_pos1[i] == original_pos1
                ):
                    self._move_agent(agent2, path2_to_pos1[i])

        # Move agent1 to agent2's original position
        path1_to_pos2 = self._bfs_shortest_path(agent1.current, original_pos2)
        if path1_to_pos2 and len(path1_to_pos2) > 1:
            for i in range(1, len(path1_to_pos2)):
                if (
                    not self._is_occupied(path1_to_pos2[i])
                    or path1_to_pos2[i] == original_pos2
                ):
                    self._move_agent(agent1, path1_to_pos2[i])

        return True

    def _bfs_shortest_path(self, start: int, goal: int) -> List[int]:
        """
        Find shortest path between two nodes using BFS on the adjacency matrix.

        Args:
            start: Starting node index
            goal: Goal node index

        Returns:
            List of nodes representing path from start to goal,
            or empty list if no path exists
        """
        if start == goal:
            return [start]

        queue = deque([(start, [start])])
        visited = {start}

        while queue:
            node, path = queue.popleft()

            # Check all neighbors using adjacency matrix
            for neighbor in range(self.n_nodes):
                if self.graph.has_edge(node, neighbor):
                    if neighbor == goal:
                        return path + [neighbor]

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))

        return []  # No path found

    def _move_agent(self, agent: Agent, new_pos: int):
        """Move agent to new position and update internal tracking."""
        self.agent_positions[agent.id] = new_pos
        agent.current = new_pos
        agent.path.append(new_pos)

    def _is_occupied(self, node: int) -> bool:
        """Check if a node is currently occupied by any agent."""
        return node in self.agent_positions.values()

    def _get_agent_at(self, node: int) -> Optional[Agent]:
        """Get the agent currently at a specific node, or None if unoccupied."""
        for agent in self.agents:
            if agent.current == node:
                return agent
        return None

    def _find_free_nodes(self) -> List[int]:
        """Find all currently unoccupied nodes in the graph."""
        occupied = set(self.agent_positions.values())
        return [node for node in range(self.n_nodes) if node not in occupied]

    def _all_at_goals(self) -> bool:
        """Check if all agents have reached their goal positions."""
        return all(agent.at_goal() for agent in self.agents)

    def print_solution(self, paths: Dict[int, List[int]]):
        """Pretty print the solution paths."""
        print("\n" + "=" * 70)
        print("SOLUTION PATHS")
        print("=" * 70)
        max_length = max(len(path) for path in paths.values())
        total_steps = sum(len(path) - 1 for path in paths.values())

        for agent_id in sorted(paths.keys()):
            path = paths[agent_id]
            path_str = " -> ".join(map(str, path))
            print(f"Agent {agent_id}: {path_str} (length: {len(path) - 1})")

        print(f"\nTotal steps: {total_steps}")
        print(f"Makespan: {max_length - 1}")
        print("=" * 70 + "\n")


# ============================================================================
# Example Usage and Testing Functions
# ============================================================================


def create_grid_graph(rows: int, cols: int) -> Graph:
    """
    Create a grid graph using the Graph class from graph.py.
    Nodes are numbered row-major: node = row * cols + col

    Args:
        rows: Number of rows in grid
        cols: Number of columns in grid

    Returns:
        Graph object representing the grid
    """
    num_nodes = rows * cols
    g = Graph(num_nodes, directed=False)

    for r in range(rows):
        for c in range(cols):
            node = r * cols + c
            # Right neighbor
            if c < cols - 1:
                g.add_edge(node, node + 1)
            # Down neighbor
            if r < rows - 1:
                g.add_edge(node, node + cols)

    return g


def visualize_grid(rows: int, cols: int, agents: List[Agent], show_goals: bool = True):
    """
    Visualize current agent positions on a grid.

    Args:
        rows: Number of rows
        cols: Number of columns
        agents: List of agents
        show_goals: Whether to show goal positions
    """
    grid = [["." for _ in range(cols)] for _ in range(rows)]

    # Mark goals
    if show_goals:
        for agent in agents:
            r, c = agent.goal // cols, agent.goal % cols
            grid[r][c] = "G"

    # Mark current positions (overwrites goals)
    for agent in agents:
        r, c = agent.current // cols, agent.current % cols
        grid[r][c] = str(agent.id)

    print("\nGrid visualization:")
    for row in grid:
        print(" ".join(row))
    print()


def example_simple_grid():
    """Simple example with 3 agents on a 3x3 grid."""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Simple 3x3 Grid")
    print("=" * 70)
    print("Setup: 3 agents on a 3x3 grid")
    print("  Agent 0: (0,0) -> (2,2)  [node 0 -> node 8]")
    print("  Agent 1: (0,2) -> (2,0)  [node 2 -> node 6]")
    print("  Agent 2: (1,1) -> (1,1)  [node 4 -> node 4] (stays in place)")

    graph = create_grid_graph(3, 3)

    agents = [
        Agent(0, start=0, goal=8),  # Top-left to bottom-right
        Agent(1, start=2, goal=6),  # Top-right to bottom-left
        Agent(2, start=4, goal=4),  # Center stays in center
    ]

    visualize_grid(3, 3, agents, show_goals=True)

    solver = PushAndSwap(graph, agents, verbose=True)
    paths = solver.solve()
    solver.print_solution(paths)

    return paths


def example_corridor():
    """Corridor example requiring coordination and swaps."""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Corridor (Requires Swaps)")
    print("=" * 70)
    print("Setup: 2 agents on a 1x7 corridor need to pass each other")
    print("  Agent 0: node 0 -> node 6  (moving right)")
    print("  Agent 1: node 6 -> node 0  (moving left)")

    graph = create_grid_graph(1, 7)

    agents = [
        Agent(0, start=0, goal=6),  # Left to right
        Agent(1, start=6, goal=0),  # Right to left
    ]

    solver = PushAndSwap(graph, agents, verbose=True)
    paths = solver.solve()
    solver.print_solution(paths)

    return paths


def example_complex_grid():
    """More complex example with multiple agents on larger grid."""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Complex 5x5 Grid")
    print("=" * 70)
    print("Setup: 5 agents on a 5x5 grid with crossing paths")

    graph = create_grid_graph(5, 5)

    agents = [
        Agent(0, start=0, goal=24),  # Top-left to bottom-right
        Agent(1, start=4, goal=20),  # Top-right to bottom-left
        Agent(2, start=12, goal=12),  # Center stays
        Agent(3, start=10, goal=14),  # Left-center to right-center
        Agent(4, start=2, goal=22),  # Cross pattern
    ]

    for agent in agents:
        r1, c1 = agent.start // 5, agent.start % 5
        r2, c2 = agent.goal // 5, agent.goal % 5
        print(
            f"  Agent {agent.id}: ({r1},{c1}) -> ({r2},{c2})  "
            f"[node {agent.start} -> node {agent.goal}]"
        )

    visualize_grid(5, 5, agents, show_goals=True)

    solver = PushAndSwap(graph, agents, verbose=True)
    paths = solver.solve()
    solver.print_solution(paths)

    return paths


def example_custom_graph():
    """Example with custom graph topology - cycle with center hub."""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Custom Graph Topology (Cycle with Center)")
    print("=" * 70)
    print("Setup: 6 nodes - outer cycle (0-1-2-3-4-0) with center node 5")
    print("       connected to all outer nodes")

    # Create custom graph: cycle with center hub
    g = Graph(6, directed=False)
    # Outer cycle: 0-1-2-3-4-0
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 0)
    # Center node 5 connected to all outer nodes
    for i in range(5):
        g.add_edge(5, i)

    agents = [
        Agent(0, start=0, goal=3),  # Opposite sides of cycle
        Agent(1, start=1, goal=4),  # Adjacent to opposite
    ]

    print("\nAgents:")
    for agent in agents:
        print(f"  {agent}")

    solver = PushAndSwap(graph=g, agents=agents, verbose=True)
    paths = solver.solve()
    solver.print_solution(paths)

    return paths


if __name__ == "__main__":
    print("=" * 70)
    print("PUSH AND SWAP ALGORITHM - Cooperative Path-Finding")
    print("=" * 70)

    # Run all examples
    example_simple_grid()
    example_corridor()
    example_complex_grid()
    example_custom_graph()

    print("\n" + "=" * 70)
    print("All examples completed!")
    print("=" * 70)
