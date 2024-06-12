import config

def detect_collision(ball, paddle_left, paddle_right):
    if ball.x < paddle_left.width + 30 and paddle_left.y < ball.y < paddle_left.y + paddle_left.height:
        ball.speed_x *= -1
    elif ball.x > config.SCREEN_WIDTH - paddle_right.width - 40 and paddle_right.y < ball.y < paddle_right.y + paddle_right.height:
        ball.speed_x *= -1

def compute_score(ball, score_left, score_right):

    ball_pos_x = config.SCREEN_WIDTH // 2 - ball.size // 2
    ball_pos_y = config.SCREEN_HEIGHT // 2 - ball.size // 2 

    if ball.x < 0:
        score_right += 1
        ball.reset(ball_pos_x, ball_pos_y)
    elif ball.x > config.SCREEN_WIDTH - ball.size:
        score_left += 1
        ball.reset(ball_pos_x, ball_pos_y)

    return score_left, score_right