import glob
import json
import platform
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from pprint import pprint
from xml.etree.ElementTree import Element

import pytz
from slugify import slugify
from tqdm import tqdm


def ppe(root: Element):
    # pretty print XML element
    print(root.tag, root.attrib)
    for i, child in enumerate(root):
        print(f"{i}:", child.tag, child.attrib)


def ppl(es: list[Element]):
    # pretty print list of elements
    for i, e in enumerate(es):
        print(f"{i}:", e.tag, e.attrib)


def flatten(ll: list[list]) -> list:
    return [item for l in ll for item in l]


def write_json(filename: str, obj):
    with open(filename, "w", encoding="utf8") as f:
        json.dump(obj, f, indent=2)


def get_success_and_duration(
    root: Element,
    test_package: str,
    test_class: str,
    test_method: str,
) -> tuple[bool, float]:
    _project, testproject = root
    package = [
        e for e in testproject.findall("./package") if e.attrib["name"] == test_package
    ][0]
    file = [
        e
        for e in package.findall("./file")
        if Path(e.attrib["name"]).stem == test_class
    ][0]
    lines = [e.attrib for e in file.findall("./line")]
    line = [
        d
        for d in lines
        if "signature" in d and d["signature"].split("() : ")[0] == test_method
    ][0]
    test_success = line["testsuccess"] == "true"
    test_duration = float(line["testduration"])
    return test_success, test_duration


def get_coverage(root: Element):
    project, _testproject = root
    packages = project.findall("./package")
    test_coverage: list[dict] = []
    for package in packages:
        package_name = package.attrib["name"]
        files = package.findall("./file")
        for file in files:
            file_name = file.attrib["name"]
            class_name = Path(file_name).stem
            lines = [e.attrib for e in file.findall("./line")]
            cov = []
            for line in lines:
                line_num = int(line["num"])
                line_type = line["type"]
                if line_type == "stmt":
                    if int(line["count"]) > 0:
                        cov.append(f"{line_num}")
                elif line_type == "method":
                    if int(line["count"]) > 0:
                        cov.append(f"{line_num}M")
                elif line_type == "cond":
                    if int(line["truecount"]) > 0:
                        cov.append(f"{line_num}T")
                    if int(line["falsecount"]) > 0:
                        cov.append(f"{line_num}F")
                else:
                    assert False, "line_type invalid?"
            if cov:
                cov.sort()
                test_coverage.append(
                    {
                        "package": package_name,
                        "class": class_name,
                        "lines": cov,
                    }
                )
    return test_coverage


def get_data(xmls: list[str]):
    data: list[dict] = []
    # xml = xmls[0]
    for xml in tqdm(xmls):
        root = ET.parse(xml).getroot()
        _, test_package, test_class, test_method = Path(xml).stem.split("#")

        test_name = f"{test_package}.{test_class}#{test_method}"
        test_success, test_duration = get_success_and_duration(
            root, test_package, test_class, test_method
        )
        test_coverage = get_coverage(root)

        data.append(
            {
                "name": test_name,
                "package": test_package,
                "class": test_class,
                "method": test_method,
                "success": test_success,
                "duration": test_duration,
                "coverage": test_coverage,
            }
        )
    return data


def iso_time():
    KST = pytz.timezone("Asia/Seoul")
    t = datetime.now(timezone.utc).replace(microsecond=0).astimezone(KST).isoformat()
    return t


def iso_fromtimestamp(timestamp: int):
    KST = pytz.timezone("Asia/Seoul")
    s = datetime.fromtimestamp(timestamp, KST).isoformat()
    return s


def get_info(clover_xml: str, git_log: str):

    log = Path(git_log).read_text()
    github_url, commit_timestamp, commit_hash = [
        s.strip() for s in log.strip().split("\n")
    ]
    github_url = github_url.rstrip("/").lower()
    commit_url = f"{github_url}/tree/{commit_hash}"
    commit_timestamp = int(commit_timestamp)
    commit_datetime = iso_fromtimestamp(commit_timestamp)

    dev_name, repo_name = github_url.replace("https://github.com/", "").split("/")
    filename = f"{dev_name}_{repo_name}.json"

    root = ET.parse(clover_xml).getroot()
    project, testproject = root
    project_name = project.attrib["name"]
    metrics_project = project.find("./metrics").attrib
    metrics_testproject = testproject.find("./metrics").attrib

    platform_str = platform.platform()
    java_str = (
        subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT)
        .decode("utf8")
        .strip()
        .split("\n")[0]
    )
    maven_str = (
        subprocess.check_output(["mvn", "--version"], stderr=subprocess.STDOUT)
        .decode("utf8")
        .strip()
        .split("\n")[0]
    )

    metadata = {
        # project name
        "project": project_name,
        "filename": filename,
        # github: url, dev, repo
        "github": {
            "url": github_url,
            "dev": dev_name,
            "repo": repo_name,
        },
        # env: platform, java version, maven version
        "env": {
            "platform": platform_str,
            "java": java_str,
            "maven": maven_str,
        },
        # commit: url, hash, time
        "commit": {
            "datetime": commit_datetime,
            "url": commit_url,
            "hash": commit_hash,
            "timestamp": commit_timestamp,
        },
        # metrics: project, test
        "metrics": {
            "project": metrics_project,
            "testproject": metrics_testproject,
        },
    }

    return metadata


def main():
    clover_xml = "clover.xml"
    git_log = "git.log"
    info = get_info(clover_xml, git_log)

    xmls = sorted(glob.glob("clover/*.xml"))
    data = get_data(xmls)

    filename = info["filename"]
    output = {"info": info, "data": data}

    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)
    write_json(f"{output_dir}/{filename}", output)

    print("Done.")


if __name__ == "__main__":
    main()
