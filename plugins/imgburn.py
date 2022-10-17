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
        value_list = []

        for value in self.get_values(self.registry_hive, self.registry_path, self.registry_keys):
            if value is None:
                value_list.append(f"!!!{None}!!!")
            else:
                value_list.append(value[0])

        try:
            html_report.printh("ImgBurn")
            html_report.printp(f"Total number of burns: {value_list[0]}")
        except IndexError:
            pass

    if __init__ == "__main__":
        main()
