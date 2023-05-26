# Home Assistant Configuration and Documentation

[![License][license-shield]](LICENSE.md) [![GitHub Last Commit][last-commit-shield]][commits] ![GitHub Stars][stars-shield] ![GitHub Watchers][watchers-shield] ![GitHub Forks][forks-shield]

[![Community Forum][forum-shield]][forum]

- Home Assistant Configuration &amp; Documentation for my Smart House.
- Write-ups, part lists, and links throughout.

## Architecture

## General Information

This configuration controls a couple of significant features in my smart home.

- Floor heating
- Huawei SUN2000 solar inverter and connected Huawei LUNA2000 battery
- ...

## Dashboards

Copy the following folder

- **YAML packages** `<config>/packages`

to your HA `<config>` folder and modify your `<config>/configuration.yaml`:

```
homeassistant:
  customize_glob: !include customize_glob.yaml
  customize: !include customize.yaml
  packages:
    dwd_pollenflug: !include packages/dwd-pollenflug-package.yaml
    dwd_weather_warnings: !include packages/dwd-weather-warnings-package.yaml
    geo_rss_feeds: !include packages/geo-rss-feeds-package.yaml
    heating: !include packages/heating-package.yaml
    hochwasser: !include packages/hochwasser-package.yaml
    huawei_solar_yield: !include packages/huawei-solar-yield-package.yaml
    huawei_solar_battery_card: !include packages/huawei-solar-battery-card-package.yaml
    huawei_solar_battery_correction: !include packages/huawei-solar-battery-correction-package.yaml
    huawei_solar_diagnostic: !include packages/huawei-solar-diagnostic-package.yaml
    huawei_solar_power_flow_card: !include packages/huawei-solar-power-flow-card-package.yaml
    huawei_solar_energy_flow_card: !include packages/huawei-solar-energy-flow-card-package.yaml
    illuminance: !include packages/illuminance-package.yaml
    local_calendar: !include packages/local-calendar-package.yaml
    mold_indicator: !include packages/mold-indicator-package.yaml
    moon_phase_image: !include packages/moon_phase_image-package.yaml
    mqtt_sensor: !include packages/mqtt-sensor-package.yaml
    powercalc: !include packages/powercalc-package.yaml
    pulsemeter: !include packages/pulsemeter-package.yaml
    shelly_light: !include packages/shelly-light-package.yaml
    shelly_sockets: !include packages/shelly-sockets-package.yaml
    # skyfield: !include packages/skyfield-package.yaml
    solcast_solar: !include packages/solcast-solar-package.yaml
    temperature_feels_like: !include packages/temperature-feels-like-package.yaml
    xiaomi_miio_fan: !include packages/xiaomi-miio-fan-package.yaml
```

Copy the following folders

- **YAML dashboards** `<config>/dashboards`<br>
- **Jinja templates used in cards** `<config>/custom_templates`<br>
- **Card-Mod theme** (css styles) `<config>/themes/dashboards.yaml`<br>
- **Card background images** `<config>/www/images`<br>

to your HA `<config>` folder and modify your `<config>/configuration.yaml` and `<config>/ui-lovelace.yaml`.

`<config>/configuration.yaml`

```
automation: !include automations.yaml
group: !include groups.yaml
lovelace: !include ui-lovelace.yaml
script: !include scripts.yaml
scene: !include scenes.yaml
frontend:
  themes: !include_dir_merge_named themes
```

`<config>/ui-lovelace.yaml`

```
# UI managed dashboards
#
mode: storage
```

```
# Additional YAML dashboards
#
dashboards:
  100-rooms-yaml:
    mode: yaml
    title: 100_Rooms
    icon: mdi:home
    show_in_sidebar: true
    filename: dashboards/100-rooms/index.yaml
```

![image](https://github.com/heinemannj/home-assistant-config/blob/master/assets/100-tablet-home.png)

![image](https://github.com/heinemannj/home-assistant-config/blob/master/assets/010-pollenflug.png)

![image](https://github.com/heinemannj/home-assistant-config/blob/master/assets/010-uvi.png)

![image](https://github.com/heinemannj/home-assistant-config/blob/master/assets/010-pegel.png)

![image](https://github.com/heinemannj/home-assistant-config/blob/master/assets/010-aqi.png)

```
  420-pv-yaml:
    mode: yaml
    title: 420_PV
    icon: mdi:solar-power-variant
    show_in_sidebar: true
    filename: dashboards/420-pv/index.yaml
```

![image](https://github.com/heinemannj/home-assistant-config/blob/master/assets/421-pv.png)

![image](https://github.com/heinemannj/home-assistant-config/blob/master/assets/422-pv.png)

![image](https://github.com/heinemannj/home-assistant-config/blob/master/assets/423-pv.png)

```
  406-heating-yaml:
    mode: yaml
    title: 406_Heating
    icon: mdi:hvac
    show_in_sidebar: true
    filename: dashboards/406-heating/index.yaml
 ```

![image](https://github.com/heinemannj/home-assistant-config/blob/master/assets/034-20-2-HK2-Fussbodenheizung-Heizkreise.png)

## Notes

- Private information is stored in secrets.yaml (not uploaded).

[commits-shield]: https://img.shields.io/github/commit-activity/y/heinemannj/home-assistant-config.svg
[commits]: https://github.com/heinemannj/home-assistant-config/commits/master
[actions-shield]: https://github.com/heinemannj/home-assistant-config/workflows/Home%20Assistant%20CI/badge.svg
[actions]: https://github.com/heinemannj/home-assistant-config/actions
[contributors]: https://github.com/heinemannj/home-assistant-config/graphs/contributors
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg
[discord]: https://discord.gg/c5DvZ4e
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/?u=heinemannj
[heinemannj]: https://github.com/heinemannj
[travis-shield]: https://travis-ci.org/heinemannj/home-assistant-config.svg?branch=master
[travis]: https://travis-ci.org/heinemannj/home-assistant-config
[home-assistant]: https://home-assistant.io
[issue]: https://github.com/heinemannj/home-assistant-config/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/heinemannj/home-assistant-config.svg
[stars-shield]: https://img.shields.io/github/stars/heinemannj/home-assistant-config.svg?style=social&label=Stars
[forks-shield]: https://img.shields.io/github/forks/heinemannj/home-assistant-config.svg?style=social&label=Forks
[watchers-shield]: https://img.shields.io/github/watchers/heinemannj/home-assistant-config.svg?style=social&label=Watchers
[black-duck-shield]: https://copilot.blackducksoftware.com/github/repos/heinemannj/home-assistant-config/branches/master/badge-risk.svg
[black-duck]: https://copilot.blackducksoftware.com/github/repos/heinemannj/home-assistant-config/branches/master/
