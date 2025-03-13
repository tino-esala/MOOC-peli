import pygame
import random

#Pelin nimi
pygame.display.set_caption("Mörköpeli")

#Resoluutio
naytto = pygame.display.set_mode((640, 480))

class Peli:
    def __init__(self):
        pygame.init()
        self.robo = pygame.image.load("C:/Users/Asus/Documents/GitHub/MOOC-peli/robo.png")
        self.hirviot = []
        self.hirviot.append(Hirvio(-2, 2))
        self.x = 100
        self.y = 100
        self.oikealle = False
        self.vasemmalle = False
        self.ylos = False
        self.alas = False
        self.pisteet = 0
        self.ajastin = 120
        self.silmukka()

    def silmukka(self):
        while True:
            self.ajastus()
            self.tutki_tapahtumat()
            self.robo_liike()
            self.hirvio_liike()
            self.hirvion_lisays()
            self.pistelasku()
            self.piirra_naytto()
            self.tormays()

    def piirra_naytto(self):
        naytto.fill((180, 180, 220))
        naytto.blit(self.robo, (self.x, self.y))
        fontti = pygame.font.SysFont("Arial", 24)
        teksti = fontti.render(f"Pisteet: {self.pisteet}", True, (255, 0, 0))
        naytto.blit(teksti, (520, 0))
        for i in self.hirviot:
            naytto.blit(i.hirvio, (i.x, i.y))
        pygame.display.flip()
        kello = pygame.time.Clock()
        kello.tick(80)

    def hirvio_liike(self):
        for i in self.hirviot:
            i.liiku()

    def robo_liike(self):
        if self.oikealle:
            self.x += 2
            self.x = clamp(self.x, -5, 645-self.robo.get_width())
        if self.vasemmalle:
            self.x -= 2
            self.x = clamp(self.x, -5, 595)
        if self.ylos:
            self.y -= 2
            self.y = clamp(self.y, 0, 480)
        if self.alas:
            self.y += 2
            self.y = clamp(self.y, 0, 480-self.robo.get_height())

    # Mitä nappulaa painetaan
    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = True
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = True
                if tapahtuma.key == pygame.K_F2:
                    Peli()
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()

            # Mikä nappula irroitetaan
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = False
                
            if tapahtuma.type == pygame.QUIT:
                exit()
            
    # Game over ruutu
    def pistenaytto(self):
        fontti = pygame.font.SysFont("Arial", 24)
        fontti2 = pygame.font.SysFont("Arial", 36)
        teksti = fontti.render(f"Uusi peli: F2", True, (0, 0, 0))
        teksti2 = fontti.render(f"Sulje peli: Esc", True, (0, 0, 0))
        teksti3 = fontti2.render(f"Pisteet: {self.pisteet}", True, (0, 0, 0))
        naytto.blit(teksti, (520, 0))
        while True:
            naytto.fill((180, 180, 180))
            naytto.blit(teksti, (240, 240))
            naytto.blit(teksti2, (240, 270))
            naytto.blit(teksti3, (240, 200))
            pygame.display.flip()
            self.tutki_tapahtumat()

    def ajastus(self):
        self.ajastin -= 1
        if self.ajastin == 0:
            self.ajastin = 120

    def pistelasku(self):
        if self.ajastin % 5 == 0:
            self.pisteet += 1
    
    # Hirviön lisäys ajastimen mukaan
    def hirvion_lisays(self):
        if self.ajastin <= 1 and len(self.hirviot) < 12:
            self.hirviot.append(Hirvio(-2, 2))

    # Tarkistaa törmääkö Robo Hirviöön
    def tormays(self):
        self.xrange = range(self.x-30, self.x+30)
        self.yrange = range(self.y-55, self.y+70)
        for i in self.hirviot:
            if i.x in self.xrange and i.y in self.yrange:
                self.pistenaytto()

class Hirvio():
    def __init__(self, x1, x2):
        self.x = random.randint(50, 590)
        self.y = -100
        self.xnopeus = random.choice([x1, x2])
        self.ynopeus = 2
        self.hirvio = pygame.image.load("C:/Users/Asus/Documents/GitHub/MOOC-peli/hirvio.png")

    def liiku(self):
        if self.xnopeus > 0 and self.x+self.hirvio.get_width() >= 640:
            self.xnopeus = -2
        elif self.xnopeus < 0 and self.x <= 0:
            self.xnopeus = 2
        elif self.ynopeus > 0 and self.y+self.hirvio.get_height() >= 480:
            self.ynopeus = -2
        elif self.ynopeus < 0 and self.y <= 0:
            self.ynopeus = 2
        self.x += self.xnopeus
        self.y += self.ynopeus

# Pitää Robon pelialueen sisällä
def clamp(n, min, max): 
    if n < min: 
        return min
    elif n > max: 
        return max
    else: 
        return n 


Peli()

