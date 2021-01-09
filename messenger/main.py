# main file
# Please use multiclasses 
# ~ZaZa
#Main by zekiahepic
import io
import os
import pathlib
import yaml


class __main__:
    def __init__(self):
        print("ENTER LANGUAGE: (DE)  (EN)")
        language = input().lower()
        self.handleStartup(language)

    def handleStartup(self, language):
        print(self.translate("main.welcome", language))
        resp = str(input().lower())
        if resp == "--terminal":
            print(self.translate("main.climode", language))
            open = input(">> ")
            # run the StartCli CLASS
        else:
            print(self.translate("main.guimode", language))
            # run the startWindows CLASS

    @staticmethod
    def translate(string, language):
        languageFile = os.path.join(os.getcwd(), "resources\lang.yml")
        languageFileParsed = yaml.load(open(languageFile), Loader=yaml.FullLoader)

        if language == "en":
            string = languageFileParsed["EN_US"][string]
            return string
        if language == "de":
            string = languageFileParsed["DE_GE"][string]
            return string


if __name__ == "__main__":
    __main__()
