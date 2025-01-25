#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from marketing_agent.crew import MarketingAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Delloite'
    }

    try:
        model_output = MarketingAgent().crew().kickoff(inputs=inputs)

        task_output_list = model_output.tasks_output
        raw_outputs_list = [i.raw + "\n" for i in task_output_list]
        print(f"Task output list:")
        # print(*raw_outputs_list, sep="\n")

        with open('report.md', 'w', encoding='utf-8') as f:
            for line in raw_outputs_list:
                f.write(f"{line}\n")

        # agent_output_string = output_model.tasks[0].output
        # with open("out.md", encoding="utf-8", mode="w") as f:
        #     f.write(agent_output_string)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Deloitte"
    }
    try:
        MarketingAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MarketingAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Deloitte"
    }
    try:
        MarketingAgent().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
