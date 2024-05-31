#!/usr/bin/env python

from fabric import *
import os
import yaml

sign = ("$$$$$$$$\\                      $$\\ $$$$$$$\\  \r\n"
        "\\__$$  __|                     \\__|$$  __$$\\ \r\n"
        "   $$ | $$$$$$\\  $$$$$$\\$$$$\\  $$\\ $$ |  $$ |\r\n"
        "   $$ |$$  __$$\\ $$  _$$  _$$\\ $$ |$$$$$$$\\ |\r\n"
        "   $$ |$$ /  $$ |$$ / $$ / $$ |$$ |$$  __$$\\ \r\n"
        "   $$ |$$ |  $$ |$$ | $$ | $$ |$$ |$$ |  $$ |\r\n"
        "   $$ |\\$$$$$$  |$$ | $$ | $$ |$$ |$$$$$$$  |\r\n"
        "   \\__| \\______/ \\__| \\__| \\__|\\__|\\_______/ \r\n")

try:
    print(sign)
    connect_kwargs = {}
    # for pid in $(ps -ef | awk '/RPiRainbow/ {print $2}'); do kill -9 $pid; done

    with open('private.yml', 'r') as f:
        private_data = yaml.safe_load(f)

    connect_kwargs['passphrase'] = private_data['SSH_KEY_PASSWORD']

    c = Connection(
        host=private_data['HOST_NAME'],
        user=private_data['USER_NAME'],
        connect_kwargs=connect_kwargs
    )
    print(f"Connecting to {private_data['USER_NAME']}@{private_data['HOST_NAME']}")
    local_path = private_data['LOCAL_PROJECT_SRC_PATH']
    project_dir = private_data['REMOTE_PROJECT_PATH']
    local_main_file = "RPiRainbowHatController.py"
    controller_full_path = f"{project_dir}/{local_main_file}"

    filenames = next(os.walk(local_path), (None, None, []))[2]
    print(f"Local files: {filenames}")

    for filename in filenames:
        c.put(f"src/{filename}", project_dir)
    with c.cd(project_dir):
        c.run(f'ls -a')
        c.run(f'chmod +x {local_main_file}')
        c.run(f'python3 {local_main_file}', pty=True)

except KeyboardInterrupt:
    pass
