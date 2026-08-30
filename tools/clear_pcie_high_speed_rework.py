#!/usr/bin/env python3
"""Remove only the PCIe/REFCLK copper for a controlled rework iteration."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TARGET_NETS = {
    "/PER0_P",
    "/PER0_N",
    "/PET0_P_RAW",
    "/PET0_N_RAW",
    "/PET0_P",
    "/PET0_N",
    "/REFCLK_P",
    "/REFCLK_N",
}


def balanced(text: str, start: int) -> int:
    depth = 0
    quoted = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if quoted:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
            continue
        if char == '"':
            quoted = True
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index + 1
    raise ValueError("unbalanced board object")


def net_names(board: str) -> dict[int, str]:
    return {int(code): name for code, name in re.findall(r'\(net (\d+) "([^"]*)"\)', board)}


def remove_objects(board: str) -> tuple[str, int]:
    names = net_names(board)
    target_codes = {code for code, name in names.items() if name in TARGET_NETS}
    objects: list[tuple[int, int]] = []
    for match in re.finditer(r"\n\t\((segment|via) ", board):
        start = match.start()
        end = balanced(board, start + 1)
        obj = board[start + 1:end]
        net_match = re.search(r"\(net (\d+)\)", obj)
        if net_match and int(net_match.group(1)) in target_codes:
            objects.append((start, end))
    for start, end in reversed(objects):
        board = board[:start] + board[end:]
    return board, len(objects)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("board", type=Path)
    args = parser.parse_args()
    board = args.board.read_text()
    updated, count = remove_objects(board)
    args.board.write_text(updated)
    print(f"removed_pcie_objects={count}")


if __name__ == "__main__":
    main()
