from escape import Escape

class Game(object):

    def run(self):
        self.game = Escape()
        self.game.start()

## Starting point
if __name__ == "__main__":
    app = Game()
    app.run()
