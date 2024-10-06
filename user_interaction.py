class UserInteraction:
    def prompt_task(self):
        # Prompt the user for their desired task or query
        task_description = input("Please enter the task description: ")
        return task_description

    def prompt_num_agents(self):
        # Ask how many agents the user wants to deploy (maximum of 5)
        while True:
            try:
                num_agents = int(input("Enter the number of agents to deploy (1-5): "))
                if 1 <= num_agents <= 5:
                    return num_agents
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

    def display_output(self, output):
        # Display the final output to the user
        print("Final Output:")
        print(output)