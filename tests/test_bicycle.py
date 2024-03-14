import pytest
from bicycle.wheel import Wheel
from bicycle.gear import Gear
from bicycle.observer import Observer


# Incoming Query Messages
def test_diameter():
    """
    Test the diameter of the wheel
    """
    wheel = Wheel(rim=26, tire=1.5)
    assert (
        wheel.diameter() == 29
    )  # Test incoming query message by making assertions about what they send back


def test_calculates_gear_inches():
    """
    Test the gear inches calculation
    """
    wheel = Wheel(rim=26, tire=1.5)
    gear = Gear(chainring=52, cog=11, wheel=wheel)
    assert (
        gear.gear_inches() == 137.17
    )  # Test the interface, not implementation e.g. __ratio, Test Incoming Query Message


# Outgoing Command Messages
def test_set_cog():
    """
    Test the set cog method
    """
    wheel = Wheel(rim=26, tire=1.5)
    gear = Gear(chainring=52, cog=11, wheel=wheel)
    gear.set_cog(10)  # Outgoing Command Message (causes side effects)
    assert (
        gear.cog == 10
    )  # Test outgoing command message by making assertions about direct public side effects


# AntiPattern: Testing the implementation - DO NOT TEST PRIVATE METHODS
def test_calculates_ratio():
    """
    Test the ratio calculation
    """
    wheel = Wheel(rim=26, tire=1.5)
    gear = Gear(chainring=52, cog=11, wheel=wheel)
    assert gear._Gear__ratio() == 4.73  # DO NOT TEST PRIVATE METHODS


def test_calculates_gear_inches_ratio():
    """
    Test the gear inches calculation
    """
    wheel = Wheel(rim=26, tire=1.5)
    gear = Gear(chainring=52, cog=11, wheel=wheel)
    assert gear.gear_inches() == 137.17
    assert gear._Gear__ratio() == 4.73  # DO NOT TEST PRIVATE METHODS


# Outgoing Query Messages
# AntiPattern: Testing outgoing query messages - Do NOT test as they are tested as part of the incoming query messages
def test_calculates_gear_inches_outgoing():
    """
    Test the gear inches calculation
    """
    wheel = Wheel(rim=26, tire=1.5)
    gear = Gear(chainring=52, cog=11, wheel=wheel)
    assert gear.gear_inches() == 137.17
    assert gear.wheel.diameter() == 29  # Redundant and duplicates the Wheel test


# Outgoing Command Messages
# AntiPattern: If you assert what's in the DB, it creates a dependency on distance side effect
def test_saves_changed_cog_in_db():
    obs = Observer()
    wheel = Wheel(rim=26, tire=1.5)
    gear = Gear(chainring=52, cog=11, wheel=wheel, observer=obs)
    gear.set_cog(27)
    # Assert something about the state of the db


@pytest.mark.skip(reason="Test in progress")
def test_notifies_observers_when_cogs_change():
    obs = Observer()
    wheel = Wheel(rim=26, tire=1.5)
    gear = Gear(chainring=52, cog=11, wheel=wheel, observer=obs)
    obs.changed.assert_called_with(52, 11)  # Assert that the observer was notified
    gear.set_cog(27)
    obs.changed.assert_called_with(52, 27)  # Assert that the observer was notified
