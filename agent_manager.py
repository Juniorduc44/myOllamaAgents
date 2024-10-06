from ollama_agent import OllamaAgent
from multiprocessing import Pool

class AgentManager:
    def __init__(self, num_agents, config, logger):
        self.num_agents = num_agents
        self.config = config
        self.logger = logger
        self.agents = [OllamaAgent(i, config, logger) for i in range(num_agents)]

    def distribute_tasks(self, subtasks):
        self.subtasks = subtasks
        # Ensure we don't have more subtasks than agents
        if len(self.subtasks) > self.num_agents:
            self.logger.warning(f"More subtasks ({len(self.subtasks)}) than agents ({self.num_agents}). Some tasks may be dropped.")
            self.subtasks = self.subtasks[:self.num_agents]

    def execute_tasks(self):
            results = []
            previous_result = None
            for i, task in enumerate(self.subtasks):
                if i == 0:
                    result = self.agents[i].execute_task(task)
                else:
                    result = self.agents[i].execute_task(f"{task} based on:\n\n{previous_result}")
                results.append(result)
                previous_result = result
            return results

    def _execute_agent_task(self, task_info):
        agent_id, task = task_info
        if agent_id < len(self.agents):
            return self.agents[agent_id].execute_task(task)
        else:
            self.logger.error(f"No agent available for task {agent_id}")
            return f"Error: No agent available for task {agent_id}"