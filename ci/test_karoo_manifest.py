"""Checks for the public Karoo application-manifest integration."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ANDROID = "{http://schemas.android.com/apk/res/android}"
MANIFEST_URL = "https://github.com/gdilo/powerclimb/releases/latest/download/manifest.json"


class KarooManifestTest(unittest.TestCase):
    def test_application_exposes_manifest_without_changing_extension_discovery(self):
        app = ET.parse(ROOT / "app/src/main/AndroidManifest.xml").getroot().find("application")
        metadata = app.find("meta-data[@" + ANDROID + "name='io.hammerhead.karooext.MANIFEST_URL']")
        self.assertIsNotNone(metadata)
        self.assertEqual(metadata.get(ANDROID + "value"), MANIFEST_URL)

        service = app.find("service")
        self.assertEqual(service.get(ANDROID + "name"), ".PowerClimbExtension")
        self.assertEqual(service.get(ANDROID + "exported"), "true")
        self.assertEqual(
            service.find("intent-filter/action").get(ANDROID + "name"),
            "io.hammerhead.karooext.KAROO_EXTENSION",
        )
        self.assertEqual(service.find("meta-data").get(ANDROID + "resource"), "@xml/extension_info")

    def test_generation_uses_built_apk_identity_and_version(self):
        with tempfile.TemporaryDirectory() as directory:
            metadata = Path(directory) / "output-metadata.json"
            output = Path(directory) / "manifest.json"
            metadata.write_text(json.dumps({
                "applicationId": "com.powerclimb",
                "elements": [{"versionName": "0.3.2", "versionCode": 302}],
            }))
            result = subprocess.run(
                [sys.executable, str(ROOT / "ci/generate_manifest.py"),
                 str(metadata), "Danybs/powerclimb", str(output)],
                capture_output=True, text=True,
            )
            self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))
            self.assertEqual(json.loads(output.read_text()), {
                "label": "PowerClimb",
                "packageName": "com.powerclimb",
                "latestApkUrl": "https://github.com/Danybs/powerclimb/releases/download/v0.3.2/powerclimb.apk",
                "latestVersion": "0.3.2",
                "latestVersionCode": 302,
            })

    def test_release_generates_and_publishes_both_assets(self):
        workflow = (ROOT / ".github/workflows/release.yml").read_text()
        self.assertIn('python3 -m unittest discover -s ci -p "test_*.py"', workflow)
        self.assertIn('python3 ci/generate_manifest.py', workflow)
        self.assertIn('app/build/outputs/apk/release/output-metadata.json', workflow)
        self.assertIn('"$GITHUB_REPOSITORY" manifest.json', workflow)
        publication = workflow.split("- name: Publish GitHub release", 1)[1]
        self.assertRegex(publication, r"files: \|\s+powerclimb\.apk\s+manifest\.json")
        # The existing APK remains available for USB/ADB installation.
        self.assertIn("cp app/build/outputs/apk/release/app-release.apk powerclimb.apk", workflow)
        self.assertIn("apksigner\" verify --verbose powerclimb.apk", workflow)


if __name__ == "__main__":
    unittest.main()
