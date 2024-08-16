import unittest
from unittest.mock import MagicMock, Mock

from ropemode.environment import Environment
from ropemode.interface import RopeMode

class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.env = self._get_environment_mock()
        self.interface = RopeMode(self.env)
        self._mock_rope_project()

    def test_show_doc_none(self):
        self.env.get_offset = Mock(return_value=1)
        self.interface.show_doc(None)
        assert not self.env.show_doc.called
        self.env.message.assert_called_once_with('No docs available!')

    def test_show_doc(self):
        self.env.get_offset = Mock(return_value=10)
        self.interface.show_doc(None)
        self.env.show_doc.assert_called_once_with("class SomeClass():\n\n  docstring", None)

    def test_code_assist(self):
        self.env.get_offset = Mock(return_value=10)
        self.interface.code_assist("Som")
        self.env.ask_completion.assert_called_once_with('Completion for SomeClass: ', ['SomeClass'], 'SomeClass')
        
    def _mock_rope_project(self):
        self.interface.open_project = Mock()
        self.interface.project = MagicMock()

    def _get_environment_mock(self):
        env = Environment()
        env.message = Mock()
        env.show_doc = Mock()
        env.ask_completion = MagicMock()
        env.get_text = MagicMock(return_value="""
class SomeClass:
  \"\"\"docstring\"\"\"
  def abc(self):
      pass
""")
        return env

if __name__ == '__main__':
    unittest.main()
