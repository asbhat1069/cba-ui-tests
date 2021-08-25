

class ChallengePageObjects:

    game_header = "//*[text()='COVID-19 THE GAME']"
    battlefield_challenge_button = "#news"

    start_battlefield_challenge_button = "#start"
    continue_button = "#continue"
    answer_link = "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{0}')]"
    leaderboard_header = "//*[contains(text(), 'COVID-19 THE GAME - LEADERBOARD')]"
    continue_fighting_button = "#leaderboard_link"
    correct_answer_header = "//*[text()='That is correct!']"
    wrong_answer_header = "//*[text()='Oh no!']"
    try_again_button = "//button[text()='Try again']"

    bus_challenge_button = "#bus"
    bus_timer_start = "#bus_timer_start"
    try_next_battle_button = "#close_correct_modal_btn"
    check_final_score_button = "#leaderboard_link"

    start_challenge_button = "//*[text()='Start']"
