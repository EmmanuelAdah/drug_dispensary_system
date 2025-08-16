from data.models.gender import Gender


class Drugs:
    drugs = list()

    def save_drug(self, drug : Drug):
        self.drugs.append(drug)