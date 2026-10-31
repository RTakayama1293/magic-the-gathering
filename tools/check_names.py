#!/usr/bin/env python3
"""Markdown 中の「日本語名（English Name）」の書き方を oracle/cards.csv の日本語名と照らす。

使い方:
    python3 tools/check_names.py            # ARCHIVE/ と oracle/ 以外の .md をすべて調べる
    python3 tools/check_names.py decks/x.md # ファイルを指定して調べる

cards.csv に無い英語名は（tools/name_ignore.txt の語を除き）「未収録」として出す。oracle/lists/ に名前を足して tools/fetch_oracle.py を実行すると収録される。
不一致か未収録が1件でもあれば終了コード1を返す。
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r"([^\s（）()|*`、。,「」《》]+)（([A-Z][A-Za-z0-9',.\- ]+?)）")


def load_cards():
    by_name = {}
    for r in csv.DictReader((ROOT / "oracle" / "cards.csv").open(encoding="utf-8")):
        names = [r["name"], *r["name"].split(" // ")]
        if r["alias"]:
            names.append(r["alias"])
        ja = r["ja_name"].split(" // ")
        for n in names:
            by_name[n] = ja
    return by_name


def load_ignore():
    path = ROOT / "tools" / "name_ignore.txt"
    return {l.split("#", 1)[0].strip() for l in path.read_text(encoding="utf-8").splitlines()} - {""}


def main():
    cards = load_cards()
    ignore = load_ignore()
    files = [Path(a).resolve() for a in sys.argv[1:]] or [
        p for p in ROOT.rglob("*.md")
        if not {"ARCHIVE", "oracle", ".claude", ".git"} & set(p.relative_to(ROOT).parts)
    ]
    problems = 0
    for path in files:
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for ja_written, en in PATTERN.findall(line):
                if en in ignore:
                    continue
                if en not in cards:
                    print(f"{path.relative_to(ROOT)}:{i}: 未収録 {en}（書かれた日本語名: {ja_written}）")
                    problems += 1
                elif not any(j and (ja_written.endswith(j) or j.endswith(ja_written)) for j in cards[en]):
                    print(f"{path.relative_to(ROOT)}:{i}: 不一致 {ja_written}（{en}） -> 正しい日本語名: {' // '.join(cards[en])}")
                    problems += 1
    print(f"問題 {problems}件")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
