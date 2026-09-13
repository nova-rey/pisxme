# Researcher evidence sack — Branch-B power-envelope gaps

Date: 2026-09-13  
Commission owner: Librarian  
Session: `d3dd71d7-b412-435d-8dbb-a12cac7174bd`  
Scope: exact Molex 0039300020 harness/terminal derating; NVIDIA/OEM V100 SXM2 input-current and load-step data; primary PI standards for sharing, surge, thermal and transient requirements.  
Disposition: metadata and bounded gap result only; no restricted material retained.

## Returned evidence

The researcher could inspect cached project files but had no live web/search permission in its worker. This limitation is recorded as a search limitation, not a not-found claim about the public web.

- Cached `pisxme/reva-clean/authority-inventory/primary-docs/NVIDIA-Tesla-V100-datasheet.pdf`, NVIDIA, December 2019, SHA-256 `ca694a4789eae7feb9ce9090f2207cbe82f5da1448922d4855e346680c59d3`, states maximum power consumption of 300 W for V100 SXM2. It does not provide rail voltage, continuous or peak current, branch allocation, or load-step behavior.
- Cached `authority-inventory/primary-docs/power/MOLEX_0039300020_AUTHORITY.md`, checked 2026-08-30, closes connector identity and land pattern only. It does not contain an amperage or temperature-rise curve and explicitly leaves the mating cable/terminal as a separate assembly decision.
- No cached primary PI standards or source records were found for the requested numeric branch imbalance, surge/load-dump, thermal, current-sharing, or load-step limits.

## Limits and handoff

This sack does not override the Librarian's direct manufacturer-source packet. The Molex manufacturer part page, TI LM74700-Q1 datasheet/product page, TI LM74700 load-sharing article, TI CSD19536KCS datasheet, Amphenol connector record, and Littelfuse catalog are indexed in `sources.json`. Together with the project `PHASE5_POWER_CALCULATIONS.md` design envelope, they support A/B/C classification. The exact harness choice, V100 waveform, and numeric system policies remain inputs for Power Authority's internal signed artifact. No field is classified D solely because this worker lacked live search.
