from statemachine import State, StateMachine


class Game_State(StateMachine):
    # Game States
    start_screen = State("start", initial=True)
    game_live = State("live")
    game_over = State("over")

    # State Transitions
    start_game = start_screen.to(game_live)
    end_current_game = game_live.to(game_over)
    restart = game_over.to(game_live)
