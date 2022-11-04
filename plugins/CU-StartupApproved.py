from pbre.plugin_base import RegistryValues
from pbre.generate_report import HtmlReport


class Plugin(RegistryValues):

    def __init__(self):
        super().__init__()
        self.registry_hive = "hcu"
        self.registry_path = "Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
        self.registry_keys = ["OneDriveSetup"]

    def main(self):
        html_report = HtmlReport("Current User")

        value_list = self.parse_values(self.registry_hive, self.registry_path, self.registry_keys)

        html_report.printh("StartupApproved\\Run")
        html_report.printp(f"OneDriveSetup: {value_list[0][0]}") #.hex()})

    if __init__ == "__main__":
        main()
