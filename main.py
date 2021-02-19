from Simulation import Simulation
from TerminalVisualiser import TerminalVisualiser
from MatPlotLibVisualiser import MatPlotLibVisualiser
from SaveVisualiser import SaveVisualiser
from AnimationVisualiser import AnimationVisualiser
from YoutubeVisualiser import YoutubeVisualiser

menu = """
Zvolte typ visualizace:
1. V terminalu.
2. Postupne otevirani grafu v grafickem okne (uzivatelsky neprivetive).
3. Ulozeni vizualizace jako sekvenci obrazku do lokalni slozky.
4. Vytvoreni animace ve formatu GIF souboru.
5. Otevreni jiz vypracovaneho videa na YouTube.
"reset" pro obnovu simulace
"exit" pro ukonceni programu
"""


def main():
    print(menu)
    sim = Simulation(title='OSA úkol 1 - cesta k výtahu')
    while(True):
        response = input(" > ")
        if response.lower() in ["konec", "quit", "q", "exit"]:
            break
        if response.lower() in ["reset", "r", "restart"]:
            sim.reset()
            print("Simulace obnovena.")
            continue
        try:
            response = int(response)
            assert 1 <= response <= 5
            
        except ValueError:
            print("Neplatna volba.")
            continue
        except AssertionError:
            print("Cislo 1-5 prosim.")
            continue
        if response == 1:
            
            vis = TerminalVisualiser(sim)
        elif response == 2:
            vis = MatPlotLibVisualiser(sim)
        elif response == 3:
            folder = "./" + input("Zadejte nazev slozky pro vytvoreni obrazku: ")
            if folder == "./":
                folder = "./tmp"
            frames = int(input("Zadejte pocet obrazku k vytvoreni: "))
            sim.reset()
            vis = SaveVisualiser(sim, folder, frames)
        elif response == 4:
            folder = "./" + input("Zadejte nazev souboru: ")
            if folder == "./":
                folder = "./result.gif"
            frames = int(input("Zadejte pocet obrazku k vytvoreni: "))
            sim.reset()
            vis = AnimationVisualiser(sim, frames, folder)
        elif response == 5:
            vis = YoutubeVisualiser()
        vis.run()
        print(menu)

main()