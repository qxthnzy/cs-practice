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
    total = 0.0
    for row in rows:
        if row["тип"] != kind: continue
        text = row["минуты"].strip().replace(",", ".")
        try: total = total + float(text)
        except ValueError: continue
    return round(total, 1)

def to_csv(counts: dict) -> str:
    text = "тип,количество\n"
    for kind in sorted(counts):
        text = text + kind + "," + str(counts[kind]) + "\n"
    return text