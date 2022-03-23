from flask import Flask
from utils import SCORES_FILE_NAME

app = Flask(__name__)


@app.route("/", methods=['GET'])
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as scores_file:
            score_file_content = scores_file.read()
            current_points_saved = int(score_file_content.strip())
        return f"""<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is <div id="score">{current_points_saved}</div></h1>
</body>
</html>"""
    except Exception as error:
        return f"""<html>
<head>
<title>Scores Game</title>
</head>
<body>
<body>
<h1><div id="score" style="color:red">{str(error)}</div></h1>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
