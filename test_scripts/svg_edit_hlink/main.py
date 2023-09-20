import svg_edit


def main():
    svgconfig = svg_edit.SVGedit()
    df = svgconfig.df_teams
    for team in df.team.values:
        df_team = df[df.team == team].fillna(" ")
        contents = svgconfig.get_team_svgcontent(df_team)
        svgconfig.write_svg_contents(contents, team)
        print(f"{team} SVG config written succesfully")


if __name__ == "__main__":
    main()
