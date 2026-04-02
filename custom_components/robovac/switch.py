"""Switch platform for Eufy RoboVac."""
from __future__ import annotations

from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_DESCRIPTION, CONF_ID, CONF_MAC, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CONF_VACS, DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up RoboVac switch entities from a config entry."""
    vacuums = config_entry.data[CONF_VACS]
    entities: list[SwitchEntity] = []

    for item_key in vacuums:
        item = vacuums[item_key]
        entities.append(RoboVacAutoReturnSwitch(hass, item))

    async_add_entities(entities)


class RoboVacAutoReturnSwitch(SwitchEntity):
    """Representation of the RoboVac Auto Return switch."""

    _attr_has_entity_name = True

    def __init__(self, hass: HomeAssistant, item: dict[str, Any]) -> None:
        """Initialize the switch."""
        self.hass = hass
        self._item = item
        self._vacuum_id = item[CONF_ID]
        self._attr_unique_id = f"{self._vacuum_id}_auto_return"
        self._attr_name = "Auto Return"
        self._attr_icon = "mdi:home-arrow-right"

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, item[CONF_ID])},
            name=item[CONF_NAME],
            manufacturer="Eufy",
            model=item[CONF_DESCRIPTION],
            connections={
                (CONNECTION_NETWORK_MAC, item[CONF_MAC]),
            },
        )

    @property
    def available(self) -> bool:
        """Return whether the entity is available."""
        vacuum_entity = self.hass.data[DOMAIN][CONF_VACS].get(self._vacuum_id)
        return vacuum_entity is not None

    @property
    def is_on(self) -> bool | None:
        """Return true if auto return is enabled."""
        vacuum_entity = self.hass.data[DOMAIN][CONF_VACS].get(self._vacuum_id)
        if vacuum_entity is None:
            return None

        value = vacuum_entity.auto_return
        if value is None:
            return None

        if isinstance(value, bool):
            return value

        if isinstance(value, str):
            return value.lower() == "true"

        return bool(value)

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn auto return on."""
        vacuum_entity = self.hass.data[DOMAIN][CONF_VACS].get(self._vacuum_id)
        if vacuum_entity is None:
            return

        if self.is_on is not True:
            await vacuum_entity.async_send_command("autoReturn")
            await vacuum_entity.async_update()
            self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn auto return off."""
        vacuum_entity = self.hass.data[DOMAIN][CONF_VACS].get(self._vacuum_id)
        if vacuum_entity is None:
            return

        if self.is_on is not False:
            await vacuum_entity.async_send_command("autoReturn")
            await vacuum_entity.async_update()
            self.async_write_ha_state()

    async def async_update(self) -> None:
        """Update switch state."""
        self.async_write_ha_state()
