from SnakeGame import SnakeGame
import keyboard
import time

def main():
    game = SnakeGame()

    direction = None

    while not keyboard.is_pressed("q"):
        if keyboard.is_pressed("up"):
            direction = "up"

        elif keyboard.is_pressed("down"):
            direction = "down"

        elif keyboard.is_pressed("left"):
            direction = "left"

        elif keyboard.is_pressed("right"):
            direction = "right"

        start = time.time()
        end = game.sp_game_loop(direction)
        finish = time.time()


        # new snake is made if this happens
        if end:
            # if some sort of collision occurs we pause and sleep for a very short period of time indicating game being over
            time.sleep(0.5)
            game.sp.snake = Snake(WINDOW_SIZE[0] / 2, WINDOW_SIZE[0] / 2, SPEED, WINDOW_SIZE[0], WINDOW_SIZE[0])
        time.sleep(0.05)

if __name__ == "__main__":
    main()
