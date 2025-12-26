import unittest
from state import AgentState

class TestAgentState(unittest.TestCase):
    def test_initial_state(self):
        state = AgentState(topic="AI", research_data=[], blog_post="")
        self.assertEqual(state['topic'], "AI")
        self.assertEqual(state['research_data'], [])

if __name__ == '__main__':
    unittest.main()
