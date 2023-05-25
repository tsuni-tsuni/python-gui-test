from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def open_delete_group(self):
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group = self.app.application.window(title="Delete group")
        self.delete_group.wait("visible")

    def close_delete_group(self):
        self.delete_group.close()

    def add_new_group(self, group):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group.name)
        input.type_keys("\n")
        self.close_group_editor()

    # def select_group_by_name(self, name):
    #     self.group_editor.window(name=name).click()

    def delete_group_by_name(self, name):
        self.open_group_editor()
        # self.select_group_by_name(name)
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        self.open_delete_group()
        self.delete_group.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = []
        for node in root.children():
            text = node.text()
            group_list.append(Group(name=text))
        self.close_group_editor()
        return group_list
