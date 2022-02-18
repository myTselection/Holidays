"""Test calendar for simple integration."""
from datetime import date

from custom_components.holidays import const
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry

# from unittest.mock import AsyncMock


async def test_calendar(hass: HomeAssistant):
    """Test calendar."""

    config_entry: MockConfigEntry = MockConfigEntry(
        domain=const.DOMAIN,
        data={"country": "GB", "subdiv": "England"},
        title="UK Holidays",
        version=1,
    )
    config_entry.add_to_hass(hass)
    await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()
    uk_holidays = hass.states.get("calendar.uk_holidays")
    next_date = uk_holidays.attributes["next_date"].date()
    assert next_date == date(2022, 4, 15)
