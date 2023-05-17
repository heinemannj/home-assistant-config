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

## YAMLDashboards

`<config>/ui-lovelace.yaml`

mode: storage
# Add yaml dashboards
dashboards:
  100-raeume-yaml:
    mode: yaml
    title: 100_Raeume
    icon: mdi:home
    show_in_sidebar: true
    filename: dashboards/100-raeume/index.yaml
  420-pv-yaml:
    mode: yaml
    title: 420_PV
    icon: mdi:solar-power-variant
    show_in_sidebar: true
    filename: dashboards/420-pv/index.yaml
  406-heizung-yaml:
    mode: yaml
    title: 406_Heizung
    icon: mdi:hvac
    show_in_sidebar: true
    filename: dashboards/406-heizung/index.yaml

**Note: Private information is stored in secrets.yaml (not uploaded).**

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
