from pathlib import Path

text = Path("programs.txt").read_text()

l = [s.strip().lower() for s in text.strip().split("\n")]
l = [s for s in l if s]
# [i for i, s in enumerate(l) if "#" in s]
l1 = l[:59][1:]
l2 = l[59:110][1:]
l3 = l[110:][1:]

ll = list(set(l1) & set(l2) & set(l3))
lll = [s for s in l1 if s in ll]
