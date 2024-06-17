import os
from getpass import getpass

def get(key: str):
    r = os.environ.get(key)
    if r is None:
        raise Exception(f"Cannot find {key} key in .env")
    
    return r

def format_input_cmd(v: str, add_info: str | None = None):
    cmd = f"specify {v}"
    if add_info:
        return f"{cmd} ({add_info}):"
    
    return f"{cmd}:"

def new_env_var(key: str, val: str):
    return f'{key}="{val}"\n'

def setup_env(env: str, force: bool):
    if os.path.exists(env) and not force:
        return
    
    with open(env, "w") as e:
        e.write(new_env_var("CHANNEL_ID", input(format_input_cmd("Your telegram channel id", "You can get it from https://t.me/LeadConverterToolkitBot"))))
        e.write(new_env_var("BOT_TOKEN", getpass(format_input_cmd("Your telegram bot token", "You can get it from https://t.me/BotFather"))))

        e.write(new_env_var("GRPC_ADDRESS", input(format_input_cmd("Your grpc server address"))))

if __name__ == "__main__":
    setup_env(".env", True)
