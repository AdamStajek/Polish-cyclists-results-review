
# inserting results to database
def insertion(results_list, cursor):
    for result in results_list:
        cursor.execute(f"INSERT INTO public.cyclists(name) SELECT \'{result[0]}\' "
                       f" WHERE NOT EXISTS(SELECT name from public.cyclists WHERE name = \'{result[0]}\')")  # inserting into table cyclists
        cursor.execute(f"INSERT INTO public.races(race_name) SELECT \'{result[1]}\' "
                       f" WHERE NOT EXISTS(SELECT race_name from public.races WHERE race_name = \'{result[1]}\')")  # inserting into table races
        if result[2] == "DNF" or result[2] == "DNS" or result[2] == "OOT":
            cursor.execute(f"INSERT INTO public.\"Results\" "
                           f"VALUES (DEFAULT, "
                           f"(SELECT id from public.cyclists WHERE public.cyclists.name = \'{result[0]}\'), "  # inserting into main table results
                           f"(SELECT id from public.races WHERE public.races.race_name = \'{result[1]}\'), "
                           f"\'{result[2]}\', "
                           f"\'NULL\')")
        else:
            cursor.execute(f"INSERT INTO public.\"Results\" "
                           f"VALUES (DEFAULT, "
                           f"(SELECT id from public.cyclists WHERE public.cyclists.name = \'{result[0]}\'), "
                           f"(SELECT id from public.races WHERE public.races.race_name = \'{result[1]}\'), "
                           f"\'{result[2]}.\', "
                           f"\'{result[3]}\')")