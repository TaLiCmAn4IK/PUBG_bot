import mysql.connector

# Класс Teammate (пока не задействован)
class Teammate:
    def __init__(self, nickname, games, wins):
        self.nickname = nickname
        self.games = games
        self.wins = wins

# Класс Player
class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.games_id = []      # Список идентификаторов игр
        self.teammates = []     # Список объектов Teammate

    def add_teammate(self, teammate):
        if isinstance(teammate, Teammate):
            self.teammates.append(teammate)
        else:
            print("Ошибка: добавляемый объект не является тиммейтом!")

    def add_game_id(self, game_id):
        if game_id in self.games_id:
            print("Этот Id игры уже есть в списке")
        else:
            self.games_id.append(game_id)

    def set_name(self, name):
        self.nickname = name


# Формируем список игроков (объектов класса Player)
players = [
    Player("oran_gg_e"),
    Player("ol1v0CHKA"),
    Player("TexasDolly"),
    Player("magichka_nuar"),
    Player("Shafi____"),
    Player("B1mBOSS"),
    Player("karma-__-"),
    Player("kuatkamiev"),
    Player("TechnicolorBlack"),
    Player("ClickMer"),
    Player("CougarHex"),
    Player("EV0Like"),
    Player("freaky_slider"),
    Player("General-L1"),
    Player("Glenn_ufa"),
    Player("Kingjulyen"),
    Player("levirran"),
    Player("lillypillyhell"),
    Player("Luka_Shymkent"),
    Player("maksason14"),
    Player("MIKHAILB9"),
    Player("Nikita_Kotov17"),
    Player("Rengoku1237"),
    Player("Romzes19"),
    Player("Ryukbtww"),
    Player("Shelby_Young"),
    Player("TaLiCmAn4IK"),
    Player("telnoter"),
    Player("tOKAE-v"),
    Player("TSARrrr"),
    Player("vazgenxer"),
    Player("wii663"),
    Player("Zef1r_off"),
    Player("ZLOY_PISUN"),
    Player("ZRideR59"),
    Player("zZzAlexXxzZz"),
    Player("Meehoa"),
    Player("S0XFATEEV"),
]

# Подключаемся к базе MySQL
cnx = mysql.connector.connect(
    user='Vadim',
    password='7830',
    host='127.0.0.1',
    database='PUBGdatabase'
)
cursor = cnx.cursor()

select_query = "SELECT COUNT(*) FROM players WHERE nickname = %s"

# Команда для вставки
insert_query = "INSERT INTO players (nickname) VALUES (%s)"

for p in players:
    # Сначала проверяем, есть ли такой никнейм
    cursor.execute(select_query, (p.nickname,))
    count = cursor.fetchone()[0]

    if count == 0:
        # Никнейм не встречается, вставляем
        cursor.execute(insert_query, (p.nickname,))
        cnx.commit()
        print(f"Ник {p.nickname} добавлен.")
    else:
        # Уже есть такой ник
        print(f"Ник {p.nickname} уже существует, пропускаем.")

# Фиксируем изменения в базе
cnx.commit()

cursor.close()
cnx.close()

print("Все игроки добавлены в таблицу players.")
