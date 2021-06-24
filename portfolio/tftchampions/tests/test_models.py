import pytest

from ..models import Champion

pytestmark = pytest.mark.django_db


def test___str__():
    champion = Champion.objects.create(
        name="Zyra",
        dps=50,
        attackspeed=2.1,
        dmg=30,
        range=Champion.Range.Three,
        hp=550,
        mana=10,
        armor=30,
        mr=0,
        origin_prim="Draconic",
        class_prim="Spellweaver",
        cost=Champion.Cost.Two,
        tier=Champion.Tier.D,
    )

    assert champion.__str__() == champion.name
    assert str(champion) == champion.name


def test_get_absolute_url():
    champion = Champion.objects.create(
        name="Zyra",
        dps=50,
        attackspeed=2.1,
        dmg=30,
        range=Champion.Range.Three,
        hp=550,
        mana=10,
        armor=30,
        mr=0,
        origin_prim="Draconic",
        class_prim="Spellweaver",
        cost=Champion.Cost.Two,
        tier=Champion.Tier.D,
    )
    url = champion.get_absolute_url()

    assert url == f"/tftchampions/{champion.slug}/"
