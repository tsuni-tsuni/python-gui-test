def test_add_group(app, excel_groups):
    group = excel_groups
    old_list = app.group.get_group_list()
    app.group.add_new_group(group)
    new_list = app.group.get_group_list()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(group)
    assert sorted(old_list, key=lambda x: x.name) == sorted(old_list, key=lambda x: x.name)
