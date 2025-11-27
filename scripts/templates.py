# -------------------------
# GraphQL Queries
# -------------------------

POKEMON_LIST_QUERY = """
query pokemon_name_list {
    pokemon_list: pokemon(order_by: {id: asc}) {
        name
        specy: pokemonspecy {
            gender_rate
        }
        game_list: pokemonmoves(
            distinct_on: version_group_id
            order_by: [{version_group_id: asc}]
        ) {
            game: versiongroup {
                name
            }
        }
    }
}
"""

POKEMON_DATA_QUERY = """
query pokemon_details {
    pokemon: pokemon {
        name
        weight
        height
        exp_yield: base_experience
        abilities: pokemonabilities {
            ability {
                name
            }
        }
        types: pokemontypes {
            type {
                name
            }
        }
        stats: pokemonstats {
            base_stat
            stat {
                name
            }
        }
        levelUpMoves: pokemonmoves(
            where: {movelearnmethod: {name: {_eq: "level-up"}}}
            order_by: {level: asc, version_group_id: asc}
        ) {
            version: versiongroup {
                name
            }
            move {
                name
                power
                type {
                    name
                }
                category: movedamageclass {
                    name
                }
            }
            level
        }
        machineMoves: pokemonmoves(
            where: {movelearnmethod: {name: {_eq: "machine"}}}
            order_by: {id: asc, version_group_id: asc}
        ) {
            version: versiongroup {
                name
            }
            move {
                name
                power
                type {
                    name
                }
                category: movedamageclass {
                    name
                }
            }
        }
        eggMoves: pokemonmoves(
            where: {movelearnmethod: {name: {_eq: "tutor"}}}
            order_by: {id: asc, version_group_id: asc}
        ) {
            version: versiongroup {
                name
            }
            move {
                name
                power
                type {
                    name
                }
                category: movedamageclass {
                    name
                }
            }
        }
        specy: pokemonspecy {
            specy_id: id
            pokedex: pokemondexnumbers(where: {pokedex_id: {_eq: 1}}) {
                pokedex_number
            }
            gender_rate
            category: pokemonspeciesnames(where: {language_id: {_eq: 9}}) {
                genus
            }
            evolution_chain: evolutionchain {
                chain_id: id
                species: pokemonspecies(order_by: {id: asc}) {
                    name
                    pre_evolution: evolves_from_species_id
                    evolution_condition: pokemonevolutions(limit: 1) {
                        evolutiontrigger {
                            name
                        }
                        level: min_level
                        happiness: min_happiness
                        item: evolution_item_id
                        held_item: held_item_id
                        time: time_of_day
                    }
                }
            }
        }
    }
}
"""
# -------------------------
# HTML TEMPLATE
# -------------------------

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
        <title>PokeData</title>
        <meta
            name="description"
            content="A static JSON-based pokemon data API"
        />
        <link rel="stylesheet" href="/styles.css" />
    </head>
    <body>
        <h1>PokeData</h1>
        <div class="grid">
            <a class="card" href="/api/poke-list.json">Poke List</a>
[ANCHORS]
        </div>
        <div class="footer">
            <p>
                This site uses data provided by
                <a target="_blank" href="https://pokeapi.co">PokeAPI</a>. All
                Pokémon names, data, and related intellectual property are owned
                by The Pokémon Company.
            </p>
            <p>
                This is a fan-made site and is not affiliated with The Pokémon
                Company, Nintendo, Game Freak, or Creatures Inc.
            </p>
        </div>
    </body>
</html>
"""
