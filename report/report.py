def _chdir(sub_dir: str = "report"):
    import os
    from pathlib import Path

    p = Path().resolve().joinpath(sub_dir)
    if p.is_dir():
        os.chdir(p)
    print(Path().resolve())


_chdir()


import subprocess


def main():
    name = "report"
    subprocess.run(
        f"pandoc --standalone --citeproc --pdf-engine=xelatex --from markdown --to pdf {name}.md -o {name}.pdf".split()
    )
    subprocess.run(f"open {name}.pdf".split())
    subprocess.run(
        f"pandoc --standalone --citeproc --pdf-engine=xelatex --from markdown --to docx {name}.md -o {name}.docx".split()
    )
    print("Done.")


if __name__ == "__main__":
    main()
