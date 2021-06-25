class Category:
    
	def __init__(self,z):
		self.name = z
		self.ledger = []
			
	def __str__(self):
		lines = []
		lines.append(self.name.center(30,'*'))
		total = 0
		for operation in self.ledger:
			lines.append(f"{operation.get('description')[0:23]:<23}" + '{0:.2f}'.format(round(operation.get('amount'),2)).rjust(7))
			total += operation.get('amount')
		lines.append(f'Total: {total}')
		return "\n".join(lines)
							
	def deposit(self,amount,description = ''):
		self.ledger.append({'amount': amount,'description': description})
			
	def withdraw(self,amount,description = ''):
		if (self.check_funds(amount)):
			self.ledger.append({'amount': -amount,'description': description})
			return True
		return False
			
	def get_balance(self):
		balance = 0
		for operation in self.ledger:
			balance += operation.get('amount')
		return balance
	
	def check_funds(self,withdrawValue):
		if self.get_balance() >= withdrawValue:
			return True
		return False
	
	def transfer(self,amount,destinationCategory):
		if self.check_funds(amount):
			self.withdraw(amount,'Transfer to ' + destinationCategory.name)
			destinationCategory.deposit(amount,'Transfer from ' + self.name)
			return True
		return False

def create_spend_chart(categories):
    outString = 'Percentage spent by category\n'
    names = []
    withdraws = {}
    for k in categories:
        currWithdraw = 0
        for j in k.ledger:
            currWithdraw -= j.get('amount') if j.get('amount')<0 else 0
        withdraws[k.name] = currWithdraw
        names.append(k.name)
    percentageWithdraws = {k: (100*v / total) for total in (sum(withdraws.values()),) for k, v in withdraws.items()}
    print(withdraws)
    print(percentageWithdraws)
    print(sum(withdraws.values()))
    for i in range(100,-10,-10):
        outString += (f'{i}|'.rjust(4))
        for j in range(len(categories)):
            if percentageWithdraws.get(names[j])>=i:
                outString += 'o'.center(3,' ')
            else:
                outString += '   '
        outString += ' \n'
    outString += ' '*4 + '---'*len(categories) + '-'
    for i in range(len(max(names,key=len))):
        outString += '\n' + ' '*4
        for x in categories:
            if len(x.name)>i:
                outString += x.name[i].center(3,' ')
            else:
                outString += ' '*3
        outString += ' '
    
    return outString