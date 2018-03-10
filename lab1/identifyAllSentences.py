from utils import *
import identifyLanguage

pl1 = "Ala ma kota, który jest rudy."
pl2 = "Jaskinia Nietoperzowa jest dziś zamknięta."

en1 = "There are many people in the double-decker bus."
en2 = "I am very hungry!"

ge1 = "Hier sollen Materialien zum DSD gesammelt werden."
ge2 = "Es ist ein offenes Portal für Deutschlehrer und Deutschlerner."

it1 = "Fate lamore con il sapore."
it2 = "Il conto, per favore."

fn1 = "Voisitko kirjoittaa sen ylös?"
fn2 = "En puhu suomea."

es1 = "El juez pronunció la sentencia a la corte."
es2 = "¿Qué hora es?"


sentences = [pl1, pl2, en1, en2, ge1, ge2, it1, it2, fn1, fn2, es1, es2]

for sentence in sentences:
    for i in range (2,6):
        identifyLanguage.identifyAndWriteToFile(i, sentence)
