import unittest

from examples.migrator.migrator_apk_validator import (
    MigratorApkValidator,
    MigratorApkValidationError,
)


class TestMigratorApkValidator(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.migrator_apk_validator: MigratorApkValidator = None

    def setUp(self) -> None:
        self.migrator_apk_validator = MigratorApkValidator()

    def test_validate_with_appcoins_billing(self):
        permissions = ["com.android.vending.BILLING", "com.appcoins.BILLING"]
        with self.assertRaises(MigratorApkValidationError) as e:
            self.migrator_apk_validator.validate(permissions)
        self.assertEqual(str(e.exception), "AppCoins IAB declared in manifest")

    def test_validate_with_aptoide_billing(self):
        permissions = [
            "com.android.vending.BILLING",
            "cm.aptoide.pt.permission.BILLING",
        ]
        with self.assertRaises(MigratorApkValidationError) as e:
            self.migrator_apk_validator.validate(permissions)
        self.assertEqual(str(e.exception), "Aptoide IAB declared in manifest")

    def test_validate_without_google_billing(self):
        permissions = ["com.sec.android.iap.permission.BILLING"]
        with self.assertRaises(MigratorApkValidationError) as e:
            self.migrator_apk_validator.validate(permissions)
        self.assertEqual(str(e.exception), "Google IAB not declared in manifest")
