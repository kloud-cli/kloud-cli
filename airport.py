#!/usr/bin/env python3

#  Copyright 2024 Denis Lussier All rights reserved. #

import sqlite
import fire
from prettytable import PrettyTable



def airport_list(geo=None, country=None, airport=None, provider=None):
    import sqlite
    wr = "1 = 1"
    if geo:
        wr = wr + f" AND geo = '{geo}'"
    if country:
        wr = wr + f" AND country = '{country}'"
    if airport:
        wr = wr + f" AND airport = '{airport}'"
    if provider:
        wr = wr + f" AND provider= '{provider}'"
    cols = "geo, country, airport, airport_area, lattitude, longitude, provider, region, parent, zones"
    try:
        cursor = cL.cursor()
        cursor.execute(f"SELECT {cols} FROM v_airports WHERE {wr}")
        data = cursor.fetchall()
    except Exception as e:
        util.exit_message(str(e), 1)
    al = []
    for d in data:
        al.append([str(d[0]), str(d[1]), str(d[2]), str(d[3]), d[4],
                   d[5], str(d[6]), str(d[7]), str(d[8]), str(d[9])])
    return (al)



def list_airports(geo=None, country=None, airport=None, provider=None):
    """List airport codes & provider regions"""

    al = airport_list(geo, country, airport, provider)

    if not pretty:
        return(al)

    p = PrettyTable()
    p.field_names = ["Geo", "Country", "Airport", "Area", "Lattitude", "Longitude", "Provider", "Region", "Parent", "Zones"]
    p.float_format = ".4"
    p.align["Lattitude"] = "r"
    p.align["Longitude"] = "r"
    p.align["Area"] = "l"
    p.align["Region"] = "l"
    p.align["Parent"] = "l"
    p.align["Zones"] = "l"
    p.add_rows(al)
    print(p)

    return


if __name__ == "__main__":
    fire.Fire(
        {
            "list": list_airports,
        }
    )
