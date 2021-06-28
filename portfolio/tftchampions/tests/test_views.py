import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from ..models import Champion
from ..views import (
    ChampionCreateView,
    ChampionDeleteView,
    ChampionDetailView,
    ChampionListView,
    ChampionUpdateView,
)
from .factories import ChampionFactory

pytestmark = pytest.mark.django_db


def test_good_champion_list_view_expanded(rf):
    url = reverse("tftchampions:list")
    request = rf.get(url)
    callable_obj = ChampionListView.as_view()
    response = callable_obj(request)

    assertContains(response, "Champion List")


def test_good_champion_detail_view(rf, champion):
    url = reverse("tftchampions:detail", kwargs={"slug": champion.slug})
    request = rf.get(url)
    callable_obj = ChampionDetailView.as_view()
    response = callable_obj(request, slug=champion.slug)

    assertContains(response, champion.name)


def test_good_champion_create_view(rf, admin_user, champion):
    request = rf.get(reverse("tftchampions:add"))
    request.user = admin_user
    response = ChampionCreateView.as_view()(request)

    assert response.status_code == 200


def test_champion_list_contains_2_champions(rf):
    champion1 = ChampionFactory()
    champion2 = ChampionFactory()

    request = rf.get(reverse("tftchampions:list"))
    response = ChampionListView.as_view()(request)

    assertContains(response, champion1.name)
    assertContains(response, champion2.name)


def test_detail_constains_champion_data(rf, champion):
    url = reverse("tftchampions:detail", kwargs={"slug": champion.slug})
    request = rf.get(url)
    callable_obj = ChampionDetailView.as_view()
    response = callable_obj(request, slug=champion.slug)

    assertContains(response, champion.name)
    assertContains(response, champion.dps)
    assertContains(response, champion.attackspeed)
    assertContains(response, champion.dmg)
    assertContains(response, champion.range)
    assertContains(response, champion.hp)
    assertContains(response, champion.mana)
    assertContains(response, champion.armor)
    assertContains(response, champion.origin_prim)
    assertContains(response, champion.origin_sec)
    assertContains(response, champion.class_prim)
    assertContains(response, champion.class_sec)
    assertContains(response, champion.cost)
    assertContains(response, champion.tier)
    assertContains(response, champion.creator.username)


def test_champion_create_form_valid(rf, admin_user, champion):
    form_data = {
        "name": champion.name,
        "dps": champion.dps,
        "attackspeed": champion.attackspeed,
        "dmg": champion.dmg,
        "range": Champion.Range.One,
        "hp": champion.hp,
        "mana": champion.mana,
        "armor": champion.armor,
        "origin_prim": champion.origin_prim,
        "origin_sec": champion.origin_sec,
        "class_prim": champion.class_prim,
        "class_sec": champion.class_sec,
        "cost": champion.cost,
        "tier": champion.tier,
    }
    request = rf.post(reverse("tftchampions:add"), form_data)
    request.user = admin_user
    ChampionCreateView.as_view()(request)

    created_champion = Champion.objects.get(name=champion.name)

    assert created_champion.name == champion.name
    assert created_champion.dps == champion.dps
    assert created_champion.attackspeed == champion.attackspeed
    assert created_champion.dmg == champion.dmg
    assert created_champion.range == champion.range
    assert created_champion.hp == champion.hp
    assert created_champion.mana == champion.mana
    assert created_champion.armor == champion.armor
    assert created_champion.origin_prim == champion.origin_prim
    assert created_champion.origin_sec == champion.origin_sec
    assert created_champion.class_prim == champion.class_prim
    assert created_champion.class_sec == champion.class_sec
    assert created_champion.cost == champion.cost
    assert created_champion.tier == champion.tier


def test_champion_create_correct_title(rf, admin_user):
    """Page title for ChampionCreateView should be Add Champion"""
    request = rf.get(reverse("tftchampions:add"))
    request.user = admin_user
    response = ChampionCreateView.as_view()(request)
    assertContains(response, "Add Champion")


def test_good_champion_update_view(rf, admin_user, champion):
    url = reverse("tftchampions:update", kwargs={"slug": champion.slug})
    request = rf.get(url)
    request.user = admin_user
    callable_obj = ChampionUpdateView.as_view()
    response = callable_obj(request, slug=champion.slug)

    assertContains(response, "Update Champion")


def test_champion_update(rf, admin_user, champion):
    """Post request to ChampionUpdateView updates a champion and redirects."""
    form_data = {
        "name": champion.name,
        "dps": 68,
        "attackspeed": champion.attackspeed,
        "dmg": champion.dmg,
        "range": Champion.Range.One,
        "hp": champion.hp,
        "mana": champion.mana,
        "armor": champion.armor,
        "mr": champion.mr,
        "origin_prim": champion.origin_prim,
        "origin_sec": champion.origin_sec,
        "class_prim": champion.class_prim,
        "class_sec": champion.class_sec,
        "cost": champion.cost,
        "tier": champion.tier,
    }

    url = reverse("tftchampions:update", kwargs={"slug": champion.slug})
    request = rf.post(url, form_data)
    request.user = admin_user
    callable_obj = ChampionUpdateView.as_view()
    response = callable_obj(request, slug=champion.slug)

    assert response.status_code == 302
    updated_champion = Champion.objects.get(dps=68)

    assert updated_champion.name == champion.name
    assert updated_champion.dps == 68
    assert updated_champion.range == Champion.Range.One


def test_good_champion_delete_view(rf, admin_user, champion):
    url = reverse("tftchampions:delete", kwargs={"slug": champion.slug})
    request = rf.get(url)
    request.user = admin_user
    callable_obj = ChampionDeleteView.as_view()
    response = callable_obj(request, slug=champion.slug)

    assertContains(response, "Are you sure you want to delete")


def test_champion_delete(rf, admin_user, champion):
    url = reverse("tftchampions:delete", kwargs={"slug": champion.slug})
    request = rf.post(url)
    request.user = admin_user
    callable_obj = ChampionDeleteView.as_view()
    response = callable_obj(request, slug=champion.slug)

    assert response.status_code == 302
    assert list(Champion.objects.all()) == list(Champion.objects.none())
    # test redirect https://stackoverflow.com/questions/48293627/how-to-test-redirection-in-django-using-pytest
    assert response["Location"] == reverse("tftchampions:list")
