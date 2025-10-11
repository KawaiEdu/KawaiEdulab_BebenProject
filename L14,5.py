MLBB_hero = {
    "ruby": "a fighter hero who has a high durability and spellvamp and is very good in team fight ruby can play as an explaner,roamer and a goldlaner",
    "cici": "cici is a figther  heo who has high mobility and a good amount of spellvamp and has a good HP for and can be good for team figth cici can be played in explaner and jungler",
    "terizla": "a figther hero who has a slow movement speed but a good amount of damage and has good amount of CC and spellvamp and can be played as an expaner or a midlaner",
    "benedetta": "a hero who has a huge mobility and a high burst damage and has a good spellvamp but a low HP but very good for teamfights and good for killing low HP hero" 
}

search = input("masukan hero yang ingin di cari ")
if search in MLBB_hero:
    print(f"{search} di temukan dalam kamus {MLBB_hero[search]}")
else:
    print(f"{search} tidak di temukan dalam kamus")