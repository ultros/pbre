class Report:

    def __init__(self, report_file_name: str):
        self.report_file_name = "reports/" + report_file_name


class HtmlReport(Report):

    def printt(self):
        """Print a <title>"""
        with open(f"{self.report_file_name}.html", 'a') as file_obj:
            file_obj.write(f"<title>{self.report_file_name}</title>\n")
            file_obj.close()

    def printp(self, line: str):
        """Print an input in <p> tags."""
        with open(f"{self.report_file_name}.html", 'a') as file_obj:
            file_obj.write(f"<p>{line}</p>\n")
            file_obj.close()

    def printh(self, line: str):
        """Print an input in <h3> tags."""
        with open(f"{self.report_file_name}.html", 'a') as file_obj:
            file_obj.write(f"<h3>{line}</h3>\n")
            file_obj.close()
