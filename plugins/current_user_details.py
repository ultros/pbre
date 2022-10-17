from plugin_base import RegistryValues


class Plugin(RegistryValues):

    def __init__(self):
        super().__init__()
        self.registry_hive = "hcu"
        self.registry_path = "Volatile Environment"
        self.registry_keys = ["HOMEPATH", "LOGONSERVER", "USERDOMAIN", "USERDOMAIN_ROAMINGPROFILE",
                              "USERNAME", "USERPROFILE"]

    def main(self):
        value_list = []
        for value in self.get_values(self.registry_hive, self.registry_path, self.registry_keys):
            value_list.append(value[0])
        print(value_list)

    if __init__ == "__main__":
        main()
