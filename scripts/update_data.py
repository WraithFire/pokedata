import shutil
import orjson
import requests
from pathlib import Path
from templates import POKEMON_LIST_QUERY, POKEMON_DATA_QUERY, HTML_TEMPLATE

# -------------------------
# Config
# -------------------------

JSON_DIR = Path("api")

GRAPHQL_URL = "https://graphql.pokeapi.co/v1beta2"

STATIC_URL = "https://pokedata.pages.dev/api/poke-list.json"

# -------------------------
# Utility Functions
# -------------------------


def canonical_json(data: dict) -> bytes:
    return orjson.dumps(data, option=orjson.OPT_SORT_KEYS)


def fetch_from_api(url: str, query: str):
    try:
        if query:
            response = requests.post(url, json={"query": query}, timeout=120)
        else:
            response = requests.get(url, timeout=60)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, dict) and "errors" in data:
            raise RuntimeError(f"Errors: {data['errors']}")
        return data
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return None


def save_json(path: Path, data: dict):
    options = orjson.OPT_INDENT_2
    path.write_bytes(orjson.dumps(data, option=options))


def make_anchor_tag(name: str) -> str:
    name_parts = name.split("-")
    title_case = "-".join(part.capitalize() for part in name_parts)
    return f'            <a class="card" href="/api/{name}.json">{title_case}</a>'


# -------------------------
# Main Logic
# -------------------------


def main_function():
    # Fetch Pokemon list
    static_poke_list_data = fetch_from_api(STATIC_URL, None)
    graphql_poke_list_data = fetch_from_api(GRAPHQL_URL, POKEMON_LIST_QUERY)

    # Handle first run and exit early on errors or no changes
    if not JSON_DIR.is_dir():
        print("✅ First run — no api folder found.")

        if graphql_poke_list_data is None:
            print("❌ Can't fetch pokemon list — Exiting")
            return
    elif static_poke_list_data is None or graphql_poke_list_data is None:
        print("❌ Unable to Compare — Exiting.")
        return
    elif canonical_json(static_poke_list_data) == canonical_json(
        graphql_poke_list_data
    ):
        print("✅ No changes detected — Exiting.")
        return

    # Fetch Pokemon Data
    pokemon_data = fetch_from_api(GRAPHQL_URL, POKEMON_DATA_QUERY)

    if pokemon_data is None:
        print("❌ Can't fetch pokemon data — Exiting.")
        return

    # Reset API folder
    if JSON_DIR.is_dir():
        shutil.rmtree(JSON_DIR)
        print("✅ Deleted old api folder")

    JSON_DIR.mkdir()

    # Save Pokemon list
    save_json(JSON_DIR / "poke-list.json", graphql_poke_list_data)
    print("✅ Pokemon list updated")

    # Save Pokemon Data JSON files
    pokemon_list = pokemon_data["data"]["pokemon"]

    for i, pokemon in enumerate(pokemon_list, start=1):
        name = pokemon["name"]
        output_data = {"data": {"pokemon": [pokemon]}}
        save_json(JSON_DIR / f"{name}.json", output_data)

        if i % 100 == 0:
            print(f"{i} Pokemon processed...")

    print("✅ Pokemon data updated")

    # Update HTML
    anchor_tags = "\n".join(
        make_anchor_tag(p["name"])
        for p in graphql_poke_list_data["data"]["pokemon_list"]
    )

    final_html = HTML_TEMPLATE.replace("[ANCHORS]", anchor_tags)

    Path("index.html").write_text(final_html, encoding="utf-8")

    print("✅ index.html updated")


if __name__ == "__main__":
    main_function()
