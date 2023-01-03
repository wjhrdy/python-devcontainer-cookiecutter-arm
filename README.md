# Python Devcontainer for arm based computers deploying on x86 servers

Working on python projects that are deployed on x86 infrastructure in the cloud on an arm-based mac can be difficult because some python packages don't work on arm. To get around this we use devcontainers in vscode that run on x86 versions of base images.

## Get Started

### Prerequisite

* Install Python via the perfered method for your OS.
* [Install pipx](https://pypa.github.io/pipx/installation/)
* [Install vscode](https://code.visualstudio.com/download)
* [Install vscode: Remote Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
* Use pipx to install `pipx install cookiecutter`
* [Install podman desktop + podman cli](https://podman-desktop.io/)

## Generate your project

```bash
cookiecutter https://github.com/wjhrdy/python-devcontainer-cookiecutter-arm.git --checkout 2023.01.03
```

### Configure VSCode

1. Open VSCode Settings and search for `dev.containers.dockerPath`
2. Make sure that this docker path is set to `podman`. This will change `docker` to `podman` for all the commands that vscode runs to start the container.
3. Open this project directory in vscode. You should see a prompt in the bottom right to reopen in container.
4. All remote container functions to start, stop, restart can be accessed from the button that looks like this `><` in the left of the bottom bar.

### Start Devcontainer

1. Open `Podman Desktop` and make sure `podman` is installed, it will prompt you.
2. Ensure Podman is running.
3. On **Mac** you will need to mount your home directory to the Podman VM with this command `./mac_podman_machine_init.sh` it might take a couple of minutes to run. **Need to run this once every time you restart your computer.** *You may need to adjust the cpu or memory values in that file*
4. Open your newly generated project directory in vscode. 
5. You should see a button that looks like this `><` where you can reopen in container. 

### Git in the DevContainer

VSCode has a [Source Control panel](https://code.visualstudio.com/docs/sourcecontrol/overview) where you can do most of your git operations locally.

When it comes to pushing to gitlab or github however; you will either have to reload your project outside of your DevContainer or [configure your host system to share your ssh key with the ssh agent.](https://code.visualstudio.com/docs/devcontainers/containers#_using-ssh-keys)
