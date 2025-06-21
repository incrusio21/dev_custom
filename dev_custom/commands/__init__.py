# Copyright (c) 2025, incrsuio21 and contributors
# For license information, please see license.txt

# imports - standard imports
import os

from frappe.commands import site

def use(site, sites_path="."):
    from frappe.installer import update_site_config
    from dev_custom.utils import update_app_version

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
