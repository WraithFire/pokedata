# PokeData – Static API

PokeData is a static, **JSON-based** pokémon data API generated using data from the PokeAPI GraphQL endpoint. Each pokémon data is provided as an individual JSON file containing detailed information such as stats, types, abilities, moves, and evolution data.

## Running Locally

This project is a **fully static website** - no backend and no build tools required. You can simply open `index.html` in your browser or serve the files with any static file server.

### Updating the Data

This project includes a Python script (`update_data.py`) that can fetch the latest pokémon data from the pokeAPI and update the JSON files in the `api` folder. To use it, you’ll need **Python** installed along with the required dependencies.

Before running the script, **delete** the existing `api` folder; the script will automatically generate a new one. Make sure to run all commands from **the root** of the project folder.

**Install script dependencies:**

```bash
pip install -r scripts/requirements.txt
```

**Run the update script:**

```bash
python scripts/update_data.py
```

## Disclaimer

This project uses data provided by [PokeAPI](https://pokeapi.co/). All Pokémon names, data, and related intellectual property are owned by **The Pokémon Company**. This is a fan-made project and is not affiliated with The Pokémon Company, Nintendo, Game Freak, or Creatures Inc.

The data is provided “as is,” and I make no guarantees about its accuracy, completeness, or reliability. I am not responsible for any issues, errors, or damages resulting from the use of this data or this project.
