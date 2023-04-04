import os
import subprocess

# Define the path to the IIB toolkit installation
iib_toolkit_path = "/path/to/IIBToolkit"

# Define the path to the Git plugin archive
git_plugin_path = "/path/to/git-plugin.tar.gz"

# Define the command to install the Git plugin
install_cmd = "{}eclipsec -application org.eclipse.equinox.p2.director \
  -repository jar:file:{}/tools/plugins/{}!/ \
  -installIU com.ibm.etools.git.feature.feature.group".format(iib_toolkit_path, iib_toolkit_path, git_plugin_path)

# Run the command to install the Git plugin
subprocess.call(install_cmd, shell=True)
