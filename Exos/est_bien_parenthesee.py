ouvrant = "([{<"
fermant = ")]}>"
ouverture = {  # dictionnaire qui donne l'ouvrant en fonction du fermant
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}


def est_bien_parenthesee(expression) :
    pile = []
    for car in expression :
        if car in ouvrant :
            pile.append(car)
        elif car in fermant :
            if len(pile) > 0 :
                if pile[len(pile)-1] == ouverture[car]:
                    pile.pop()
                else :
                    return False
            else :
                return False
    return len(pile) == 0 

print(est_bien_parenthesee("()"))
assert est_bien_parenthesee("(2 + 4)*7") == True
assert est_bien_parenthesee("tableau[f(i) - g(i)]") == True
assert est_bien_parenthesee(
    "int main(){int liste[2] = {4, 2}; return (10*liste[0] + liste[1]);}"
) == True

assert est_bien_parenthesee("(une parenthèse laissée ouverte") == False
assert est_bien_parenthesee("{<(}>)") == False
assert est_bien_parenthesee("c'est trop tard ;-)") == False