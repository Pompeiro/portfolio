from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

DPS_LOWER_CONSTRAINT = 0
ATTACKSPEED_LOWER_CONSTRAINT = 0.0
DMG_LOWER_CONSTRAINT = 0
HP_LOWER_CONSTRAINT = 0
MANA_LOWER_CONSTRAINT = 0
ARMOR_LOWER_CONSTRAINT = 0
MR_LOWER_CONSTRAINT = 0

DPS_UPPER_CONSTRAINT = 800
ATTACKSPEED_UPPER_CONSTRAINT = 8.0
DMG_UPPER_CONSTRAINT = 500
HP_UPPER_CONSTRAINT = 5000
MANA_UPPER_CONSTRAINT = 300
ARMOR_UPPER_CONSTRAINT = 300
MR_UPPER_CONSTRAINT = 300


class Champion(TimeStampedModel):

    Range = models.IntegerChoices("Cost", "One Two Three Four Five Six Seven")
    Cost = models.IntegerChoices("Cost", "One Two Three Four Five Six Seven")
    Tier = models.IntegerChoices("Tier", "D C B A S")

    name = models.CharField("Name of champion", unique=True, max_length=50)
    dps = models.IntegerField("Damage per second(dmg*attackspeed) of champion")
    attackspeed = models.FloatField("Attack speed of champion")
    dmg = models.IntegerField("Damage of champion")
    range = models.IntegerField("Range of champion in hexes", choices=Range.choices)
    hp = models.IntegerField("Health points of champion")
    mana = models.IntegerField("Mana points of champion")
    armor = models.IntegerField("Armor of champion")
    mr = models.IntegerField("Magic resistance of champion")
    origin_prim = models.CharField("Origin primary of champion", max_length=30)
    origin_sec = models.CharField(
        "Origin secondary of champion", max_length=30, blank=True
    )
    class_prim = models.CharField("Class primary of champion", max_length=30)
    class_sec = models.CharField(
        "Class secondary of champion", max_length=30, blank=True
    )
    cost = models.IntegerField("Cost of champion", choices=Cost.choices)
    tier = models.IntegerField("Tier of champion", choices=Tier.choices)
    slug = AutoSlugField(
        "Champion name", unique=True, always_update=False, populate_from="name"
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(dps__gte=DPS_LOWER_CONSTRAINT)
                & models.Q(dps__lte=DPS_UPPER_CONSTRAINT),
                name="A dps value is valid between 0 and 800",
            ),
            models.CheckConstraint(
                check=models.Q(attackspeed__gte=ATTACKSPEED_LOWER_CONSTRAINT)
                & models.Q(attackspeed__lte=ATTACKSPEED_UPPER_CONSTRAINT),
                name="An attackspeed value is valid between 0.0 and 8.0",
            ),
            models.CheckConstraint(
                check=models.Q(dmg__gte=DMG_LOWER_CONSTRAINT)
                & models.Q(dmg__lte=DMG_UPPER_CONSTRAINT),
                name="A dmg value is valid between 0 and 500",
            ),
            models.CheckConstraint(
                check=models.Q(hp__gte=HP_LOWER_CONSTRAINT)
                & models.Q(hp__lte=HP_UPPER_CONSTRAINT),
                name="A hp value is valid between 0 and 5000",
            ),
            models.CheckConstraint(
                check=models.Q(mana__gte=MANA_LOWER_CONSTRAINT)
                & models.Q(mana__lte=MANA_UPPER_CONSTRAINT),
                name="A mana value is valid between 0 and 300",
            ),
            models.CheckConstraint(
                check=models.Q(armor__gte=ARMOR_LOWER_CONSTRAINT)
                & models.Q(armor__lte=ARMOR_UPPER_CONSTRAINT),
                name="AN armor value is valid between 0 and 300",
            ),
            models.CheckConstraint(
                check=models.Q(mr__gte=MR_LOWER_CONSTRAINT)
                & models.Q(mr__lte=MR_UPPER_CONSTRAINT),
                name="A mr value is valid between 0 and 300",
            ),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute URL to the champion Detail page."""
        return reverse("tftchampions:detail", kwargs={"slug": self.slug})
