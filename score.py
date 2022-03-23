from utils import SCORES_FILE_NAME


def add_score(difficulty):
    with open(SCORES_FILE_NAME, 'r') as score_file:
        score_file_content = score_file.read()
        current_points_saved = int(score_file_content.strip())

    updated_points_saved = current_points_saved + ((difficulty*3)+5)

    with open(SCORES_FILE_NAME, 'w') as score_file:
        score_file.write(str(updated_points_saved))
