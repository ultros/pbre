import winreg


class RegistryValues:

    def __init__(self):
        # self.report_name = report_name
        pass

    def get_values(self, hive, key, key_value):
        values = []

        assert hive != "" or None

        match hive:
            case "hcu":
                hive = winreg.HKEY_CURRENT_USER

        registry_hive = winreg.ConnectRegistry(None, hive)
        try:
            registry_key = winreg.OpenKey(registry_hive, key)
            for value_name in key_value:
                try:
                    values.append(winreg.QueryValueEx(registry_key, value_name))
                except:
                    values.append(None)
                    print(f"\t[!] No value for {value_name}! Skipping...")
        except FileNotFoundError:
            print(f"\t[!] Cannot find value for: {key}")
            pass

        return values
