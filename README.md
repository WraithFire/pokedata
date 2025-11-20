# PokeAPI GraphQL Static Website

This is a static website created using responses from the PokeAPI GraphQL API. The GraphQL query `pokemon_details` fetches various details about a Pokémon based on its ID and the game version for moveset details.

## GraphQL Query

```graphql
query pokemon_details($pokemonId: Int, $movesetGame: String) {
    pokemon: pokemon_v2_pokemon(where: { id: { _eq: $pokemonId } }) {
        name
        dex_id: pokemon_species_id
        weight
        height
        exp_yield: base_experience
        abilities: pokemon_v2_pokemonabilities {
            ability: pokemon_v2_ability {
                name
            }
        }
        types: pokemon_v2_pokemontypes {
            type: pokemon_v2_type {
                name
            }
        }
        stats: pokemon_v2_pokemonstats {
            base_stat
            stat: pokemon_v2_stat {
                name
            }
        }
        levelUpMoves: pokemon_v2_pokemonmoves(
            where: {
                pokemon_v2_movelearnmethod: { name: { _eq: "level-up" } }
                pokemon_v2_versiongroup: { name: { _eq: $movesetGame } }
            }
            order_by: { level: asc }
        ) {
            move: pokemon_v2_move {
                name
                power
                type: pokemon_v2_type {
                    name
                }
                category: pokemon_v2_movedamageclass {
                    name
                }
            }
            level
        }
        machineMoves: pokemon_v2_pokemonmoves(
            where: {
                pokemon_v2_movelearnmethod: { name: { _eq: "machine" } }
                pokemon_v2_versiongroup: { name: { _eq: $movesetGame } }
            }
            order_by: { id: asc }
        ) {
            move: pokemon_v2_move {
                name
                power
                type: pokemon_v2_type {
                    name
                }
                category: pokemon_v2_movedamageclass {
                    name
                }
            }
        }
        eggMoves: pokemon_v2_pokemonmoves(
            where: {
                pokemon_v2_movelearnmethod: { name: { _eq: "tutor" } }
                pokemon_v2_versiongroup: { name: { _eq: $movesetGame } }
            }
            order_by: { id: asc }
        ) {
            move: pokemon_v2_move {
                name
                power
                type: pokemon_v2_type {
                    name
                }
                category: pokemon_v2_movedamageclass {
                    name
                }
            }
        }
        specy: pokemon_v2_pokemonspecy {
            evolution_chain: pokemon_v2_evolutionchain {
                id
                species: pokemon_v2_pokemonspecies(order_by: { id: asc }) {
                    name
                    pre_evolution: evolves_from_species_id
                    evolution_condition: pokemon_v2_pokemonevolutions {
                        level: min_level
                        iq: min_happiness
                        item: evolution_item_id
                        held_item: held_item_id
                        trigger: evolution_trigger_id
                        time: time_of_day
                    }
                }
            }
            category: pokemon_v2_pokemonspeciesnames(
                where: { language_id: { _eq: 9 } }
            ) {
                genus
            }
        }
    }
}
```

## Disclaimer
This project uses Pokémon data provided by [PokeAPI](https://pokeapi.co/).
All Pokémon names, data, and related intellectual property are owned by their respective rights holders.
The API data is provided “as is,” and I make no guarantees about its accuracy, completeness, or reliability.
I am not responsible for any issues, errors, or damages resulting from the use of this data or this project.
