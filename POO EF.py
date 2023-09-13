class Balance():
    MargenCaja = 300
    def __init__(self):
        self.Caja = 0
        self.CtasxCob = 0
        self.Inven = 0
        self.AFijo = 0
        self.DepreAc = 0
        self.PasCP = 0
        self.PasLP = 0
        self.Patrim = 0
        self.ResAc = 0

    def Add_Patrim(self,Aporte):
        self.Patrim += Aporte
        self.Caja += Aporte

class EGyP(Balance):
    def __init__(self):
        Balance.__init__(self)
        self.Ventas = 0
        self.CVenta = 0
        self.GAdm = 0
        self.GVenta = 0
        self.DeprePer = 0

        self.Compras = 0

    def Add_Venta(self, Venta=0, PorcCred=0.3, Margen = 0.2):
        self.Ventas += Venta
        self.Caja += Venta * PorcCred
        self.CtasxCob += Venta * (1-PorcCred)
        
        self.CVenta = Venta * (1 - Margen)
        self.Inven -= self.CVenta
        self.ResAc += Venta * Margen

    def Add_Compras(self,Compras):
        self.Compras += Compras
        self.Inven += Compras
        if self.Caja - Balance.MargenCaja > Compras:
            self.Caja -= Compras
        else: self.PasCP += Compras

EF = EGyP()
EF.Add_Patrim(300)
EF.Add_Compras(500)
EF.Add_Venta(500, 0.3, 0.2)

print('Caja\t\t', EF.Caja, '\t\tPas CP\t\t', EF.PasCP)
print('Ctas x Cob\t', EF.CtasxCob, '\t\tPasLP\t\t', EF.PasLP)
print('Inventario\t', EF.Inven)
print('Act Fijo\t\t', EF.AFijo, '\t\tPatrim\t\t', EF.Patrim)
print('DeprecAc\t\t', EF.DepreAc, '\t\tRes Acum\t', EF.ResAc)
print('TOTAL ACTIVO\t', EF.Caja + EF.CtasxCob + EF.Inven + EF.AFijo + EF.DepreAc, end='')
print('\t\tTOT PAS PATRIM\t', EF.PasCP + EF.PasLP + EF.Patrim + EF.ResAc, end='')

print('\n\nVentas \t\t\t', EF.Ventas)
print('C. Ventas\t\t', EF.CVenta)
print('Ut. Bruta \t\t', EF.Ventas - EF.CVenta)
print('G. Ventas\t\t', EF.GVenta)
print('G. Adminis\t\t', EF.GAdm)
print('DeprecPer\t\t', EF.DeprePer)
print('UT. NETA \t\t', EF.Ventas - EF.CVenta - EF.GVenta - EF.GAdm - EF.DeprePer)
