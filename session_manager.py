sessions = {}

def track_session(user: str):
    sessions[user] = sessions.get(user, 0) + 1

