import glob
import json
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


def get_iso_time():
    KST = pytz.timezone("Asia/Seoul")
    t = datetime.now(timezone.utc).replace(microsecond=0).astimezone(KST).isoformat()
    return t


def get_info(clover_xml: str):
    root = ET.parse(clover_xml).getroot()
    project, testproject = root
    project_name = project.attrib["name"]
    project_slug = slugify(project_name)
    project_metrics = project.find("./metrics").attrib
    testproject_metrics = testproject.find("./metrics").attrib
    metadata = {
        "name": project_name,
        "slug": project_slug,
        "project_metrics": project_metrics,
        "test_metrics": testproject_metrics,
    }
    return metadata


def main():
    clover_xml = "clover.xml"
    info = get_info(clover_xml)

    xmls = glob.glob("clover/*.xml")
    xmls.sort()
    data = get_data(xmls)

    output = {"info": info, "data": data}

    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    slug = info["slug"]
    write_json(f"{data_dir}/{slug}.json", output)

    print("Done.")


if __name__ == "__main__":
    main()
