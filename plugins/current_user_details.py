from pbre.plugin_base import RegistryValues
from pbre.generate_report import HtmlReport


class Plugin(RegistryValues):

    def __init__(self):
        super().__init__()
        self.registry_hive = "hcu"
        self.registry_path = "Volatile Environment"
        self.registry_keys = ["HOMEPATH", "LOGONSERVER", "USERDOMAIN", "USERDOMAIN_ROAMINGPROFILE",
                              "USERNAME", "USERPROFILE"]

    def main(self):
        html_report = HtmlReport("Current User")
        value_list = []
        for value in self.get_values(self.registry_hive, self.registry_path, self.registry_keys):
            if value is None:
                value_list.append(f"!!!{None}!!!")
            else:
                value_list.append(value[0])

        html_report.printh("Volatile Environment")
        html_report.printp(f"HOMEPATH: {value_list[0]}")
        html_report.printp(f"LOGONSERVER: {value_list[1]}")
        html_report.printp(f"USERDOMAIN: {value_list[2]}")
        html_report.printp(f"USERDOMAIN_ROAMINGPROFILE: {value_list[3]}")
        html_report.printp(f"USERNAME: {value_list[4]}")
        html_report.printp(f"USERPROFILE: {value_list[5]}")

    if __init__ == "__main__":
        main()
