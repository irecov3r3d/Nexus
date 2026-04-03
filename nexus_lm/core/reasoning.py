import random
import html
from typing import List

class REEREngine:
    """
    Reverse-Engineered Reasoning (REER) Core.
    Optimizes reasoning trajectories without gradient descent,
    treating logic search as an optimization problem.
    """

    MUTATIONS = [
        "\nWe must also consider the edge cases.",
        "\nWait, a better approach might be optimizing the memory footprint.",
        "\nLet's break this down into smaller sub-problems.",
        "\nActually, this requires a state machine.",
        "\nHmm... alternatively, ",
        "\nWait, that's a bit... ",
        "\nWait, the user said... "
    ]

    def __init__(self, max_iterations=5, temperature=0.7):
        self.max_iterations = max_iterations
        self.temperature = temperature

    def _calculate_ppl_proxy(self, thought_text: str) -> float:
        """Mock perplexity calculation for local search heuristic."""
        # Simple heuristic: longer, well-structured thoughts lower PPL
        return random.uniform(0.5, 2.0) - (len(thought_text) * 0.001)

    def _construct_trajectory(self, initial_thought: str, mutations: List[str]) -> str:
        """Helper to construct the reasoning trajectory."""
        # Using "\n".join for robustness and clarity as recommended by review.
        # Mutations in self.MUTATIONS already start with \n, so we strip them for a clean join.
        content_parts = [initial_thought] + [m.strip("\n") for m in mutations]
        joined = "\n".join(content_parts)
        return f"<thought>\n{joined}\n</thought>"

    def search(self, initial_query: str) -> str:
        """
        Executes gradient-free local search to find optimal trajectory.
        Iteratively appending or modifying thoughts based on previous iterations.
        """
        # Start with an initial seed plan based on query
        sanitized_query = html.escape(initial_query)
        initial_thought = f"Let me think... maybe we should address '{sanitized_query}'."
        best_mutations = []
        best_thought = self._construct_trajectory(initial_thought, best_mutations)
        best_ppl = self._calculate_ppl_proxy(best_thought)

        for _ in range(self.max_iterations):
            # Mutate thought (append a random mutation)
            mutation = random.choice(self.MUTATIONS)
            current_mutations = best_mutations + [mutation]

            # Simulated thought insertion
            new_thought = self._construct_trajectory(initial_thought, current_mutations)
            new_ppl = self._calculate_ppl_proxy(new_thought)

            # Acceptance criteria (simulated annealing-like)
            if new_ppl < best_ppl or random.random() < self.temperature:
                best_mutations = current_mutations
                best_thought = new_thought
                best_ppl = new_ppl

        return best_thought
