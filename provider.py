#!/usr/bin/env python3

#  Copyright 2024 Denis Lussier All rights reserved. #

import fire
from prettytable import PrettyTable

PROVIDERS = \
    [
        ["akm", "linode",       "Akamai Linode"],
        ["eqn", "equinixmetal", "Equinix Metal"],
        ["aws", "ec2",          "Amazon Web Services"],
        ["azr", "azure",        "Microsoft Azure"],
        ["gcp", "gce",          "Google Cloud Platform"],
    ]

def list_providers():
    """Supported Cloud Provider List"""

    p = PrettyTable()
    p.field_names = ["Provider", "Libcloud Name", "Description"]
    p.add_rows(PROVIDERS)
    p.align["Cloud Name"] = "l"
    p.align["Description"] = "l"
    print(p)

    return

if __name__ == "__main__":
    fire.Fire(
        {
            "list": list_providers,
        }
    )
