# Brunata Online Custom Integration for Home Assistant

[![hacs][hacsbadge]][hacs]
[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

<!-- Sponsors -->

[![ko-fi][kofi_badge]](https://ko-fi.com/X8X3205KS)

## ⚠️ DO NOT INSTALL, THIS INTEGRATION DOES NOT WORK YET. I AM NOT RESPONSIBLE FOR ANY HARM CAUSED BY INSTALLING THIS INTEGRATION ⚠️

**This integration is still a work in progress.**

Furthermore, this integration is not endorsed by Brunata, and could stop functioning at any time at their behest; your Brunata account might also be closed, although no EULA is provided for the Brunata Online Portal at the time of writing

## ⚠️ Please ensure your credentials work on [online.brunata.com][brunata] ⚠️

If your credentials don't work **AND** you use a different Brunata portal to view your metrics, please open a pull request and/or contact me on the [Home Assistant Forum][ha_profile].

In most cases, you will likely have to add support for alternate portals yourself; I will gladly assist you in getting the login-flow working and finding the API endpoints. Then you can simply submit a Pull Request, and I'll review it when I have time 🙂

---

This integration allows Home Assistant to read meter values from the [Brunata Online][brunata] Portal.
Brunata is an IoT-enabled utilities provider that's part of the Minol-ZENNER Group, mostly providing utilities to housing cooperatives in the EEA

### Trying it out

[Adjusted instructions based on this GitHub issue comment](https://github.com/YukiElectronics/ha-brunata/issues/13#issuecomment-2258440139)
and added additional tooling to make it easier to fetch the data.

1. Put your credentials in the file `brunata-secrets.cfg` (create it if it doesn't exist)
```cfg
[brunata]
username = your_username
password = your_password
```
2. Run the script `fetch_brunata_data.py` to see if it works

### ✨ Planned Features

- [x] Add support for more metrics

  - [x] 💧 Water consumption

  - [x] 🔥 District heating / gas consumption

- [ ] Expose metrics as Home Assistant sensors

- [ ] Configure Python tests

- [ ] Support writing historical metrics to sensor

### The integration can fetch the following metrics

- 📊 Available meter types — ⚠️ Only tested on two accounts so far ⚠️

- ⚡ Energy meters

- 💧 Water meters

- 🔥 Heating meters — Thanks to [WallyR](https://community.home-assistant.io/u/wallyr) on the Home Assistant Community forum

### The following Home Assistant sensors have been implemented

⚠️ No sensors have been implemented yet ⚠️

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter][custom_component] template

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

Active Directory B2C Login-flow was mostly based on [@itchannel](https://github.com/itchannel)'s [FordPass Integration][fordpass]

---

[brunata]: https://online.brunata.com
[custom_component]: https://github.com/oncleben31/cookiecutter-homeassistant-custom-component
[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[fordpass]: https://github.com/itchannel/fordpass-ha
[ha_profile]: https://community.home-assistant.io/u/YukiElectronics
[kofi_badge]: https://ko-fi.com/img/githubbutton_sm.svg
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/YukiElectronics/ha-brunata.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/YukiElectronics/ha-brunata.svg?style=for-the-badge
[releases]: https://github.com/YukiElectronics/ha-brunata/releases
