# -*- coding: utf-8 -*-
import json

with open("columns.json", encoding="utf-8") as f:
    columns = json.load(f)

with open("dtypes.json", encoding="utf-8") as f:
    dtypes = json.load(f)

type_map = dtypes["type_map"]

with open("../tables-and-columns.md", "w", encoding="utf-8") as f:

    for table in ["bis", "ofelia"]:

        f.write(f"# {table.upper()}\n\n")
        f.write("| Column | Type | Swedish | English |\n")
        f.write("|----------|----------|----------|----------|\n")

        for col, info in columns[table].items():

            dtype = dtypes[table][col]
            sql_type = type_map.get(dtype, dtype)

            f.write(
                f"| {col} | {sql_type} | "
                f"{info['sv']} | {info['en']} |\n"
            )

        f.write("\n\n")