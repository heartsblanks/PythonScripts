from workspace_utils import WorkspaceUtils

class InstallOrchestration:
    def __init__(self, master):
        # ...
        self.workspace_utils = WorkspaceUtils(install_type)

    def performInstallation(self, system_type, install_type):
        # ...
        self.workspace_utils.checkWorkspaceDirectory()
        if self.workspace_utils.workspace_path is None:
            return

        # Generate self variables
        self.create_self_variables()

        # Continue with installation...
