import pandas as pd
import yaml
import os


class SVGedit:
    def __init__(self):
        # gets the current active location of the file
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        with open(self.__location__ + "\settings.yaml") as f:
            self.settings = yaml.safe_load(f)

        # read team url settings
        team_settings_xlsx = ("\\").join(os.getcwd().split("\\")[:-1]) + self.settings[
            "team_settings"
        ]
        self.df_teams = pd.read_excel(team_settings_xlsx, sheet_name="url")

    def get_team_svgcontent(self, df_team):
        # read template and attach links unique to the team
        link_home = df_team["home"].values[0]
        link_c3 = df_team["c3"].values[0]
        link_c7 = df_team["c7"].values[0]
        link_c8 = df_team["c8"].values[0]
        link_weather = df_team["weather"].values[0]

        with open(self.__location__ + self.settings["muster_home"]) as f:
            contents_home = f.read()
        with open(self.__location__ + self.settings["muster_contest3"]) as f:
            contents_c3 = f.read()
        with open(self.__location__ + self.settings["muster_contest7"]) as f:
            contents_c7 = f.read()
        with open(self.__location__ + self.settings["muster_contest8"]) as f:
            contents_c8 = f.read()
        with open(self.__location__ + self.settings["muster_weather"]) as f:
            contents_weather = f.read()

        contents = {
            "home": contents_home.format(
                link_c3=link_c3,
                link_c7=link_c7,
                link_c8=link_c8,
                link_weather=link_weather,
            ),
            "c3": contents_c3.format(
                link_home=link_home,
                link_c7=link_c7,
                link_c8=link_c8,
                link_weather=link_weather,
            ),
            "c7": contents_c7.format(
                link_home=link_home,
                link_c3=link_c3,
                link_c8=link_c8,
                link_weather=link_weather,
            ),
            "c8": contents_c8.format(
                link_home=link_home,
                link_c3=link_c3,
                link_c7=link_c7,
                link_weather=link_weather,
            ),
            "weather": contents_weather.format(
                link_home=link_home, link_c3=link_c3, link_c7=link_c7, link_c8=link_c8
            ),
        }
        return contents

    def write_svg_contents(self, contents, team):
        # save all team svg to unique txt files
        def write_content(svgcontent, filename):
            # save a single svg config to a txt file
            file = open(self.__location__ + self.settings["output_dir"] + filename, "w")
            file.write(svgcontent)
            file.close()

        write_content(contents["home"], team + "_home_svg.txt")
        write_content(contents["c3"], team + "_c3_svg.txt")
        write_content(contents["c7"], team + "_c7_svg.txt")
        write_content(contents["c8"], team + "_c8_svg.txt")
        write_content(contents["weather"], team + "_weather_svg.txt")
