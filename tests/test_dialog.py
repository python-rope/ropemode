from ropemode import dialog


def test_trivial_case():
    action, confs = dialog.show_dialog(_MockAskConfig(["done"]), ["done"])
    assert action == "done"
    assert confs == {}


def test_asking_normal_configs():
    confs = {"name": dialog.Data()}
    minibuffer = _MockAskConfig(["value", "done"])
    action, result = dialog.show_dialog(minibuffer, ["done", "cancel"], confs)
    assert result == {"name": "value"}
    assert action == "done"


def test_optional_confs():
    optionals = {"name": dialog.Data()}
    minibuffer = _MockAskConfig(["done"])
    action, result = dialog.show_dialog(
        minibuffer, ["done", "cancel"], optionals=optionals
    )
    assert result.get("name", None) == None
    assert action == "done"


def test_optional_confs2():
    optionals = {"name": dialog.Data()}
    minibuffer = _MockAskConfig(["name", "value", "done"])
    action, result = dialog.show_dialog(
        minibuffer, ["done", "cancel"], optionals=optionals
    )
    assert result == {"name": "value"}
    assert action == "done"


def test_trivial_batchset():
    optionals = {"name": dialog.Data()}
    minibuffer = _MockAskConfig(["batchset", "name value", "done"])
    action, result = dialog.show_dialog(
        minibuffer, ["done", "cancel"], optionals=optionals
    )
    assert result == {"name": "value"}
    assert action == "done"


def test_batchset_multiple_sets():
    optionals = {"name1": dialog.Data(), "name2": dialog.Data()}
    minibuffer = _MockAskConfig(["batchset", "name1 value1\nname2 value2", "done"])
    action, result = dialog.show_dialog(
        minibuffer, ["done", "cancel"], optionals=optionals
    )
    assert result == {"name1": "value1", "name2": "value2"}
    assert action == "done"


def test_multiline_sets():
    optionals = {"name": dialog.Data()}
    minibuffer = _MockAskConfig(["batchset", "name\n line1\n  line2\n", "done"])
    action, result = dialog.show_dialog(
        minibuffer, ["done", "cancel"], optionals=optionals
    )
    assert result == {"name": "line1\n line2\n"}
    assert action == "done"


def test_complex_batchset():
    optionals = {
        "name1": dialog.Data(),
        "name2": dialog.Data(),
        "name3": dialog.Data(),
    }
    minibuffer = _MockAskConfig(
        [
            "batchset",
            "name3\n value3\nname1\n line1\n  " "line2\n\nname2 value2\n",
            "done",
        ]
    )
    action, result = dialog.show_dialog(
        minibuffer, ["done", "cancel"], optionals=optionals
    )
    assert result == {
        "name1": "line1\n line2\n",
        "name2": "value2",
        "name3": "value3\n",
    }
    assert action == "done"


def test_skipping_blanks():
    optionals = {"name1": dialog.Data(), "name2": dialog.Data()}
    minibuffer = _MockAskConfig(
        ["batchset", "\nname1\n value1\n\nname2 value2\n\n", "done"]
    )
    action, result = dialog.show_dialog(
        minibuffer, ["done", "cancel"], optionals=optionals
    )
    assert result == {"name1": "value1\n", "name2": "value2"}
    assert action == "done"


def test_skip_initial_asking():
    confs = {"name": dialog.Data()}
    minibuffer = _MockAskConfig(["name", "value", "done"])
    action, result = dialog.show_dialog(
        minibuffer, ["done", "cancel"], confs=confs, initial_asking=False
    )
    assert result == {"name": "value"}
    assert action == "done"


def test_ignoring_trailing_colon_in_config_names():
    optionals = {"name1": dialog.Data()}
    minibuffer = _MockAskConfig(["batchset", "name1: value1\n", "done"])
    action, result = dialog.show_dialog(
        minibuffer, ["done", "cancel"], optionals=optionals
    )
    assert result == {"name1": "value1"}
    assert action == "done"


class _MockAskConfig(object):
    def __init__(self, responses=[]):
        self.responses = responses
        self.asked = []

    def __call__(self, config, starting=None):
        self.asked.append(config)
        return self.responses[len(self.asked) - 1]
