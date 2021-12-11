def _chdir(sub_dir: str = "."):
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
    md2pdf = f"pandoc --standalone --citeproc --pdf-engine=xelatex --from markdown --to pdf {name}.md -o {name}.pdf"
    subprocess.run(md2pdf.split())
    openpdf = f"open {name}.pdf"
    subprocess.run(openpdf.split())
    print("Done.")


if __name__ == "__main__":
    main()
