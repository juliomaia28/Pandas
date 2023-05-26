import csv

data = [
    ["Por time", "", ""],
    ["Jogador", "Time", ""],
    ["2022-23 Pós-temporada", "", ""],
    ["Líderes Ofensivos", "", ""],
    ["PONTOS", "PTS", ""],
    ["1", "Kawhi Leonard", "LAC", 34.5],
    ["2", "Devin Booker", "PHX", 33.7],
    ["3", "Anthony Edwards", "MIN", 31.6],
    ["4", "Stephen Curry", "GS", 30.5],
    ["5", "Nikola Jokic", "DEN", 29.9],
    ["", "", ""],
    ["ASSISTÊNCIAS", "AST", ""],
    ["1", "Nikola Jokic", "DEN", 10.3],
    ["2", "Trae Young", "ATL", 10.2],
    ["3", "James Harden", "PHI", 8.3],
    ["4", "Jrue Holiday", "MIL", 8.0],
    ["5", "De'Aaron Fox", "SAC", 7.7],
    ["", "", ""],
    ["ARREMESSOS DE 3 PONTOS", "3PM", ""],
    ["1", "Stephen Curry", "GS", 4.4],
    ["2", "Klay Thompson", "GS", 3.8],
    ["3", "Jamal Murray", "DEN", 3.1],
    ["3", "Tyrese Maxey", "PHI", 3.1],
    ["5", "Kawhi Leonard", "LAC", 3.0],
    ["", "", ""],
    ["Líderes Defensivos", "", ""],
    ["REBOTES", "REB", ""],
    ["1", "Anthony Davis", "LAL", 14.1],
    ["2", "Nikola Jokic", "DEN", 13.3],
    ["3", "Kevon Looney", "GS", 13.1],
    ["4", "Rudy Gobert", "MIN", 12.2],
    ["5", "Giannis Antetokounmpo", "MIL", 11.0],
    ["", "", ""],
    ["TOCOS", "BLK", ""],
    ["1", "Anthony Davis", "LAL", 3.1],
    ["2", "Joel Embiid", "PHI", 2.8],
    ["3", "Jaren Jackson Jr.", "MEM", 2.0],
    ["3", "Anthony Edwards", "MIN", 2.0],
    ["5", "Al Horford", "BOS", 1.8],
    ["", "", ""],
    ["ROUBOS", "STL", ""],
    ["1", "De'Aaron Fox", "SAC", 2.1],
    ["1", "Jimmy Butler", "MIA", 2.1],
    ["3", "Kawhi Leonard", "LAC", 2.0],
    ["3", "Dejounte Murray", "ATL", 2.0]
]

filename = "nba_stats.csv"

with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)