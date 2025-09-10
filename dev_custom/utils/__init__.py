# Copyright (c) 2025, incrsuio21 and contributors
# For license information, please see license.txt

import os
import json
import subprocess

import git

import frappe
from frappe.build import get_node_env
from frappe.utils.synchronization import filelock

def update_app_version(site_path):

    version_path = os.path.join(site_path, "app_version.json")
    if os.path.exists(version_path):
        with filelock("version_config", is_global=1):
            _update_app_version(version_path)

        
def _update_app_version(version_config_path):
    with open(version_config_path) as f:
        apps = json.loads(f.read())
    
    for app, tags in apps.items():
        source_app = frappe.get_app_source_path(app)
        repo = git.Repo(source_app, search_parent_directories=True)
        is_local = any(tag.name == tags for tag in repo.tags)

        if not is_local:
            repo.remote("upstream").fetch(
                refspec=f"refs/tags/{tags}:refs/tags/{tags}", 
                no_tags=True,
                verbose=True
            )

         # 1. Set konfigurasi untuk abaikan permission
        with repo.config_writer() as config:
            config.set_value("core", "filemode", "false")

        repo.git.checkout(tags, force=True)
        print(f"{app} use version {tags}")
  
        command = f"yarn install"
        frappe.commands.popen(command, cwd=source_app, env=get_node_env(), raise_err=True)

    print(f"bench build for apps")
    command = f"bench build --apps {','.join(apps.keys())}"
    frappe.commands.popen(command, env=get_node_env(), raise_err=True)
        