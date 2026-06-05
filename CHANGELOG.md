# Changelog

All notable changes to the CredSleuth project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-05

### Added
- ✨ Initial release of CredSleuth
- 🔍 Directory scanning capability
- 📜 Git history scanning capability
- 🔐 Multi-credential type detection:
  - AWS Access Keys
  - Private Keys (RSA, SSH, DSA)
  - GitHub Tokens
  - Stripe API Keys
  - SendGrid API Keys
  - Twilio Tokens
  - MongoDB Connection Strings
  - PostgreSQL Connection Strings
  - MySQL Credentials
  - Bearer Tokens and OAuth tokens
  - JWT Secrets
- 📊 Risk scoring system (Critical, High, Medium)
- 📈 HTML report generation with visualizations
- 📄 JSON report generation for CI/CD integration
- 🎨 Color-coded console output
- 💾 .gitignore pattern respect
- ⚡ Optimized file scanning
- 🚀 Fast Git history analysis

### Changed
- N/A (Initial release)

### Fixed
- N/A (Initial release)

### Deprecated
- N/A

### Removed
- N/A

### Security
- Credentials detected are not logged or stored beyond report generation
- Local-only processing with no external data transmission
- Safe handling of sensitive file content

## [Unreleased]

### Planned Features
- 🔧 Configuration file support (.credsleuth.yaml)
- 🌍 Multi-language support
- 📊 PDF report generation
- 🔄 Parallel file scanning for improved performance
- 🎯 Custom pattern configuration
- 🔔 Webhook integration for CI/CD
- 💾 Database backend for historical tracking
- 🌐 Web UI for interactive scanning
- 🐍 Python package publication (PyPI)
- 🧪 Comprehensive test suite
- 📱 CLI progress indicators
- 🎚️ Configurable sensitivity levels

---

## Version Details

### v1.0.0 Release Notes

**Overview:** CredSleuth v1.0.0 is the stable initial release featuring dual scanning modes and comprehensive credential detection.

**Key Highlights:**
- Production-ready credential detection
- Flexible scanning (filesystem and Git)
- Beautiful reporting capabilities
- Easy integration with existing workflows

**Known Limitations:**
- Single-threaded scanning (parallel support coming in v1.1.0)
- Limited to file-based configuration (config file support in v1.1.0)
- No web UI (coming in v2.0.0)

**Migration Guide:** N/A (First release)

**Support:** Open issues on GitHub for bugs and feature requests

---

## How We Version

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version: Breaking changes
- **MINOR** version: New features (backward compatible)
- **PATCH** version: Bug fixes (backward compatible)

---

## Release Schedule

- 🎯 **v1.1.0** (Q3 2026): Performance improvements, configuration files
- 🚀 **v1.2.0** (Q4 2026): Enhanced patterns, PDF reports
- 💫 **v2.0.0** (2027): Web UI, database backend, plugins

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Getting Help

- 📖 Check [README.md](README.md) for usage documentation
- 💬 Search existing [GitHub Issues](https://github.com/Officiallynith/CredSleuth/issues)
- 🐛 Report bugs with reproduction steps
- ✨ Suggest features with use cases
