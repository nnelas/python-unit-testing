class MigratorApkValidationError(Exception):
    pass


class MigratorApkValidator:
    __IAB_PERMISSION_APPCOINS = "com.appcoins.BILLING"
    __IAB_PERMISSION_APTOIDE = "cm.aptoide.pt.permission.BILLING"
    __IAB_PERMISSION_GOOGLE = "com.android.vending.BILLING"

    def __init__(self):
        pass

    def validate(self, permissions: list) -> None:
        self.__is_appcoins_billing_declared(
            permissions
        ) or self.__is_aptoide_billing_declared(
            permissions
        ) or self.__is_google_billing_declared(
            permissions
        )

    def __is_appcoins_billing_declared(self, permissions: list) -> None:
        if self.__IAB_PERMISSION_APPCOINS in permissions:
            raise MigratorApkValidationError("AppCoins IAB declared in manifest")

    def __is_aptoide_billing_declared(self, permissions: list) -> None:
        if self.__IAB_PERMISSION_APTOIDE in permissions:
            raise MigratorApkValidationError("Aptoide IAB declared in manifest")

    def __is_google_billing_declared(self, permissions: list) -> None:
        if self.__IAB_PERMISSION_GOOGLE not in permissions:
            raise MigratorApkValidationError("Google IAB not declared in manifest")
