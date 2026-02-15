def align_table(rows):
    if not rows:
        return ""
    col_widths = []
    for row in rows:
        if row.strip().startswith('|---'): continue
        cells = [c.strip() for c in row.split('|') if c.strip()]
        for i, cell in enumerate(cells):
            if i >= len(col_widths):
                col_widths.append(len(cell))
            else:
                col_widths[i] = max(col_widths[i], len(cell))

    print(f"Widths: {col_widths}")
    result = []
    # Header
    cells = [c.strip() for c in rows[0].split('|') if c.strip()]
    line = "| " + " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(cells)) + " |"
    result.append(line)

    # Separator
    line = "| " + " | ".join("-" * col_widths[i] for i in range(len(col_widths))) + " |"
    result.append(line)

    # Data
    for row in rows[2:]:
        cells = [c.strip() for c in row.split('|') if c.strip()]
        line = "| " + " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(cells)) + " |"
        result.append(line)

    return "\n".join(result)

table1 = [
    "| Module      | Description |",
    "|-------------|-------------|",
    "| **BitPath** | Tools for pathology slide annotation, format conversion, WSI viewing, and AI-assisted labeling. |",
    "| **BitEdge** | Edge-side compute nodes deployed within hospitals/labs. Enables federated learning without data leaving the institution. |",
    "| **BitFlow** | Central orchestration for workflow scheduling, model deployment, artifact storage, and audit logging. |"
]

table2 = [
    "| Repo        | Description |",
    "|-------------|-------------|",
    "| [`annota`](https://github.com/bitroc-ai/annota) | High-performance React-based annotation framework for WSI and cell segmentation. |",
    "| [`kfbviewer`](https://github.com/bitroc-ai/kfbviewer) | Lightweight viewer for `.kfb` pathology slides using OpenSeadragon. |"
]

print("Table 1:")
print(align_table(table1))
print("\nTable 2:")
print(align_table(table2))
