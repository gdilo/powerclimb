# Karoo extension listing
Objective: complete the app metadata integration for Karoo's installed-extension listing; branch: fix/karoo-extension-listing.
Delivery: ask-on-risk, one work unit (~200 authored lines); checks: Python unittest, Android build when available, independent verification, physical Karoo acceptance.

## Specs
S1. "Yo necesito que aparezca en el listado de extensiones del karoo"
S2. "la aplicacion en el karoo sale installing, y nunca termina... si doy back, se cancela y no sale en las extensiones instaladas"
S3. "la apk, si se instala, y me salen los campos que anade, pero no me sale en el listado de extensiones, ni la puedo desinstalar"

## Tasks
T1 | S1-S3 | inline | done | Added documented app manifest integration, release generation/publication, regression checks and installation docs. Python tests: 3 RED before implementation, 3 GREEN afterward; diff whitespace check passed. Commit: pending. Risk: item 5 (release workflow). Device outcome is tracked separately in T3.
T2 | S1-S3 | delegated verification + inline checks | in_progress | Independent verifier passed; native review pending. Android build unavailable (no Java runtime). Commit: pending.
T3 | S1-S3 | device acceptance | blocked | Waiting for user-authorized publication/build environment and a physical Karoo test: install candidate via Companion; confirm Installing completes, app is listed and uninstall is available, existing fields still work. Commit: n/a.

## Log
L1. Original request: "Yo necesito que aparezca en el listado de extensiones del karoo"
L2. Device evidence shows INSTALL_SUCCEEDED, connected service and working fields, but user reports incomplete Karoo UI/listing. Hosted app manifest integration is missing. Adding it is the documented integration, not proof that proprietary HHApp will finish Installing.
L3. Official SDK 1.1.9: https://github.com/hammerheadnav/karoo-ext/blob/1.1.9/lib/src/main/kotlin/io/hammerhead/karooext/models/KarooAppManifest.kt confirms required label, packageName, latestApkUrl, latestVersion, latestVersionCode (since 1.1.1). No launcher activity will be added without evidence it is needed.
L4. Explore subagent could not fetch external sources; parent retrieved the versioned source. Local Java reports no runtime, adb and gentle-ai are not on PATH. No device reproduction is possible here; user logs establish the symptom, not a local reproduction.
L5. T1 integration checks observed 3 RED failures (missing application metadata, generator, publication) followed by 3 GREEN tests, including unchanged exported extension service discovery. Generator derives identity/version from the release APK metadata. git diff --check passed. Native assess attempted through codemode was rejected as direct-only; no native assessment occurred in that call.
L6. Direct native assess is available despite no gentle-ai on PATH; first assess reported nativeRisk unassessable due to intended-untracked declaration, with item 5 independent verification required. Ruby YAML parsing and exact release asset-list checks passed. Android build and real device checks remain unavailable; native review is not yet complete.
L7. Independent verifier mwhpfdxe-2-092f passed T2 implementation checks, found no concrete blockers. In isolated state: 3 tests passed; public generator produced exact output with no input mutation for 0.3.9/309, 1.0.0/10000 and 0.0.0/0; malformed JSON failed without modifying existing output. Service XML and existing extension code/resources remained unchanged against baseline 6ff8e0e. Suggested extra boundary tests were advisory, not required to fix any finding. Parent spot check: 3 tests and git diff --check passed. No external scratch cleanup attempted outside the authorized project. Native review still pending.
