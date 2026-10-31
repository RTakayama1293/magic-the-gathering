#!/usr/bin/env python3
"""Scryfall からカードのオラクルテキストと日本語名を取得し、oracle/cards.csv と oracle/cards.md を作り直す。

対象カードは次の2か所から集める。
- decks/*.md のコードブロック内の「枚数 カード名」の行（現行デッキの75枚）
- oracle/lists/*.txt の1行1枚のカード名（相手デッキ・新カード候補など。# 以降はコメント）

使い方:
    python3 tools/fetch_oracle.py

日本語名は日本語版の印刷があるカードだけ入る。無いカード（Arena専用、日本語版未発売など）は空欄になる。
"""
import csv
import datetime
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.scryfall.com"
HEADERS = {"User-Agent": "mtg-pioneer-repo/1.0", "Accept": "application/json"}
WAIT = 0.12  # Scryfall の推奨（1秒10リクエスト以下）


def request(url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    headers = dict(HEADERS)
    if data:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers)
    time.sleep(WAIT)
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            return json.load(res)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def collect_names():
    """カード名 -> 出どころのリスト名（deck:ファイル名 / list:ファイル名）"""
    sources = {}
    for path in sorted((ROOT / "decks").glob("*.md")):
        in_block = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("```"):
                in_block = not in_block
                continue
            m = re.match(r"^\s*(\d+)\s+(.+?)\s*$", line) if in_block else None
            if m:
                sources.setdefault(m.group(2), []).append(f"deck:{path.stem}")
    for path in sorted((ROOT / "oracle" / "lists").glob("*.txt")):
        for line in path.read_text(encoding="utf-8").splitlines():
            name = line.split("#", 1)[0].strip()
            if name:
                sources.setdefault(name, []).append(f"list:{path.stem}")
    return sources


def fetch_cards(names):
    """/cards/collection で英語版を75枚ずつ取得する。見つからない名前は not_found に入れる。"""
    found, not_found = {}, []
    names = list(names)
    for i in range(0, len(names), 75):
        chunk = names[i:i + 75]
        res = request(f"{API}/cards/collection", {"identifiers": [{"name": n} for n in chunk]})
        for card in res["data"]:
            found[card["name"]] = card
        for ident in res.get("not_found", []):
            # Arena やユニバース・ビヨンドの別名（例: Exclusive Nightclub = Oscorp Industries）は曖昧検索で引く
            card = request(f"{API}/cards/named?" + urllib.parse.urlencode({"fuzzy": ident["name"]}))
            if card:
                card["_alias"] = ident["name"]
                found[card["name"]] = card
            else:
                not_found.append(ident["name"])
    return found, not_found


def match_input(card_name, input_names):
    """入力名（両面カードの表面だけ等）と Scryfall の正式名を対応づける。"""
    if card_name in input_names:
        return card_name
    front = card_name.split(" // ")[0]
    for n in input_names:
        if n == front or n.lower() == card_name.lower() or n.lower() == front.lower():
            return n
    return None


def strip_ruby(name):
    """「量（りょう）子（し）」のようなふりがな付きの印刷名から、ふりがなを除く。"""
    return re.sub(r"（[ぁ-ゖー]+）", "", name)


def fetch_japanese_name(card):
    q = f'oracleid:{card["oracle_id"]} lang:ja'
    url = f"{API}/cards/search?" + urllib.parse.urlencode({"q": q, "unique": "prints", "order": "released"})
    res = request(url)
    if not res or not res.get("data"):
        return ""
    # 最新の印刷の日本語名を使う。両面カードは面ごとの名前を // でつなぐ
    for c in res["data"]:
        if c.get("printed_name"):
            return strip_ruby(c["printed_name"])
        faces = c.get("card_faces") or []
        names = [f.get("printed_name") for f in faces if f.get("printed_name")]
        if names:
            return strip_ruby(" // ".join(names))
    return ""


def on_arena(card):
    """どれか1つの印刷が MTG Arena にあれば yes。collection が返す印刷だけでは判定できない。"""
    q = f'oracleid:{card["oracle_id"]} game:arena'
    res = request(f"{API}/cards/search?" + urllib.parse.urlencode({"q": q, "unique": "prints"}))
    return "yes" if res and res.get("data") else "no"


def face_fields(card):
    faces = card.get("card_faces")
    if faces and "oracle_text" in faces[0]:
        parts = []
        for f in faces:
            pt = f"{f['power']}/{f['toughness']}" if "power" in f else (f"忠誠{f['loyalty']}" if "loyalty" in f else "")
            parts.append({
                "name": f["name"], "mana_cost": f.get("mana_cost", ""), "type_line": f.get("type_line", ""),
                "pt": pt, "oracle_text": f.get("oracle_text", ""),
            })
        return parts
    pt = f"{card['power']}/{card['toughness']}" if "power" in card else (f"忠誠{card['loyalty']}" if "loyalty" in card else "")
    return [{
        "name": card["name"], "mana_cost": card.get("mana_cost", ""), "type_line": card.get("type_line", ""),
        "pt": pt, "oracle_text": card.get("oracle_text", ""),
    }]


def main():
    sources = collect_names()
    if not sources:
        sys.exit("対象カードがない")
    found, not_found = fetch_cards(sources.keys())
    today = datetime.date.today().isoformat()

    rows = []
    for name, card in found.items():
        input_name = card.get("_alias") or match_input(name, sources.keys())
        faces = face_fields(card)
        rows.append({
            "name": name,
            "ja_name": fetch_japanese_name(card),
            "alias": card.get("_alias", ""),
            "mana_cost": " // ".join(f["mana_cost"] for f in faces if f["mana_cost"]),
            "cmc": card.get("cmc", ""),
            "type_line": card.get("type_line", ""),
            "pt": " // ".join(f["pt"] for f in faces if f["pt"]),
            "oracle_text": "\n//\n".join(f"{f['name']}: {f['oracle_text']}" if len(faces) > 1 else f["oracle_text"] for f in faces),
            "pioneer": card["legalities"].get("pioneer", ""),
            "arena": on_arena(card),
            "set": card.get("set", "").upper(),
            "released_at": card.get("released_at", ""),
            "sources": ";".join(sorted(set(sources.get(input_name or name, [])))),
            "scryfall_uri": card.get("scryfall_uri", "").split("?")[0],
            "fetched": today,
        })
    rows.sort(key=lambda r: r["name"])

    out_csv = ROOT / "oracle" / "cards.csv"
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    out_md = ROOT / "oracle" / "cards.md"
    lines = [
        "# カードテキスト一覧",
        "",
        f"`tools/fetch_oracle.py` が Scryfall から {today} に取得した。手で編集しない（次の実行で上書きされる）。",
        "日本語名が空欄のカードは日本語版の印刷が無い。カード名を書くときは英語名だけを使う。",
        "",
    ]
    for r in rows:
        title = f"{r['ja_name']}（{r['name']}）" if r["ja_name"] else r["name"]
        if r["alias"]:
            title += f"　別名: {r['alias']}"
        legal = f"Pioneer: {r['pioneer']} / Arena収録: {r['arena']}"
        lines += [
            f"## {title}",
            "",
            f"{r['mana_cost']}　{r['type_line']}" + (f"　{r['pt']}" if r["pt"] else ""),
            "",
            "```",
            r["oracle_text"],
            "```",
            "",
            f"{legal}　出どころ: {r['sources']}　{r['scryfall_uri']}",
            "",
        ]
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"取得: {len(rows)}枚 -> {out_csv.relative_to(ROOT)}, {out_md.relative_to(ROOT)}")
    banned = [r for r in rows if r["pioneer"] != "legal" and any(s.startswith("deck:") for s in r["sources"].split(";"))]
    for r in banned:
        print(f"注意: デッキのカードがパイオニアで {r['pioneer']}: {r['name']}")
    if not_found:
        print("Scryfall で見つからなかった名前（綴りを直す）:")
        for n in not_found:
            print(f"  {n}")
        sys.exit(1)


if __name__ == "__main__":
    main()
