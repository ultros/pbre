import winreg


class RegistryValues:

    def __init__(self):
        # self.report_name = report_name
        pass

    def trace(func):
        def wrapper(*args, **kwargs):
            print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
            original_result = func(*args, **kwargs)
            print(f'TRACE: {func.__name__}() returned {original_result}')
            return original_result

        return wrapper

    def get_values(self, hive, key, key_value):
        values = []

        assert hive != "" or None

        match hive:
            case "hcu":
                hive = winreg.HKEY_CURRENT_USER

        registry_hive = winreg.ConnectRegistry(None, hive)
        try:
            registry_key = winreg.OpenKey(registry_hive, key)
        except FileNotFoundError:
            print(f"[!] Cannot find {key}.")

        for value_name in key_value:
            try:
                values.append(winreg.QueryValueEx(registry_key, value_name))
            except:
                values.append(None)
                print(f"\t[!] No value for {value_name}! Skipping...")

        return values

    #@trace
    def parse_values(self, registry_hive, registry_path, registry_keys):
        value_list = []

        for value in self.get_values(registry_hive, registry_path, registry_keys):
            if value is None:
                value_list.append(None)
            else:
                value_list.append(value[0])

        if value_list:
            return value_list

