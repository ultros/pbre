from pbre.plugin_base import RegistryValues
from pbre.generate_report import HtmlReport


class Plugin(RegistryValues):

    def __init__(self):
        super().__init__()
        self.registry_hive = "hklm"
        self.registry_path = '\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
        self.registry_keys = [""]



    def main(self):
        values = self.discover_values(self.registry_hive, self.registry_path)

        html_report = HtmlReport("Run (Startup)")
        html_report.printh("Run (Startup)")
        for value in values:
            html_report.printp(f"{value[0]} - {value[1]} - {value[2]}")

    if __init__ == "__main__":
        main()

