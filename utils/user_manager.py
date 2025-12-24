from dataclasses import dataclass
@dataclass
class User:
    username: str
    password: str
    role: str # 'standard', 'locked', 'problem', 'performance'
    expected_behavior: str

class UserManager:
    USERS = {
        'standard': User(
            username="standard_user",
            password="secret_sauce",
            role="standard",
            expected_behavior="Normal user, all features work"
        ),
        'locked': User(
            username="locked_out_user",
            password="secret_sauce",
            role="locked",
            expected_behavior="Cannot login, shows error"
        ),
        'problem': User(
            username="problem_user",
            password="secret_sauce",
            role="problem",
            expected_behavior="UI issues, images might not load"
        ),
        'performance': User(
            username="performance_glitch_user",
            password="secret_sauce",
            role="performance",
            expected_behavior="Slow responses, needs longer waits"
        )
    }

    @classmethod
    def get_user(cls,role):
        return cls.USERS.get(role)
