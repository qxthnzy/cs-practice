def read_rows(lines: list[str]) -> list[dict]:
    header = None
    rows = []
    for line in lines:
        line = line.strip()                               
        if line == "": continue
        parts = line.split(",")
        values = []
        for part in parts: values.append(part.strip())     
        if header is None:
            header = values
            continue                                       
        if len(values) != len(header): continue
        row = {}
        for i in range(len(header)): row[header[i]] = values[i]
        rows.append(row)
    return rows

def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]
        if kind in counts: counts[kind] += 1
        else: counts[kind] = 1
    return counts

def total_minutes(rows: list[dict], kind: str) -> float:
    raise NotImplementedError
def to_csv(counts: dict) -> str:
    raise NotImplementedError