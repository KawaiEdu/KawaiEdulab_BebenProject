MLBB_dict = {
    "Mage": "a hero who use magic power and some has high mobility a mage is very usefull in a game that can do burst damage and has a good HP for team figth as they can do a combo with the marksman or the assasin with their combined phisical and magical damage",
    "fighter": "a hero who has a close range figthing style and a couple hero has high very high durabilirty and high spellvamp like ruby, yu zhong, lapu-lapu, benedeta ,alpha, terizla and more. and some hero have very high mobility like benedeta,sun,zilong,cici and yu zhong nad some have high attack speed like zilong, sun, thamus, freya and more",
    "marksman": "a hero who has a long range figthing style and have high damage and lifesteal and critical but have very low HP and is one of the most usefull role in the game as they can carry to late game if in tghe rigth hand",
    "support": "a hero who have the ability to heal others teammate and can stun he enemy they are not very meta but if the pick is rigth then the support role is very usefull if used rigth",
    "tank": "a hero who has a high durability and HP and tanks have a lot of CC or crowd control and is very usefull in game as they can defend their team and protect them from death",
    "assasin": "a hero who has a big damage and easy to pick off the enemy and has a high mobility but low HP assasin is more recommended in the jungle and not in any lane because of thir low HP"
}

search = input("masukan role yang ingin di cari ")
if search in MLBB_dict:
    print(f"{search} di temukan dalam kamus {MLBB_dict[search]}")
else:
    print(f"{search} tidak di temukan dalam kamus")