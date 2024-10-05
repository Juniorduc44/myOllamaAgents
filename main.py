import sys
from user_interaction import UserInteraction
from agent_manager import AgentManager
from task_analyzer import TaskAnalyzer
from result_synthesizer import ResultSynthesizer
from config import Configuration
from logger import Logger

def main():
    # Initialize configuration and logger
    config = Configuration()
    logger = Logger(config)

    # Initialize user interaction module
    user_interaction = UserInteraction()

    # Get user input for task and number of agents
    task_description = user_interaction.prompt_task()
    num_agents = user_interaction.prompt_num_agents()

    # Initialize task analyzer and agent manager
    task_analyzer = TaskAnalyzer()
    agent_manager = AgentManager(num_agents, config, logger)

    # Analyze and distribute tasks
    subtasks = task_analyzer.decompose_task(task_description, num_agents)
    agent_manager.distribute_tasks(subtasks)

    # Execute tasks and collect results
    results = agent_manager.execute_tasks()

    # Synthesize results
    result_synthesizer = ResultSynthesizer()
    final_output = result_synthesizer.synthesize_results(results)

    # Present final output to the user
    user_interaction.display_output(final_output)

if __name__ == "__main__":
    main()