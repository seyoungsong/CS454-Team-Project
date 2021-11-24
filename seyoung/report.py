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
    md2pdf = "pandoc --standalone --pdf-engine=xelatex --from markdown --to pdf report.md -o report.pdf"
    subprocess.run(md2pdf.split())
    openpdf = "open report.pdf"
    subprocess.run(openpdf.split())
    print("Done")


if __name__ == "__main__":
    main()
