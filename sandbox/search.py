import random
import json
import polars as pl


def get_random_lines(count: int, filepath: str) -> list:
    with open(filepath) as f:
        lines = f.readlines()
        lines = random.sample(lines, count)
    return lines

def pretty_print(json_str: str) -> None:
    return json.dumps(json.loads(json_str), indent=4, sort_keys=True)

lines = get_random_lines(10, "kaikki.org-dictionary-Latin.json")
with open("sample.json", "w") as f:
    for line in lines:
        f.write(line)
with open("sample.txt", "w") as f:
    for line in lines:
        f.write(pretty_print(line))

FORM_OF = pl.col("senses").list.get(0).struct.field("form_of").fill_null(pl.lit([{"word": "null"}])).list.get(0).struct.field("word").alias("form_of")
GLOSSES = pl.col("senses").list.get(0).struct.field("glosses").list.get(0).alias("glosses")

df = pl.scan_ndjson("sample.json")
table = df.select(pl.col("pos"),
                  pl.col("word"),
                  pl.col("head_templates").list.get(0).struct.field("expansion").alias("expansion"),
                  FORM_OF,
                  GLOSSES
                 ).collect()

print(table)

