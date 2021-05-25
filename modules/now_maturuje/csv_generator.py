
import csv

schedule = {
    1: [
        ["Jakub Šépka", "čj", 8, 0],
        ["Štěpán Pechman", "m", 8, 15],
        ["Šimon Taněv", "m", 8, 30],
        ["Emma Sternbergová", "m", 8, 45],
        ["Anaïs Ariadne Dix", "bi", 9, 0],
        ["Adéla Škvorová", "bi", 9, 15],
        ["Hana Tvrdá", "bi", 9, 30],
        ["Barbora Lubovská", "bi", 9, 45],
        ["Emma Sternbergová", "bi", 10, 0],
        ["Jakub Šépka", "bi", 10, 15],
        ["Anaïs Ariadne Dix", "ch", 10, 30],
        ["Adéla Škvorová", "ch", 10, 45],
        ["Hana Tvrdá", "ch", 11, 00],
        ["Barbora Lubovská", "ch", 11, 15],
        ["Emma Sternbergová", "ch", 11, 30],
        ["Jakub Šépka", "ch", 11, 45],
        ["Anaïs Ariadne Dix", "fj", 12, 30],
        ["Jakub Šépka", "aj", 12, 45],
        ["Adéla Škvorová", "aj", 13, 00],
        ["Štěpán Pechman", "aj", 13, 15],
        ["Šimon Taněv", "aj", 13, 30],
        ["Barbora Lubovská", "aj", 13, 45],
        ["Emma Sternbergová", "aj", 14, 00],
        ["Hana Tvrdá", "aj", 14, 15],
        ["Anaïs Ariadne Dix", "čj", 14, 35],
        ["Adéla Škvorová", "čj", 14, 55],
        ["Barbora Lubovská", "čj", 15, 15],
        ["Emma Sternbergová", "čj", 15, 35],
        ["Štěpán Pechman", "ivt", 15, 55],
        ["Šimon Taněv", "ivt", 16, 20]
    ],
    2: [
        ["Veronika Lišková", "ch", 7, 45],
        ["Dominik Soudil", "ch", 8, 00],
        ["Matěj Havlík", "ch", 8, 15],
        ["Michal Hložánek", "ch", 8, 30],
        ["Diana Katlinskaya", "ch", 8, 45],
        ["Helena Kouwen", "ch", 9, 0],
        ["Jasmína Branná", "ch", 9, 15],
        ["Vojtěch Boháček", "ch", 9, 30],
        ["Dominik Soudil", "bi", 9, 45],
        ["Matěj Havlík", "bi", 10, 0],
        ["Veronika Lišková", "bi", 10, 15],
        ["Diana Katlinskaya", "bi", 10, 30],
        ["Michal Hložánek", "bi", 10, 45],
        ["Helena Kouwen", "bi", 11, 0],
        ["Jasmína Branná", "bi", 11, 15],
        ["Vojtěch Boháček", "nj", 11, 30],
        ["Veronika Lišková", "nj", 11, 45],
        ["Dominik Soudil", "nj", 12, 00],
        ["Matěj Havlík", "aj", 12, 55],
        ["Michal Hložánek", "aj", 13, 10],
        ["Helena Kouwen", "aj", 13, 25],
        ["Jasmína Branná", "aj", 13, 40],
        ["Veronika Lišková", "čj", 14, 00],
        ["Dominik Soudil", "čj", 14, 20],
        ["Matěj Havlík", "čj", 14, 40],
        ["Michal Hložánek", "čj", 15, 00],
        ["Helena Kouwen", "čj", 15, 20],
        ["Jasmína Branná", "čj", 15, 40],
        ["Vojtěch Boháček", "čj", 16, 00]
    ],
    3: [
        ["Michal Poskočil", "aj", 7, 45],
        ["Eliška Kurečková", "aj", 8, 00],
        ["Martin Korba", "aj", 8, 15],
        ["Lea Bilá", "aj", 8, 30],
        ["Martin Vidmar", "aj", 8, 45],
        ["Matyáš Valigura", "aj", 9, 0],
        ["Michal Poskočil", "fy", 9, 15],
        ["Eliška Kurečková", "fy", 9, 30],
        ["Martin Korba", "fy", 9, 45],
        ["Lea Bilá", "zsv", 10, 5],
        ["Eva Závadová", "zsv", 10, 30],
        ["Jan Herczeg", "zsv", 10, 50],
        ["Dominika Hörnerová", "zsv", 11, 45],
        ["Eva Závadová", "nj", 12, 45],
        ["Jan Herczeg", "nj", 13, 00],
        ["Dominika Hörnerová", "aj", 13, 15],
        ["Eva Závadová", "aj", 13, 30],
        ["Jan Herczeg", "aj", 13, 45],
        ["Matyáš Valigura", "čj", 14, 5],
        ["Martin Korba", "čj", 14, 25],
        ["Eva Závadová", "čj", 14, 45],
        ["Dominika Hörnerová", "vv", 15, 5],
        ["Martin Vidmar", "ivt", 15, 30],
        ["Matyáš Valigura", "dg", 15, 55]
    ],
    4: [
        ["Natalia Eiseltová", "nj", 8, 00],
        ["Klára Sieglová", "nj", 8, 15],
        ["Klára Jeřábková", "nj", 8, 30],
        ["Anton Achedžak", "nj", 8, 45],
        ["Anna Adelaide Leschová", "d", 9, 0],
        ["Klára Maříková", "čj", 9, 20],
        ["Klára Sieglová", "čj", 9, 40],
        ["Marlene Kenclová", "čj", 10, 0],
        ["Anna Adelaide Leschová", "čj", 10, 20],
        ["Klára Jeřábková", "aj", 10, 35],
        ["Natalia Eiseltová", "aj", 10, 50],
        ["Klára Sieglová", "aj", 11, 5],
        ["Anna Adelaide Leschová", "aj", 11, 20],
        ["Klára Maříková", "hv", 11, 45],
        ["Marlene Kenclová", "aj", 12, 45],
        ["Anton Achedžak", "aj", 13, 0],
        ["Natalia Eiseltová", "bi", 13, 15],
        ["Klára Jeřábková", "z", 13, 30],
        ["Klára Sieglová", "z", 13, 45],
        ["Marlene Kenclová", "z", 14, 0],
        ["Anna Adelaide Leschová", "z", 14, 15],
        ["Klára Maříková", "tv", 14, 40]
    ]
}

with open("schedule.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    for key in schedule:
        
        writer.writerow([str(key)] + schedule[key][0]) # první řádek ze dne obsahuje info o dni

        for row in schedule[key][1:]:
            writer.writerow([""] + row) # další řádky bez info o dni