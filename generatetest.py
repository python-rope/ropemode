import unittest
from unittest.mock import MagicMock, Mock, patch

from rope.base import libutils
from rope.base.project import Project

from ropemode.environment import Environment
from ropemode.interface import RopeMode
from ropemode.refactor import GenerateClass


class ResourceMock:
    real_path = "/tmp/other.py"
    path = "other.py"


class GenerateTest(unittest.TestCase):
    def setUp(self):
        self.env = self._get_environment_mock()
        self.interface = RopeMode(self.env)

        self._mock_rope_project()
        self._mock_rope_create_generate_method()
        self._mock_libutils_path_to_resource()

    def tearDown(self):
        self._cg_patcher.stop()
        self._libutils_patcher.stop()

    def test_generate_class_asks_for_destination_module(self):
        self._given_menu_options_will_be_selected(["cancel"])

        generate = GenerateClass(self.interface, self.env)
        generate.show()

        asked_values = self._get_asked_values()
        self.assertIn("destination module", asked_values)

    def test_generate_class_perform_refactoring_with_specified_module(self):
        self._given_menu_options_will_be_selected(["destination module", "perform"])
        self._given_value_answered("other.py")

        generate = GenerateClass(self.interface, self.env)
        generate.show()

        self.assertEqual(self.create_generate.call_count, 2)
        self.assertEqual(
            self._create_generate_called_with("goal_resource").path, "other.py"
        )

    def _mock_rope_project(self):
        self.interface.open_project = Mock()
        self.interface.project = MagicMock()
        self.interface.project.get_resource.return_value = ResourceMock

    def _mock_rope_create_generate_method(self):
        self._cg_patcher = patch("rope.contrib.generate.create_generate")
        self.create_generate = self._cg_patcher.start()

        generator = MagicMock()
        generator.get_location.return_value = Mock(), 0
        self.create_generate.return_value = generator

    def _mock_libutils_path_to_resource(self):
        self._libutils_patcher = patch.object(libutils, "path_to_resource")
        self._libutils_patcher.start()

    def _get_asked_values(self):
        asked_values = self.env.get_called_kwargs_list(self.env.ask_values)["values"]
        return asked_values

    def _given_menu_options_will_be_selected(self, options):
        self.env.ask_values = MagicMock(side_effect=options)

    def _given_value_answered(self, value):
        self.env.ask = MagicMock()
        self.env.ask.return_value = value

    def _get_environment_mock(self):
        env = Environment()
        env.ask_directory = MagicMock(return_value="/tmp/")
        env.y_or_n = MagicMock(return_value=True)
        env.create_progress = MagicMock(return_value=Mock())
        env.filenames = MagicMock(
            return_value=[
                "test.py",
            ]
        )
        env.get_called_kwargs_list = lambda x: list(x.call_args)[1]
        return env

    def _create_generate_called_with(self, key):
        return self.create_generate.call_args[1][key]


if __name__ == "__main__":
    unittest.main()
