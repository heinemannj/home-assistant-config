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

## YAML Dashboards

`<config>/ui-lovelace.yaml`

```
mode: storage
# Add yaml dashboards
dashboards:
  100-raeume-yaml:
    mode: yaml
    title: 100_Raeume
    icon: mdi:home
    show_in_sidebar: true
    filename: dashboards/100-raeume/index.yaml
```
![image](https://github.com/heinemannj/home-assistant-config/assets/3251642/ada412ce-bb80-4e03-9b6a-cf7c74f3349a)

![image](https://github.com/heinemannj/home-assistant-config/assets/3251642/50baf54d-ae9f-400c-82ef-9ee04917d75a)

![image](https://github.com/heinemannj/home-assistant-config/assets/3251642/2f43982e-ee10-496d-bc7e-aa0162d66bf2)

![image](https://github.com/heinemannj/home-assistant-config/assets/3251642/aeed7ec1-b295-4872-9b81-72358979fe08)

![image](https://github.com/heinemannj/home-assistant-config/assets/3251642/cef2c53a-f39a-4eab-ae40-4318cbcd0d27)

```
  420-pv-yaml:
    mode: yaml
    title: 420_PV
    icon: mdi:solar-power-variant
    show_in_sidebar: true
    filename: dashboards/420-pv/index.yaml
```

![image](https://github.com/heinemannj/home-assistant-config/assets/3251642/1f74c8b3-4caa-4148-bb3c-6f74de71a2fe)

![image](https://github.com/heinemannj/home-assistant-config/assets/3251642/8972daf9-6c6c-45e3-91de-e1f0b95071d0)

![image](https://github.com/heinemannj/home-assistant-config/assets/3251642/77ce04ce-9e0f-4c60-b371-eb90a84724d2)

```
  406-heizung-yaml:
    mode: yaml
    title: 406_Heizung
    icon: mdi:hvac
    show_in_sidebar: true
    filename: dashboards/406-heizung/index.yaml
 ```
![image](https://github.com/heinemannj/home-assistant-config/assets/3251642/d46d9e1c-89e3-47c7-b925-8fb9a69353ab)

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
