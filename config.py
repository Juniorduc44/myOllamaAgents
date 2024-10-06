

class Configuration:
    def __init__(self):
        ## List Of Models
        #llama="internlm2:latest"
        #llama="llama3:8b"
        #llama="gemma2:latest"
        #llama="llama3:70b"
        #llama="deepseek-coder-v2:16b"
        llama="deepseek-coder-v2:236b"
        # Load configuration settings
        self.settings = {
        "ollama_command": "ollama run {llama}",
        "max_agents": 5
    }