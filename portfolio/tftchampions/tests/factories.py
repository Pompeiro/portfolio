import factory
import factory.fuzzy
from django.template.defaultfilters import slugify

from ..models import (
    ARMOR_LOWER_CONSTRAINT,
    ARMOR_UPPER_CONSTRAINT,
    ATTACKSPEED_LOWER_CONSTRAINT,
    ATTACKSPEED_UPPER_CONSTRAINT,
    DMG_LOWER_CONSTRAINT,
    DMG_UPPER_CONSTRAINT,
    DPS_LOWER_CONSTRAINT,
    DPS_UPPER_CONSTRAINT,
    HP_LOWER_CONSTRAINT,
    HP_UPPER_CONSTRAINT,
    MANA_LOWER_CONSTRAINT,
    MANA_UPPER_CONSTRAINT,
    MR_LOWER_CONSTRAINT,
    MR_UPPER_CONSTRAINT,
    Champion,
)


class ChampionFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    dps = factory.fuzzy.FuzzyInteger(DPS_LOWER_CONSTRAINT, DPS_UPPER_CONSTRAINT)
    attackspeed = factory.fuzzy.FuzzyFloat(
        ATTACKSPEED_LOWER_CONSTRAINT, ATTACKSPEED_UPPER_CONSTRAINT
    )
    dmg = factory.fuzzy.FuzzyInteger(DMG_LOWER_CONSTRAINT, DMG_UPPER_CONSTRAINT)
    range = factory.fuzzy.FuzzyChoice([x[0] for x in Champion.Range.choices])
    hp = factory.fuzzy.FuzzyInteger(HP_LOWER_CONSTRAINT, HP_UPPER_CONSTRAINT)
    mana = factory.fuzzy.FuzzyInteger(MANA_LOWER_CONSTRAINT, MANA_UPPER_CONSTRAINT)
    armor = factory.fuzzy.FuzzyInteger(ARMOR_LOWER_CONSTRAINT, ARMOR_UPPER_CONSTRAINT)
    mr = factory.fuzzy.FuzzyInteger(MR_LOWER_CONSTRAINT, MR_UPPER_CONSTRAINT)
    origin_prim = factory.fuzzy.FuzzyText()
    origin_sec = factory.fuzzy.FuzzyText()
    class_prim = factory.fuzzy.FuzzyText()
    class_sec = factory.fuzzy.FuzzyText()
    cost = factory.fuzzy.FuzzyChoice([x[0] for x in Champion.Cost.choices])
    tier = factory.fuzzy.FuzzyChoice([x[0] for x in Champion.Tier.choices])

    class Meta:
        model = Champion
