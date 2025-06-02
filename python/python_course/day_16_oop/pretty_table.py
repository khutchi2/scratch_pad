from prettytable import PrettyTable


table: PrettyTable = PrettyTable()

pokemon: list[str] = ["Squirtle", "Pikachu", "Charmander"]
type: list[str] = ["Water", "Lightning", "Fire"]

table.add_column("Name", pokemon)
table.add_column("Type", type)
table.align = "l"

print(table)