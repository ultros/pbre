from pbre.plugin_base import RegistryValues
from pbre.generate_report import HtmlReport


class Plugin(RegistryValues):

    def __init__(self):
        super().__init__()
        self.registry_hive = "hcu"
        self.registry_path = "SOFTWARE\ImgBurn"
        self.registry_keys = ["TotalNumberOfBurns"]

    def main(self):
        html_report = HtmlReport("Optical Media")

        value_list = self.parse_values(self.registry_hive, self.registry_path, self.registry_keys)

        html_report.printh("ImgBurn")
        html_report.printp(f"Total number of burns: {value_list[0]}")

    if __init__ == "__main__":
        main()
