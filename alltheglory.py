import glob
import time

from flask import Flask, Response, request
app = Flask('ascii-hypnotoad')

frames = ['\x1b[2J']  # clear screen


def load_frames():
    path = './frames/*.ansi'
    files = glob.glob(path)
    for f in files:
        with open(f, 'r') as frame:
            frames.append('\x1b[42A' + frame.read())
        frame.close()


def to_hypnotoad():
    while True:
        for f in frames:
            yield f
            time.sleep(0.2)


@app.route('/')
def all_the_glory():
    plain_text_agents = [
        "curl",
        "wget",
        "httpie",
        "python-requests",
        "lwp-request"
    ]
    user_agent = request.headers.get('User-Agent').lower()
    is_plain_text = any(agent in user_agent for agent in plain_text_agents)
    return Response(to_hypnotoad()) if is_plain_text else 'All the glory to the Hypnotoad!!!'

load_frames()

if __name__ == '__main__':
    app.debug = True
    app.run()
