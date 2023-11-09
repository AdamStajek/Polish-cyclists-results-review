
class DatabaseInsertion:
    def insertData(self, cursor, results_list):
        for result in results_list:
            self.insertCyclists(cursor, result)
            self.insertRaces(cursor, result)
            self.insertResults(cursor, result)

    def insertCyclists(self, cursor, result):
        cursor.execute(f"INSERT INTO public.cyclists(name) "
                       f"SELECT \'{result[0]}\' WHERE NOT EXISTS("
                       f"SELECT name from public.cyclists WHERE name = \'{result[0]}\')")

    def insertRaces(self, cursor, result):
        cursor.execute(f"INSERT INTO public.races(race_name) "
                       f"SELECT \'{result[1]}\' WHERE NOT EXISTS("
                       f"SELECT race_name from public.races WHERE race_name = \'{result[1]}\')")

    def insertResults(self, cursor, result):
        self.timeNoneToNull(result)  # Because None does not function in SQL
        cursor.execute(f"INSERT INTO public.\"Results\" "
                       f"VALUES (DEFAULT, "
                       f"(SELECT id from public.cyclists WHERE public.cyclists.name = \'{result[0]}\'), "  # inserting into main table results
                       f"(SELECT id from public.races WHERE public.races.race_name = \'{result[1]}\'), "
                       f"\'{result[2]}\', "
                       f"\'{result[3]}\')")

    def timeNoneToNull(self, result):
        result[3] = result[3] or "NULL"
