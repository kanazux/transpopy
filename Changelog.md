# transpopy

## [Unreleased]
### Added
- Accept msgid's with multiple lines
- New tests
- flake8 to tox.ini

### Changed
- Refactor code with a main loop, reading, translating and saving
	 (to the PO file) while it is passing through the POT file
- Change Google translation function to preserve line breaks
- Install transpopy script through setuptools

### Removed
- Unused opt arguments, added them to TODO.md
- Outdated tests

## [0.1.1] - 2018-09-01
### Added
- Initial release
