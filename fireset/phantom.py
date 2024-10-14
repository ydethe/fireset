# https://hub.phantombuster.com/reference/get_orgs-export-agent-usage-1

import requests

from . import settings


def get_leads_list():
    url = f"https://api.phantombuster.com/api/v2/org-storage/leads/by-list/{settings.phantombuster_listid}"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-Phantombuster-Key": f"{settings.phantombuster_key}",
    }

    response = requests.post(url, headers=headers)

    return response.json()
