import subprocess
#llama="internlm2:latest"
#llama="llama3:8b"
#llama="gemma2:latest"
#llama="llama3:70b"
#llama="deepseek-coder-v2:16b"
llama="deepseek-coder-v2:236b"


class OllamaAgent:
    def __init__(self, agent_id, config, logger):
        self.agent_id = agent_id
        self.config = config
        self.logger = logger

    def execute_task(self, task):
            prompt = f"""
            You are an AI assistant specialized in Python programming, software and game development.
            Your task: {task}
            
            If you're improving existing code, analyze it carefully and suggest meaningful improvements.
            If you're creating new code, ensure it's well-structured and commented.
            
            Provide your response as valid Python code with comments explaining key parts.
            """
            
            command = ["ollama", "run", "llama3:8b", prompt]
            self.logger.info(f"Agent {self.agent_id} executing task: {task[:50]}...")
            try:
                result = subprocess.run(command, capture_output=True, text=True, check=True)
                self.logger.info(f"Agent {self.agent_id} task completed successfully")
                return result.stdout.strip()
            except subprocess.CalledProcessError as e:
                error_message = f"Agent {self.agent_id} failed to execute task. Error: {e.stderr.strip()}"
                self.logger.error(error_message)
                return f"Error: {error_message}"
            except Exception as e:
                error_message = f"Agent {self.agent_id} encountered an unexpected error: {str(e)}"
                self.logger.error(error_message)
                return f"Error: {error_message}"