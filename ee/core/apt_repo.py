"""EasyEngine packages repository operations"""
from ee.core.shellexec import EEShellExec
from ee.core.variables import EEVariables
import os


class EERepo():
    """Manage Repositories"""

    def __init__(self):
        """Initialize """
        pass

    def add(self, repo_url=None, ppa=None):

        if repo_url is not None:
            repo_file_path = ("/etc/apt/sources.list.d/"
                              + EEVariables().ee_repo_file)
            try:
                if not os.path.isfile(repo_file_path):
                    with open(repo_file_path, "a") as repofile:
                        repofile.write(repo_url)
                        repofile.close()
                elif repo_url not in open(repo_file_path).read():
                    with open(repo_file_path, "a") as repofile:
                        repofile.write(repo_url)
                        repofile.close()
                return True
            except IOError as e:
                Log.debug(self, "{0}".format(e))
                Log.error(self, "File I/O error.")
            except Exception as e:
                Log.debug(self, "{0}".format(e))
                Log.error(self, "Unable to add repo")
        if ppa is not None:
            if EEVariables.ee_platform_distro == 'squeeze':
                print("Cannot add repo for {distro}"
                      .format(distro=EEVariables.ee_platform_distro))
            else:
                EEShellExec.cmd_exec(self, "add-apt-repository -y "
                                           "'{ppa_name}'"
                                     .format(ppa_name=ppa))

    def remove(self, repo_url=None):
        EEShellExec.cmd_exec(self, "add-apt-repository -y "
                             "--remove '{ppa_name}'"
                             .format(ppa_name=repo_url))

    def add_key(keyids, keyserver=None):
        if keyserver is None:
            EEShellExec.cmd_exec("gpg --keyserver {serv}"
                                 .format(serv=(keyserver
                                         or "hkp://keys.gnupg.net"))
                                 + " --recv-keys {key}".format(key=keyids))
            EEShellExec.cmd_exec("gpg -a --export --armor {0}".format(keyids)
                                 + " | apt-key add - ")
