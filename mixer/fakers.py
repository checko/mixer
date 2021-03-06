""" Generate fake data.

Functions for generation some kind of fake datas. You can use ``mixer.fakers``
by manual, like this:

::

    from mixer import fakers as f

    name = f.get_name()
    country = f.get_country()

    url_gen = f.gen_url()(hostname=True)
    urls = [next(url_gen) for _ in range(10)]

"""

from . import generators as g
import random
import uuid
import decimal

DEFAULT_NAME_MASK = "{firstname} {lastname}"

FIRSTNAME_CHOICES = (
    "Adams", "Allen", "Anderson", "Baker", "Barbara", "Betty", "Brown",
    "Campbell", "Carol", "Carter", "Clark", "Collins", "Davis", "Deborah",
    "Donna", "Dorothy", "Edwards", "Elizabeth", "Evans", "Garcia", "Gonzalez",
    "Green", "Hall", "Harris", "Helen", "Hernandez", "Hill", "Jackson",
    "Jennifer", "Johnson", "Jones", "Karen", "Kimberly", "King", "Laura",
    "Lee", "Lewis", "Linda", "Lisa", "Lopez", "Margaret", "Maria", "Martin",
    "Martinez", "Mary", "Michelle", "Miller", "Mitchell", "Moore", "Nancy",
    "Nelson", "Parker", "Patricia", "Perez", "Phillips", "Roberts", "Robinson",
    "Rodriguez", "Ruth", "Sandra", "Sarah", "Scott", "Sharon", "Smith",
    "Susan", "Taylor", "Thomas", "Thompson", "Turner", "Walker", "White",
    "Williams", "Wilson", "Wright", "Young",
)

LASTNAME_CHOICES = (
    "Allen", "Anderson", "Angelo", "Baker", "Bell", "Boulstridge", "Bungard",
    "Bursnell", "Cabrera", "Carlisle", "Carlisle", "Cart", "Chaisty", "Clark",
    "Clayworth", "Colchester", "Cooper", "Darlington", "Davis", "Denial",
    "Derby", "Dissanayake", "Domville", "Dorchester", "Dua", "Dudley",
    "Dundee", "Dundee", "Durham", "Edeson", "Galashiels", "Galashiels",
    "Galashiels", "Garrott", "Gaspar", "Gauge", "Gelson", "Gloucester",
    "Happer", "Harris", "Harrison", "Harrow", "Hawa", "Helling",
    "Hollingberry", "Howsham", "Huddersfield", "Husher", "Ipswich", "James",
    "Khambaita", "Kilmarnok", "King", "Kinlan", "Le", "Leatherby", "Lee",
    "Leicester", "Lerwick", "Lerwick", "Lerwick", "Lincoln", "Llandrindod",
    "Llandrindod", "Llandudno", "Llandudno", "Llandudno", "Llandudno",
    "Llandudno", "London", "Lowsley", "Mardling", "Martin", "McCalman",
    "McKiddie", "McQuillen", "Meath", "Mitchell", "Moore", "Morgan", "Morris",
    "Mustow", "Nana", "Newcastle", "Newport", "Norwich", "Norwich", "Oldham",
    "Parker", "Patel", "Pepall", "Perdue", "Phillips", "Ravensdale", "Rukin",
    "Selvaratnam", "Shelsher", "Shrewsbury", "Silsbury", "Smih", "Southway",
    "Sunderland", "Swansea", "Swansea", "Swansea", "Swansea", "Swansea",
    "Taunton", "Upadhyad", "Valji", "Virji", "Wadd", "Wakefield", "Walsall",
    "Ward", "Watson", "Weild", "Wigan", "Witte", "Wolverhampton", "York",
)

COUNTRY_CHOICES = (
    "Afghanistan", "Algeria", "Argentina", "Canada", "Colombia", "Ghana",
    "Iraq", "Kenya", "Malaysia", "Morocco", "Mozambique", "Nepal", "Peru",
    "Poland", "Sudan", "Uganda", "Ukraine", "Uzbekistan", "Venezuela", "Yemen",
    'Bangladesh', 'Brazil', 'Burma', 'China', 'Egypt', 'Ethiopia', 'France',
    'Germany', 'India', 'Indonesia', 'Iran', 'Italy', 'Japan', 'Mexico',
    'Nigeria', 'Pakistan', 'Philippines', 'Russia', 'South Africa', 'Spain',
    'Tanzania', 'Thailand', 'Turkey', 'United Kingdom', 'United States',
    'Vietnam',
)

CITY_PREFIX_CHOICES = ("North", "East", "West", "South", "New", "Lake", "Port")

CITY_SUFFIX_CHOICES = (
    "town", "ton", "land", "ville", "berg", "burgh", "borough", "bury", "view",
    "port", "mouth", "stad", "furt", "chester", "mouth", "fort", "haven",
    "side", "shire"
)

LOREM_CHOICES = (
    "alias", "consequatur", "aut", "perferendis", "sit", "voluptatem",
    "accusantium", "doloremque", "aperiam", "eaque", "ipsa", "quae", "ab",
    "illo", "inventore", "veritatis", "et", "quasi", "architecto", "beatae",
    "vitae", "dicta", "sunt", "explicabo", "aspernatur", "aut", "odit", "aut",
    "fugit", "sed", "quia", "consequuntur", "magni", "dolores", "eos", "qui",
    "ratione", "voluptatem", "sequi", "nesciunt", "neque", "dolorem", "ipsum",
    "quia", "dolor", "sit", "amet", "consectetur", "adipisci", "velit", "sed",
    "quia", "non", "numquam", "eius", "modi", "tempora", "incidunt", "ut",
    "labore", "et", "dolore", "magnam", "aliquam", "quaerat", "voluptatem",
    "ut", "enim", "ad", "minima", "veniam", "quis", "nostrum",
    "exercitationem", "ullam", "corporis", "nemo", "enim", "ipsam",
    "voluptatem", "quia", "voluptas", "sit", "suscipit", "laboriosam", "nisi",
    "ut", "aliquid", "ex", "ea", "commodi", "consequatur", "quis", "autem",
    "vel", "eum", "iure", "reprehenderit", "qui", "in", "ea", "voluptate",
    "velit", "esse", "quam", "nihil", "molestiae", "et", "iusto", "odio",
    "dignissimos", "ducimus", "qui", "blanditiis", "praesentium", "laudantium",
    "totam", "rem", "voluptatum", "deleniti", "atque", "corrupti", "quos",
    "dolores", "et", "quas", "molestias", "excepturi", "sint", "occaecati",
    "cupiditate", "non", "provident", "sed", "ut", "perspiciatis", "unde",
    "omnis", "iste", "natus", "error", "similique", "sunt", "in", "culpa",
    "qui", "officia", "deserunt", "mollitia", "animi", "id", "est", "laborum",
    "et", "dolorum", "fuga", "et", "harum", "quidem", "rerum", "facilis",
    "est", "et", "expedita", "distinctio", "nam", "libero", "tempore", "cum",
    "soluta", "nobis", "est", "eligendi", "optio", "cumque", "nihil",
    "impedit", "quo", "porro", "quisquam", "est", "qui", "minus", "id", "quod",
    "placeat", "facere", "possimus", "omnis", "voluptas", "assumenda", "est",
    "omnis", "dolor", "repellendus", "temporibus", "autem", "quibusdam", "et",
    "aut", "consequatur", "vel", "illum", "qui", "dolorem", "eum", "fugiat",
    "quo", "voluptas", "nulla", "pariatur", "at", "vero", "eos", "et",
    "accusamus", "officiis", "debitis", "aut", "rerum", "necessitatibus",
    "saepe", "eveniet", "ut", "et", "voluptates", "repudiandae", "sint", "et",
    "molestiae", "non", "recusandae", "itaque", "earum", "rerum", "hic",
    "tenetur", "a", "sapiente", "delectus", "ut", "aut", "reiciendis",
    "voluptatibus", "maiores", "doloribus", "asperiores", "repellat", "maxime",
)


HOSTNAMES = (
    "facebook", "google", "youtube", "yahoo", "baidu", "wikipedia", "amazon",
    "qq", "live", "taobao", "blogspot", "linkedin", "twitter", "bing",
    "yandex", "vk", "msn", "ebay", "163", "wordpress", "ask", "weibo", "mail",
    "microsoft", "hao123", "tumblr", "xvideos", "googleusercontent", "fc2"
)

HOSTZONES = (
    "aero", "asia", "biz", "cat", "com", "coop", "info", "int", "jobs", "mobi",
    "museum", "name", "net", "org", "post", "pro", "tel", "travel", "xxx",
    "edu", "gov", "mil", "eu", "ee", "dk", "de", "ch", "bg", "vn", "tw", "tr",
    "tm", "su", "si", "sh", "se", "pt", "ar", "pl", "pe", "nz", "my", "it",
    "gr", "fr", "pm", "re", "tf", "wf", "yt", "fi", "br", "ac", "ru", "cn"
)

USERNAMES = (
    "admin", "akholic", "ass", "bear", "bee", "beep", "blood", "bone", "boots",
    "boss", "boy", "boyscouts", "briefs", "candy", "cat", "cave", "climb",
    "cookie", "cop", "crunching", "daddy", "diller", "dog", "fancy", "gamer",
    "garlic", "gnu", "hot", "jack", "job", "kicker", "kitty", "lemin", "lol",
    "lover", "low", "mix", "mom", "monkey", "nasty", "new", "nut", "nutjob",
    "owner", "park", "peppermint", "pitch", "poor", "potato", "prune",
    "raider", "raiser", "ride", "root", "scull", "shattered", "show", "sleep",
    "sneak", "spamalot", "star", "table", "test", "tips", "user", "ustink",
    "weak"
)

COMPANY_SYFFIXES = ('LLC', 'Group', 'LTD', 'PLC', 'LLP', 'Corp', 'Inc', 'DBA')

GEOCOORD_MASK = decimal.Decimal('.000001')


def get_firstname(**kwargs):
    """ Get a first name.

    :return str:

    ::
        print get_firstname()  # -> Johnson

    """
    return g.get_choice(FIRSTNAME_CHOICES)

#: Generator's fabric for :meth:`mixer.fakers.get_firstname`
gen_firstname = g.loop(get_firstname)


def get_lastname(**kwargs):
    """ Get a last name.

    :return str:

    ::
        print get_lastname()  # -> Gaspar

    """
    return g.get_choice(LASTNAME_CHOICES)

#: Generator's fabric for :meth:`mixer.fakers.get_lastname`
gen_lastname = g.loop(get_lastname)


def get_name(mask=DEFAULT_NAME_MASK, length=100, **kwargs):
    """ Get a full name.

    :return str:

    ::
        print get_name()  # -> Barbara Clayworth

    """
    name = mask.format(firstname=get_firstname(), lastname=get_lastname())
    return name[:length]

#: Generator's fabric for :meth:`mixer.fakers.get_lastname`
gen_name = g.loop(get_name)


def get_country(**kwargs):
    """ Get a country.

    :return str:

    ::
        print get_country()  # -> Italy

    """
    return g.get_choice(COUNTRY_CHOICES)

#: Generator's fabric for :meth:`mixer.fakers.get_country`
gen_country = g.loop(get_country)


def get_city(**kwargs):
    """ Get a city.

    :return str:

    ::
        print get_city()  # -> North Carter

    """
    return g.get_choice((
        "{0} {1}".format(g.get_choice(CITY_PREFIX_CHOICES), get_firstname()),
        "{0} {1}".format(get_lastname(), g.get_choice(CITY_SUFFIX_CHOICES)),
    ))

#: Generator's fabric for :meth:`mixer.fakers.get_city`
gen_city = g.loop(get_city)


def get_lorem(length=None, **kwargs):
    """ Get a text (based on lorem ipsum.

    :return str:

    ::
        print get_lorem()  # -> atque rerum et aut reiciendis...

    """
    lorem = ' '.join(g.get_choices(LOREM_CHOICES))
    if length:
        lorem = lorem[:length]
    return lorem

#: Generator's fabric for :meth:`mixer.fakers.get_lorem`
gen_lorem = g.loop(get_lorem)


def get_numerify(template='', symbol='#', **kwargs):
    """ Generate number string from templates.

    :return str:

    ::
        print get_numerify('####-##')  # -> 2345-23

    """
    return ''.join(
        (str(random.randint(0, 10)) if c == '#' else c)
        for c in template
    )

#: Generator's fabric for :meth:`mixer.fakers.get_numerify`
gen_numerify = g.loop(get_numerify)


def get_username(length=100, **kwargs):
    """ Get a username.

    :return str:

    ::
        print get_username()  # -> boss1985

    """
    gen = g.gen_choice(USERNAMES)
    params = dict(
        one=next(gen),
        two=next(gen),
        num=g.get_integer(low=1900, high=2020),
    )
    username = g.get_choice((
        '{one}_{two}'.format(**params),
        '{one}.{two}'.format(**params),
        '{two}{one}{num}'.format(**params),
    ))
    return username[:length]

#: Generator's fabric for :meth:`mixer.fakers.get_username`
gen_username = g.loop(get_username)


def get_hostname(host=None, zone=None, **kwargs):
    """ Get a hostname.

    :return str:

    ::
        print get_hostname()  # -> twitter.az

    """
    params = dict(
        host=host or g.get_choice(HOSTNAMES),
        zone=zone or g.get_choice(HOSTZONES)
    )
    return g.get_choice((
        '{host}.{zone}'.format(**params),
        'www.{host}.{zone}'.format(**params)
    ))

#: Generator's fabric for :meth:`mixer.fakers.get_hostname`
gen_hostname = g.loop(get_hostname)


def get_email(username=None, host=None, zone=None, **kwargs):
    """ Get a email.

    :param username: set the username or get it by random if none
    :param host: set the host or get it by random if none
    :param zone: set the zone or get it by random if none

    :return str:

    ::
        print get_email()  # -> team.cool@microsoft.de

    """
    hostname = get_hostname(host, zone)
    if hostname.startswith('www.'):
        hostname = hostname[4:]
    return '{0}@{1}'.format(username or get_username(), hostname)

#: Generator's fabric for :meth:`mixer.fakers.get_email`
gen_email = g.loop(get_email)


def get_ip4(**kwargs):
    """ Get IP4 address.

    :return str:

    ::
        print get_ip4()  # 192.168.1.1

    """
    gen = g.gen_positive_integer(256)
    return '{0}.{1}.{2}.{3}'.format(
        next(gen), next(gen), next(gen), next(gen),
    )

#: Generator's fabric for :meth:`mixer.fakers.get_ip4`
gen_ip4 = g.loop(get_ip4)


def get_url(hostname=None, **kwargs):
    """ Get a URL.

    :return str:

    """
    if hostname is None:
        hostname = g.get_choice((True, False))

    if hostname:
        parts = [get_hostname()]

    else:
        parts = ['']

    parts += g.get_choices(LOREM_CHOICES, g.get_integer(1, 3))

    return '/'.join(parts)

#: Generator's fabric for :meth:`mixer.fakers.get_url`
gen_url = g.loop(get_url)


def get_uuid(**kwargs):
    """ Get a UUID.

    :return str:

    """
    return str(uuid.uuid1())

#: Generator's fabric for :meth:`mixer.fakers.get_uuid`
gen_uuid = g.loop(get_uuid)


def get_phone(template='###-###-###', **kwargs):
    """ Get a phone number.

    :param template: A template for number.
    :return str:

    """
    return get_numerify(template)

#: Generator's fabric for :meth:`mixer.fakers.get_phone`
gen_phone = g.loop(get_phone)


def get_company():
    """ Get a company name.

    :return str:

    """
    return '%s %s' % (get_lastname(), g.get_choice(COMPANY_SYFFIXES))

#: Generator's fabric for :meth:`mixer.fakers.get_company`
gen_company = g.loop(get_company)


def get_latlon():
    """ Get a value simular to latitude (longitude).

    :return float:

    ::

        print get_latlon()  # -> 137.60858

    """
    return float(
        decimal.Decimal(str(g.get_float(-180, 180))).quantize(GEOCOORD_MASK))

#: Generator's fabric for :meth:`mixer.fakers.get_latlon`
gen_latlon = g.loop(get_latlon)


def get_coordinates():
    """ Get a geographic coordinates.

    :return [float, float]:

    ::

        print get_coordinates()  # -> [116.256223, 43.790918]

    """
    return [get_latlon(), get_latlon()]

#: Generator's fabric for :meth:`mixer.fakers.get_coordinates`
gen_coordinates = g.loop(get_coordinates)
