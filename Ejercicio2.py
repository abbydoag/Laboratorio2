"""
2. Usted tiene un análisis de sangre para detectar una enfermedad rara que ocurre por casualidad en 
1 persona en 100,000. Si tiene la enfermedad, la prueba reportará que la tiene con probabilidad 0.95 
(y que no lo hace con probabilidad 0.05). Si no tiene la enfermedad, la prueba reportará un falso 
positivo con probabilidad 1e-3. Si la prueba dice que tiene la enfermedad, ¿cuál es la probabilidad 
de que realmente tenga la enfermedad? Escriba las listas en Python de las probabilidades respectivas
 y resuelva el problema
"""
#Abby Donis 22440
#Eliazar Canastuj 23384
#

#Teorema de bayes
"""
A: Tener la enfermedad -> P(A)= 1/100,000 = 1x10^-5 
B: No tener enfermedad -> P(B) = 1-1x10^-5
C: Prueba positiva
D: Prueba negativa
P(C|A): Si se tiene, prueba + = 0.95
P(D|A): Si se tiene, prueba - = 0.05
P(C|B): No la tiene, prueba + = 1x10^-3
P(D|B): No la tiene, prueba - = 1-1x10^-3 = 0.999

Bayes: P(A|C)= P(C|A)*P(A)/P(C)
       P(C) = P(C|A)*P(A) + P(C|B)*P(B)
"""
probA = 1e-5
probB = 1-probA

probC_A = 0.95 #P(C|A)
probD_A = 0.05 #P(D|A)

probC_B = 1e-3 #P(C|B)
probD_B = 1-probC_B #P(D|B)

#Probabilidad total de obtener un resultado positivo
probTotal = probC_A*probA + probC_B*probB


probA_C = (probC_A * probA) / probTotal #P(A|C)

# Mostrar probabilidades respectivas
print("Probabilidad de tener la enfermedad: ", probA)
print("Probabilidad de no tener la enfermedad: ", probB)
print("Probabilidad de prueba positiva si se tiene la enfermedad: ", probC_A)
print("Probabilidad de falso positivo: ", probC_B)
print("Probabilidad total de resultado positivo: ", probTotal)

# Mostrar resultado final
print("\nProbabilidad de tener la enfermedad dado que la prueba fue positiva: ", probA_C)