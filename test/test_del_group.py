from model.group import Group
import random


def test_delete_some_group(app):
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="testGroup"))
    old_groups = app.group.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_name(group.name)
    new_groups = app.group.get_group_list()
    # uncomment after implementing the scenario by actual group name
    # assert len(old_groups) - 1 == len(new_groups)
    assert len(old_groups) == len(new_groups)
    # old_groups.remove(group)
    assert old_groups == new_groups
