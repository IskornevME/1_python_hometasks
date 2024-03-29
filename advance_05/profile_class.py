import cProfile
import io
import pstats
import weakref
from random import choice
from memory_profiler import profile


class FootballPlayer:  # pylint: disable=too-few-public-methods
    def __init__(self, country_name=None,
                 pos_name=None, team_name=None,
                 team_sponsor=None):
        self.country = Country(self, country_name)
        self.position = Position(self, pos_name)
        self.team = Team(self, team_name, team_sponsor)


class Country:  # pylint: disable=too-few-public-methods
    def __init__(self, player, country_name):
        self.player = player
        self.country_name = country_name


class Position:  # pylint: disable=too-few-public-methods
    def __init__(self, player, pos_name):
        self.player = player
        self.pos_name = pos_name


class Team:  # pylint: disable=too-few-public-methods
    def __init__(self, player, team_name, team_sponsor):
        self.player = player
        self.team_name = team_name
        self.team_sponsor = team_sponsor


class FootballPlayerSlots:  # pylint: disable=too-few-public-methods
    __slots__ = ("country", "position", "team")

    def __init__(self, country_name=None,
                 pos_name=None, team_name=None,
                 team_sponsor=None):
        self.country = CountrySlots(self, country_name)
        self.position = PositionSlots(self, pos_name)
        self.team = TeamSlots(self, team_name, team_sponsor)


class CountrySlots:  # pylint: disable=too-few-public-methods
    __slots__ = ("player", "country_name")

    def __init__(self, player, country_name):
        self.player = player
        self.country_name = country_name


class PositionSlots:  # pylint: disable=too-few-public-methods
    __slots__ = ("player", "pos_name")

    def __init__(self, player, pos_name):
        self.player = player
        self.pos_name = pos_name


class TeamSlots:  # pylint: disable=too-few-public-methods
    __slots__ = ("player", "team_name", "team_sponsor")

    def __init__(self, player, team_name, team_sponsor):
        self.player = player
        self.team_name = team_name
        self.team_sponsor = team_sponsor


class FootballPlayerWeakref:  # pylint: disable=too-few-public-methods
    def __init__(self, country_name=None,
                 pos_name=None, team_name=None,
                 team_sponsor=None):
        self.country = CountryWeakref(self, country_name)
        self.position = PositionWeakref(self, pos_name)
        self.team = TeamWeakref(self, team_name, team_sponsor)


class CountryWeakref:  # pylint: disable=too-few-public-methods
    def __init__(self, player, country_name):
        self.player = weakref.ref(player)
        self.country_name = country_name


class PositionWeakref:  # pylint: disable=too-few-public-methods
    def __init__(self, player, pos_name):
        self.player = weakref.ref(player)
        self.pos_name = pos_name


class TeamWeakref:  # pylint: disable=too-few-public-methods
    def __init__(self, player, team_name, team_sponsor):
        self.player = weakref.ref(player)
        self.team_name = team_name
        self.team_sponsor = team_sponsor


def random_word(words):
    return choice(words)


@profile
def create(n):
    players_ = [FootballPlayer(countries[i], positions[i], teams[i]) for i in range(n)]
    players_slots_ = [FootballPlayerSlots(countries[i], positions[i], teams[i]) for i in range(n)]
    players_weakref_ = [FootballPlayerWeakref(countries[i], positions[i], teams[i]) for i in range(n)]
    players_[0].position.pos_name += " in team"
    players_slots_[0].position.pos_name += " in team"
    players_weakref_[0].position.pos_name += " in team"
    del players_weakref_


def profile_deco(func):
    prof = cProfile.Profile()
    stats = io.StringIO()
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count, stats, prof
        count += 1
        print(f"Число вызовов функции {func.__name__} =", count)
        prof.enable()

        res = func(*args, **kwargs)

        prof.disable()
        return res

    def print_statisctic():
        sortby = 'cumulative'
        ps_ = pstats.Stats(prof, stream=stats).sort_stats(sortby)
        ps_.print_stats()
        print(stats.getvalue())

    wrapper.print_stat = print_statisctic
    return wrapper


@profile_deco
def simple_class(n):
    players_ = [FootballPlayer(countries[i], positions[i], teams[i]) for i in range(n)]
    return players_


@profile_deco
def slots_class(n):
    players_slots_ = [FootballPlayerSlots(countries[i], positions[i], teams[i]) for i in range(n)]
    return players_slots_


@profile_deco
def weakref_class(n):
    players_weakref_ = [FootballPlayerWeakref(countries[i], positions[i], teams[i]) for i in range(n)]
    return players_weakref_


@profile_deco
def simple_class_get(n):
    for j in range(n):
        ctry_name = players[j].country.country_name
        ctry_name += " "


@profile_deco
def slots_class_get(n):
    for k in range(n):
        ctry_name = players_slots[k].country.country_name
        ctry_name += " "


@profile_deco
def weakref_class_get(n):
    for i in range(n):
        ctry_name = players_weakref[i].country.country_name
        ctry_name += " "


@profile_deco
def simple_class_change(n):
    for i in range(n):
        players[i].position.pos_name += " in team"


@profile_deco
def slots_class_change(n):
    for i in range(n):
        players_slots[i].position.pos_name += " in team"


@profile_deco
def weakref_class_change(n):
    for i in range(n):
        players_weakref[i].position.pos_name += " in team"


@profile_deco
def simple_class_del(n):
    for i in range(n):
        del players[i].position.pos_name


@profile_deco
def slots_class_del(n):
    for i in range(n):
        del players_slots[i].position.pos_name


@profile_deco
def weakref_class_del(n):
    for i in range(n):
        del players_weakref[i].position.pos_name


COUNTRIES = ["England", "France", "Russia", "Spain", "Italy",
             "Brazil", "USA", "Germany", "Argentina", "Belgium"]
POSITIONS = ["Forward", "Goalkeeper", "Defender", "Midfielder"]
TEAMS = ["Barcelona", "Bayern", "Manchester City", "Real",
         "Atletico", "Chelsea", "Arsenal", "Inter", "Juventus"]

N = 100_000

if __name__ == "__main__":
    countries = [random_word(COUNTRIES) for _ in range(N)]
    teams = [random_word(TEAMS) for _ in range(N)]
    positions = [random_word(POSITIONS) for _ in range(N)]
    players = []
    players_slots = []
    players_weakref = []

    create(N)

    for i in range(N):
        players.append(FootballPlayer(countries[i], positions[i], teams[i]))
        players_slots.append(FootballPlayerSlots(countries[i], positions[i], teams[i]))
        players_weakref.append(FootballPlayerWeakref(countries[i], positions[i], teams[i]))
    simple_class(N)
    simple_class.print_stat()
    slots_class(N)
    slots_class.print_stat()
    weakref_class(N)
    weakref_class.print_stat()

    for _ in range(10):
        simple_class_get(N)
    simple_class_get.print_stat()
    for _ in range(10):
        slots_class_get(N)
    slots_class_get.print_stat()
    for _ in range(10):
        weakref_class_get(N)
    weakref_class_get.print_stat()

    for _ in range(10):
        simple_class_change(N)
    simple_class_change.print_stat()
    for _ in range(10):
        slots_class_change(N)
    slots_class_change.print_stat()
    for _ in range(10):
        weakref_class_change(N)
    weakref_class_change.print_stat()

    simple_class_del(N)
    simple_class_del.print_stat()
    slots_class_del(N)
    slots_class_del.print_stat()
    weakref_class_del(N)
    weakref_class_del.print_stat()
