# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## Unreleased

<small>[Compare with latest](https://github.com/ydethe/fireset/compare/v0.2.11...HEAD)</small>

### Added

- Added pushover ([4624582](https://github.com/ydethe/fireset/commit/4624582b9299eadd00da3cee7f8d494f77d8572f) by Yann de The).
- Added hypothesis based test ([1f5a4e3](https://github.com/ydethe/fireset/commit/1f5a4e3b942b024a210fdebf3ebaa4075303b6e3) by Yann de The).
- Added unit tests ([cc2e401](https://github.com/ydethe/fireset/commit/cc2e401578e9e798122250deab82f008111dda41) by Yann de The).
- Added typer ([ab9bb36](https://github.com/ydethe/fireset/commit/ab9bb36cfc05cf2e501d566ab46ecd37574acb85) by Yann de The).
- Added test (wip) ([4547aa6](https://github.com/ydethe/fireset/commit/4547aa684252bf73ddd2a5f8e9c2c4d68144a75a) by Yann de The).
- Added pre commit hooks ([7e78ad5](https://github.com/ydethe/fireset/commit/7e78ad51b1eb2d1ad539610400106311ab6ce122) by Yann de The).
- Added logging in logfire + basic auth ([af5fe3c](https://github.com/ydethe/fireset/commit/af5fe3c82fd9ad11787c31848b7751b38627e0b3) by Yann de The).
- Added auth ([317c5cd](https://github.com/ydethe/fireset/commit/317c5cdcd727450540fee924ff0e4af9b11d9954) by Yann de The).
- Added docker compose file ([f55f6ef](https://github.com/ydethe/fireset/commit/f55f6ef184e92132b9546347f87a0225985acbfd) by Yann de The).

### Removed

- Removed support files ([3e53b91](https://github.com/ydethe/fireset/commit/3e53b91d5e96c2c0d8eab7876416b08300842f99) by Yann de The).

<!-- insertion marker -->
## [v0.2.11](https://github.com/ydethe/fireset/releases/tag/v0.2.11) - 2024-03-29

<small>[Compare with v0.2.10](https://github.com/ydethe/fireset/compare/v0.2.10...v0.2.11)</small>

### Added

- Add support for Python 3.11/3.12 (#296) ([ebc1aa7](https://github.com/ydethe/fireset/commit/ebc1aa7f39d89ac7350de232afd1f7aa10787d9f) by Jelmer Vernooĳ).
- Add multiarch Docker build ([a97da79](https://github.com/ydethe/fireset/commit/a97da795c8767f57ee7d24d6170c49638830a31b) by Maya the bee).
- Add dependabot config ([2901833](https://github.com/ydethe/fireset/commit/2901833a6051d13873b6d1022897bae51259b045) by Jelmer Vernooĳ).
- Add tests for href_to_path ([7e9f5e4](https://github.com/ydethe/fireset/commit/7e9f5e4d59d2a5671232227245701bd2453e13a5) by Jelmer Vernooĳ).
- Add Backend.get_resources ([c2b667a](https://github.com/ydethe/fireset/commit/c2b667a61e285d8f5c4699c6aa2b478cdaab6f1d) by Jelmer Vernooĳ).
- Add reformat target ([86e2b2b](https://github.com/ydethe/fireset/commit/86e2b2bd9096118d659c9d6305f165555854ea5b) by Jelmer Vernooĳ).

### Fixed

- Fix pycaldav (#297) ([fcdb84a](https://github.com/ydethe/fireset/commit/fcdb84a1175e9d2c630f536f9acb6e8255f7a25b) by Jelmer Vernooĳ).
- Fix tasks.org link ([97a81e2](https://github.com/ydethe/fireset/commit/97a81e25f7b4fef9b60b0bda82b841516e0f2f69) by Jelmer Vernooĳ).
- Fix disperse workflow name ([978f9d8](https://github.com/ydethe/fireset/commit/978f9d87b767e12f69f971c2ce21477f985264a8) by Jelmer Vernooĳ).
- Fix href handling ([01264f7](https://github.com/ydethe/fireset/commit/01264f7acfe05952b801d5f89c235b148dabf55f) by Tcc100).

## [v0.2.10](https://github.com/ydethe/fireset/releases/tag/v0.2.10) - 2023-09-04

<small>[Compare with v0.2.8](https://github.com/ydethe/fireset/compare/v0.2.8...v0.2.10)</small>

### Added

- Add some more typing ([728d6aa](https://github.com/ydethe/fireset/commit/728d6aa76d8e60d35aa12b768003e134d637dffa) by Jelmer Vernooĳ).
- Add basic rust crate ([1520f3d](https://github.com/ydethe/fireset/commit/1520f3de1bdca8f72cfbf3c5d92797865d2a8a57) by Jelmer Vernooĳ).
- Add more typing ([de74413](https://github.com/ydethe/fireset/commit/de74413290796e2f9288b6e9b9e5ee297dd0f6c3) by Jelmer Vernooĳ).
- Add CODEOWNERS. ([1475c57](https://github.com/ydethe/fireset/commit/1475c57d846775870b17eb78d7adf8741c158c9c) by Jelmer Vernooĳ).
- Add new pycaldav dep. ([54c5636](https://github.com/ydethe/fireset/commit/54c56360edae2f602a51fdd17a49095bfdf4b0b6) by Jelmer Vernooĳ).
- Add more debug data in error message. ([dd968d4](https://github.com/ydethe/fireset/commit/dd968d45c6a7a79b5ec2ea869d5c9d159308a730) by Jelmer Vernooĳ).
- Add a pyproject.toml file. ([de48762](https://github.com/ydethe/fireset/commit/de48762961d7bb9463c6e49dcc3c77c26b5594ee) by Jelmer Vernooĳ).
- Add hidden options --paranoid and --index-threshold. ([4529841](https://github.com/ydethe/fireset/commit/45298417d78db419ea07eef616cd010df173b0b5) by Jelmer Vernooĳ).
- Add support for TextMatcher against vCategory. ([9c13cfc](https://github.com/ydethe/fireset/commit/9c13cfcb01683f126bc1760efc7781d9aaa0d723) by Jelmer Vernooĳ).
- Add more typing. ([873bd39](https://github.com/ydethe/fireset/commit/873bd39354a7ecf4cad1660869df6f7a0995c5d9) by Jelmer Vernooĳ).
- Add a really basic grafana dashboard. ([2c44293](https://github.com/ydethe/fireset/commit/2c44293847af316edc7cb09c6327f450e30a8616) by Jelmer Vernooĳ).
- Add py.typed. ([92c26ad](https://github.com/ydethe/fireset/commit/92c26ad22c994c5f003ff4b1a72ab292f3e01282) by Jelmer Vernooĳ).
- Add --metrics-port. ([c4f1953](https://github.com/ydethe/fireset/commit/c4f1953601a179996f3152fb63e6851315518865) by Jelmer Vernooĳ).
- Add helper function for reporting that things are bad about a request. ([1ea2c26](https://github.com/ydethe/fireset/commit/1ea2c26ef51b3d1bf06198aa21292e6d3ef3df0c) by Jelmer Vernooĳ).
- Add typing. ([74d2770](https://github.com/ydethe/fireset/commit/74d27709bfc92e7a6362cbc7d5d71e674432175b) by Jelmer Vernooĳ).
- Add github url. ([675bd5b](https://github.com/ydethe/fireset/commit/675bd5b1bcaa4b90d4ee54faaacf285a313ccd64) by Jelmer Vernooĳ).
- Add link to docs. ([f287f50](https://github.com/ydethe/fireset/commit/f287f500857c94f18b8ca8b3601a3703916f1f6f) by Jelmer Vernooĳ).
- Add readthedocs config. ([914f9ac](https://github.com/ydethe/fireset/commit/914f9ac171caca0eb1c9b5800172e1d8ef401640) by Jelmer Vernooĳ).
- add #noqa. ([59e6a99](https://github.com/ydethe/fireset/commit/59e6a99d9968fe78cc59d5860ee02b48e4c9ea0d) by Jelmer Vernooĳ).
- Add troubleshooting docs. ([cb8040a](https://github.com/ydethe/fireset/commit/cb8040a00654d3bc53c36ac78ed25e266d313878) by Jelmer Vernooĳ).
- Add notes on ingress and client configuration. ([213b2bf](https://github.com/ydethe/fireset/commit/213b2bf6b93ac26ce334dff7b77a4f29dda333f3) by Jelmer Vernooĳ).
- Add kubernetes deployment instructions. ([7d1ae64](https://github.com/ydethe/fireset/commit/7d1ae645b5a844cc6848bf3be6877021de398d2a) by Jelmer Vernooĳ).
- Add note to dev docs directory. ([56816f7](https://github.com/ydethe/fireset/commit/56816f793c12b5d53390a531a5d6501cc071cb88) by Jelmer Vernooĳ).
- Add sphinx skeleton. ([39639c8](https://github.com/ydethe/fireset/commit/39639c878c8a230e3a6db861ce984340a6a7b76b) by Jelmer Vernooĳ).
- Add xandikos.web.run_simple_server. ([8863dc9](https://github.com/ydethe/fireset/commit/8863dc9b5a50c81c962af86c49a0dafbf493e926) by Jelmer Vernooĳ).
- add support for systemd socket activation ([d0d56c8](https://github.com/ydethe/fireset/commit/d0d56c8133d749d8cfa8bf024ee687dc9753def2) by schnusch).

### Fixed

- Fix rustc version for clap ([b7cd275](https://github.com/ydethe/fireset/commit/b7cd27591f67dabbba7d98a138d0ff2026d878d8) by Jelmer Vernooĳ).
- Fix compatibility with newer dulwich ([28b77ca](https://github.com/ydethe/fireset/commit/28b77ca220a385ab75125cbaae1ce3cb231502e6) by Jelmer Vernooĳ).
- Fix style ([4818187](https://github.com/ydethe/fireset/commit/4818187d200ac6bacbf0049991e8c1ec9a30e3bb) by Jelmer Vernooĳ).
- Fix typing. ([41c53e0](https://github.com/ydethe/fireset/commit/41c53e0cf24b436a197d7ee9dcab3efa44b6cc91) by Jelmer Vernooĳ).
- Fix job names ([6eee74e](https://github.com/ydethe/fireset/commit/6eee74ebcfd88911ecf0d34429bce0a47c08f130) by Jelmer Vernooĳ).
- Fix pycaldav tests for the moment; enable text_search_not_working ([4e1cca3](https://github.com/ydethe/fireset/commit/4e1cca322c48a8ef7426f568593a728360e0e107) by Jelmer Vernooĳ).
- fixup for commit 45298417d78db419ea07eef616cd010df173b0b5 pull request https://github.com/jelmer/xandikos/pull/222 ([f088e0e](https://github.com/ydethe/fireset/commit/f088e0e5810803c0a410152cc94035ca5444dfb9) by Tobias Brox).
- Fix index handling for datetimes. ([fa325f5](https://github.com/ydethe/fireset/commit/fa325f5c50d13a1f113a31ba7e67a2c328651eb5) by Jelmer Vernooĳ).
- Fix syntax error. ([5758693](https://github.com/ydethe/fireset/commit/575869358ab44ef4e82b6affebe18ec7dbe885dc) by Jelmer Vernooĳ).
- Fix more typing. ([4e593a6](https://github.com/ydethe/fireset/commit/4e593a61f89bc40d5c6ddc448649326c0843fa4b) by Jelmer Vernooĳ).
- Fix import order. ([467daf6](https://github.com/ydethe/fireset/commit/467daf6c9966e8534468bb20db393391cb078a9a) by Jelmer Vernooĳ).
- Fix test ([e192ff9](https://github.com/ydethe/fireset/commit/e192ff9e4e3eb64f20c2bbe079a08fdd07b37256) by Jelmer Vernooĳ).
- fix type ([aa8d596](https://github.com/ydethe/fireset/commit/aa8d5967fb8a6ad8be238f26b3491d3873131ef2) by Jelmer Vernooĳ).
- Fix long line. ([1bccb16](https://github.com/ydethe/fireset/commit/1bccb16a25e6256d485cb55a6300c4241ef81b40) by Jelmer Vernooĳ).
- Fix compat tests. ([2863181](https://github.com/ydethe/fireset/commit/286318124d94a729f6bc70b26f85017b71bbfb68) by Jelmer Vernooĳ).
- Fix formatting. ([3ae201e](https://github.com/ydethe/fireset/commit/3ae201e27ff06d55536f6f39a52b6a64fb688807) by Jelmer Vernooĳ).
- Fix tests. ([7fec34f](https://github.com/ydethe/fireset/commit/7fec34f028de36081c51d5558ed20268cd6fee86) by Jelmer Vernooĳ).
- Fix note about authentication in getting started docs page ([0f66e2c](https://github.com/ydethe/fireset/commit/0f66e2c98c26ce6a5a0d06c56d17d415be7b13c1) by Denis Laxalde).
- Fix cross-references in documentation ([e8c13b7](https://github.com/ydethe/fireset/commit/e8c13b78d3d2b9a9d49c1d5e1628419867f29af9) by Denis Laxalde).
- Fix flake8 formatting compatibility. ([85482eb](https://github.com/ydethe/fireset/commit/85482eb441f5d7f1dd0a979cc41a7ee73fd81183) by Jelmer Vernooĳ).
- Fix typing errors. ([c1ce379](https://github.com/ydethe/fireset/commit/c1ce3791fadd0a2b165f9c8677baae4bce99bb5b) by Jelmer Vernooĳ).
- Fix syntax. ([b22ced4](https://github.com/ydethe/fireset/commit/b22ced40c294ead29aeaa6a7832aa127942e6187) by Jelmer Vernooĳ).
- Fix style. ([ddd67ab](https://github.com/ydethe/fireset/commit/ddd67abf4e13107a5e5d44b71623acfdcab8e1b4) by Jelmer Vernooĳ).
- Fix handling of missing trees. ([7745285](https://github.com/ydethe/fireset/commit/7745285dfb6c6ce10dc8e4105c4b662624673777) by Jelmer Vernooĳ).
- Fix typo. ([727646a](https://github.com/ydethe/fireset/commit/727646aef321e51c3aba070847a761509d7a4d8b) by Jelmer Vernooĳ).
- Fix hierarchy for supported report. Fixes #149 ([eadc405](https://github.com/ydethe/fireset/commit/eadc405698ce6d94ffa4517bbc26aaf733d9c761) by Jelmer Vernooĳ).
- Fix ordering. ([31364b6](https://github.com/ydethe/fireset/commit/31364b6a62085cb1d4d75bf76198698c81a1c9ad) by Jelmer Vernooĳ).

### Removed

- Remove specification of deprecated data_files. See https://github.com/pypa/setuptools/issues/2832 (#214) ([c0ddfd8](https://github.com/ydethe/fireset/commit/c0ddfd80499baae43cf7d22de5148c1bc941967d) by Jelmer Vernooĳ).
- Remove apt lists from Dockerfile ([72a474f](https://github.com/ydethe/fireset/commit/72a474fbb1cdaceec029c436039b7cb78365026e) by Galen Abell).
- Remove unnecessary #noqa comments (#154) ([9575eb1](https://github.com/ydethe/fireset/commit/9575eb12b901e22af59fdb9366151f029c75f84a) by Upstream Janitor).

## [v0.2.8](https://github.com/ydethe/fireset/releases/tag/v0.2.8) - 2022-01-09

<small>[Compare with v0.2.7](https://github.com/ydethe/fireset/compare/v0.2.7...v0.2.8)</small>

## [v0.2.7](https://github.com/ydethe/fireset/releases/tag/v0.2.7) - 2021-12-27

<small>[Compare with v0.2.6](https://github.com/ydethe/fireset/compare/v0.2.6...v0.2.7)</small>

### Added

- Add .stestr. ([59cbe9d](https://github.com/ydethe/fireset/commit/59cbe9d533b10589db5ea48a41c1f42ed90d44a4) by Jelmer Vernooĳ).
- Add stestr config. ([305649b](https://github.com/ydethe/fireset/commit/305649b322dc35d84ff1a1a7b9abceb7969e37c4) by Jelmer Vernooĳ).
- add a /health target. ([398d799](https://github.com/ydethe/fireset/commit/398d799865911a2ed6f7a9853f0fc14168cdd2c4) by Jelmer Vernooĳ).
- Add SUPPORT.md. ([554e8f0](https://github.com/ydethe/fireset/commit/554e8f00d6acf4e4a23f527b1965326ed1453da7) by Jelmer Vernooĳ).
- Add basic xmpp property support. ([94ec35a](https://github.com/ydethe/fireset/commit/94ec35a6f253b1a77392125520271c3d86caa225) by Jelmer Vernooĳ).

### Fixed

- Fix yaml ([be42c06](https://github.com/ydethe/fireset/commit/be42c0678ea2ed8b1e2975d7b64f34c2d59b541d) by Jelmer Vernooĳ).
- Fix typo. ([9de2b51](https://github.com/ydethe/fireset/commit/9de2b514b965c92eced6eea86b6a5b6a8681ae33) by Jelmer Vernooĳ).
- Fix docker image. ([87bd4ce](https://github.com/ydethe/fireset/commit/87bd4ce9838a1f7b049c53b38b38ede62ec05b99) by Jelmer Vernooĳ).
- Fix link. ([462cae0](https://github.com/ydethe/fireset/commit/462cae0b21a72299e8442a256c2eafaadeb9c5a7) by Jelmer Vernooĳ).

### Changed

- Change CONTRIBUTING to markdown. ([773b4f9](https://github.com/ydethe/fireset/commit/773b4f91e1de6c831e010b5a69da4ea3689dd933) by Jelmer Vernooĳ).

## [v0.2.6](https://github.com/ydethe/fireset/releases/tag/v0.2.6) - 2021-03-20

<small>[Compare with v0.2.5](https://github.com/ydethe/fireset/compare/v0.2.5...v0.2.6)</small>

### Added

- Add manual page. Fixes #128 ([1fc7e78](https://github.com/ydethe/fireset/commit/1fc7e78af7ccf17d3b542833ccfea8074b509355) by Jelmer Vernooĳ).
- Add SECURITY.md. ([ac123f0](https://github.com/ydethe/fireset/commit/ac123f037b40d8bd30efb9dc15cd729294fb2b7a) by Jelmer Vernooĳ).
- Add CODE_OF_CONDUCT.md. ([2905832](https://github.com/ydethe/fireset/commit/29058325fab32a3d72cc3c5643a5c02bc8eef8e9) by Jelmer Vernooĳ).

### Fixed

- Fix handling of async generators. ([11c5c33](https://github.com/ydethe/fireset/commit/11c5c33df8d4993a95d86eb48485e0d33f96c7cc) by Jelmer Vernooĳ).
- Fix contact email. ([2e3c92a](https://github.com/ydethe/fireset/commit/2e3c92a3942ae0a6b946a050452b199e0a432d66) by Jelmer Vernooĳ).

## [v0.2.5](https://github.com/ydethe/fireset/releases/tag/v0.2.5) - 2021-02-18

<small>[Compare with v0.2.4](https://github.com/ydethe/fireset/compare/v0.2.4...v0.2.5)</small>

## [v0.2.4](https://github.com/ydethe/fireset/releases/tag/v0.2.4) - 2021-02-16

<small>[Compare with v0.2.3](https://github.com/ydethe/fireset/compare/v0.2.3...v0.2.4)</small>

### Added

- Add releaser configuration. ([49c1504](https://github.com/ydethe/fireset/commit/49c15044ce2c18518b0242415c12ffd77cfa1fe1) by Jelmer Vernooĳ).
- Add support for EXRULE. ([a5e3e0e](https://github.com/ydethe/fireset/commit/a5e3e0edf52d9d6915ac5b117078c63896949ab9) by Jelmer Vernooĳ).
- Add support for schedule-tag. ([f6af45e](https://github.com/ydethe/fireset/commit/f6af45e80e0b924a4279720e5238b32d1c77b144) by Jelmer Vernooĳ).
- Add basic support for expanding rrules. Fixes #8 ([22af238](https://github.com/ydethe/fireset/commit/22af238d3543f7e4a892156cf6e5ab5aa8da90c3) by Jelmer Vernooĳ).

### Fixed

- Fix formatting. ([cbde8f7](https://github.com/ydethe/fireset/commit/cbde8f77896c0c3c0211c6696e54b9b3176ec65e) by Jelmer Vernooĳ).
- fix Dockerfile ([f321bf6](https://github.com/ydethe/fireset/commit/f321bf60aea1457b227c35790b743dff6be53a57) by Tobias Salzmann).
- Fix Expect support. ([7fefcdb](https://github.com/ydethe/fireset/commit/7fefcdb4f4e99f093779a8ca66e99204a8f0f3d4) by Jelmer Vernooĳ).
- Fix schedule-tag behaviour. ([2539f24](https://github.com/ydethe/fireset/commit/2539f24e698382275e1826c5e6f022325e345761) by Jelmer Vernooĳ).
- Fix typos, update NEWS. ([f983dd5](https://github.com/ydethe/fireset/commit/f983dd5dfc62415b19fcd7a739c52a3a8faa1995) by Jelmer Vernooĳ).

## [v0.2.3](https://github.com/ydethe/fireset/releases/tag/v0.2.3) - 2020-07-25

<small>[Compare with v0.2.2](https://github.com/ydethe/fireset/compare/v0.2.2...v0.2.3)</small>

### Added

- Add --no-strict option for clients that don't follow the spec. ([f90510e](https://github.com/ydethe/fireset/commit/f90510e00b1074db9b04a57b1360ad32d60b5506) by Jelmer Vernooĳ).
- Add avahi support. ([22abdbb](https://github.com/ydethe/fireset/commit/22abdbb85fe1080583c0130ee26a2b1e1864390f) by Jelmer Vernooĳ).
- Add example avahi service file. ([4e4541d](https://github.com/ydethe/fireset/commit/4e4541d9e0cfc21dbcaebee04e3ac0a15acebd54) by Jelmer Vernooĳ).
- Add universal wheel. ([1317c3e](https://github.com/ydethe/fireset/commit/1317c3e4a837abb09a8c6c05e0e2b568e50ab662) by Jelmer Vernooĳ).
- Add dependency on pytest. ([7cef0c3](https://github.com/ydethe/fireset/commit/7cef0c3ce28d2d328356cdd3f74716ba70076482) by Jelmer Vernooĳ).
- Add workflow for publishing. ([c78b613](https://github.com/ydethe/fireset/commit/c78b61361c48d3f36bbb58c7a8ef51b30be65e70) by Jelmer Vernooĳ).
- Add github action. ([1fac6ba](https://github.com/ydethe/fireset/commit/1fac6ba9a79adc6acd49bdd16cfebbeff06cd720) by Jelmer Vernooĳ).
- Add CollectionSetResource.get_creationdate. ([fe12b64](https://github.com/ydethe/fireset/commit/fe12b64ae25a75d7380d11e89fa8f9b81302a259) by Jelmer Vernooĳ).

### Fixed

- Fix typing. ([b556753](https://github.com/ydethe/fireset/commit/b556753e5def9c3bea9a46b89df70fffe6ede8db) by Jelmer Vernooĳ).
- Fix attribute name in error. ([3ecda32](https://github.com/ydethe/fireset/commit/3ecda32c18b57b50f4dae9714ec2373666b7404d) by Jelmer Vernooĳ).
- Fix name error. ([5b96fa6](https://github.com/ydethe/fireset/commit/5b96fa6d36f3f9eb602d5994a1ad3a3a6ef97e61) by Jelmer Vernooĳ).
- Fix formatting. ([0d6920d](https://github.com/ydethe/fireset/commit/0d6920ddef4658c35a86aea126e0875787cd4665) by Jelmer Vernooĳ).
- Fix style. ([0fef5e9](https://github.com/ydethe/fireset/commit/0fef5e918aec527c37c376efaf433630e4e4bc02) by Jelmer Vernooĳ).
- Fix regresion. ([32a142e](https://github.com/ydethe/fireset/commit/32a142eae5949aa238f268ac6a2b4a6354bcb297) by Jelmer Vernooĳ).

## [v0.2.2](https://github.com/ydethe/fireset/releases/tag/v0.2.2) - 2020-05-14

<small>[Compare with v0.2.1](https://github.com/ydethe/fireset/compare/v0.2.1...v0.2.2)</small>

### Fixed

- Fix uwsgi use. ([30f3e4b](https://github.com/ydethe/fireset/commit/30f3e4bbc4c4d4f3008a5ce5b5bcfe1d296c669c) by Jelmer Vernooĳ).

## [v0.2.1](https://github.com/ydethe/fireset/releases/tag/v0.2.1) - 2020-05-06

<small>[Compare with v0.2.0](https://github.com/ydethe/fireset/compare/v0.2.0...v0.2.1)</small>

### Added

- Add missing dependencies on aiohttp, multidict. ([e6edfcc](https://github.com/ydethe/fireset/commit/e6edfccec29c24b5a291c4ffaee6956aea55ac62) by Jelmer Vernooĳ).

### Fixed

- Fix style. ([947be27](https://github.com/ydethe/fireset/commit/947be2768fe075f4dbe75dceb1528aedea8a4edb) by Jelmer Vernooĳ).
- Fix underindent. ([bdd1441](https://github.com/ydethe/fireset/commit/bdd14419cbe24787a2ec4cb92f039362c40f0eb3) by Jelmer Vernooĳ).
- Fix types. ([f5761cb](https://github.com/ydethe/fireset/commit/f5761cb041d6c760c159f4cab0ac7193f591905f) by Jelmer Vernooĳ).

## [v0.2.0](https://github.com/ydethe/fireset/releases/tag/v0.2.0) - 2020-05-04

<small>[Compare with v0.1.0](https://github.com/ydethe/fireset/compare/v0.1.0...v0.2.0)</small>

### Added

- Add some more typing. ([5d8cd12](https://github.com/ydethe/fireset/commit/5d8cd12ba5e1e643dc99121e3d84de38cc21be24) by Jelmer Vernooĳ).
- Add uwsgi notes. ([0d11a88](https://github.com/ydethe/fireset/commit/0d11a88a352a5f36b439b3e3ee2aab58c9f02dfd) by Jelmer Vernooĳ).
- Add systemd configuration. ([0b32591](https://github.com/ydethe/fireset/commit/0b32591a3067a99b0bbf9a3b50563cedb63acdec) by Jelmer Vernooĳ).
- Add support for listening on unix domain sockets. ([a7fcae1](https://github.com/ydethe/fireset/commit/a7fcae1f2e61025ce9081aa3ac2dad8303fcf091) by Jelmer Vernooĳ).
- Add some type annotations. ([9c0fc23](https://github.com/ydethe/fireset/commit/9c0fc23c2fbfa8275dc0ec129c15b2f5dcad61ec) by Jelmer Vernooĳ).
- Add missing awaits. ([2f0780d](https://github.com/ydethe/fireset/commit/2f0780daefae5c92e2011ac46c383b3acb476eac) by Jelmer Vernooĳ).
- Add some performance metrics. ([0eeb9c4](https://github.com/ydethe/fireset/commit/0eeb9c40faf47b27ce4542c2fbc33025ebdbe9ef) by Jelmer Vernooĳ).
- Add explicit dependency on prometheus_client. ([3b23cf6](https://github.com/ydethe/fireset/commit/3b23cf60faa2ea2c58de2b98bcd7a6d3de25dccc) by Jelmer Vernooĳ).
- Add a few more properties to Subscription. ([b22a456](https://github.com/ydethe/fireset/commit/b22a456835fb91567664bfd8810a4a57a7c2a26c) by Jelmer Vernooĳ).
- Add basic support for Apple's source property. ([7cad2b2](https://github.com/ydethe/fireset/commit/7cad2b216508e69f0776efafcda6ce93c837f212) by Jelmer Vernooĳ).
- Add WSGI Request wrapper. ([4905973](https://github.com/ydethe/fireset/commit/4905973f5d61b7759e39d9c1b8252c2046ee69bb) by Jelmer Vernooĳ).
- Add test for CALDAV:expand. ([925eb6b](https://github.com/ydethe/fireset/commit/925eb6b3b30bac7b45d3c998338ff3f54b58112c) by Jelmer Vernooĳ).
- Add tests for extract_from_calendar. ([44924a2](https://github.com/ydethe/fireset/commit/44924a23de432c6cda880222954afd8f66ca8d5f) by Jelmer Vernooĳ).
- Add requirements.txt. ([9b77457](https://github.com/ydethe/fireset/commit/9b77457f36df84f7ab21f1d90191424a06254fc6) by Jelmer Vernooĳ).
- Add TODO. ([5a83457](https://github.com/ydethe/fireset/commit/5a83457687079f5003d56fbcfd9d9e208431f774) by Jelmer Vernooĳ).
- Add a /metrics page. ([fc25afb](https://github.com/ydethe/fireset/commit/fc25afbdf34f53c4aa3488b08175bb3d71561cd8) by Jelmer Vernooĳ).
- Add initial asyncio version using aiowsgi. ([c068c37](https://github.com/ydethe/fireset/commit/c068c37e3f9e1cb3a0a409f863efc519f1169e28) by Jelmer Vernooĳ).

### Fixed

- Fix formatting. ([70a3030](https://github.com/ydethe/fireset/commit/70a303046eb4bedd9c74b8603dd58f97697589ba) by Jelmer Vernooĳ).
- Fix docker image. Fixes #117 ([f89e984](https://github.com/ydethe/fireset/commit/f89e984e6ab14fecd302c53c4557499b4012bf10) by Jelmer Vernooĳ).
- Fix style. ([501d519](https://github.com/ydethe/fireset/commit/501d519cf09eee88631dd03713fcaa231b50ac09) by Jelmer Vernooĳ).
- Fix base path. ([d8ed224](https://github.com/ydethe/fireset/commit/d8ed22475997c3f2448e6cfa0fddbae4c2414a8e) by Jelmer Vernooĳ).
- Fix wsgi handling. ([1fd52a8](https://github.com/ydethe/fireset/commit/1fd52a872f89e3120582603386502ce82469025a) by Jelmer Vernooĳ).
- Fix filtering on property/component in extract_from_calendar. ([9a90449](https://github.com/ydethe/fireset/commit/9a90449cfb90a26f3983b0d8e185e533e08c4716) by Jelmer Vernooĳ).

## [v0.1.0](https://github.com/ydethe/fireset/releases/tag/v0.1.0) - 2019-04-07

<small>[Compare with v0.0.11](https://github.com/ydethe/fireset/compare/v0.0.11...v0.1.0)</small>

### Added

- Add support for ParameterFilter. ([9137473](https://github.com/ydethe/fireset/commit/91374734db74144d014340d16139f7301cf9dfe7) by Jelmer Vernooĳ).
- Add some assertions. ([a747ce4](https://github.com/ydethe/fireset/commit/a747ce40fbc52646ced5ca8179bd3d2033d06f63) by Jelmer Vernooĳ).
- Add test for missing components. ([9e35a1e](https://github.com/ydethe/fireset/commit/9e35a1eb2ae2eb4099e3afda01a981046763697f) by Jelmer Vernooĳ).
- Add tests for time-range. ([c6c160a](https://github.com/ydethe/fireset/commit/c6c160abb04c6880bf13a52e6f31c54736c34957) by Jelmer Vernooĳ).
- Add repr, fix missing argument. ([23fe659](https://github.com/ydethe/fireset/commit/23fe65994280bb85b6485905534bbc77cf6b22c4) by Jelmer Vernooĳ).
- Add note about python 3.8 compatibility for defusedxml. ([74b05be](https://github.com/ydethe/fireset/commit/74b05bee13887f8ccc58ac29def0d86d5434a98b) by Jelmer Vernooĳ).
- Add pycaldav tests for xandikos. ([f4a1251](https://github.com/ydethe/fireset/commit/f4a1251f1cd4299f29ac40bb4159aad663fc2014) by Jelmer Vernooĳ).
- Add some more tests. ([9d5c872](https://github.com/ydethe/fireset/commit/9d5c8725aebf3309a382a84bae3a8e6f68346e1c) by Jelmer Vernooĳ).
- add more tests for web. ([a4329e6](https://github.com/ydethe/fireset/commit/a4329e6821c8f7990b0f54beb8175b1df835f3b9) by Jelmer Vernooĳ).
- Add tests for text matching. ([1f61142](https://github.com/ydethe/fireset/commit/1f6114237b9ec52ea649a795d8f319231a9bba34) by Jelmer Vernooĳ).
- Add test for Store.iter_with_filter. ([05dec69](https://github.com/ydethe/fireset/commit/05dec69ed220530d0d4347b093711650117c0aeb) by Jelmer Vernooĳ).
- Add some initial notes on indexes. ([d9a7fe2](https://github.com/ydethe/fireset/commit/d9a7fe216c0fd7fb3695eed5df82c1f70505ae00) by Jelmer Vernooĳ).
- Add a bit of background on why trailing slashes are included. ([07feec7](https://github.com/ydethe/fireset/commit/07feec7e5731e8a165e43fa3f50cd89a7a07bb25) by Jelmer Vernooĳ).
- Add support for calendar-order property. ([4c87142](https://github.com/ydethe/fireset/commit/4c87142585c4030a2f4d4b745333b2905e656e46) by Jelmer Vernooĳ).
- Add debugging notes. ([d856e15](https://github.com/ydethe/fireset/commit/d856e1576e4db101e228fbcb142976efd28217da) by Jelmer Vernooĳ).
- Add type to configuration. ([f63034e](https://github.com/ydethe/fireset/commit/f63034ed7090d74987d78683219b604b809789bf) by Jelmer Vernooĳ).
- Add TODO, add note on prometheus. ([1e970f8](https://github.com/ydethe/fireset/commit/1e970f8a1bb0377fdd080fa7f4f1df6422d48f87) by Jelmer Vernooĳ).
- Add initial devnotes on subcommands. ([71c8210](https://github.com/ydethe/fireset/commit/71c82100031c94cbff0e692a5ba1de0abc323bca) by Jelmer Vernooĳ).
- Add comment about hostnames. ([3be9f24](https://github.com/ydethe/fireset/commit/3be9f2455bd5cb6f1a571b09dab4dfcc86c0311b) by Jelmer Vernooĳ).
- Add notes on acl configuration. ([ea62d54](https://github.com/ydethe/fireset/commit/ea62d5468afc7a50d4cc0f59cdc7515ce3b8b51b) by Jelmer Vernooĳ).
- Add set functions for config. ([6f09590](https://github.com/ydethe/fireset/commit/6f09590f00afb4e39fe45484984986cbcf024b47) by Jelmer Vernooĳ).
- Add repo based configuration. ([9ab8b33](https://github.com/ydethe/fireset/commit/9ab8b33c253ca662f9f9861bf74ed1ed236d6183) by Jelmer Vernooĳ).
- Add metadata base class. ([23f3058](https://github.com/ydethe/fireset/commit/23f3058d6bc21b910cba90f54b33ad10285973a8) by Jelmer Vernooĳ).
- Add some tests for config. ([c85c8f5](https://github.com/ydethe/fireset/commit/c85c8f587be5d9f3471afa10c60e67af1b0060d1) by Jelmer Vernooĳ).

### Fixed

- Fix templates for bare principal. ([1d47639](https://github.com/ydethe/fireset/commit/1d47639c3f7900633fbeb5432d347115fd8d9ba6) by Jelmer Vernooĳ).
- Fix templates. ([18c2a94](https://github.com/ydethe/fireset/commit/18c2a945cc31472e6f80b6d2d8eb43e396271c84) by Jelmer Vernooĳ).
- Fix checking. ([b786b46](https://github.com/ydethe/fireset/commit/b786b46a1907fd54444e263a6270f6078b0d1fdf) by Jelmer Vernooĳ).
- Fix handling of filters with missing properties. ([16c0874](https://github.com/ydethe/fireset/commit/16c08749b780104b2b38badd0e50b65aa1b87c48) by Jelmer Vernooĳ).
- Fix various minor issues. ([91ed9aa](https://github.com/ydethe/fireset/commit/91ed9aa9c10dfc65cd5eb18f3aa2f6f9cb2229c8) by Jelmer Vernooĳ).
- Fix style. ([0995c18](https://github.com/ydethe/fireset/commit/0995c182c52a38301934d4b519b8c8f5293b0d0a) by Jelmer Vernooĳ).
- Fix filter parsing. ([1f369ee](https://github.com/ydethe/fireset/commit/1f369eeb569994fa008876427dbd2c05f42900ce) by Jelmer Vernooĳ).
- Fix tests. ([4f02326](https://github.com/ydethe/fireset/commit/4f02326904fa70602e13ed70b9ab5753b4e6dd99) by Jelmer Vernooĳ).
- Fix pycaldav test on travis. ([5b23b7b](https://github.com/ydethe/fireset/commit/5b23b7bab7e4b8a43dff23e37f7b2113a7cdac9d) by Jelmer Vernooĳ).
- Fix handling of get_managed_attachements_server_url. ([69bf99b](https://github.com/ydethe/fireset/commit/69bf99bc6f24f730803f3fab47afdecde63e0f9a) by Jelmer Vernooĳ).
- Fix error message when unable to convert between content types. ([d3f54cb](https://github.com/ydethe/fireset/commit/d3f54cbb6c5d02321a93ae10e8f0e30d2a08b6ce) by Jelmer Vernooĳ).
- Fix handling of missing DTSTART in VEVENT. ([f8782b0](https://github.com/ydethe/fireset/commit/f8782b065140fff14dedf8ffbaa957ddae2794ae) by Jelmer Vernooĳ).

### Removed

- Remove unused import. ([6d7b8b0](https://github.com/ydethe/fireset/commit/6d7b8b096b241258723c1e2ec3e9809329436541) by Jelmer Vernooĳ).
- Remove obsolete class. ([b162e63](https://github.com/ydethe/fireset/commit/b162e630c388167699490cc93d52f4fec80a6777) by Jelmer Vernooĳ).
- Remove TODO from manifest template ([19042f5](https://github.com/ydethe/fireset/commit/19042f58d0dba6ace778488062d5459414d01a41) by Daniel M. Capella).
- Remove win32-specific hack. ([adf6837](https://github.com/ydethe/fireset/commit/adf6837cb0744e9830bd86a6e2ed9a43ea4ac3cc) by Jelmer Vernooĳ).

## [v0.0.11](https://github.com/ydethe/fireset/releases/tag/v0.0.11) - 2018-11-14

<small>[Compare with v0.0.10](https://github.com/ydethe/fireset/compare/v0.0.10...v0.0.11)</small>

### Added

- Add GOALS.rst. ([e0f3358](https://github.com/ydethe/fireset/commit/e0f3358fce5a52daadd97b110c2c20a46460f980) by Jelmer Vernooĳ).

### Fixed

- Fix two more style errors. ([9073c7c](https://github.com/ydethe/fireset/commit/9073c7c49397e0d118e610fad947cd3ce12c039e) by Jelmer Vernooĳ).
- Fix style errors. ([32f70e0](https://github.com/ydethe/fireset/commit/32f70e0b399584c7c11df3dca47e4cb3e2b58a32) by Jelmer Vernooĳ).

## [v0.0.10](https://github.com/ydethe/fireset/releases/tag/v0.0.10) - 2018-10-31

<small>[Compare with v0.0.9](https://github.com/ydethe/fireset/compare/v0.0.9...v0.0.10)</small>

### Added

- Add detail string to InvalidFileContent ([bb87de3](https://github.com/ydethe/fireset/commit/bb87de38164e13aae2ab214b92288ef294d1850d) by Jelmer Vernooĳ).
- Add cardbook to supported clients. Fixes #77 ([739daab](https://github.com/ydethe/fireset/commit/739daab936e5d79d5565b4fa1fdb21b9d2a4b862) by Jelmer Vernooĳ).
- Add trailing slash to hrefs. ([1ec180c](https://github.com/ydethe/fireset/commit/1ec180c3d61ade57a4651917a23b0f7d1a61f896) by Jelmer Vernooĳ).
- Add a separate template for principals. ([1e750cf](https://github.com/ydethe/fireset/commit/1e750cf28a7bbfa20e40c0cc94188f943b407604) by Jelmer Vernooĳ).
- Add xandikos.__main__. ([4283e94](https://github.com/ydethe/fireset/commit/4283e9457dd19a3694651b454144c7bd66268eb8) by Jelmer Vernooĳ).

### Fixed

- Fix style. ([12a7bb3](https://github.com/ydethe/fireset/commit/12a7bb3ccd164880f4607ae9adbae5e976e6ec48) by Jelmer Vernooĳ).
- Fix coverage reporting for vdirsyncer tests. ([663d746](https://github.com/ydethe/fireset/commit/663d74654ead977599d5521f29316deb58a41173) by Jelmer Vernooĳ).
- Fix vdirsyncer tests. ([65a2891](https://github.com/ydethe/fireset/commit/65a2891fb98188f556ad7b7b4311eb1f51e5ec76) by Jelmer Vernooĳ).
- Fix typo: resource_types => resource_type. ([54de4b9](https://github.com/ydethe/fireset/commit/54de4b94bf402e62dfc309acb5c6f3654766de20) by Jelmer Vernooĳ).

### Removed

- Remove unnecessary __main__. ([e1368f9](https://github.com/ydethe/fireset/commit/e1368f92067ac7f4729f3dbb9e4365d12b4ce265) by Jelmer Vernooĳ).

## [v0.0.9](https://github.com/ydethe/fireset/releases/tag/v0.0.9) - 2018-04-07

<small>[Compare with v0.0.7](https://github.com/ydethe/fireset/compare/v0.0.7...v0.0.9)</small>

## [v0.0.7](https://github.com/ydethe/fireset/releases/tag/v0.0.7) - 2018-04-02

<small>[Compare with v0.0.6](https://github.com/ydethe/fireset/compare/v0.0.6...v0.0.7)</small>

### Added

- Add really basic validation test for calendar. ([b838f8e](https://github.com/ydethe/fireset/commit/b838f8e4d1494bff76afe74fa1bbbd3218c44fe3) by Jelmer Vernooĳ).
- Add comment about validation. ([421e73e](https://github.com/ydethe/fireset/commit/421e73e94c73dcd0287eeae5fb992d89238fb070) by Jelmer Vernooĳ).
- Add inbox in glue. ([7474629](https://github.com/ydethe/fireset/commit/7474629717980d7b983ca20238a20dbf6ae882ce) by Jelmer Vernooĳ).
- Add schedule inbox/outbox store types. ([5f8bc77](https://github.com/ydethe/fireset/commit/5f8bc775e6707a7462aaf9e3294970e8b919e5c2) by Jelmer Vernooĳ).
- Add tests for apply_text_match. ([764f6ee](https://github.com/ydethe/fireset/commit/764f6eedd6de63596c5e8f36dbabc0cf0de75101) by Jelmer Vernooĳ).
- Add support for max-attachments-per-resource and max-attachment-size properties. ([6033119](https://github.com/ydethe/fireset/commit/60331191b4ab645feaf53c2aea2926dd58b4fcd6) by Jelmer Vernooĳ).
- Add missing config file. ([bc06fec](https://github.com/ydethe/fireset/commit/bc06fec844d2cb313e5e69e7f90e1b4cb6586289) by Jelmer Vernooĳ).
- Add notes on deploying on Heroku. ([6c270ca](https://github.com/ydethe/fireset/commit/6c270caf670b4c492e2c49a520a34c3b4dbc60bd) by Jelmer Vernooĳ).
- Add instructions on running heroku. ([913ec7b](https://github.com/ydethe/fireset/commit/913ec7b19b7cf209e8a26f0efe2d2ca24cd3a973) by Jelmer Vernooĳ).
- Add heroku configuration. ([ab04d31](https://github.com/ydethe/fireset/commit/ab04d31cc85e798ce444c43b2e6e1c1e9c3f8c8b) by Jelmer Vernooĳ).
- Add CalDAV scheduling implementation notes. ([fe0d311](https://github.com/ydethe/fireset/commit/fe0d311e6972ed0f33b67ae0ca67929d62012a6d) by Jelmer Vernooĳ).
- Add schedule-tag property status in notes. ([8c982b4](https://github.com/ydethe/fireset/commit/8c982b434b93ead463f7a9f287799c366af0fb57) by Jelmer Vernooĳ).
- Add schedule-default-calendar-URL property. ([902fbb2](https://github.com/ydethe/fireset/commit/902fbb2d6b15f914de3ff20de42767d2aeababf3) by Jelmer Vernooĳ).
- Add remaining schedule-inbox/schedule-outbox properties. ([a04c0d5](https://github.com/ydethe/fireset/commit/a04c0d5a70b7d309c650c8858d5133eba49c8c2e) by Jelmer Vernooĳ).
- Add max-instance-size for calendars. ([eadc3b9](https://github.com/ydethe/fireset/commit/eadc3b9561a1c4f37644a6831c567c8cafb04426) by Jelmer Vernooĳ).
- Add --dump-dav-xml option to dump out DAV XML requests/responses to stdout. ([4e7f821](https://github.com/ydethe/fireset/commit/4e7f8218117e861bf25f8625d4f264f30d4fc356) by Jelmer Vernooĳ).
- Add print statements to dump DAV input/output. ([4e4cbf7](https://github.com/ydethe/fireset/commit/4e4cbf7a62b2ab8cb6371e57a10c2b9f3eba49f5) by Jelmer Vernooĳ).
- Add features for quota/sync-collection/add-member. ([4db1a4b](https://github.com/ydethe/fireset/commit/4db1a4b986d055c6d55e4d1501779a810c4fdf2c) by Jelmer Vernooĳ).
- Add simple client configuration instructions ([09f5ee6](https://github.com/ydethe/fireset/commit/09f5ee648afe79648a752897f2ff33067597a882) by Linus Wallgren).
- Add tasks to list of supported clients. ([a4f22c7](https://github.com/ydethe/fireset/commit/a4f22c79a8c5c4a030cb96013e3a927d17e3c402) by Jelmer Vernooĳ).
- Add an environ argument to get_value(). ([16e9a96](https://github.com/ydethe/fireset/commit/16e9a96c594564a1a2a6fd7856b18b25a665c29d) by Jelmer Vernooĳ).
- Add implementation notes. ([37e2dc5](https://github.com/ydethe/fireset/commit/37e2dc5bcef7d2d5036bbf6d4be4a39c7590315f) by Jelmer Vernooĳ).
- Add some notes on multi-user support. ([5befd6d](https://github.com/ydethe/fireset/commit/5befd6d55e2ff38e0327f9e78956800a62f8e559) by Jelmer Vernooĳ).

### Fixed

- Fix style. ([6cae497](https://github.com/ydethe/fireset/commit/6cae49755f7d726d89788fd2d347b05e5e2943a5) by Jelmer Vernooĳ).
- Fix use of max-attachment-per-resource, max-attachment-size. ([54b7bda](https://github.com/ydethe/fireset/commit/54b7bda3d3ec93a14914ab845e467a3cd2f8d746) by Jelmer Vernooĳ).
- Fix style errors. --BZR-- parent-ids: git-v1:7474629717980d7b983ca20238a20dbf6ae882ce property-branch-nick: HEAD ([e45de8b](https://github.com/ydethe/fireset/commit/e45de8b85c42282988d3df41429ffa1a830c8b09) by Jelmer Vernooĳ).
- Fix order of arguments to get_property_from_element. ([c4fdc24](https://github.com/ydethe/fireset/commit/c4fdc248c00450d933ce27d8b504d0938409b796) by Jelmer Vernooĳ).
- Fixes for vdirsyncer's rust usage ([a461c83](https://github.com/ydethe/fireset/commit/a461c83afb34b28ec5c2a2e5b565225f6c9d4b4e) by Markus Unterwaditzer).
- Fix style error. ([36cdbbb](https://github.com/ydethe/fireset/commit/36cdbbb59ceed4ac43f2eadf9a9f4fb2c9cccec6) by Jelmer Vernooĳ).
- Fix missing store subpackage ([931c149](https://github.com/ydethe/fireset/commit/931c149123204189de26265b382b93631b675001) by Markus Unterwaditzer).
- Fix style errors. ([5663a6e](https://github.com/ydethe/fireset/commit/5663a6ea1c72ab008ed2461bad4f502111224d18) by Jelmer Vernooĳ).
- Fix formatting. ([845ed35](https://github.com/ydethe/fireset/commit/845ed35f2f8f3ee73358b5dee34cc4f43af23b8d) by Jelmer Vernooĳ).
- Fix the build. ([56b7ba4](https://github.com/ydethe/fireset/commit/56b7ba4661bf4aa662bfda4ed51be980caf9da43) by Jelmer Vernooĳ).

### Removed

- Remove uwsgitop since it's not a strict requirement. ([e763f21](https://github.com/ydethe/fireset/commit/e763f211de11b0b62ae12e6fff33ca46f5934994) by Jelmer Vernooĳ).

## [v0.0.6](https://github.com/ydethe/fireset/releases/tag/v0.0.6) - 2017-07-13

<small>[Compare with v0.0.5](https://github.com/ydethe/fireset/compare/v0.0.5...v0.0.6)</small>

### Added

- Add some constants for scheduling. ([adc16ba](https://github.com/ydethe/fireset/commit/adc16ba34f5d478ffd421c633561a28a620f0055) by Jelmer Vernooĳ).
- Add TODO. ([cde1156](https://github.com/ydethe/fireset/commit/cde115635f305b35fac79f97eb98331806adfb67) by Jelmer Vernooĳ).
- Add section on contributing to README. ([7a439aa](https://github.com/ydethe/fireset/commit/7a439aad81fb94143a7e133b5eb54932313242ab) by Jelmer Vernooĳ).
- Add note on DAV Mount support. ([00b3838](https://github.com/ydethe/fireset/commit/00b3838ec117e56f5c1f72a182be48c1a0c06279) by Jelmer Vernooĳ).
- Add note about WebDAV Mount. ([1ac49c0](https://github.com/ydethe/fireset/commit/1ac49c02a3a28bcbfdfd5499e9643d693c4a1c8e) by Jelmer Vernooĳ).

### Fixed

- Fix a style error. ([ce765e1](https://github.com/ydethe/fireset/commit/ce765e1f3339d9016efccf1dfa6a0d56a26b818c) by Jelmer Vernooĳ).

### Removed

- Remove duplicate www. Thanks, dmc :) ([a953a5d](https://github.com/ydethe/fireset/commit/a953a5d7a31c217380019188723119067087a22b) by Jelmer Vernooĳ).
- Remove unnecessary umask. ([766ee8f](https://github.com/ydethe/fireset/commit/766ee8f548e400691050a03da687c588639ea4a5) by Jelmer Vernooĳ).

## [v0.0.5](https://github.com/ydethe/fireset/releases/tag/v0.0.5) - 2017-06-24

<small>[Compare with v0.0.4](https://github.com/ydethe/fireset/compare/v0.0.4...v0.0.5)</small>

### Added

- Add 'et al' to copyright lines. ([a0d19a4](https://github.com/ydethe/fireset/commit/a0d19a4a1a511d0d9cca87b0a64973badb83b1e9) by Jelmer Vernooĳ).
- Add a principal store type. ([5ab68a6](https://github.com/ydethe/fireset/commit/5ab68a6ccd1aadc0736685fb82eded886463a59e) by Jelmer Vernooĳ).
- Add additional collections for caldavtester. ([ff7cd60](https://github.com/ydethe/fireset/commit/ff7cd60914407a54d4b0bb1797a958895e163b46) by Jelmer Vernooĳ).
- Add Windows build status badge. ([592a8a7](https://github.com/ydethe/fireset/commit/592a8a736e05e2dfe2d273cb7bf168b20bebb481) by Jelmer Vernooĳ).
- Add appveyor config. ([a17c5fd](https://github.com/ydethe/fireset/commit/a17c5fde51a13ed42f1f7646fa118695da2451e1) by Jelmer Vernooĳ).
- Add calendarsync to supported clients. ([e2a3e54](https://github.com/ydethe/fireset/commit/e2a3e548228483df005250b1e5f410dd9c8da37c) by Jelmer Vernooĳ).
- Add mailmap. ([7cb4d92](https://github.com/ydethe/fireset/commit/7cb4d92f79b4a9e23b328dccc13d50cae7d4ea98) by Jelmer Vernooĳ).

### Fixed

- Fix support for mkcol-extended. ([f98557c](https://github.com/ydethe/fireset/commit/f98557c0685d54112065ae6ba58d915e37375068) by Jelmer Vernooĳ).
- Fix returning of supported-report-set. ([b38b8a7](https://github.com/ydethe/fireset/commit/b38b8a7b64b20a88cf6bb8a393e1270fff1a0976) by Jelmer Vernooĳ).
- Fix mkcalendar. ([df73b92](https://github.com/ydethe/fireset/commit/df73b92b667861461b952be17ddf5639570053e6) by Jelmer Vernooĳ).

## [v0.0.4](https://github.com/ydethe/fireset/releases/tag/v0.0.4) - 2017-04-23

<small>[Compare with v0.0.3](https://github.com/ydethe/fireset/compare/v0.0.3...v0.0.4)</small>

### Fixed

- Fix link to dav-compliance, now in rst. ([a9ada67](https://github.com/ydethe/fireset/commit/a9ada67abab031a3d568c90ecce9e100f5856f58) by Jelmer Vernooĳ).
- Fix support for CalDAV-sync/CardDAV-sync. ([56870f7](https://github.com/ydethe/fireset/commit/56870f7a207c5829a6ea0bbcfada8fe791ebff5a) by Jelmer Vernooĳ).
- Fix recursive includes. ([0f85485](https://github.com/ydethe/fireset/commit/0f854856376584f15ab7b70940df6d5c90221ddc) by Jelmer Vernooĳ).

## [v0.0.3](https://github.com/ydethe/fireset/releases/tag/v0.0.3) - 2017-04-11

<small>[Compare with v0.0.2](https://github.com/ydethe/fireset/compare/v0.0.2...v0.0.3)</small>

### Added

- Add initial support for auth. ([14d7b8e](https://github.com/ydethe/fireset/commit/14d7b8e4dbaa5baf58d025a315de40a2c611de62) by Jelmer Vernooĳ).
- Add Method class. ([1540bb7](https://github.com/ydethe/fireset/commit/1540bb768fb4ea6598640aa898cb7c4054601b27) by Jelmer Vernooĳ).
- Add headers to txt docs. ([bda33f6](https://github.com/ydethe/fireset/commit/bda33f6d33d955dd162fcc73d328c5bd4772f212) by Jelmer Vernooĳ).
- Add codecov config. ([5eb63ba](https://github.com/ydethe/fireset/commit/5eb63bac031c1e75397b8bfccd131c24414214fa) by Jelmer Vernooĳ).
- Add initial support for WebDAV quota. ([1299fbd](https://github.com/ydethe/fireset/commit/1299fbda8cd0c70fa07996694e2c595576d50e71) by Jelmer Vernooĳ).
- Add coverage-litmus. ([908be5b](https://github.com/ydethe/fireset/commit/908be5bb23792f0c866eee308adbb43caf2d7e50) by Jelmer Vernooĳ).
- Add vdirsyncer to CI ([bdd75a9](https://github.com/ydethe/fireset/commit/bdd75a918e9cc0857561a85e353015c71f14ddf8) by Markus Unterwaditzer).
- Add test for path_from_environ. ([e40334d](https://github.com/ydethe/fireset/commit/e40334d7f133ce5d4ad4ff73afd312b59ee745fa) by Jelmer Vernooĳ).
- Add initial support for calendar-proxy-{write,read}-for. ([d91b312](https://github.com/ydethe/fireset/commit/d91b3126887e17a52fcd1b00bcaaa9849a0746bc) by Jelmer Vernooĳ).
- Add support for mod_dav's executable property, and some other assorted fixes for issues found with cadaver. ([157eef2](https://github.com/ydethe/fireset/commit/157eef2149cf18a27580a37ed06ef3fbafdcbb0c) by Jelmer Vernooĳ).
- Add jinja2 to dependencies list in README. ([6fc9da0](https://github.com/ydethe/fireset/commit/6fc9da03062c89abc669dbec23e1e42496d635a0) by Jelmer Vernooĳ).
- Add basic tests for parse_accept_header. ([0add000](https://github.com/ydethe/fireset/commit/0add000a66b7b18300b2156e25e9f4b27459bc6c) by Jelmer Vernooĳ).
- Add tests for pick_content_types. ([80be1f6](https://github.com/ydethe/fireset/commit/80be1f6e0ee98a83db62b451a1071e1308562860) by Jelmer Vernooĳ).
- Add convenience function for rendering HTML using jinja. ([c3e51b7](https://github.com/ydethe/fireset/commit/c3e51b7e0ee68b518ce99e102f40249d47d1548f) by Jelmer Vernooĳ).
- Add basic content type negotiation support. ([d93c1cf](https://github.com/ydethe/fireset/commit/d93c1cfbd1ce46ef520cf9fd669b4189c0f457bf) by Jelmer Vernooĳ).
- Add convenience method for getting resource from environment. ([53e6e7d](https://github.com/ydethe/fireset/commit/53e6e7d9d1df86a54fe5c78ce6f54c665da70f12) by Jelmer Vernooĳ).
- Add convenience function for retrieving path from environment. ([11ff4af](https://github.com/ydethe/fireset/commit/11ff4af06bb058f959f3f8185e58236399f11faa) by Jelmer Vernooĳ).
- Add MKCALENDAR implementation. ([8cc0f95](https://github.com/ydethe/fireset/commit/8cc0f9501e0176d500d6233daa69f8af6ba06c72) by Jelmer Vernooĳ).
- Add convenience method for creating principal. ([e8bc97e](https://github.com/ydethe/fireset/commit/e8bc97e28ec54231e511c40b443b73742b379047) by Jelmer Vernooĳ).

### Fixed

- Fix style. ([87f0025](https://github.com/ydethe/fireset/commit/87f002525b7d297bd65299d799b77a6bb513de34) by Jelmer Vernooĳ).
- Fix codecov flags. ([d882bc5](https://github.com/ydethe/fireset/commit/d882bc52778240047028076598329dbc669f1efb) by Jelmer Vernooĳ).
- Fix paths to coverage files. ([8fb792b](https://github.com/ydethe/fireset/commit/8fb792b559d081b4761a95031ad2d27fa0b7db2c) by Jelmer Vernooĳ).
- Fix style issue, improve TODO. ([91cd01d](https://github.com/ydethe/fireset/commit/91cd01d1140c4fe986f10097935561504ba78207) by Jelmer Vernooĳ).
- Fix infrastructure for running caldavtester tests. ([c8e0b74](https://github.com/ydethe/fireset/commit/c8e0b7498d0ca97980ad02cd8da13fa630730f16) by Jelmer Vernooĳ).
- Fix DAV errors without description. ([c211d5a](https://github.com/ydethe/fireset/commit/c211d5a407c258d3f40dcb80701a34135d93b657) by Jelmer Vernooĳ).
- Fix trailing slashes ([e90d89e](https://github.com/ydethe/fireset/commit/e90d89e9ea9b59ab39026cc46bdad195d642af4c) by Markus Unterwaditzer).
- Fix some recently introduced style issues, fix regression. ([722ea0a](https://github.com/ydethe/fireset/commit/722ea0a76cd244c143f03eab0f265b3b10da9f6e) by Jelmer Vernooĳ).
- Fix line continuation ([9995713](https://github.com/ydethe/fireset/commit/99957134bb5eb0070cbf0b460f149c185b9cd145) by Markus Unterwaditzer).
- Fix undefined name errors found by flake8. ([2c4f69e](https://github.com/ydethe/fireset/commit/2c4f69eddb4be692e82a21729ac3c88710b2bb42) by Jelmer Vernooĳ).
- Fix missing reference to href. ([b9b3a2b](https://github.com/ydethe/fireset/commit/b9b3a2b85f0b9be531de96c80a553a96ca873e96) by Jelmer Vernooĳ).

### Changed

- Change line length limit ([76468e6](https://github.com/ydethe/fireset/commit/76468e6885dea626d76bb8e071a8ffa30b77c187) by Markus Unterwaditzer).

### Removed

- Remove unused imports ([d452ec5](https://github.com/ydethe/fireset/commit/d452ec50fa43a1a9d812d19927f49e31a7a6b19c) by Hugo Osvaldo Barrera).

## [v0.0.2](https://github.com/ydethe/fireset/releases/tag/v0.0.2) - 2017-03-14

<small>[Compare with first commit](https://github.com/ydethe/fireset/compare/71d444e03f33530abd6ea0ad8c7d05baa052d4b3...v0.0.2)</small>

### Added

- Add Store(check_for_duplicate_uids=True). ([58c1c4b](https://github.com/ydethe/fireset/commit/58c1c4ba236af70e24f8f01a0e929dc9fec0c03d) by Jelmer Vernooĳ).
- Add principal notes. ([9dd5299](https://github.com/ydethe/fireset/commit/9dd52999cf12b629c1f357232d3ea8ea77ce54db) by Jelmer Vernooĳ).
- Add support for RFC5689, fix some errors. ([9ad889b](https://github.com/ydethe/fireset/commit/9ad889bda30196689e22997d291d848ccac33257) by Jelmer Vernooĳ).
- Add pip install instructions as well. ([c6c1952](https://github.com/ydethe/fireset/commit/c6c195243407997d8746135f9f5b7ecbd7250404) by Jelmer Vernooĳ).
- Add Collection.destroy. ([2f78591](https://github.com/ydethe/fireset/commit/2f785916603917e96f8dd525f499b8dd47dfc3ad) by Jelmer Vernooĳ).
- Add xandikos-litmus. ([a3ce4cb](https://github.com/ydethe/fireset/commit/a3ce4cb3b9209092739724dce1af2b85512bed20) by Jelmer Vernooĳ).
- Add script for running litmus. ([3a95d16](https://github.com/ydethe/fireset/commit/3a95d16dbcd7228dfe2ebb373b25dea4df2cea8c) by Jelmer Vernooĳ).
- Add default mime type. ([c682ca5](https://github.com/ydethe/fireset/commit/c682ca5522f3d540cb0841472fb17e41eda48026) by Jelmer Vernooĳ).
- Add --defaults option. ([5a7dd08](https://github.com/ydethe/fireset/commit/5a7dd083f97aa33511dc119f908f4b15990a1dc4) by Jelmer Vernooĳ).
- Add note on collection creation. ([6cfd307](https://github.com/ydethe/fireset/commit/6cfd3071bc2092ff39cf65c64bf4392cb6225a3f) by Jelmer Vernooĳ).
- Add --autocreate option. ([0809913](https://github.com/ydethe/fireset/commit/08099137ac3ad0a61a00cd54e405ba12b60b1999) by Jelmer Vernooĳ).
- Add notes on store. ([d8bc8d0](https://github.com/ydethe/fireset/commit/d8bc8d04dbbdd860ef215698970fe2b589a70590) by Jelmer Vernooĳ).
- Add example uwsgi commands. ([7b743eb](https://github.com/ydethe/fireset/commit/7b743ebf58c26498d5569f7e96f6042cfc8b4c44) by Jelmer Vernooĳ).
- Add delta describer functions. ([ae35130](https://github.com/ydethe/fireset/commit/ae35130a879bb2b944e3c0eff57c8411ab8fbf8b) by Jelmer Vernooĳ).
- Add missing href. ([0a65b34](https://github.com/ydethe/fireset/commit/0a65b3493cdfe860e02bcb4d6b185a819a6552b0) by Jelmer Vernooĳ).
- Add add-member property. ([dd9bd08](https://github.com/ydethe/fireset/commit/dd9bd089af13ccaddb8ba2a5f3ee76dd6acb5c13) by Jelmer Vernooĳ).
- Add some notes on context. ([377cb86](https://github.com/ydethe/fireset/commit/377cb86d8432e2cf3337748db06bdadd057283f7) by Jelmer Vernooĳ).
- Add calendar property on CalendarFile. ([cdf6acb](https://github.com/ydethe/fireset/commit/cdf6acbd9ba865381a5f281af3b743a875fe9fc5) by Jelmer Vernooĳ).
- Add timezones property, feature flags. ([394c0e8](https://github.com/ydethe/fireset/commit/394c0e89b6033abe0e8fdc2477e63c8f7437b406) by Jelmer Vernooĳ).
- Add a resource_type field to Reporter. ([d578385](https://github.com/ydethe/fireset/commit/d578385c1ca186f243059661db3a7787062ea9f9) by Jelmer Vernooĳ).
- Add repr, make default collection a collection. ([b3febc9](https://github.com/ydethe/fireset/commit/b3febc90d79668d8a5fac4f01da748ebe846b958) by Jelmer Vernooĳ).
- Add missing , ([3709ccc](https://github.com/ydethe/fireset/commit/3709ccc3516dcf715b2573c21bd3121789deeef6) by Jelmer Vernooĳ).
- add author ([66a6de0](https://github.com/ydethe/fireset/commit/66a6de0488e2eec2e02eb3aa6f03e5fe792c517e) by Jelmer Vernooĳ).
- Add xandikos manpage. ([1c206cd](https://github.com/ydethe/fireset/commit/1c206cdc9207fccb3e349a1166280beb7d26e035) by Jelmer Vernooĳ).
- Add version info, add --version flag. ([045719a](https://github.com/ydethe/fireset/commit/045719af9c061b43a1f7dbcd9d4615aa72d3d2fd) by Jelmer Vernooĳ).
- Add xandikos script. ([cc6cea2](https://github.com/ydethe/fireset/commit/cc6cea2c28d635482d510635f9c6195724da4168) by Jelmer Vernooĳ).
- Add classifiers. ([81a29e7](https://github.com/ydethe/fireset/commit/81a29e71eb4c02cbc52e3e96f36b034986d4b975) by Jelmer Vernooĳ).
- Add coverage config. ([0c058f8](https://github.com/ydethe/fireset/commit/0c058f8bff4b1a2377742dad239c96618f150b0c) by Jelmer Vernooĳ).
- Add coverage targets. ([05bda81](https://github.com/ydethe/fireset/commit/05bda81fbda85f8c8cdedcfa547f1632db14d0c4) by Jelmer Vernooĳ).
- Add live attribute to Property. ([db0275b](https://github.com/ydethe/fireset/commit/db0275b5f57f1e435054f7598cc90568eefd6a34) by Jelmer Vernooĳ).
- Add note about aCALdav. ([c1c0a0f](https://github.com/ydethe/fireset/commit/c1c0a0f6c1c510818074795f502bef885decf7ca) by Jelmer Vernooĳ).
- Add support for activelocks/supportedlocks. ([fe39026](https://github.com/ydethe/fireset/commit/fe3902616f8c2cf2d6fb6bf99c4db7f2643ee566) by Jelmer Vernooĳ).
- Add notes on support for custom properties. ([99a2cb8](https://github.com/ydethe/fireset/commit/99a2cb80ed4c91d802176bf8ef66708de25831ac) by Jelmer Vernooĳ).
- Add support for addressbook-color property. ([9b33e93](https://github.com/ydethe/fireset/commit/9b33e93f2463566890de38ce836f8cc8a48786cb) by Jelmer Vernooĳ).
- Add support for max-image-size property. ([aa2cf66](https://github.com/ydethe/fireset/commit/aa2cf66eeab176e3c49649931bec1e394ae6edda) by Jelmer Vernooĳ).
- Add note on supported clients. ([596d17e](https://github.com/ydethe/fireset/commit/596d17e335138e2d8a869620cf8eb72e585aa329) by Jelmer Vernooĳ).
- Add doc on RFC implementation status. ([dc6a58a](https://github.com/ydethe/fireset/commit/dc6a58afe0eafc5a7e506b65afcbdd842053047d) by Jelmer Vernooĳ).
- Add notes about dav compliance. ([7e43e20](https://github.com/ydethe/fireset/commit/7e43e2088a4c5d4499b04548b33f4b7cda54a35d) by Jelmer Vernooĳ).
- Add a root page. ([e515cb6](https://github.com/ydethe/fireset/commit/e515cb6cfdc6f8efe39f04127dd0c0a21f26d423) by Jelmer Vernooĳ).
- Add newly observed properties to TODO. ([c2a22a1](https://github.com/ydethe/fireset/commit/c2a22a15ccb5ce34bd80d3ad48fcb4c0cc41c2ae) by Jelmer Vernooĳ).
- Add support for base prefix. ([1be68ac](https://github.com/ydethe/fireset/commit/1be68acea069dfd749788ced720dc3a3180a327a) by Jelmer Vernooĳ).
- Add simple wsgi wrapper. ([5f6a7b5](https://github.com/ydethe/fireset/commit/5f6a7b532ff54d7c32f70e785a6820a9bd76b1d0) by Jelmer Vernooĳ).
- Add basic options implementation. ([b3467b5](https://github.com/ydethe/fireset/commit/b3467b5f2b5f98462810d12cd3506d4e382e3403) by Jelmer Vernooĳ).
- Add stores more generic, and add basic support for etags. ([23f2821](https://github.com/ydethe/fireset/commit/23f28211dd33a9a8e0c744f8ee98dcc889efde4f) by Jelmer Vernooĳ).
- Add Collection.get_member. ([66869cc](https://github.com/ydethe/fireset/commit/66869cc874503e1fc46fdff2b04044702a6e0bfc) by Jelmer Vernooĳ).
- Add basic caldavtester runner. ([21534e1](https://github.com/ydethe/fireset/commit/21534e1e27abdfb50e0d4b3eccd004d34da5e0a0) by Jelmer Vernooĳ).
- Add Adressbook class. ([f23dd66](https://github.com/ydethe/fireset/commit/f23dd660d987c768161fb8922e790672c0743b0b) by Jelmer Vernooĳ).
- Add constant for {DAV:}principal. ([1d1e5c8](https://github.com/ydethe/fireset/commit/1d1e5c8f8e9a94cf6f701946264773f9c3441be4) by Jelmer Vernooĳ).
- Add basic but functioning addressbook-multiget. ([ef0e68d](https://github.com/ydethe/fireset/commit/ef0e68dc25ce6ff5bb88911ff5f71f9584d513f5) by Jelmer Vernooĳ).
- Add more example data to base server. ([866e4a8](https://github.com/ydethe/fireset/commit/866e4a8277278a6dd1790e38a154f3015ac76890) by Jelmer Vernooĳ).
- Add support for getcontenttype property. ([c667cf6](https://github.com/ydethe/fireset/commit/c667cf6141ff8942849efaa6285b4fcc943d385e) by Jelmer Vernooĳ).
- Add calendar description property. ([06a7de6](https://github.com/ydethe/fireset/commit/06a7de63aa3915105078ef30b89a9b901d1536b3) by Jelmer Vernooĳ).
- Add etag property. ([4b6e92f](https://github.com/ydethe/fireset/commit/4b6e92f39ec6263c9384ad0d6fb145e5f614d0b0) by Jelmer Vernooĳ).
- add structure doc ([878adb3](https://github.com/ydethe/fireset/commit/878adb3f1d22d08414e7e53361cc57d25588e014) by Jelmer Vernooĳ).
- Add tox config. ([2bc6f09](https://github.com/ydethe/fireset/commit/2bc6f096f5cca91f3f4b118d786026b3bcf95ac0) by Jelmer Vernooĳ).
- Add basic file checker. ([1be8984](https://github.com/ydethe/fireset/commit/1be898485800df3664ec2bbdff95f20d01fe5162) by Jelmer Vernooĳ).
- Add Collection.iter_raw. ([22dc6a1](https://github.com/ydethe/fireset/commit/22dc6a1bc49da035b72d8d8b61e287c4252305e8) by Jelmer Vernooĳ).
- Add headers. ([4acb0d2](https://github.com/ydethe/fireset/commit/4acb0d2d953250790e0528b6f01d721481d31c90) by Jelmer Vernooĳ).
- Add testr configuration. ([d16e03c](https://github.com/ydethe/fireset/commit/d16e03c633edf07faad14a974e5b0d7cf30b611e) by Jelmer Vernooĳ).
- Add basic caldav tests. ([076463e](https://github.com/ydethe/fireset/commit/076463e6fef95c139eac2d1807f3a766eac8e80a) by Jelmer Vernooĳ).
- Add webdav note. ([dbcea83](https://github.com/ydethe/fireset/commit/dbcea83a553a544f3588b2f3ae5d7deb74d15ddc) by Jelmer Vernooĳ).
- Add missing file. ([5d11299](https://github.com/ydethe/fireset/commit/5d112992b526cfced67df1662f087b349383d90c) by Jelmer Vernooĳ).
- Add root endpoint. ([69cca71](https://github.com/ydethe/fireset/commit/69cca71689e9cb78ddb5e1f79ecbbb676053b6a9) by Jelmer Vernooĳ).
- Add DebugEndpont. ([06ac620](https://github.com/ydethe/fireset/commit/06ac62083859c4d1c8d66250b8e3dbc65bef87f9) by Jelmer Vernooĳ).
- Add Endpoint class. ([a80d544](https://github.com/ydethe/fireset/commit/a80d544d7942543683d9772f601c816780bde708) by Jelmer Vernooĳ).
- Add BaseCollection.delete_one. ([a8ee453](https://github.com/ydethe/fireset/commit/a8ee45344154f40f4f9e556e64d4894169b8514d) by Jelmer Vernooĳ).
- Add Collection.iter_vcalendars. ([0410f70](https://github.com/ydethe/fireset/commit/0410f7081918bd371cb7638fb24b6cfb504a660d) by Jelmer Vernooĳ).
- Add GitCollection.open_from_path and GitCollection.open. ([c596675](https://github.com/ydethe/fireset/commit/c5966751509851e75d2a8b9ee36de46cb2273471) by Jelmer Vernooĳ).
- Add more TODOs. ([3392c75](https://github.com/ydethe/fireset/commit/3392c7539e52e2cd37147a714b534fed53ea0610) by Jelmer Vernooĳ).
- Add requirements.txt. ([0d0dbf4](https://github.com/ydethe/fireset/commit/0d0dbf4902786a3b917d8b012c2fd3afbad457fa) by Jelmer Vernooĳ).
- Add travis file. ([ccd245b](https://github.com/ydethe/fireset/commit/ccd245b325948f08b6fd0093813b7c8558380281) by Jelmer Vernooĳ).
- Add Collection.get_ctag(). ([52f342a](https://github.com/ydethe/fireset/commit/52f342a9d0def5d8a5e5370441ea6ee1e41ddf2e) by Jelmer Vernooĳ).
- Add iter_with_etag. ([b84b20d](https://github.com/ydethe/fireset/commit/b84b20d07a497f72bc4982f15fafa320888f717e) by Jelmer Vernooĳ).
- Add basic web server infrastructure. ([e54e8be](https://github.com/ydethe/fireset/commit/e54e8beffcf043f52a5e054a9301cc42d2896966) by Jelmer Vernooĳ).
- Add GitCollection.create. ([d87b882](https://github.com/ydethe/fireset/commit/d87b88296348322cc62bf55e1e264dd10314c645) by Jelmer Vernooĳ).
- Add Python3 infrastructure. ([a56ede9](https://github.com/ydethe/fireset/commit/a56ede9fc4703c0f6baae7bfb576e80c354e01f9) by Jelmer Vernooĳ).
- Add file format notes. ([164ebef](https://github.com/ydethe/fireset/commit/164ebefeffb7012ffe3d4d0f73ff1eea6fd6c5b4) by Jelmer Vernooĳ).
- Add copyright headers. ([e9b25ef](https://github.com/ydethe/fireset/commit/e9b25efeba5f79f3eca2f9b900513674ada57ab0) by Jelmer Vernooij).
- Add docstrings. ([325cc04](https://github.com/ydethe/fireset/commit/325cc04e310a7ba4d7ea1c84ae08f47d2a8aaa50) by Jelmer Vernooĳ).
- Add -tense argument. ([e6b4c9b](https://github.com/ydethe/fireset/commit/e6b4c9b7fdb33b86fd0b325ea236251ce9124352) by Jelmer Vernooĳ).
- Add setup. ([273c576](https://github.com/ydethe/fireset/commit/273c576a3ed8dabe60043300606309eea963c90c) by Jelmer Vernooij).
- Add module. ([4324515](https://github.com/ydethe/fireset/commit/432451576ffbb70f522299cdebcce31b1f85d2e3) by Jelmer Vernooij).
- Add basic README. ([6b05f03](https://github.com/ydethe/fireset/commit/6b05f03455b2bdee05d632a80b630cfe6ab9dc62) by Jelmer Vernooij).
- Add --obscured-category flag. ([33c09fd](https://github.com/ydethe/fireset/commit/33c09fd81d1b61920fb34573c1b3ee729b272d7a) by Jelmer Vernooij).
- Add common command line parsing. ([c10037a](https://github.com/ydethe/fireset/commit/c10037a7c110788acec0ac28f0023502a027b138) by Jelmer Vernooij).

### Fixed

- Fix license field (GPLv3) ([0c6127a](https://github.com/ydethe/fireset/commit/0c6127a4f4a79a1f02d913a71394c3979bbe3d80) by Jelmer Vernooĳ).
- fix typo in web.py ([f3b3994](https://github.com/ydethe/fireset/commit/f3b3994fa740354b8500073d23087834999363b4) by Félix Sipma).
- Fix DTSTART/DTEND fields. ([704e8e1](https://github.com/ydethe/fireset/commit/704e8e130661428c859902f1de1d9d380f5b31f5) by Jelmer Vernooĳ).
- Fix typo. ([4445fc3](https://github.com/ydethe/fireset/commit/4445fc37aa4c4340d0b94d05cbdc35b2f40b0492) by Jelmer Vernooĳ).
- Fix link. ([b20520c](https://github.com/ydethe/fireset/commit/b20520c4393b427550f39065ea2ea21e992b8c9b) by Jelmer Vernooĳ).
- Fix POST. ([209a8e5](https://github.com/ydethe/fireset/commit/209a8e5a37f83b39030e45002479db31302fdccf) by Jelmer Vernooĳ).
- Fix data properties. ([15963b6](https://github.com/ydethe/fireset/commit/15963b6a0b85c14a4b6584726bc30d822bb15805) by Jelmer Vernooĳ).
- Fix missing import. ([16ad9cb](https://github.com/ydethe/fireset/commit/16ad9cbdd8a82fb9a0a237076f170c3a82c3178f) by Jelmer Vernooĳ).
- Fix calendar-query. ([4d855f8](https://github.com/ydethe/fireset/commit/4d855f83fbfe41c0258403f138c3dc168ee144d8) by Jelmer Vernooĳ).
- Fix multi-get report. ([a4df85d](https://github.com/ydethe/fireset/commit/a4df85d402be4909fefb95321043f04a7cbc5487) by Jelmer Vernooĳ).
- Fix sync. ([3333d3d](https://github.com/ydethe/fireset/commit/3333d3d60579000eedc4b6f532e40847193500e4) by Jelmer Vernooĳ).
- Fix add-member element. ([fa34699](https://github.com/ydethe/fireset/commit/fa34699363f86eb32b801e378204401dbdd81c98) by Jelmer Vernooĳ).
- Fix property import. ([01fc043](https://github.com/ydethe/fireset/commit/01fc043e22b8a9c343fbfe3e541de87d54feae35) by Jelmer Vernooĳ).
- Fix use of return with value in generator. ([d58e0bd](https://github.com/ydethe/fireset/commit/d58e0bd9d4131883c960ffd63c1ebfd00e902713) by Jelmer Vernooĳ).
- Fix typo, provide get_content_language. ([4678bef](https://github.com/ydethe/fireset/commit/4678bef6abc02c47386d7e9bfb5163ec34ab34c1) by Jelmer Vernooĳ).
- Fix OPTIONS. ([10bb076](https://github.com/ydethe/fireset/commit/10bb076e57eddcc82b8aee0fb170b5200ec2483a) by Jelmer Vernooĳ).
- Fix allprop/propname handling. ([1391fcc](https://github.com/ydethe/fireset/commit/1391fcc686fb5180b2753475662dd3ce55e8a67f) by Jelmer Vernooĳ).
- Fix content-* names. ([5f318d0](https://github.com/ydethe/fireset/commit/5f318d04153aeb01577dc1eee775b254f3f51800) by Jelmer Vernooĳ).
- Fix support for depth=infinity. ([c7055ed](https://github.com/ydethe/fireset/commit/c7055ed46403e684c1ce7b7c4835a1b38ef834aa) by Jelmer Vernooĳ).
- Fix namespace. ([a1f0f95](https://github.com/ydethe/fireset/commit/a1f0f9572922f242f5e9e5d5ec5ad50217ef083f) by Jelmer Vernooĳ).
- Fix REPORT. ([bd8c2a0](https://github.com/ydethe/fireset/commit/bd8c2a0f17744e92e783269be4c20cd66ac45a9d) by Jelmer Vernooĳ).
- Fix tests. ([411409b](https://github.com/ydethe/fireset/commit/411409b89c80dc159e8073be2ab717c6b90bf939) by Jelmer Vernooĳ).
- Fix syntax errors. ([ba52b6d](https://github.com/ydethe/fireset/commit/ba52b6d515caf84cd1219db7246e36267e3f1069) by Jelmer Vernooĳ).
- Fix getting by uid. ([cb86139](https://github.com/ydethe/fireset/commit/cb86139bbe9540c1d36336a2c25185a901eebeef) by Jelmer Vernooĳ).
- Fix typos in property names. ([fc0ab8c](https://github.com/ydethe/fireset/commit/fc0ab8c1fb1950defed032c022bdeb042b4b90f6) by Jelmer Vernooĳ).
- Fix href querying. ([f29d4ab](https://github.com/ydethe/fireset/commit/f29d4ab704b552bb9aa848a616a162bbd471a3ef) by Jelmer Vernooĳ).
- Fix MKCOL. ([661c2bf](https://github.com/ydethe/fireset/commit/661c2bf4fcf5da3c572bff9b903e321ec84a9ec7) by Jelmer Vernooĳ).
- Fix test. ([26660ed](https://github.com/ydethe/fireset/commit/26660edd7f104ee48768282aa451698f6d774ac9) by Jelmer Vernooĳ).
- Fix HREFs, be more lenient in DTEND/DTSTART validation. ([5247341](https://github.com/ydethe/fireset/commit/524734159e5146d425847e815ffdf458d1721ab8) by Jelmer Vernooĳ).
- Fix timezone. ([752235e](https://github.com/ydethe/fireset/commit/752235ec977d457f402974977ef97ae7c87d888a) by Jelmer Vernooĳ).
- Fix test with older dulwich. ([b134222](https://github.com/ydethe/fireset/commit/b134222906d3a4a8bc7dbfb84360fb00f5512174) by Jelmer Vernooĳ).
- Fix sync-collection. ([aaf144f](https://github.com/ydethe/fireset/commit/aaf144f0fda43d965b490fe9bef9679efc46dc0f) by Jelmer Vernooĳ).
- Fix expand-property. ([59dfb5d](https://github.com/ydethe/fireset/commit/59dfb5d28710f32bfbb05034f76c14248ed5c2bd) by Jelmer Vernooĳ).
- Fix deletes. ([e4790d8](https://github.com/ydethe/fireset/commit/e4790d89185d1487f10a1dcb80297d4028318c24) by Jelmer Vernooĳ).
- Fix TreeGitStore._get_etag. ([7036e51](https://github.com/ydethe/fireset/commit/7036e51a0467cdfb593a4691421ba6f1b9d27c1e) by Jelmer Vernooĳ).
- Fix handling of 404 in REPORT. ([85409ed](https://github.com/ydethe/fireset/commit/85409eddfc0e54d21c0d9e8c71b92e4b88441ac1) by Jelmer Vernooĳ).
- Fix SCRIPT_NAME handling. ([f4b92e9](https://github.com/ydethe/fireset/commit/f4b92e9413bcc0cfc27cb8265fb61a75fbaf0b23) by Jelmer Vernooĳ).
- Fix path handling. ([3e9f886](https://github.com/ydethe/fireset/commit/3e9f886972e4ede987f5ada8b1fbbf987b178ba1) by Jelmer Vernooĳ).
- Fix disk path mapping. ([96c3bb0](https://github.com/ydethe/fireset/commit/96c3bb02094714d49fe7eee0b108e43442a78b85) by Jelmer Vernooĳ).
- Fix syntax error. ([7ef5de1](https://github.com/ydethe/fireset/commit/7ef5de10c7214b3dd58c205b378f985172fbd4ab) by Jelmer Vernooĳ).
- Fix path parsing. ([dbb32b0](https://github.com/ydethe/fireset/commit/dbb32b0a7522a968d44192e5e68911531a31a090) by Jelmer Vernooĳ).
- fix argument ([cd36beb](https://github.com/ydethe/fireset/commit/cd36bebadda52c5165a7aca7ff240967cf5c9c0b) by Jelmer Vernooĳ).
- Fix import. ([cf777d2](https://github.com/ydethe/fireset/commit/cf777d25b1568a06a8074d3097748f97c273907d) by Jelmer Vernooĳ).
- Fix types. ([8e0c347](https://github.com/ydethe/fireset/commit/8e0c3479df52fde5bec3ebb9c81891eb6cfcddac) by Jelmer Vernooĳ).
- Fix caldav module. ([c7d337e](https://github.com/ydethe/fireset/commit/c7d337ea4966454fa9ef9e5125ff61e5523cdea1) by Jelmer Vernooĳ).
- Fix tests ([144b411](https://github.com/ydethe/fireset/commit/144b4119cd506234b7d7599af1c280659f2836c0) by Jelmer Vernooĳ).
- Fix tests to use properties. ([17d861e](https://github.com/ydethe/fireset/commit/17d861e8b35af7a1405962614ce9ed2acc31b187) by Jelmer Vernooĳ).
- Fix fix-songkick. ([821fc69](https://github.com/ydethe/fireset/commit/821fc6943f2386c453a53a68fa6e2d42663bd911) by Jelmer Vernooĳ).
- Fix todo. ([70e287c](https://github.com/ydethe/fireset/commit/70e287c26a4ee2d7ca7dc40c71d17a08c9dc823d) by Jelmer Vernooĳ).
- Fix python3 compatibility - cmp is no longer an argument to sort. ([2182c52](https://github.com/ydethe/fireset/commit/2182c5207be5a1d4bf3ffe4d29110fc77b62a42a) by Jelmer Vernooĳ).
- Fix. ([1515bcd](https://github.com/ydethe/fireset/commit/1515bcd9cbfc79a8f045cf3b1854a279eef9a795) by Jelmer Vernooĳ).
- Fix option handling. ([701440b](https://github.com/ydethe/fireset/commit/701440bb3b6324ec237130f04be97796a241c5d3) by Jelmer Vernooĳ).

### Changed

- Change default calendar path for travel to 'calendar'. ([ec597e4](https://github.com/ydethe/fireset/commit/ec597e4937444cf47ac9bd8e1976c6c10700d4f3) by Jelmer Vernooij).

### Removed

- Remove public lookup_uid. ([9de14d8](https://github.com/ydethe/fireset/commit/9de14d8f72d4c8f65bed82c5e2298a25e7d809bb) by Jelmer Vernooĳ).
- Remove unused imports. ([c1588cf](https://github.com/ydethe/fireset/commit/c1588cf0e8885519d43dc2bce177ae25e141d97e) by Jelmer Vernooĳ).
- Remove extensions. ([31ec930](https://github.com/ydethe/fireset/commit/31ec9300f48cc8237740022c99a2132904e24ce7) by Jelmer Vernooĳ).
- Remove dystros-specific items from TODO. ([eb364b7](https://github.com/ydethe/fireset/commit/eb364b797c2f0d99e2462463bf785de5ca0b47a6) by Jelmer Vernooĳ).
- Remove RFCs, they're non-DFSG-free :( ([0f79f70](https://github.com/ydethe/fireset/commit/0f79f705df85f41c723b2c6fbf5037f763994439) by Jelmer Vernooĳ).
- Remove one more Dystros reference. ([4e3cbea](https://github.com/ydethe/fireset/commit/4e3cbea632c170a87cd569a436fed68bf65f039c) by Jelmer Vernooĳ).
- Remove files not relevant for Xandikos. ([0fbd280](https://github.com/ydethe/fireset/commit/0fbd280040eadab6f4d9e375199ac75fc2f068f9) by Jelmer Vernooĳ).
- Remove unused StoreSet class. ([120a42b](https://github.com/ydethe/fireset/commit/120a42bdd539bd6fe9b7bf725f417c8adc14f47b) by Jelmer Vernooĳ).
- Remove generated output. ([d599740](https://github.com/ydethe/fireset/commit/d599740d81407e068165e639f8ca7e6f9768b7fe) by Jelmer Vernooĳ).
- Remove porting to vobject from the TODO list. ([7cb464d](https://github.com/ydethe/fireset/commit/7cb464d51af6a31bde4f7a8990f2d178ddba6ffd) by Jelmer Vernooĳ).

