#!/bin/python

from typing import Dict
import argparse
import xml.etree.ElementTree as ET

"""
Script to convert iterm2 theme to Xresources
"""


def rgb2hex(r: float, g: float, b: float) -> str:
    return "#{:02x}{:02x}{:02x}".format(round(r*255), round(g*255), round(b*255))


def extract_iterm_colors_from_xml(file_path: str) -> Dict[str, Dict[str, str]]:
    iterm_colors_dict: Dict[str, Dict[str, str]] = {}
    tree = ET.parse(file_path)
    root = tree.getroot()
    dict_element = root.find("dict")
    if dict_element is None:
        return iterm_colors_dict

    keys = dict_element.findall("key")
    dicts = dict_element.findall("dict")
    for k, d in zip(keys, dicts):
        iterm_colors_dict[k.text] = {}
        for index, element in enumerate(d):
            if element.tag == "key":
                continue
            iterm_colors_dict[k.text][d[index-1].text] = element.text

    return iterm_colors_dict


def convert_iterm_to_xresources(iterm_colors: Dict[str, Dict[str, str]]) -> Dict[str, str]:
    xresources_colors = {}
    for k, v in iterm_colors.items():
        print(k, v)
        if "Ansi" in k:
            # Ansi 0 color
            color = f"*color{k.split()[1]}"
        elif k in ["Background Color", "Foreground Color"]:
            color = f"*{k.split()[0].lower()}"
        elif k == "Cursor Color":
            color = "*cursorColor"

        xresources_colors[color] = rgb2hex(
            float(v["Red Component"]),
            float(v["Green Component"]),
            float(v["Blue Component"])
        )
    return xresources_colors


def write_xresource_colors_to_file(file_path: str, xresources_colors: Dict[str, str]):
    with open(file_path, "w") as f:
        for color, value in xresources_colors.items():
            f.write(f"{color}: {value}\n")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog="iter2Xresources.py",
        usage="%(prog)s [options]",
        description="Converts iterm2 colors to Xresources")
    arg_parser.add_argument("--from", dest="file_path", help="Xml file containing iterm2 colors")
    arg_parser.add_argument("--to", dest="output_file_path", help="output file to store the conversion")

    args = arg_parser.parse_args()
    iterm_colors = extract_iterm_colors_from_xml(args.file_path)
    xresources_colors = convert_iterm_to_xresources(iterm_colors)
    write_xresource_colors_to_file(args.output_file_path, xresources_colors)
