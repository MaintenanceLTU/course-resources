# -*- coding: utf-8 -*-
import json

with open("columns.json", encoding="utf-8") as f:
    columns = json.load(f)

with open("../tables-and-columns.md", "w", encoding="utf-8") as f:

    for table in ["bis", "ofelia"]:
        f.write(f"# {table.upper()}\n\n")
        f.write("| Column | Swedish | English |\n")
        f.write("|----------|----------|----------|\n")

        for col, info in columns[table].items():
            f.write(
                f"| {col} | {info['sv']} | {info['en']} |\n"
            )

        f.write("\n\n")