str = 'X-DSPAM-Confidence:0.8475'

finding = str.find(':')
slicing = str[finding+1:]
final = float(slicing)

print(final)
