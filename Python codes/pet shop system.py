has_license=False
has_space=True
has_experience=False
can_sell_regular_pet=(has_license) or (has_experience)and (has_space)
                                                        
can_sell_exotic_pet= (has_license)and (has_experience)and (has_space)
can_sell_any_pet=(has_license)and (has_experience) or (has_space)
print(f"Can sell regular pet:",can_sell_any_pet)
print(f"Can sell exotic pet:",can_sell_exotic_pet)
print(f"Can sell any pet:",can_sell_any_pet)

