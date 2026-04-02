IMPORTANT!!!

Hi folks! I’ve made some changes to the 1.3.1 release to make the Eufy G10 Hybrid work properly. In addition, I’ve added the ability to change the auto return mode directly from the UI under Details. Moreover, I adjusted the vacuum modes to match the robot’s functionality.

# Eufy RobovVac control for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
[![Sponsor me on Github Sponsors](https://img.shields.io/badge/Sponsor-ea4aaa?style=for-the-badge&logo=github-sponsors&logoColor=%23EA4AAA&labelColor=white)](https://github.com/sponsors/damacus)

A Eufy RoboVac integration for Home Assistant.

📖 **[Full Documentation](https://damacus.github.io/robovac)**

## ⚠️ Breaking Change in v2.0.0

**Version 2.0.0 requires you to remove and re-add the integration.** See the [upgrade guide](https://damacus.github.io/robovac) for details.

## Installation

See the [installation guide](https://damacus.github.io/robovac) for full instructions.

## Debugging

See the [troubleshooting guide](https://damacus.github.io/robovac) for debugging instructions.

## Model Validation

Validate if your RoboVac model is supported:

```bash
python -m custom_components.robovac.model_validator_cli --list
```

## Development

See [DEVELOPMENT.md](DEVELOPMENT.md) for contribution guidelines and development setup.
