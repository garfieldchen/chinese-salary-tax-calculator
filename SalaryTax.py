class SalaryTax:
    def __init__(self, base, steps):
        self.base = base
        self.steps = steps

        self.stepTopSalary = []

    def getTax(self, income, dutyfree):
        taxSalary = income - self.base - dutyfree

        i = 0
        ladderTaxs = []
        while (taxSalary > 0):
            ladder, rate = self.steps[i][0], self.steps[i][1]            
            ladderTaxs.append(min(ladder, taxSalary) * rate)
            print str(min(ladder, taxSalary)) + " -> " + str(rate) + "  "  + str(ladderTaxs[-1])
            taxSalary -= ladder

            i += 1
                              
        print "** " + str(ladderTaxs)
        return sum(ladderTaxs)

    def salaryAgainst(self, expect, dutyfree):
        preTax = expect

        taxSalary = expect - self.base 
        i  = 0
        while (taxSalary > 0):
            ladder, rate = self.steps[i][0], self.steps[i][1]

            preTax += min(taxSalary - ladder, ladder) * rate
            taxSalary -= ladder

            i += 1

        return preTax + dutyfree
                
                            
        

TaxBaseLine = [(1500,0.03), (4500, 0.1), (9000, 0.2), (35000,0.25), (55000, 0.3), (0x7ffffff, 0.45)]

stax = SalaryTax(3500, TaxBaseLine)
print stax.getTax(500, 0)
print stax.getTax(5000000, 0)
print stax.getTax(9550, 0)
print stax.getTax(9550, 100)

print stax.salaryAgainst(9500 - 495, 0)
print stax.salaryAgainst(9500 - 495, 500)
