import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import changelog


class ChangelogVerifierTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        (self.repo / "README.md").write_text("| Version | 1.2.0 |\n", encoding="utf-8")
        self.write_changelog(
            "## [Unreleased]\n\n"
            "## [1.2.0] - 2026-11-26\n\n"
            "### Changed\n- Example.\n\n"
            "[Unreleased]: https://example.invalid/compare/v1.2.0...HEAD\n"
            "[1.2.0]: https://example.invalid/releases/tag/v1.2.0\n"
        )

    def tearDown(self):
        self.temp.cleanup()

    def write_changelog(self, content):
        (self.repo / "CHANGELOG.md").write_text(content, encoding="utf-8")

    def test_valid_changelog_and_readme_version_pass(self):
        self.assertTrue(changelog.verify(self.repo, quiet=True))

    def test_missing_unreleased_heading_fails(self):
        self.write_changelog("## [1.2.0] - 2026-11-26\n")
        self.assertFalse(changelog.verify(self.repo, quiet=True))

    def test_duplicate_release_section_fails(self):
        content = (self.repo / "CHANGELOG.md").read_text(encoding="utf-8")
        self.write_changelog(content.replace(
            "## [1.2.0] - 2026-11-26",
            "## [1.2.0] - 2026-11-26\n\n## [1.2.0] - 2026-11-25",
        ))
        self.assertFalse(changelog.verify(self.repo, quiet=True))

    def test_out_of_order_releases_fail(self):
        self.write_changelog(
            "## [Unreleased]\n"
            "## [1.1.0] - 2026-10-01\n"
            "## [1.2.0] - 2026-11-26\n"
            "[Unreleased]: https://example.invalid/compare\n"
            "[1.1.0]: https://example.invalid/1.1.0\n"
            "[1.2.0]: https://example.invalid/1.2.0\n"
        )
        self.assertFalse(changelog.verify(self.repo, quiet=True))

    def test_missing_release_reference_fails(self):
        self.write_changelog(
            "## [Unreleased]\n"
            "## [1.2.0] - 2026-11-26\n"
            "[Unreleased]: https://example.invalid/compare\n"
        )
        self.assertFalse(changelog.verify(self.repo, quiet=True))

    def test_dangling_reference_fails(self):
        content = (self.repo / "CHANGELOG.md").read_text(encoding="utf-8")
        self.write_changelog(content + "[9.9.9]: https://example.invalid/9.9.9\n")
        self.assertFalse(changelog.verify(self.repo, quiet=True))

    def test_readme_version_mismatch_fails(self):
        (self.repo / "README.md").write_text("| Version | 9.9.9 |\n", encoding="utf-8")
        self.assertFalse(changelog.verify(self.repo, quiet=True))


if __name__ == "__main__":
    unittest.main()
