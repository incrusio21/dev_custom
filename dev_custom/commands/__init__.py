# Copyright (c) 2025, incrsuio21 and contributors
# For license information, please see license.txt


# imports - standard imports
import os

# imports - third party imports
import click

from frappe.commands import pass_context, site
from dev_custom.utils import update_app_version

@click.command("update-git-version")
@pass_context
def update_git_version(context, sites_path="."):
    "Set a version tag for used site"
    site_path = os.path.join(sites_path, context.sites[0])
    if os.path.exists(site_path):
        update_app_version(site_path)

commands = [
    update_git_version
]

def use(site, sites_path="."):
    from frappe.installer import update_site_config

    site_path = os.path.join(sites_path, site)
    if os.path.exists(site_path):
        sites_path = os.getcwd()
        conifg = os.path.join(sites_path, "common_site_config.json")
        update_site_config("default_site", site, validate=False, site_config_path=conifg)
        print(f"Current Site set to {site}")
        update_app_version(site_path)
    else:
        print(f"Site {site} does not exist")

site.use = use
