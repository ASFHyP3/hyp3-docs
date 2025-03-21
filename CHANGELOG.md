# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [PEP 440](https://www.python.org/dev/peps/pep-0440/)
and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.10.2]

### Changed
* Updated [Products](docs/products.md) page to include burst-based InSAR

## [0.10.1]

### Changed
* Updated HyP3 SDK to [v7.2.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#721)

## [0.10.0]

### Added
* The [credits](docs/using/credits.md) page now displays the credit costs for multi-burst InSAR jobs.

### Removed
* Removed the year-old credits system announcement from the [credits](docs/using/credits.md) page.

## [0.9.17]

### Changed
* Updated HyP3 SDK to [v7.2.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#720)

## [0.9.16]

### Added
* [ARIA S1 GUNW Product Guide](https://hyp3-docs.asf.alaska.edu/guides/gunw_product_guide.md)

## [0.9.15]

### Changed
* Updated HyP3 SDK to [v7.1.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#710)

## [0.9.14]

### Changed
* Replace Code of Conduct with links to the [organization Code of Conduct](https://github.com/ASFHyP3/.github/blob/main/CODE_OF_CONDUCT.md).

## [0.9.13]

### Changed
* Updated HyP3 SDK to [v7.0.3](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#703)
* Updated ASF Tools for Python to [v0.8.3](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#083)

## [0.9.12]

### Changed
* Updated code of conduct per guidance from NASA.

## [0.9.11]

### Changed
* Added information about connected components files to [InSAR Product Guide](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide.md)

## [0.9.10]

### Added
- Added a Burst InSAR Story Map link to the site table of contents

### Fixed
- The [`update_asf_tools_version`](.github/workflows/update_asf_tools_version.yml) and [`update_sdk_version`](.github/workflows/update_sdk_version.yml) GitHub Actions workflows now use the `gh` CLI instead of the archived `repo-sync/pull-request` action.

## [0.9.9]

### Changed
* Updated HyP3 SDK to [v7.0.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#701)

## [0.9.8]

### Removed
* Note about incomplete archive in `burst_insar_product_guide.md` now that burst archive is complete

## [0.9.7]

### Changed
* Updated ASF Tools for Python to [v0.8.0](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#080)

## [0.9.6]

### Added
* Document the announcement banner.

## [0.9.5]

### Changed
* Updated HyP3 SDK to [v7.0.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#700)
* Upgrade to Python 3.10.

## [0.9.4]

### Changed
* Revised the Requesting Access page to reflect that a release date has not yet been set and removed the page from the navigation menu.
* Disabled the site banner now that we are postponing the Requesting Access announcement.

## [0.9.3]

### Changed
* Revised the Requesting Access page to serve as an announcement for the upcoming change and added the page to the navigation menu.
* Revised the site banner to replace the Credits announcement with the Requesting Access announcement.

## [0.9.2]

### Added
* Added [Requesting Access page](docs/using/request_access.md), not yet listed in the site index
* Added references to requesting access in the [Using HyP3](docs/using-snippet.md) documentation, commented out until new users must apply for access

### Changed
* Updated language in InSAR product guides to clarify that only co-pol interferograms are available
* Updated status of burst back-population
* Switched to the use of a descending track in the [MintPy tutorial](docs/tutorials/hyp3_insar_stack_for_ts_analysis.ipynb) so that all interferograms have full coverage of the observed event.

### Fixed
* The [MintPy tutorial](docs/tutorials/hyp3_insar_stack_for_ts_analysis.ipynb) so that it correctly specifies `asf_search` parameters.

## [0.9.1]

### Changed
* Updated HyP3 SDK to [v6.2.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#620)

## [0.9.0]

### Changed
* Updated language to reflect release of the full credit system to production HyP3.

### Removed
* Quota page now redirects to [Credits](docs/using/credits.md) page.

## [0.8.9]

### Added
* [Water Mask page](docs/water_masking.md) describing the water mask used for InSAR processing, and linking to code and resources for accessing and generating the new reference water mask

### Changed
* Updated ASF Tools for Python to [v0.7.2](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#072)

## [0.8.8]

### Changed
* Updated HyP3 SDK to [v6.1.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#610)

## [0.8.7]

### Added
* Credits system announcement.

### Changed
* Updated water mask descriptions.

## [0.8.6]

### Changed
* Updated water mask language to reflect switch to OpenStreetMap/ESA WorldCover based water map.

## [0.8.5]

### Added
* Tutorial notebook demonstrating how to merge two burst InSAR products.
* Merge sentinel-1 burst InSAR products section on burst_insar_product_guide.md.

### Changed
* Included 20 meter pixel spacing option for RTC products in product summary page.

## [0.8.4]

### Changed
* Updated HyP3 SDK to [v6.0.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#600)

## [0.8.3]

### Changed
* Updated HyP3 SDK to [v5.0.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#500)

## [0.8.2]

### Modified
* the DEM description and RTC product guide to inform users that the legacy DEM options are no longer available

## [0.8.1]

### Fixed
* Link to `hyp3_isce2_burst_stack_for_ts_analysis.ipynb` directly in GitHub because <https://nbviewer.org/github/ASFHyP3/hyp3-docs/blob/main/docs/tutorials/hyp3_isce2_burst_stack_for_ts_analysis.ipynb> returns a `404`.

## [0.8.0]

### Added
* Added `hyp3_isce2_burst_stack_for_ts_analysis.ipynb` to make the `hyp3-isce2` burst InSAR work with MintPy

### Changed
* Changed `hyp3_insar_stack_for_ts_analysis.ipynb` to make it work with MintPy v1.5.2

## [0.7.1]

### Added
* Announce Burst InSAR availability in Vertex

## [0.7.0]

### Added
* Published Sentinel-1 Burst InSAR Guide

## [0.6.7]

### Changed
* Updated HyP3 SDK to [v4.0.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#400)

## [0.6.6]

### Changed
* Updated documentation to [InSAR Product Guide](docs/guides/insar_product_guide.md#adaptive-phase-filter) to announce that the feature is available in Vertex

## [0.6.5]

### Changed
* Updated ASF Tools for Python to [v0.6.0](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#060)

## [0.6.4]

### Changed
* Updated the Burst Guide to reflect that water masking is now done before phase unwrapping.

## [0.6.3]

### Changed
* Updated HyP3 SDK to [v3.1.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#310)

## [0.6.2]

### Added
* Added documentation to [InSAR Product Guide](docs/guides/insar_product_guide.md#adaptive-phase-filter) for the adaptive phase filter parameter option.

### Changed
* Restructured the Processing Options section of the [InSAR Product Guide](docs/guides/insar_product_guide.md#processing-options-and-optional-files)

## [0.6.1]

### Fixed
* Updated admonition types to those that are supported by `mkdocs-material` v9.4.2+.

## [0.6.0]

## Added
* Added notes indicating that GLO-90 tiles will fill missing GLO-30 tiles over Armenia and Azerbaijan.

### Changed
* Upgraded to `mkdocs-asf-theme==0.3.0`.
* Google Analytics is set up directly in [mkdocs.yml](mkdocs.yml) as it's no longer set by default in the theme.

## [0.5.4]

### Added
* Unpublished Sentinel-1 Burst InSAR Product Guide

### Fixed
* Clarified the range of possible pixel values for the lv_phi.tif file in the InSAR Product Guide.
  Fixes [#334](https://github.com/ASFHyP3/hyp3-docs/issues/334).

### Removed
* `propose-tweet` GitHub action workflow. Closes [#288](https://github.com/ASFHyP3/hyp3-docs/issues/288).

## [0.5.3]

### Changed
* Updated HyP3 SDK to [v3.0.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#300)

## [0.5.2]

### Changed
* Updated docs after removing the Subscriptions feature.

## [0.5.1]

### Changed
* Revised the Subscriptions deprecation announcement to make it more clear that HyP3 itself is not being retired.

## [0.5.0]

### Added
* Added more details regarding HyP3 Subscriptions deprecation, including the timeline for removal and steps
  for saving subscription metadata before it is deleted.

## [0.4.0]

### Added
* Added tutorials for submitting HyP3 jobs based on granule search parameters (replaces HyP3 Subscriptions).

### Changed
* Replaced the Subscriptions documentation with a link to the new tutorials.
* Upgraded the Conda environment to Python 3.9.

## [0.3.74]

### Added
* References to the DEM pixel value unit (meters) in the [RTC Product Guide](docs/guides/rtc_product_guide.md#image-files) and [InSAR Product Guide](docs/guides/insar_product_guide.md#processing-options)

## [0.3.73]

### Fixed
* Corrected error in [DEM raster type description in the RTC Product Guide](docs/guides/rtc_product_guide.md#image-files)

## [0.3.72]

### Changed
* Updated HyP3 SDK to [v2.1.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#211)

## [0.3.71]

### Changed
* Updated HyP3 SDK to [v2.1.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#210)

## [0.3.70]

### Added
* Documented public visibility of jobs in the Using HyP3 section.
* Added link to tutorial on searching for other users' jobs.

## [0.3.69]

### Added
* Illustration for [Pixel spacing description in the RTC Product Guide](docs/guides/rtc_product_guide.md#pixel-spacing)
* Additional information about the pixel spacing options

### Changed
* Updated URLs in [Sentinel-1 Mission document](docs/sentinel1.md)
* Removed message that 20-m pixel spacing option for RTC is not yet available in Vertex

## [0.3.68]

### Changed
* Updated HyP3 SDK to [v2.0.2](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#202)

## [0.3.67]

### Changed
* Updated the [RTC Product Guide](docs/guides/rtc_product_guide.md) to accommodate the 20-m option for pixel spacing

## [0.3.66]

### Added
* Added processing options table and descriptive text to the [RTC Product Guide](docs/guides/rtc_product_guide.md)
* Added references/links to the processing options section as appropriate throughout the [RTC Product Guide](docs/guides/rtc_product_guide.md)
* Added [Mathjax](https://www.mathjax.org) as an option for formatting equations

## [0.3.65]

### Changed
* Updated HyP3 SDK to [v2.0.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#201)

## [0.3.64]

### Changed
* Updated HyP3 SDK to [v2.0.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#200)

## [0.3.63]

## Changed
* Updated ASF Tools for Python to [v0.5.2](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#052)

## Fixed
* Fix the reference to Copernicus DEM release version

## [0.3.62]

## Added
* A GitHub Action for spell checking, with ASF-specific words whitelisted in [.github/dictionary.txt](.github/dictionary.txt)
* A GitHub Action for link checking, with whitelisted links in [.lycheeignore](.lycheeignore)

## Fixed
* Minor grammatical and spelling mistakes
* Broken Copernicus DEM links

## [0.3.61]

## Changed
* Updated ASF Tools for Python to [v0.5.0](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#050)

## [0.3.60]

## Changed
* Updated ASF Tools for Python to [v0.4.6](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#046)

## [0.3.59]

### Changed
* Updated [RTC Product Guide](docs/guides/rtc_product_guide.md) to announce new processing options

## [0.3.58]

### Changed
* Updated HyP3 SDK to [v1.7.5](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#175)

### Fixed
* Included timezone information in the [MintPy tutorial](docs/tutorials/hyp3_insar_stack_for_ts_analysis.ipynb) when
  comparing with `asf_search` results because date-times reported in search results will have a timezone as of
  [asf_search v5.0.0](https://github.com/asfadmin/Discovery-asf_search/blob/master/CHANGELOG.md#500).

## [0.3.57]

### Changed
* Updated HyP3 SDK to [v1.7.3](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#173)

## [0.3.56]

## Added
* Section about RTC pixel spacing added to the [RTC Product Guide](docs/guides/rtc_product_guide.md)

## [0.3.55]

## Changed
* Updated ASF Tools for Python to [v0.4.5](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#045)

## [0.3.54]

### Changed
* Updated HyP3 SDK to [v1.7.2](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#172)

## [0.3.53]

### Added
* Added the decibel option in the Table 2 of the rtc-product-guide.md

## [0.3.52]

### Changed
* Updated ASF Tools for Python to [v0.4.4](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#044)

## [0.3.51]

### Changed
* Updated ASF Tools for Python to [v0.4.3](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#043)

## [0.3.50]

### Changed
* Updated HyP3 SDK to [v1.7.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#171)

## [0.3.49]

### Changed
* Updated API Use Guide to only use the ESA S2 naming convention.

## [0.3.48]

### Fixed
* Corrected broken "Get Started" link in the RTC Product Guide.

## [0.3.47]

### Changed
* Updated descriptions of water mask to reflect the new unbuffered approach to masking
* Included links to the [InSAR Water Masking Tutorial](https://storymaps.arcgis.com/stories/485916be1b1d46889aa436794b5633cb "InSAR Water Masking StoryMap")

## [0.3.46]

### Changed
* Updated HyP3 SDK to [v1.7.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#170)

## [0.3.45]

### Added
* Added an information page about the Sentinel-1 mission to the Products section, bringing particular attention to the end of mission for Sentinel-1B

## [0.3.44]

### Changed
* Updated link behavior to be consistent in formatting, and open external links in a new tab whenever possible

## [0.3.43]

### Added
* API reference for `hyp3_sdk` now documents the `util` module

### Changed
* Updated ASF Tools for Python to [v0.4.2](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#042)

### Fixed
* API reference for `asf_tools` now documents all modules recursively. Fixes [#243](https://github.com/ASFHyP3/hyp3-docs/issues/243)

## [0.3.42]

### Changed
* Updated ASF Tools for Python to [v0.4.1](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#041)

## [0.3.41]

### Changed
* Updated HyP3 SDK to [v1.6.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#161)

## [0.3.40]

### Added
* Added a quick link, `https://hyp3-docs.asf.alaska.edu/tutorials/mintpy`, to our [MintPy tutorial notebook](https://nbviewer.jupyter.org/github/ASFHyP3/hyp3-docs/blob/main/docs/tutorials/hyp3_insar_stack_for_ts_analysis.ipynb)
* Added a landing page for [HyP3 tutorials](docs/tutorials.md)
* Added the HyP3 Python SDK tutorial as a navigation menu item under the "Tutorials" section

## [0.3.39]

### Added
* Added information and reference links to the [InSAR Product Guide](docs/guides/insar_product_guide.md) for the [Minimum Cost Flow](https://www.gamma-rs.ch/uploads/media/2002-5_TR_Phase_Unwrapping.pdf) phase unwrapping algorithm used for On Demand InSAR products
* Added clarification to the [InSAR Product Guide](docs/guides/insar_product_guide.md) that the sign convention used for unwrapped phase is opposite to that used for displacement maps.
* Added landing page for [Using HyP3](docs/using.md) section
* Added references to hyp3-docs repo citation

### Changed
* Streamlined Getting Started portion of homepage
* Included more context on the [Vertex](using/vertex.md) landing page

## [0.3.38]

### Changed
* Updated references to Copernicus DEM GLO-30 to link to the [latest 2021 release of the dataset](https://spacedata.copernicus.eu/blogs/-/blogs/copernicus-dem-2021-release-now-available) and [additional release details](https://spacedata.copernicus.eu/web/cscda/dataset-details?articleId=394198)
* Updated the [Copernicus DEM GLO-30 coverage map](docs/images/cop-coverage-map.png) to include the additional tiles added to the DEM dataset with the latest release

## [0.3.37]

### Added
* Created a `CITATION.cff` file for the repository that will make it easier for others to cite.

## [0.3.36]

### Changed
* Updated the MintPy time series analysis notebook

## [0.3.35]

### Changed
* Updated HyP3 SDK to [v1.6.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#160)

## [0.3.34]

### Changed
* Updated HyP3 SDK to [v1.5.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#151)

## [0.3.33]

### Changed
* Updated HyP3 SDK to [v1.5.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#150)

## [0.3.32]

### Added
* Added a notebook to describe the time series analysis with hyp3 and mintpy

## [0.3.31]

### Changed
* Updated ASF Tools to include flood_map in [v0.4.0](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md##040)

## [0.3.30]

### Fixed
* Update MkDocs to version >1.2.3 to fix a Jinja2 compatibility issue
  (see [#197](https://github.com/ASFHyP3/hyp3-docs/pull/197))

### Changed
* Updated description of SAR image pair selection in [InSAR Product Guide](docs/guides/insar_product_guide.md) to specify that HyP3 always uses the older image as the reference image.
* Pinned `pygments=2.11.2` in environment.yml to resolve a breaking change impacting `mkdocs-material v6.2.8`

## [0.3.29]

### Changed
* Updated descriptions of validity mask thresholds and reference point calculation in [InSAR Product Guide](docs/guides/insar_product_guide.md) to reflect changes to InSAR processing code.
* Added a link for the [InSAR Product Guide](docs/guides/insar_product_guide.md) to the [Products](docs/products.md) page.

## [0.3.28]

### Changed
* Updated ASF Tools for Python to [v0.3.3](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#033)

## [0.3.27]

### Changed
* Updated ASF Tools for Python to [v0.3.1](https://github.com/ASFHyP3/asf-tools/blob/main/CHANGELOG.md#031)

## [0.3.26](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.25...v0.3.26)

### Changed
* Increase monthly job quota per user from 250 to 1,000

## [0.3.25](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.24...v0.3.25)

### Changed
* Updated Figure 2 in [Introduction to SAR](docs/guides/introduction_to_sar.md)
* Updated Figure 2 in [InSAR Product Guide](docs/guides/insar_product_guide.md)

## [0.3.24](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.23...v0.3.24)

### Changed
* Set external links in [InSAR Product Guide](docs/guides/insar_product_guide.md) to display the target URL in the tool tip and open in a new browser tab.
* Updated [Subscriptions](docs/using/subscriptions.md) document to include links to [Vertex subscription documentation](https://docs.asf.alaska.edu/vertex/manual/#subscriptions).

## [0.3.23](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.22...v0.3.23)

### Changed
* Updated HyP3 SDK to [v1.4.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#141)

## [0.3.22](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.21...v0.3.22)

### Changed
* Corrected the attribution for figures in the [InSAR Product Guide](docs/guides/insar_product_guide.md) and the [Introduction to SAR](docs/guides/introduction_to_sar.md)

## [0.3.21](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.20...v0.3.21)

### Changed
* Updated ASF Tools to [v0.3.0](https://github.com/ASFHyP3/asf-tools/blob/develop/CHANGELOG.md#030)

## [0.3.20](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.19...v0.3.20)

### Changed
* Updated the [InSAR Product Guide](docs/guides/insar_product_guide.md) to reflect the change in the location of the phase unwrapping reference point (formerly the (0,0) location of the combined image pair, now the location of the pixel with the highest coherence value)
* Updated the [InSAR Product Guide](docs/guides/insar_product_guide.md) to adjust the list of parameters included in the parameter file

## [0.3.19](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.18...v0.3.19)

### Changed
* Updated the [InSAR Product Guide](docs/guides/insar_product_guide.md) to include information about the fringe patterns in the InSAR browse images

## [0.3.18](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.17...v0.3.18)

### Added
* A [Subscriptions](docs/using/subscriptions.md) page describing subscription functionality

## [0.3.17](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.16...v0.3.17)

### Changed
* Updated HyP3 SDK to [v1.4.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#140)

## [0.3.16](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.15...v0.3.16)

### Added
* A [User Quota](docs/using/quota.md) page describing user quotas

### Changed
* Updated the [InSAR Product Guide](docs/guides/insar_product_guide.md) to reflect changes in the option for including displacement maps in InSAR product packages
* Updated the URL for the [Copernicus DEM](https://spacedata.copernicus.eu/explore-more/news-archive/-/asset_publisher/Ye8egYeRPLEs/blog/id/434960) information webpage

## [0.3.15](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.14...v0.3.15)

### Added
* Added information on the impacts of the phase unwrapping reference point on the phase difference and LOS Displacement values to the [InSAR Product Guide](docs/guides/insar_product_guide.md)

## [0.3.14](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.13...v0.3.14)

### Changed
* Clarified the availability of the 'apply water mask' option in the [InSAR Product Guide](docs/guides/insar_product_guide.md)

## [0.3.13](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.12...v0.3.13)

### Changed
* Updated HyP3 SDK to [v1.3.2](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#132)

## [0.3.12](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.11...v0.3.12)

### Changed
* Updated the [InSAR Product Guide](docs/guides/insar_product_guide.md) to document the option to apply a water mask during phase unwrapping

## [0.3.11](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.10...v0.3.11)

### Changed
* Updated HyP3 SDK to [v1.3.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#131)

## [0.3.10](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.9...v0.3.10)

### Changed
* Updated HyP3 SDK to [v1.3.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#130)

## [0.3.9](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.8...v0.3.9)

### Changed
* Updated the [InSAR Product Guide](docs/guides/insar_product_guide.md) to document the inclusion of an ellipsoid incidence angle map in the InSAR product package
* Updated the water mask description in the [InSAR Product Guide](docs/guides/insar_product_guide.md) to include large inland waterbodies

## [0.3.8](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.7...v0.3.8)

### Changed
* Updated the [InSAR Product Guide](docs/guides/insar_product_guide.md) to document the inclusion of a water mask in the InSAR product package

## [0.3.7](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.6...v0.3.7)

### Added
* A [What's New](docs/whats_new.md) page which displays [@ASFHyP3's](https://twitter.com/ASFHyP3) twitter feed

## [0.3.6](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.5...v0.3.6)

### Changed
* Updated HyP3 SDK to [v1.2.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#120)

## [0.3.5](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.4...v0.3.5)

### Added
* Added descriptions for each type of metadata file in the [InSAR Product Guide](docs/guides/insar_product_guide.md),
  including the new ArcGIS-compliant metadata XML files added in hyp3-gamma
  [4.6.0](https://github.com/ASFHyP3/hyp3-gamma/blob/develop/CHANGELOG.md#460)

## [0.3.4](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.3...v0.3.4)

### Changed
* Updated availability of InSAR options in [InSAR Product Guide](docs/guides/insar_product_guide.md)

## [0.3.3](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.2...v0.3.3)

### Fixed
* Corrected the [InSAR API examples](docs/using/api.md) `job_type` parameter value

## [0.3.2](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.1...v0.3.2)

### Changed
* Updated HyP3 SDK to [v1.1.3](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#113)

## [0.3.1](https://github.com/ASFHyP3/hyp3-docs/compare/v0.3.0...v0.3.1)

### Changed
* Updated HyP3 SDK to [v1.1.2](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#112)

## [0.3.0](https://github.com/ASFHyP3/hyp3-docs/compare/v0.2.2...v0.3.0)

### Added
* Added a [Contact Us snippet](docs/contact-snippet.md) that is used on the [Home](docs/index.md) page
  and a new [Contact Us](docs/contact-snippet.md) page
* Added SAR Basics -> [Introduction to SAR](docs/guides/introduction_to_sar.md) page
* Added Products -> InSAR -> [InSAR Product Guide](docs/guides/insar_product_guide.md) page

### Changed
* Re-organized site table of contents
* Moved product usage guidelines from Products page to a new Products ->
  [Usage Guidelines](docs/usage_guidelines.md) page
* Updated RTC Product Guide and DEM reference page to state that the Copernicus DEM is now available

## [0.2.2](https://github.com/ASFHyP3/hyp3-docs/compare/v0.2.1...v0.2.2)

### Changed
* Updated HyP3 SDK to [v1.1.1](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#111)

## [0.2.1](https://github.com/ASFHyP3/hyp3-docs/compare/v0.2.0...v0.2.1)

### Changed
* Updated HyP3 SDK to [v1.1.0](https://github.com/ASFHyP3/hyp3-sdk/blob/main/CHANGELOG.md#110)

## [0.2.0](https://github.com/ASFHyP3/hyp3-docs/compare/v0.1.0...v0.2.0)

### Changed
* Updated the RTC Product Guide and DEM Information section to include the Copernicus DEM GLO-30
* Added an abstract to the RTC Product Guide
* Updated the RTC Product Guide to include more information on SAR distortions, how they are addressed by
  radiometric terrain correction, and how to access ASF's On-Demand RTC processing functionality and resources

## [0.1.0](https://github.com/ASFHyP3/hyp3-docs/compare/v0.0.0...v0.1.0)

### Added
* HyP3 user documentation for the SDK and API, and links for Vertex's On Demand usage
* HyP3 product documentation for RTC, InSAR, and autoRIFT products
* Other associated tools documentation
