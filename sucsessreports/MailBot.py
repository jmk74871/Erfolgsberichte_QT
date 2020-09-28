class MailBot:
    def __init__(self, cpath="./SR_Data/resources/cred.csv"):
        self.cpath = cpath
        self.name = ""
        self.pw = ""
        self.server = ""
        self.port = ""

    def get_cred(self, protocoll):
        import csv

        with open(self.cpath, "r", encoding="utf_8") as cred:
            for line in csv.reader(cred):
                if line[0] == str(protocoll):
                    self.name = str(line[1]).strip()
                    print(self.name)
                    self.pw = str(line[2]).strip()
                    self.server = str(line[3]).strip()
                    self.port = str(line[4]).strip()
