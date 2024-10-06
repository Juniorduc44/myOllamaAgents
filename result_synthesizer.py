class ResultSynthesizer:
    def synthesize_results(self, results):
        synthesized_output = "Snake Game Development Process:\n\n"
        for i, result in enumerate(results):
            synthesized_output += f"Step {i+1}:\n{result}\n\n"
        synthesized_output += "Final Implementation:\n" + results[-1]
        return synthesized_output