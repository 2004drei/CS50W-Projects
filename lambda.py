hero_leaders = [{"name":"Steve Rogers","hero group":"Avengers"},
          {"name":"Reed Richards","hero group":"Fantastic Four"},
          {"name":"Scott Summers","hero group":"X-Men"}
]

hero_leaders.sort(key=lambda hero: hero["hero group"])

print(hero_leaders)
