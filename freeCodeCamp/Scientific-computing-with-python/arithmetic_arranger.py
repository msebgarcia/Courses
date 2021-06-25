def arithmetic_arranger(strList,boolean = False):
	spaceBetween = '    '    # Space between columns
	firstRow     = ''        # Row 1: first term of the sum
	secondRow    = ''        # Row 2: second term of the sum
	thirdRow     = ''        # Row 3: -----
	firstIter    = True      # Aux var to add spaces between columns
	forthRow     = ''        # Row 4: Results
	operator = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y}

	if len(strList) > 5:
			#raise TypeError("Too many problems")
			return 'Error: Too many problems.'
			
	for operation in strList:
 		elements = operation.split()
 		if (elements[1] != '+')and(elements[1] != '-'):
 			#raise TypeError("Operator must be '+' or '-'")
 			return "Error: Operator must be '+' or '-'."
 		elif (len(elements[0])>4)or(len(elements[2])>4):
 			#raise TypeError('Numbers cannot be more than four digits.')
 			return 'Error: Numbers cannot be more than four digits.'
 		else:
 			try:
 				num1 = int(elements[0]) # First number
 				num2 = int(elements[2]) # Second number
 				resl = str(operator[elements[1]](num1,num2))   # Result of the sum
 				len1 = len(elements[0]) # String length of number one
 				len2 = len(elements[2]) # String lenght of number two
 				len3 = len(resl)
 				if not(firstIter):
 					firstRow  += spaceBetween
 					secondRow += spaceBetween
 					thirdRow  += spaceBetween
 					forthRow  += spaceBetween
 					firstIter = False
 							
 					# Operations
 					sumSpace = ((len1) if (num1>=num2) else (len2)) + 1
 					firstRow  += ' '*(sumSpace-len1+1)+elements[0]
 					secondRow += elements[1] + ' '*(sumSpace-len2)+elements[2]
 					thirdRow  += '-'*(sumSpace+1)
 					forthRow  += ' '*(sumSpace-len3+1)+resl              
 						
 			except:
 				#raise TypeError('Numbers must only contain digits.')
 				return 'Error: Numbers must only contain digits.'
							
	outStr = firstRow + "\n" + secondRow + "\n" + thirdRow
	if boolean:
		outStr += "\n" + forthRow

	return outStr