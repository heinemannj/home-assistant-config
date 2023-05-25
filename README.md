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

**YAML packages**: `<config>/packages`

**YAML dashboards**: `<config>/dashboards`<br>
**Jinja templates used in cards**: `<config>/custom_templates`<br>
**Card-Mod Theme** (css styles): `<config>/themes/dashboards.yaml`<br>

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
