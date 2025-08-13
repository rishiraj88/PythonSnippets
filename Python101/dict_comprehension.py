weights_casesensitive= {'a':65,'b':66,'A':97}

weights_ignorecase= {k.lower(): weights_casesensitive.get(k.lower(),0) + weights_casesensitive.get(k.upper(),0) for k in weights_casesensitive.keys()}
print(weights_ignorecase)