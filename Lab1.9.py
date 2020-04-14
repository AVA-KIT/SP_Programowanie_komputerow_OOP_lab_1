class KonwersjaJednostek:
    def cale_na_cm(self, cm):
        return cm * 0.393700787
    def cm_na_cale(self, cal):
        return cal * 2.54
    def kg_na_funty(self, ibs):
        return ibs * 0.45359237
    def funty_na_kg(self, kg):
        return kg * 2.20462262

konw_cale_cm = KonwersjaJednostek()
print('-----------------------')
print('6 cali to: ', konw_cale_cm.cale_na_cm(6), ' cm')
konw_cale_cm = KonwersjaJednostek()
print('8 cali to: ', konw_cale_cm.cale_na_cm(8), ' cm')
konw_cale_cm = KonwersjaJednostek()
print('20 cali to: ', konw_cale_cm.cale_na_cm(20), ' cm')
print('-----------------------')
konw_cm_cale = KonwersjaJednostek()
print('6 cm to: ', konw_cm_cale.cm_na_cale(6), ' cali')
konw_cm_cale = KonwersjaJednostek()
print('8 cm to: ', konw_cm_cale.cm_na_cale(8), ' cali')
konw_cm_cale = KonwersjaJednostek()
print('20 cm to: ', konw_cm_cale.cm_na_cale(20), ' cali')
print('-----------------------')
konw_kg_funty = KonwersjaJednostek()
print('6 kg to: ', konw_kg_funty.kg_na_funty(6), ' Ibs')
konw_kg_funty = KonwersjaJednostek()
print('8 kg to: ', konw_kg_funty.kg_na_funty(8), ' Ibs')
konw_kg_funty = KonwersjaJednostek()
print('20 kg to: ', konw_kg_funty.kg_na_funty(20), ' Ibs')
print('-----------------------')
konw_funty_kg = KonwersjaJednostek()
print('6 Ibs to: ', konw_funty_kg.funty_na_kg(6), ' kg')
konw_funty_kg = KonwersjaJednostek()
print('8 Ibs to: ', konw_funty_kg.funty_na_kg(8), ' kg')
konw_funty_kg = KonwersjaJednostek()
print('20 Ibs to: ', konw_funty_kg.funty_na_kg(20), ' kg')
print('-----------------------')