class Entry:
    def __init__(self, uid, date, sender, category, text=None):
        self.uid = uid
        self.date = date
        self.sender = sender
        self.category = category
        self.text = text

    def save(self, file="./SR_Data/data.csv"):
        import csv

        with open(file, "a", newline='', encoding="utf_8") as data:
            fnames = ["UID", "DATE", "FROM", "CATEGORY", "TEXT"]
            writer = csv.DictWriter(data, fnames, restval="---")
            # writer.writeheader()  # nur ein mal
            writer.writerow({"UID": self.uid,
                             "DATE": self.date,
                             "FROM": self.sender,
                             "CATEGORY": self.category,
                             "TEXT": self.text})
